###################################################
# Measurement Problems
###################################################

# Bir müşterinin satın alma kararlarını etkileyen faktörler: Ürün Puanı, Müşteri Yorumları, Social Proof, Fiyat-Performans Dengesi, Görsel Sunum
# Sosyal Kanıt (Social Proof): Müşterilerin ürüne verdiği tepkileri anlamak için yorumlar, puanlar ve ürün incelemeleri gibi unsurların değerlendirilmesi.
# The Wisdom of Crowds: Geniş kitlelerin toplu görüşleri ve tercihleri.
# Ürün Puanı ve Puan Sayısı İlişkisi: Bir ürünün puanına ek olarak puan sayısının da dikkate alınması önemlidir. Çünkü yüksek puanlı bir ürün, az sayıda değerlendirilmiş olabilir.


# Ürün Değerlendirme ve Sıralama Süreçleri:
# Ürünlerin puanlarının hesaplanması (Rating Products)
# Ürünlerin sıralanması              (Sorting Products)
# Müşteri yorumlarının sıralanması   (Sorting Reviews)
# Sayfa etkileşim alanlarının analiz edilmesi / tasarlanması




###################################################
# Rating Products  (Ürünlerin puanlarının hesaplanması)
###################################################

# 1) Average
# 2) Time-Based Weighted Average                (Yeni, başarılı ve trend olan ürünlerin öne çıkabilmesi için zamansal bir şekilde ortalama alma)
# 3) User-Based Weighted Average                (Güvenilir kullanıcıların ağırlıklarının ortalama üzerinde daha fazla etkisi olduğu bir ortalama alma)
# 4) Weighted Rating (Time based & User based)  (Hem yeni ve başarılı ürünleri, hem güvenilir kullanıcıların oylarını birlikte ağırlandırarak karma bir ortalama alma)



############################################
# Uygulama: Kullanıcı ve Zaman Ağırlıklı Kurs Puanı Hesaplama
############################################

# import the libraries
import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler

pd.set_option("display.max_columns", None)  # DataFrame'in gösterilecek maksimum sütun sayısı (None ise tüm sütunlar gelir)
pd.set_option("display.max_rows", 100)      # DataFrame'in gösterilecek maksimum satır sayısı
pd.set_option('display.width', 500)         # Çıktının yanyana gelmesi için genişlik ayarlar.
pd.set_option("display.precision", 2)       # Float türündeki sayıların gösterilecek ondalık basamak sayısını belirler.
pd.set_option('display.expand_frame_repr', False)  # DataFrame'in tamamını bir satırda gösterir.
# pd.set_option('display.float_format', lambda x: '%.5f' % x)


# (50+ Saat) Python A-Z™: Veri Bilimi ve Machine Learning
# Puan: 4.8 (4.764925)
# Toplam Puan: 4611
# Puan Yüzdeleri: 75, 20, 4, 1, <1
# Yaklaşık Sayısal Karşılıkları: 3458, 922, 184, 46, 6

# read the data
df = pd.read_csv("/Users/gozdemadendere/Desktop/PycharmProjects/Measurement_Problems/datasets/course_reviews.csv")
df.head(10)
df.shape

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

# Kategorik değişken bazlı dağılımlar
df["Rating"].value_counts()
df["Questions Asked"].value_counts()

# Sorulan soru kırılımında verilen puan ortalamaları
df.groupby("Questions Asked").agg({"Questions Asked": "count", "Rating": "mean"})






####################
# 1) Average
####################
# Rating değişkenine ait genel ortalama
df["Rating"].mean()





####################
# 2) Time-Based Weighted Average
####################

# Puan Zamanlarına Göre Ağırlıklı Ortalama: Yeni, başarılı ve trend olan ürünlerin öne çıkabilmesi için, zamansal bir şekilde ortalama alma yöntemidir.
# Bu yöntem, daha güncel verilerin, eski verilere kıyasla daha fazla ağırlığa sahip olduğu bir hesaplama yöntemidir.
# Direkt ortalama alırsak, bazı önemli detayları gözden kaçırabiliriz: son zamanlarda trendin ne yönde ilerlediği, ürünün kargo ve iade hizmetleri gibi bilgileri atlayabiliriz.

# Örneğin, bir e-ticaret firması, son zamanlarda satılan bir ürünün stoklara yeniden gelmesiyle birlikte kargo ve paketleme hizmetleriyle ilgili bazı konuların işleyişi hakkında bilgi almak istediği için,
# puan zamanlarına göre ağırlıklı ortalama almak istiyor ve çeşitli zaman aralıkları belirliyor.
# Bu veri setindeki ürünle ilgili son 45 günde yapılan yorumlara ve ortalamasına erişmek istiyor: df.loc[df["days"] <= 45, "Rating"].mean()"

df.info()

# Bugüne ait tarihi girelim
current_date = pd.to_datetime('2021-02-10 0:0:0')

# Timestamp değişkenini, tarihsel data type a çevirelim
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# days sütunu oluşturalım : current_date den, her puanlamaya ait tarihi çıkaralım ve gün cinsine çevirelim
df["days"] = (current_date - df["Timestamp"]).dt.days


# Bazı pratikler yapalım:
# Verisetindeki son 30 günde yapılan puanlamalara erişmek:
df.loc[df["days"] <= 30, "Rating"]

