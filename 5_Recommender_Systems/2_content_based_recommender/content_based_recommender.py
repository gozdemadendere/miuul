#############################
# Content Based Recommendation (İçerik Temelli Tavsiye)
#############################

# Kullanıcının geçmiş tercihlerine bakarak, ürün içerikleri üzerinden tavsiyeler sunar.
# Ürünlerin sahip olduğu özelliklere ve içeriğe odaklanır. Örneğin, bu özellikler film açıklaması, film türü, oyuncular, yönetmenler, kitap açıklaması, kitap yazarı, konu vb. olabilir.
# Düşük veri gereksinimine sahiptir ve kullanıcı tercihlerini anlama konusunda iyidir; sadece ürün özelliklerine dayalıdır.
# Örnek: Trendyol'da Smeg kahve makinesi satın alan bir kullanıcıya, benzer tarzda kahve makineleri veya aynı markanın diğer ürünleri gibi benzer içeriklere sahip ürünler önerilebilir.


# Metin vektörleştirme (TF-IDF):  Kelimelerin sıklığını ve belirli bir belgede geçme sayısını tespit eder. TF-IDF = TF x IDF ( NLP konusudur)
# TF (Terim Frekansı) “Term Frequency” : Bir terimin bir belgede ne sıklıkta geçtiğini ölçer. Örneğin, “makine” kelimesinin bir belgede 10 kez geçtiyse ve toplam terim sayısı 100 ise TF(makine) = 10/100
# IDF (Belge Frekansı) “Inverse Document Frequency” : Bir terimin koleksiyondaki diğer belgelerde ne kadar yaygın olduğunu ölçer.

# Öklid uzaklığı: İki metin arasındaki uzaklık, Cosine Similarity: İki metin arasındaki benzerliği ölçmek için.

# Elimizde 100 tane film var, filmler indexlerde yer alır, içerisindeki unique kelimeler çıkarılır, sütunlara konulur, hangi filmde kaç kere geçtiği yazılır, ve benzerlikleri hesaplanır.
# Böylece film-kelime matrisi ile, filmler arasındaki benzerlikler hesaplanır.


#############################
# Film Açıklamalarına Göre Tavsiye Geliştirme
#############################

# PROJE ADIMLARI
# 1. Veriyi Anlama & Hazırlama
# 2. TF-IDF Matrisinin Oluşturulması
# 3. Cosine Similarity Matrisinin Oluşturulması
# 4. Benzerliklere Göre Önerilerin Yapılması
# 5. Çalışma Scriptinin Hazırlanması




#################################
# 1. Veriyi Anlama & Hazırlama
#################################

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pd.set_option('display.max_columns', None)              # DataFrame'in gösterilecek maksimum sütun sayısını belirler. (None ise tüm sütunlar gelir)
pd.set_option('display.width', 500)                     # Çıktının yanyana gelmesi için genişlik ayarlar.
pd.set_option("display.precision", 2)                   # Float türündeki sayıların gösterilecek ondalık basamak sayısını belirler.
pd.set_option('display.expand_frame_repr', False)       # Geniş Dataframe'lerin tamamını terminal penceresine sığdırmak için kullanılır.
pd.set_option("display.max_rows", 100)                  # DataFrame'in gösterilecek maksimum satır sayısını belirler.

df = pd.read_csv("datasets/the_movies_dataset/movies_metadata.csv", low_memory=False)  # DtypeWarning kapamak icin
# https://www.kaggle.com/rounakbanik/the-movies-dataset

df.head()
df.shape  # (45466, 24)
df.info()
df["overview"].isnull().sum()
df["overview"].head()





#################################
# 2. TF-IDF Matrisinin Oluşturulması
#################################

# TF-IDF matrisi, içerik tabanlı öneri sistemleri için metin verilerini temsil etmek ve analiz etmek için kullanılır.
# Bu matris, belgelerdeki kelimelerin önemini belirlemek ve belgeler arasındaki benzerlikleri hesaplamak için kullanılır.

# stop_words="english" parametresi, İngilizce dilinde sık kullanılan kelimelerin (and, the, on gibi..) kullanılmayacağını belirtir.
tfidf = TfidfVectorizer(stop_words="english")

# overview değişkenindeki Null değerleri boşluk ile dolduralım
df['overview'] = df['overview'].fillna('')

