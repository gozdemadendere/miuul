############################################
# User-Based Collaborative Filtering
#############################################

# Collaborative filtering: Topluluğun kullanıcı veya ürün bazında ortak kanaatlerini yansıtan öneriler sunulur.(User based, Item based, Hybrid Model. Korelasyon kullanılır!)

# User-Based Collaborative Filtering
# Benzer kullanıcıların tercihlerine dayanarak bir kullanıcıya öğeler önerir.
# Kullanıcı bilgilerine ihtiyaç var: UserID x Ürün dataframe'ine ihtiyaç var.
# Örnek: Trendyol'da "Bu Ürünü Alanlar Bunları da Aldı" başlığı altında ürünler sunulması: Smeg kahve makinesine bakan bir kullanıcıya, bu makineyi alanların aldığı diğer ürünler önerilebilir.



# PROJE ADIMLARI
# 1: Veriyi Anlama & Hazırlama
# 2: User-Movie Df'inin Oluşturulması
# 3: Öneri Yapılacak Kullanıcının İzlediği Filmlerin Belirlenmesi
# 4: Aynı Filmleri İzleyen Diğer Kullanıcıların Verisine ve Id'lerine Erişmek
# 5: Öneri Yapılacak Kullanıcı ile En Benzer Davranışlı Kullanıcıların Belirlenmesi
# 6: Weighted Average Recommendation Score'un Hesaplanması
# 7: Çalışmanın Fonksiyonlaştırılması



#############################################
# Adım 1: Veriyi Anlama & Hazırlama
#############################################
import pandas as pd

pd.set_option('display.max_columns', None)              # DataFrame'in gösterilecek maksimum sütun sayısını belirler. (None ise tüm sütunlar gelir)
pd.set_option('display.width', 500)                     # Çıktının yanyana gelmesi için genişlik ayarlar.
pd.set_option("display.precision", 2)                   # Float türündeki sayıların gösterilecek ondalık basamak sayısını belirler.
pd.set_option('display.expand_frame_repr', False)       # Geniş Dataframe'lerin tamamını terminal penceresine sığdırmak için kullanılır.
pd.set_option("display.max_rows", 100)                  # DataFrame'in gösterilecek maksimum satır sayısını belirler.

movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')  # Veri seti: https://grouplens.org/datasets/movielens/
rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')

movie.head()
rating.head()

movie.shape   # 27 bin film
rating.shape  # 20 milyon oylama


# movie ve rating dataframe lerini birleştirelim
df = movie.merge(rating, how="left", on="movieId")
df.shape  # 20 milyon film oylamasi var
df.head()
#    movieId             title                                       genres  userId  rating            timestamp
# 0        1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     3.0     4.0  1999-12-11 13:36:47
# 1        1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     6.0     5.0  1997-03-13 17:50:52






######################################
# Adım 2: User-Movie Df'inin Oluşturulması
######################################

# Yeni bir df oluşturalım: Hangi film kaç kere oylanmış?
comment_counts = pd.DataFrame(df["title"].value_counts())
#                                            count
# title
# Pulp Fiction (1994)                        67310
# Forrest Gump (1994)                        66172
# Shawshank Redemption, The (1994)           63366


# rare_movies: 1000'den az kere oylanan filmlerin indexlerini getirelim (index te title lar var)
rare_movies = comment_counts.loc[comment_counts["count"] <= 1000, :].index
# Index(['Bear, The (Ours, L') (1988)', 'Rosewood (1997)', ...


# common_movies: 1000'den fazla kez oylanan filmleri getirelim (rare movies te olmayan filmler)
common_movies = df[~df["title"].isin(rare_movies)]
#           movieId                          title                                       genres    userId  rating            timestamp
# 0               1               Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy       3.0     4.0  1999-12-11 13:36:47
# 1               1               Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy       6.0     5.0  1997-03-13 17:50:52



df.shape               # 20 milyon film oylamasi vardi
common_movies.shape    # 17 milyon film oylamasi kaldi
df["title"].nunique()  # 27262 unique film ilk verisetinde vardı
common_movies["title"].nunique()  # 3159 unique film kaldi


# UserId-Movie Df: Pivot ile sütunlarda title, indexlerde userid, değerlerde rating olsun.
user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")





#############################################
# Adım 3: Öneri Yapılacak Kullanıcının İzlediği Filmlerin Belirlenmesi
#############################################

# Adım 1: Rastgele bir kullanıcı id'si seçiniz.
random_user = 108170     # veya: random_user = int(pd.Series(user_movie_df.index).sample(1, random_state=45).loc[0])

# Adım 2: random_user kullanıcısının filmlere verdiği puanları gösteriniz. (NaN: izlemediği filmler)
random_user_df = user_movie_df[user_movie_df.index == random_user]

# Adım 3: random_user kullanıcısının oy kullandığı filmleri, movies_watched adında bir listeye atayınız.
movies_watched = random_user_df.columns[random_user_df.notna().any()].tolist()   # .notna().any() , NaN olmayan değerleri getirir
# ['2001: A Space Odyssey (1968)', 'Adventures of Priscilla, Queen of the Desert, ...

