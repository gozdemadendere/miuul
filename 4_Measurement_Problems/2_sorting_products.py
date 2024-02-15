###################################################
# Sorting Products (Ürünlerin sıralanması )
###################################################

# İş bilgisi açısından dikkate alınacak faktörler belirlenmeli
# Eğer 1'den fazla faktör varsa, faktörler önce standartlaştırılmalı, sonra faktörlere ağırlık verilmeli
# İstatistiksel bazı yöntemler de baz alınmalı ancak tek başına değil, kendi iş bilgimiz dahilinde belirlediğimiz yöntem ile harmanlanmalı,
# Yani farklı yöntemleri kullanıp, onlara ağırlık vererek sonuca ulaşmalıyız



# 1) Sorting by Rating   (Puanlamaya göre sıralama)
# 2) Sorting by Comment Count or Purchase Count   (Yorum sayısı veya Satın alım sayısına göre sıralama)
# 3) Sorting by Rating, Comment Count and Purchase Count ** (wss: weighted_sorting_score)  (Puanlama & Yorum sayısı & Satın alım sayısına göre sıralama)
# 4) Sorting by Bayesian Average Rating Score: Bar_Score (Sadece Rating e göre bilimsel bir sıralama)
# 5) Hybrid Sorting: Bayesian + Diğer Faktorleri bir araya getirmek (bar_score + wss_score (Rating, Comment count, Purchase count))
# 6) Uygulama: IMDB Movie Scoring & Sorting


###################################################
# Uygulama: Kurs Sıralama
###################################################

# import the libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

pd.set_option("display.max_columns", None)  # DataFrame'in gösterilecek maksimum sütun sayısı (None ise tüm sütunlar gelir)
pd.set_option("display.max_rows", 100)      # DataFrame'in gösterilecek maksimum satır sayısı
pd.set_option('display.width', 500)         # Çıktının yanyana gelmesi için genişlik ayarlar.
pd.set_option("display.precision", 2)       # Float türündeki sayıların gösterilecek ondalık basamak sayısını belirler.
pd.set_option('display.expand_frame_repr', False)  # DataFrame'in tamamını bir satırda gösterir.
# pd.set_option('display.float_format', lambda x: '%.5f' % x)

# read the data
df = pd.read_csv("/Users/gozdemadendere/Desktop/PycharmProjects/Measurement_Problems/datasets/product_sorting.csv")

####################
# Exploratory Data Analysis Function : Displays basic characteristics of the DataFrame.
def check_df(dataframe, head=5):
    print("__________________________________________________________________ FIRST 5 ROWS __________________________________________________________________ ")
    print(dataframe.head(head))
    print("__________________________________________________________________  LAST 5 ROWS __________________________________________________________________ ")
    print(dataframe.tail(head))
    print("__________________________________________________________________  DATA SHAPE ___________________________________________________________________ ")
    print(dataframe.shape)
    print("_________________________________________________________________  GENERAL INFO __________________________________________________________________ ")
    print(dataframe.info())
    print("__________________________________________________________________  NULL VALUES __________________________________________________________________ ")
    print(dataframe.isnull().sum().sort_values(ascending=False))
    print("_______________________________________________________________  DUPLICATED VALUES _______________________________________________________________ ")
    print(dataframe.duplicated().sum())
    print("____________________________________________________________________ DESCRIBE ____________________________________________________________________ ")
    print(dataframe.describe([0, 0.05, 0.1, 0.25, 0.50, 0.95, 0.99, 1]).T)

# Use the function
check_df(df)

####################





########################################
# 1) Sorting by Rating
########################################

df.sort_values("rating", ascending=False).head(20)



########################################
# 2) Sorting by Comment Count or Purchase Count
########################################

df.sort_values("purchase_count", ascending=False).head(20)
df.sort_values("commment_count", ascending=False).head(20)



########################################
# 3) Sorting by Rating, Comment, Purchase (wss: weighted_sorting_score)
########################################

# Rating 1-5 aralığında olduğu için, Comment count ve Purchase count u da 1-5 aralığına ölçeklendirmeliyiz.

# purchase_count sütunundaki değerleri, Min-Max ölçeklendirme yöntemiyle 1 ile 5 arasında bir aralığa ölçeklendirelim ((standartlaştırma işlemi)
df["purchase_count_scaled"] = MinMaxScaler(feature_range=(1, 5)). \
    fit(df[["purchase_count"]]). \
    transform(df[["purchase_count"]])


