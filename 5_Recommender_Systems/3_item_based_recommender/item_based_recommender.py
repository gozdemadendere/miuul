###########################################
# Item-Based Collaborative Filtering
###########################################

# Collaborative Filtering: Topluluğun kullanıcı veya ürün bazında ortak kanaatlerini yansıtan öneriler sunulur. (User based, Item based, Hybrid Model. Korelasyon kullanılır!)

# Item-Based Collaborative Filtering
# Bir ürünün özelliklerine dayanarak, benzer ürünler önerir.  Kullanıcıların geçmiş tercihlerine bakmak yerine, bir ürünün diğer ürünlerle olan benzerliklerine odaklanır.
# Özetle, content-based recommendation kullanıcıların önceki tercihlerine dayanırken, item-based recommendation ise ürünlerin özelliklerine dayanır.
# Kullanıcı bilgilerine ihtiyaç var: UserID x Ürün dataframe'ine ihtiyaç var.
# Örnek: Trendyol'da "Benzer Ürünler" sunulması: Smeg kahve makinesine bakan bir kullanıcıya, farklı kahve makineleri veya Smeg marka diğer ürünler önerilebilir.



# PROJE ADIMLARI
# 1: Veriyi Anlama & Hazırlama
# 2: User-Movie Df'inin Oluşturulması
# 3: Item-Based Film Önerilerinin Yapılması
# 4: Çalışma Scriptinin Hazırlanması


######################################
# Adım 1: Veri Setinin Hazırlanması
######################################
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




######################################
# Adım 3: Item-Based Film Önerilerinin Yapılması
######################################

# Örnek 1:
# 2 film arasındaki korelasyona bakarsak filmler arasındaki benzerlikleri buluruz.
movie_name = user_movie_df["Matrix, The (1999)"]
# userId
# 1.0         NaN
# 2.0         NaN
# 3.0         5.0

# user_movie_df deki tüm filmlerle, movie_name değişkenindeki film arasındaki korelasyonu hesaplar
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)
# title
# Matrix, The (1999)                                           1.00
# Matrix Reloaded, The (2003)                                  0.52
# Matrix Revolutions, The (2003)                               0.45
# Animatrix, The (2003)                                        0.37


# Örnek 2:
# user_movie_df içinde sütunlardan birini (filmlerden birini) "rastgele" seçer.
movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]
movie_name = user_movie_df[movie_name]
# userId
# 1.0        NaN
# 2.0        NaN
# 3.0        NaN

# movie_name de yer alam filmle diğer filmlerin benzerliklerinin hesaplanması:
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)
# title
# High School High (1996)                      1.00
# Mr. Nobody (2009)                            0.97
# Calendar Girls (2003)                        0.60



# Örnek 3:
# Alttaki kullanıcının en son izlediği ve en yüksek puan verdiği filmin adına göre Item-Based öneri yapınız.
user = 108170

# Kullanıcının 5 puan verdiği filmlerden, puanı en güncel olan filmin id'sinin alınız.
movie_id = rating.loc[(rating["userId"] == user) & (rating["rating"] == 5.0)].sort_values(by="timestamp", ascending=False).iloc[0,1]
# 7044

# movie df inde, movie_id: 7044 olanin title ini getir
movie.loc[movie["movieId"] == movie_id, "title"].values[0]
# 'Wild at Heart (1990)'

# user_movie_df dataframe’ini, seçilen film id’sine göre filtreleyiniz.
movie_df = user_movie_df.loc[:, movie.loc[movie["movieId"] == movie_id, "title"].values[0]]
# userId
# 1.0        NaN
# 2.0        NaN
# 3.0        NaN

# movie_df de yer alam filmle diğer filmlerin benzerliklerinin hesaplanması:
user_movie_df.corrwith(movie_df).sort_values(ascending=False).head(10)
# title
# Wild at Heart (1990)                     1.00
# My Science Project (1985)                0.57
# Mediterraneo (1991)                      0.54



# Bu fonksiyon, belirli bir kelimeyi içeren filmleri dataframe'den bulur.
# user_movie_df veri çerçevesindeki sütunları dolaşır ve belirtilen anahtar kelimeyi içeren sütunları bir liste olarak döndürür.
def check_film(keyword, user_movie_df):
    return [col for col in user_movie_df.columns if keyword in col]

check_film("Insomnia", user_movie_df)  # ['Insomnia (1997)', 'Insomnia (2002)']
check_film("Vita", user_movie_df)      # ['Dolce Vita, La (1960)', 'Life Is Beautiful (La Vita è bella) (1997)']






######################################
# Adım 4: Çalışma Scriptinin Hazırlanması
######################################

# Bu fonksiyon, UserId-Movie dataframe'ini oluşturur ve değerlerde rating'leri içerir.
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


# Bu fonksiyon, ismi girilen filme 10 adet benzer film önerisi sunar. (Film ile dataframe'deki diğer filmler arasındaki korelasyonu / benzerliği hesaplar ve en benzer filmleri getirir.)
def item_based_recommender(movie_name, user_movie_df):
    movie_name = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)

item_based_recommender("Matrix, The (1999)", user_movie_df)

# rasgele bir film adını seçerek aynı fonksiyonu tekrar çağırıyoruz
movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]
item_based_recommender(movie_name, user_movie_df)