# Kullanıcının izlediği film sayısını hesaplar.
len(movies_watched)   # 186





#############################################
# Adım 4: Aynı Filmleri İzleyen Diğer Kullanıcıların Verisine ve Id'lerine Erişmek
#############################################

# Adım 1: Seçilen kullanıcının izlediği fimlere ait sütunları, user_movie_df'ten seçiniz ve yeni bir dataframe oluşturunuz.
movies_watched_df = user_movie_df[movies_watched]

# Adım 2: Herbir kullanıcının, seçili user'in izlediği filmleri kaç kez izlediği bilgisini taşıyan, user_movie_count adında yeni bir dataframe oluşturunuz.
user_movie_count = movies_watched_df.T.notnull().sum()
user_movie_count = user_movie_count.reset_index()      # indeksi sıfırlar

# sütun adlarını değiştirir
user_movie_count.columns = ["userId", "movie_count"]
#           userId  movie_count
# 0            1.0           53
# 1            2.0           11
# 2            3.0           47

# en az 20 film izlemiş olan kullanıcıların id lerini içeren bir Seri oluşturur
users_same_movies = user_movie_count[user_movie_count["movie_count"] > 20]["userId"]
# users_same_movies
# 0              1.0
# 2              3.0
# 6              7.0


# Veya programatik bir şekilde yapmak istersek:
# Seçilen kullanıcının oy verdiği filmlerin yüzde 60 ve üstünü izleyenleri benzer kullanıcılar olarak görüyoruz.
perc = (len(movies_watched) * 60 / 100)
users_same_movies = user_movie_count.loc[user_movie_count["movie_count"] > perc, "userId"]
# users_same_movies
# 90            91.0
# 115          116.0

len(users_same_movies)   # 2326








#############################################
# Adım 5: Öneri Yapılacak Kullanıcı ile En Benzer Davranışlı Kullanıcıların Belirlenmesi
#############################################

# Bunun için 3 adım gerçekleştireceğiz:
# 1. Random user ve diğer kullanıcıların verilerini bir araya getireceğiz.
# 2. Korelasyon df'ini oluşturacağız.
# 3. En benzer bullanıcıları (Top Users) bulacağız


# Adım 1: user_same_movies listesi içerisindeki seçili user ile, benzerlik gösteren kullanıcıların id’lerinin bulunacağı şekilde movies_watched_df dataframe’ini filtreleyiniz.
final_df = movies_watched_df[movies_watched_df.index.isin(users_same_movies)]


# Adım 2: Kullanıcıların birbirleri ile ilgili olan korelasyonlarının bulunacağı yeni bir corr_df dataframe’i oluşturunuz.
corr_df = final_df.T.corr().unstack().sort_values().drop_duplicates()
# userId    userId
# 110130.0  72838.0    -0.58
# 33581.0   100618.0   -0.48
# 126121.0  89242.0    -0.48

corr_df = pd.DataFrame(corr_df, columns=["corr"])
corr_df.index.names = ['user_id_1', 'user_id_2']
corr_df = corr_df.reset_index()
#          user_id_1  user_id_2  corr
# 0         110130.0    72838.0 -0.58
# 1          33581.0   100618.0 -0.48
# 2         126121.0    89242.0 -0.48

# corr_df te random_user i filtreleyelim, diğer kullanıcılar ile korelasyonlarını görelim
corr_df[corr_df["user_id_1"] == random_user]
#          user_id_1  user_id_2  corr
# 11726     108170.0    89242.0 -0.14
# 15614     108170.0    25614.0 -0.12
# 20235     108170.0    12490.0 -0.11


# Adım 3: Seçili kullanıcı ile yüksek korelasyona sahip (0.65’in üzerinde olan) kullanıcıları filtreleyerek top_users adında yeni bir dataframe oluşturunuz.
top_users = corr_df[(corr_df["user_id_1"] == random_user) & (corr_df["corr"] >= 0.65)][["user_id_2", "corr"]].reset_index(drop=True)
top_users = top_users.sort_values(by='corr', ascending=False)
top_users.rename(columns={"user_id_2": "userId"}, inplace=True)
#      userId  corr
# 3    5155.0  0.72
# 2   11517.0  0.71



# Adım 4:  top_users dataframe’ini rating veri seti ile merge ediniz
top_users_ratings = top_users.merge(rating[["userId", "movieId", "rating"]], how='inner')
#        userId  corr  movieId  rating
# 0      5155.0  0.72        1     3.5
# 1      5155.0  0.72        2     3.0

# random_user ile aynı olmayan kullanıcıların derecelendirmelerini alır.
top_users_ratings = top_users_ratings[top_users_ratings["userId"] != random_user]
top_users_ratings["userId"].unique()
top_users_ratings.head()
#    userId  corr  movieId  rating
# 0  5155.0  0.72        1     3.5
# 1  5155.0  0.72        2     3.0




#############################################
# Adım 6: Weighted Average Recommendation Score'un Hesaplanması
#############################################