# commment_count sütunundaki değerleri, Min-Max ölçeklendirme yöntemiyle 1 ile 5 arasında bir aralığa ölçeklendirelim (standartlaştırma işlemi)
df["comment_count_scaled"] = MinMaxScaler(feature_range=(1, 5)). \
    fit(df[["commment_count"]]). \
    transform(df[["commment_count"]])


# Ağırlıklı ortalama hesaplayalım: Rating, Comment count, Purchase count bazında
(df["comment_count_scaled"] * 32 / 100 + df["purchase_count_scaled"] * 26 / 100 + df["rating"] * 42 / 100)    # (Toplamda %100 olmalı!)


# Fonksiyon haline getirelim
def weighted_sorting_score(dataframe, w1=32, w2=26, w3=42):
    return (dataframe["comment_count_scaled"] * w1 / 100 +
            dataframe["purchase_count_scaled"] * w2 / 100 +
            dataframe["rating"] * w3 / 100)


# dataframe in içine, fonksiyondan gelen tek sütunu, aktaralım
df["weighted_sorting_score"] = weighted_sorting_score(df)

# weighted_sorting_score sütununa göre sıralayalım
df.sort_values("weighted_sorting_score", ascending=False).head(20)

df[df["course_name"].str.contains("Veri Bilimi")].sort_values("weighted_sorting_score", ascending=False).head(20)






########################################
# 4) Bayesian Average Rating Score
########################################

# Bayesian Average Rating Score, sadece kullanıcıların verdiği puanları (rating) dikkate alarak ürünleri sıralamak için kullanılan bir yöntemdir.
# Bu yöntem, ürünlerin puanlarını hesaplarken, her ürün için belirli bir alt-üst limit ve bir güven aralığı belirler.  Bu güven aralığı, o ürünün aldığı puanların ne kadar güvenilir olduğunu ifade eder.

# Yeni-başarılı-ümit vaadeden ürünler de öne çıkabiliyor, bu nedenle bu faktörü de baz almak sonuçları daha faydalı hale getirir!
# Bayesian sıralama ile mesela, IK cıyız, işe alacağımız kişilere ait 3 özellik seçip, min max scaler ile özellikleri standartlaştırıp, ardından bu 3 özelliğe göre Bayesian score hesaplayabiliriz.

# Bayesian ortalama formülü: Puan dağılımlarının üzerinden, ağırlıklı bir şekilde olasılıksal ortalama hesabı yapar. Orijinal puanı bir miktar kırpar.
# Bu nedenle direkt bu hesaplamayı kullanmak yerine, bu hesaplamayı da dahil ettiğimiz bir ağırlıklı ortalama hesaplayabiliriz. (5. adımda)


# import the libraries
import pandas as pd
import math
import scipy.stats as st

# Sorting Products with 5 Star Rated
# Sorting Products According to Distribution of 5 Star Rating


# Bayesian ortalama formülü: Puan dağılımlarının üzerinden, ağırlıklı bir şekilde olasılıksal ortalama hesabı yapar.
def bayesian_average_rating(n, confidence=0.95):
    if sum(n) == 0:
        return 0
    K = len(n)
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    N = sum(n)
    first_part = 0.0
    second_part = 0.0
    for k, n_k in enumerate(n):
        first_part += (k + 1) * (n[k] + 1) / (N + K)
        second_part += (k + 1) * (k + 1) * (n[k] + 1) / (N + K)
    score = first_part - z * math.sqrt((second_part - first_part * first_part) / (N + K + 1))
    return score

df.head()



# Bayesian formülü ile bilimsel, olasılıksal bir puan hesaplama sütunu oluşturalım : sadece ratinglere (kurs puanlarına) odaklanarak bir sıralama yapmak istersek

# df.apply(lambda x:)  ile bar_score isimli yeni br sütun oluştur, x: yeni sütundaki değerler:
# df den, 1_point den 5_point e dek bayesian_average_rating fonksiyonunu uygula
# x[["1_point", "2_point", "3_point", "4_point", "5_point"]] ifadesi, her bir satırdaki "1_point", "2_point", "3_point", "4_point" ve "5_point" sütunlarına erişmek için kullanılır.
df["bar_score"] = df.apply(lambda x: bayesian_average_rating(x[["1_point", "2_point", "3_point", "4_point", "5_point"]]), axis=1)