# Bu matris, overview değişkenindeki kelimelerin TF-IDF skorlarını içerir. Bu skorlar, her bir kelimenin önemini belirtir.
tfidf_matrix = tfidf.fit_transform(df['overview'])

tfidf_matrix.shape # 45466 film, 75827 eşsiz kelime
df['title'].shape  # 45466

# Bu metod, vektörize edilen özelliklerin isimlerini almamızı sağlar
tfidf.get_feature_names_out()

# Bu metod, TF-IDF matrisini bir NumPy dizisine dönüştürür
tfidf_matrix.toarray()





#################################
# 3. Cosine Similarity Matrisinin Oluşturulması
#################################

# Kosinüs benzerliği, iki metin arasındaki açıyı temel alarak metinlerin benzerliğini ölçer.
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

cosine_sim.shape  # (45466, 45466)
cosine_sim[1]     #





#################################
# 4. Benzerliklere Göre Önerilerin Yapılması
#################################

# indices adında bir Seri oluşturur, bu Seri film başlıklarının indekslerini tutar.
indices = pd.Series(df.index, index=df['title'])

# title lardaki çoklamaları silelim, ve en sondaki kalsın
indices = indices[~indices.index.duplicated(keep='last')]

indices["Sherlock Holmes"]  # sadece en sondaki index kaldı

# "Sherlock Holmes" filmi ile diğer tüm filmlerin benzerlik skorlarını elde edelim
movie_index = indices["Sherlock Holmes"]
cosine_sim[movie_index]

# Benzerlik skorlarını bir DataFrame'e dönüştürelim. Her bir benzerlik skoru "score" sütununda yer alsın.
similarity_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])

# "Sherlock Holmes" ile en çok benzerliğe sahip olan filmlerin ındex bilgileri:
movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index

# Bu kod parçası, "Sherlock Holmes" filmine benzer olan diğer filmlerin başlıklarını getirir.
df['title'].iloc[movie_indices]




#################################
# 5. Çalışma Scriptinin Hazırlanması
#################################

# Bu fonksiyon, içerik tabanlı bir film öneri sistemi oluşturur.
def content_based_recommender(title, cosine_sim, dataframe):
    # index'leri olusturma
    indices = pd.Series(dataframe.index, index=dataframe['title'])       # indices adında bir Seri oluşturur, bu Seri film başlıklarının indekslerini tutar.
    indices = indices[~indices.index.duplicated(keep='last')]            # title lardaki çoklamaları silelim, ve en sondaki kalsın

    # title'ın index'ini yakalama
    movie_index = indices[title]

    # title'a gore benzerlik skorlarını hesaplama
    similarity_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])

    # kendisi haric ilk 10 filmi getirme
    movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index      # en yüksek benzerlik skorlarına sahip ilk 10 film, movie_indices kullanılarak seçilir
    return dataframe['title'].iloc[movie_indices]

content_based_recommender("Sherlock Holmes", cosine_sim, df)
content_based_recommender("The Matrix", cosine_sim, df)
content_based_recommender("The Godfather", cosine_sim, df)
content_based_recommender('The Dark Knight Rises', cosine_sim, df)



# Bu fonksiyon, bir veri çerçevesindeki film özetlerinin kullanılarak kosinüs benzerlik matrisini hesaplar.
def calculate_cosine_sim(dataframe):
    tfidf = TfidfVectorizer(stop_words='english')   # TfidfVectorizer kullanarak film özetlerinden TF-IDF matrisini oluşturur
    dataframe['overview'] = dataframe['overview'].fillna('')
    tfidf_matrix = tfidf.fit_transform(dataframe['overview'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)  # cosine_similarity fonksiyonunu kullanarak bu TF-IDF matrisi üzerinde kosinüs benzerlik matrisini hesaplar.
    return cosine_sim   # hesaplanan benzerlik matrisini döndürür


cosine_sim = calculate_cosine_sim(df)
content_based_recommender('The Dark Knight Rises', cosine_sim, df)
# 1 [90, 12, 23, 45, 67]
# 2 [90, 12, 23, 45, 67]




# Notlar:
# Daha büyük ölçekli bir iş olursa, veritabanı seviyesinde nasıl gerçekleştiririz?
# Kullanıcıların en fazla izlediği 100 film belirlenir, indirgenir, 100 film için de bir öneri seti oluşturururz, bir tabloda tutarız.
# Film idlerinin yanına, önermek istediğimiz film idlerini yazarız.