# Adım 1: Her bir kullanıcının corr ve rating değerlerinin çarpımından oluşan weighted_rating adında yeni bir değişken oluşturunuz.
top_users_ratings['weighted_rating'] = top_users_ratings['corr'] * top_users_ratings['rating']
#        userId  corr  movieId  rating  weighted_rating
# 0      5155.0  0.72        1     3.5             2.51
# 1      5155.0  0.72        2     3.0             2.15

# Adım 2: Film id’sive her bir filme ait tüm kullanıcıların weighted rating’lerinin ortalama değerini içeren recommendation_df adında yeni bir dataframe oluşturunuz.
recommendation_df = top_users_ratings.groupby('movieId').agg({"weighted_rating": "mean"})
recommendation_df = recommendation_df.reset_index()
#       movieId  weighted_rating
# 0           1             1.93
# 1           2             1.15


# Adım 3: recommendation_df içerisinde weighted rating'i 3.5'ten büyük olan filmleri seçiniz ve weighted rating’e göre sıralayınız.
recommendation_df[recommendation_df["weighted_rating"] > 3.5]
movies_to_be_recommend = recommendation_df[recommendation_df["weighted_rating"] > 3.5].sort_values("weighted_rating", ascending=False)
#       movieId  weighted_rating
# 79        223             3.58
# 747      2502             3.58
# 1635     8641             3.58

# Adım 4: Tavsiye edilen 5 filmin isimlerini getiriniz.
movies_to_be_recommend.merge(movie[["movieId", "title"]])["title"][:5]
# 0                                     Clerks (1994)
# 1                               Office Space (1999)
# 2      Anchorman: The Legend of Ron Burgundy (2004)
# 3                          Napoleon Dynamite (2004)
# 4    Mystery Science Theater 3000: The Movie (1996)





#############################################
# Adım 7: Çalışmanın Fonksiyonlaştırılması
#############################################

# Bu fonksiyon, userid-title (kullanıcı-film) etkileşimlerini içeren bir tablo oluşturur.
def create_user_movie_df():
    import pandas as pd
    movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
    rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')
    df = movie.merge(rating, how="left", on="movieId")                      # movie ve rating df lerini birleştirir
    comment_counts = pd.DataFrame(df["title"].value_counts())               # her film için yapılan yorum/puanlama sayısını hesaplar
    rare_movies = comment_counts.loc[comment_counts["count"] <= 1000, :].index     # 1000'den az kere oylanan filmleri getirelim
    common_movies = df[~df["title"].isin(rare_movies)]                      # rare_movies te olmayan tüm filmleri getirelim (1000'den fazla kez oylanan filmler)
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating") # kullanıcı-film etkileşimlerini içeren bir tablo oluşturur
    return user_movie_df

user_movie_df = create_user_movie_df()


# perc = len(movies_watched) * 60 / 100
# users_same_movies = user_movie_count[user_movie_count["movie_count"] > perc]["userId"]


def user_based_recommender(random_user, user_movie_df, ratio=60, cor_th=0.65, score=3.5):
    import pandas as pd
    random_user_df = user_movie_df[user_movie_df.index == random_user]
    movies_watched = random_user_df.columns[random_user_df.notna().any()].tolist()
    movies_watched_df = user_movie_df[movies_watched]
    user_movie_count = movies_watched_df.T.notnull().sum()
    user_movie_count = user_movie_count.reset_index()
    user_movie_count.columns = ["userId", "movie_count"]
    perc = len(movies_watched) * ratio / 100
    users_same_movies = user_movie_count[user_movie_count["movie_count"] > perc]["userId"]

    final_df = pd.concat([movies_watched_df[movies_watched_df.index.isin(users_same_movies)],
                          random_user_df[movies_watched]])

    corr_df = final_df.T.corr().unstack().sort_values().drop_duplicates()
    corr_df = pd.DataFrame(corr_df, columns=["corr"])
    corr_df.index.names = ['user_id_1', 'user_id_2']
    corr_df = corr_df.reset_index()

    top_users = corr_df[(corr_df["user_id_1"] == random_user) & (corr_df["corr"] >= cor_th)][
        ["user_id_2", "corr"]].reset_index(drop=True)

    top_users = top_users.sort_values(by='corr', ascending=False)
    top_users.rename(columns={"user_id_2": "userId"}, inplace=True)
    rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')
    top_users_ratings = top_users.merge(rating[["userId", "movieId", "rating"]], how='inner')
    top_users_ratings['weighted_rating'] = top_users_ratings['corr'] * top_users_ratings['rating']

    recommendation_df = top_users_ratings.groupby('movieId').agg({"weighted_rating": "mean"})
    recommendation_df = recommendation_df.reset_index()

    movies_to_be_recommend = recommendation_df[recommendation_df["weighted_rating"] > score].sort_values("weighted_rating", ascending=False)
    movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
    return movies_to_be_recommend.merge(movie[["movieId", "title"]])



random_user = int(pd.Series(user_movie_df.index).sample(1).values)
user_based_recommender(random_user, user_movie_df, cor_th=0.70, score=4)