df.sort_values("bar_score", ascending=False).head(20)
df.sort_values("weighted_sorting_score", ascending=False).head(20)



df[df["course_name"].index.isin([5, 1])].sort_values("bar_score", ascending=False)
# veya df.loc[df["course_name"].index.isin([5, 1])].sort_values("bar_score", ascending=False)






########################################
# 5) Hybrid Sorting:
########################################

# Hybrid Sorting, birden fazla sıralama yöntemini bir araya getirerek daha kapsamlı bir sıralama sonucu oluşturur.
# Burada, bar_score + wss_score (rating,comment count, purchase count) faktörlerini baz alacağız.

# bar_score, verisetinde yeni olsa da potansiyel iyi olanları da yukarı çıkarır
def hybrid_sorting_score(dataframe, bar_w=60, wss_w=40):
    bar_score = dataframe.apply(lambda x: bayesian_average_rating(x[["1_point",
                                                                     "2_point",
                                                                     "3_point",
                                                                     "4_point",
                                                                     "5_point"]]), axis=1)
    wss_score = weighted_sorting_score(dataframe)

    return bar_score*bar_w/100 + wss_score*wss_w/100

# dataframe in içine, fonksiyondan gelen tek sütunu, aktaralım
df["hybrid_sorting_score"] = hybrid_sorting_score(df)

df.sort_values("hybrid_sorting_score", ascending=False).head(20)

df[df["course_name"].str.contains("Veri Bilimi")].sort_values("hybrid_sorting_score", ascending=False).head(20)






############################################
# Uygulama: IMDB Movie Scoring & Sorting
############################################

import pandas as pd
import math
import scipy.stats as st
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df = pd.read_csv("datasets/movies_metadata.csv",
                 low_memory=False)  # DtypeWarning kapamak icin

df = df[["title", "vote_average", "vote_count"]]

df.head()
df.shape




########################
# Vote Average'a Göre Sıralama
########################

df.sort_values("vote_average", ascending=False).head(20)

# veya vote_count a göre sıralama
df["vote_count"].describe([0.10, 0.25, 0.50, 0.70, 0.80, 0.90, 0.95, 0.99]).T
df[df["vote_count"] > 400].sort_values("vote_average", ascending=False).head(20)




from sklearn.preprocessing import MinMaxScaler

# vote_count sütunundaki değerleri, 1 ile 10 arasında bir aralığa ölçeklendirelim
df["vote_count_score"] = MinMaxScaler(feature_range=(1, 10)). \
    fit(df[["vote_count"]]). \
    transform(df[["vote_count"]])




########################
# vote_average * vote_count
########################

df["average_count_score"] = df["vote_average"] * df["vote_count_score"]

df.sort_values("average_count_score", ascending=False).head(20)



########################
# IMDB Weighted Rating
########################

# 2 filmin oy puanı aynı ise, oy sayısı fazla olan daha önce çıkar.


# weighted_rating = (v/(v+M)*r) + (M/(v+M)*C)

# r = vote average                                            (ilgili filmin oy ortalamasi)
# v = vote count                                              (ilgili filmin oy sayisi)
# M = minimum votes required to be listed in the Top 250      (siralamaya girebilmek icin gerekli olan minimum oy sayisi)
# C = the mean vote across the whole report (currently 7.0)   (tum filmlerin genel ortalamasi)



## Film 1:
# r = 8         (ilgili filmin oy ortalamasi/ort puan)
# M = 500       (siralamaya girebilmek icin gerekli olan minimum oy sayisi)
# v = 1000      (ilgili filmin oy sayisi)
# (v/(v+M)*r) = (1000 / (1000+500))*8 = 5.33


## Film 2:
# r = 8
# M = 500
# v = 3000
# (v/(v+M)*r) =  (3000 / (3000+500))*8 = 6.85    #Film 1 ve 2 ayni oy puanina sahip (8), ama film 2 daha fazla oy sayisina sahip, bu nedenle 6.85 daha iyi cikti


# Diyelim ki filmin puanı 9.5 olsun, oy sayısı az olduğu için, üstteki Film 2.yi geçemedi
# (v/(v+M)*r) = (1000 / (1000+500))*9.5 = 6.33