# Verisetindeki son 30 günde yapılan puanlamalar ortalaması:
df.loc[df["days"] <= 30, "Rating"].mean()

# Verisetindeki son 1 ay-3 ay arası yapılan puanlamalar ortalaması:
df.loc[(df["days"] > 30) & (df["days"] <= 90), "Rating"].mean()

# Verisetindeki son 3 ay-6 ay arası yapılan puanlamalar ortalaması:
df.loc[(df["days"] > 90) & (df["days"] <= 180), "Rating"].mean()

# Verisetindeki 6 aydan eski yapılan puanlamalar ortalaması:
df.loc[(df["days"] > 180), "Rating"].mean()



### Puan Zamanlarına Göre Ağırlık verelim :
# Puan ağırlığı; yorum tarihi <= 30 gün ise %28 olsun, yorum tarihi > 30 ve <= 90 gün ise %26 olsun, yorum tarihi > 90 ve <= 180 gün ise %24 olsun, yorum tarihi > 180 gün ise %22 olsun. (% lerin toplamı 100 olmalı !! )
df.loc[df["days"] <= 30, "Rating"].mean() * 28/100 + \
    df.loc[(df["days"] > 30) & (df["days"] <= 90), "Rating"].mean() * 26/100 + \
    df.loc[(df["days"] > 90) & (df["days"] <= 180), "Rating"].mean() * 24/100 + \
    df.loc[(df["days"] > 180), "Rating"].mean() * 22/100


## Puanlama Zamanlarına Göre Ağırlıklı Puan Ortalaması Hesaplama Fonksiyonu
def time_based_weighted_average(dataframe, w1=28, w2=26, w3=24, w4=22):
    return dataframe.loc[df["days"] <= 30, "Rating"].mean() * w1 / 100 + \
           dataframe.loc[(dataframe["days"] > 30) & (dataframe["days"] <= 90), "Rating"].mean() * w2 / 100 + \
           dataframe.loc[(dataframe["days"] > 90) & (dataframe["days"] <= 180), "Rating"].mean() * w3 / 100 + \
           dataframe.loc[(dataframe["days"] > 180), "Rating"].mean() * w4 / 100

# Tarihe göre Ağırlıklı Puan Ortalaması:
time_based_weighted_average(df)

# Fonksiyon içindeki ağırlıkları değiştirebiliriz:
time_based_weighted_average(df, 30, 26, 22, 22)








####################
# 3) User-Based Weighted Average
####################

# Kullanıcı Bazlı Ağırlıklı Ortalama: Güvenilir kullanıcıların ağırlıklarının ortalama üzerinde daha fazla etkisi olduğu bir ortalama alma yöntemidir.
# Her bir kullanıcıya, o kullanıcının katkısına göre bir ağırlık atanır. Örneğin, daha aktif veya daha etkili kullanıcılar daha yüksek ağırlıklara sahip olabilir.
# Örneğin IMDB'de, yeni üye olup bir filme puan veren kişinin puan ağırlığı ile, daha önce yüzlerce filme puan veren birinin puan ağırlığı aynı olmayabilir.

# Kullanıcıların kurs progress ine göre, rating ortalamalarına bakalım
df.groupby("Progress").agg({"Rating": "mean"})

### Kullanıcıların kurs progress ine göre ağırlık verelim :
df.loc[df["Progress"] <= 10, "Rating"].mean() * 22 / 100 + \
    df.loc[(df["Progress"] > 10) & (df["Progress"] <= 45), "Rating"].mean() * 24 / 100 + \
    df.loc[(df["Progress"] > 45) & (df["Progress"] <= 75), "Rating"].mean() * 26 / 100 + \
    df.loc[(df["Progress"] > 75), "Rating"].mean() * 28 / 100


### Kullanıcıların kurs progress ine göre ağırlığı, fonksiyon haline getirelim
def user_based_weighted_average(dataframe, w1=22, w2=24, w3=26, w4=28):
    return dataframe.loc[dataframe["Progress"] <= 10, "Rating"].mean() * w1 / 100 + \
           dataframe.loc[(dataframe["Progress"] > 10) & (dataframe["Progress"] <= 45), "Rating"].mean() * w2 / 100 + \
           dataframe.loc[(dataframe["Progress"] > 45) & (dataframe["Progress"] <= 75), "Rating"].mean() * w3 / 100 + \
           dataframe.loc[(dataframe["Progress"] > 75), "Rating"].mean() * w4 / 100

# Fonksiyon içindeki ağırlıkları değiştirebiliriz:
user_based_weighted_average(df, 20, 24, 26, 30)






####################
# 4) Weighted Rating (Time based & User based)
####################

# Hem yeni ve başarılı ürünleri (Time based), hem güvenilir kullanıcıların oylarını (User based) birlikte ağırlandırarak karma bir ortalama alma yöntemidir.

# Yukarıdaki 2 faktörü (2. adımdaki Time based ve 3. adımdaki User based) bir fonksiyon aracılığıyla araya getirelim
def weighted_rating(dataframe, time_w=50, user_w=50):
    return time_based_weighted_average(dataframe) * time_w/100 + user_based_weighted_average(dataframe) * user_w/100

weighted_rating(df)

# Fonksiyon içindeki, Time based & User based ağırlıklarını değiştirebiliriz:
weighted_rating(df, time_w=40, user_w=60)