## Film 1:
# r = 8
# M = 500
# v = 1000
# C = 7

# Birinci bölüm:
# (v/(v+M)*r) =  (1000 / (1000+500))*8 = 5.33

# İkinci bölüm:
# (M/(v+M)*C) = 500/(1000+500) * 7 = 2.33

# Toplam = 5.33 + 2.33 = 7.66



## Film 2:
# r = 8
# M = 500
# v = 3000

# Birinci bölüm:
# (v/(v+M)*r) =  (3000 / (3000+500))*8 = 6.85

# İkinci bölüm:
# (M/(v+M)*C) = 500/(3000+500) * 7 = 1

# Toplam = 7.85


M = 2500                         # siralamaya girebilmek icin gerekli olan minimum oy sayisi
C = df['vote_average'].mean()    # tum filmlerin genel oy ortalamasi

# IMDB formülü ile, fonksiyon oluşturalım
def weighted_rating(r, v, M, C):
    return (v / (v + M) * r) + (M / (v + M) * C)

df.sort_values("average_count_score", ascending=False).head(10)

# birkac degerlerini bildigimiz film icin denemeler yapalim
weighted_rating(7.40000, 11444.00000, M, C)

weighted_rating(8.10000, 14075.00000, M, C)

weighted_rating(8.50000, 8358.00000, M, C)

# dataframe içine weighted_rating değişkenini ekleyelim, weighted_rating fonksiyonunu vote_average ve vote_count sütunlarına uygulatalım
df["weighted_rating"] = weighted_rating(df["vote_average"],
                                        df["vote_count"], M, C)

df.sort_values("weighted_rating", ascending=False).head(10)





####################
# Bayesian Average Rating Score
####################

# Bu yöntem ile, IMDB rating lerini sıralayalım

# Ilk 5 film:
# 12481                                    The Dark Knight
# 314                             The Shawshank Redemption
# 2843                                          Fight Club
# 15480                                          Inception
# 292                                         Pulp Fiction


def bayesian_average_rating(n, confidence=0.95):
    if sum(n) == 0:
        return 0
    K = len(n)
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    N = sum(n)
    first_part = 0.0
    second_part = 0.0
    for k, n_k in enumerate(n):
        first_part += (k + 1) * (n[k] + 1) / (N + K)
        second_part += (k + 1) * (k + 1) * (n[k] + 1) / (N + K)
    score = first_part - z * math.sqrt((second_part - first_part * first_part) / (N + K + 1))
    return score

# Esaretin bedeli icin, puanlarin dagilimlarini manuel girelim (kactane 1 yildiz...kac tane 10 yildiz almis degerleri)
# 9,14 olarak hesapladi, IMDB'de de 9,3 gorunuyor, gayet yakin
bayesian_average_rating([34733, 4355, 4704, 6561, 13515, 26183, 87368, 273082, 600260, 1295351])

# Baba filmi icin, puanlarin dagilimlarini manuel girelim
# 8,94 olarak hesapladi, IMDB'de de 9,2 gorunuyor, gayet yakin, biraxz kirpilmis
bayesian_average_rating([37128, 5879, 6268, 8419, 16603, 30016, 78538, 199430, 402518, 837905])

# Bu datasetinde puan dagilimlari var (kactane 1 yildiz...kac tane 10 yildiz almis degerleri)
df = pd.read_csv("datasets/imdb_ratings.csv")
df = df.iloc[0:, 1:]

# bayesian_average_rating fonksiyonunu kullanarak, bar_score sutunu olusturalim, x: one two.. yildiz olacak
df["bar_score"] = df.apply(lambda x: bayesian_average_rating(x[["one", "two", "three", "four", "five",
                                                                "six", "seven", "eight", "nine", "ten"]]), axis=1)
df.sort_values("bar_score", ascending=False).head(20)


# Weighted Average Ratings
# IMDb publishes weighted vote averages rather than raw data averages.
# The simplest way to explain it is that although we accept and consider all votes received by users,
# not all votes have the same impact (or ‘weight’) on the final rating.

# When unusual voting activity is detected,
# an alternate weighting calculation may be applied in order to preserve the reliability of our system.
# To ensure that our rating mechanism remains effective,
# we do not disclose the exact method used to generate the rating.
#
# See also the complete FAQ for IMDb ratings.