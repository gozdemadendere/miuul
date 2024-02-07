##############################################################
# Müşteri Yaşam Boyu Değeri Tahmini ( Customer Lifetime Value Prediction )
##############################################################

# Customer Lifetime Value, bir müşterinin bir şirketle olan ilişkisi boyunca, bu şirkete kazandıracağı parasal değerdir.

# Zaman projeksiyonlu olasılıksal CLTV Tahmini, bir müşterinin bir şirkete sağlayacağı gelirin tahmin edilmesine yönelik bir analiz türüdür.
# Bu yöntem, müşterinin geçmiş davranışlarını ve satın alma alışkanlıklarını kullanarak, gelecekteki satın alma olasılıklarını tahmin etmeye çalışır.
# Şirketlerin müşterileriyle ilişkilerini yönetmelerine ve pazarlama stratejilerini desteklemelerine yardımcı olur.

# CLTV prediction = BG/NBD Modeli x Gamma-Gamma Modeli
# CLTV prediction = Expected Total Transaction x Expected Average Profit  (Beklenen satın alma sayısı x Beklenen ortalama kazanç(kar))

# CLTV değerini, her bir müşteri için tahmin ederiz. Olasılık dağılımlarını kullanarak, genel kitlemizin davranışlarını modelleriz ve bunları kişilerin özeline indirgeriz.


## BG/NBD Modeli: Müşterinin beklenen satın alma sayısını tahmin etmek için kullanılır. (Expected Total Transaction)
# Modelin amacı kitleden bir dağılım yapısı öğrenmektir. Öğrenilmek istenilen bu dağılım: beklenen satin alma sayısı

# 2 süreci olasılıksal olarak modeller : Transaction Process (Buy) + Dropout Process (Till you die)

## Transaction Process: Müşterinin satın alma işlem süreci  (Buy)
# Transaction Rate, her bir müşteriye göre değişir ve tüm kitle için GAMMA dağılır. (r, a)

## Dropout Process: Müşterinin markadan uzaklaşma süreci   (Till you die)
# Dropout Rate, her bir müşteriye göre değişir ve tüm kitle için BETA dağılır. (a, b)
# Bir müşteri alışveriş yaptıktan sonra belirli bir olasılıkla dropout olur. Her bir müşterinin p olasılığı ile dropout rate (dropout probability) i vardır.


## Gamma-Gamma Modeli: Bir müşterinin beklenen ortalama karını tahmin etmek için kullanılır. (Expected average profit)
# Bir müşterinin parasal değeri(monetary), transaction value’ların ortalaması etrafında rastgele dağılır.
# Ortalama transaction value tüm müşteriler arasında gamma dağılır.


# Recency:           Müşteri son satın alma tarihi- Müşteri ilk satın alma tarihi
# Frequency:         Toplam işlem sayısı (fatura sayısı)
# Monetory:          AVERAGE harcama tutarı
# Customer Age (T):  Analiz tarihi - Müşterinin ilk satın alma tarihi





##############################################################
# Project : BG-NBD ve Gamma-Gamma Submodel ile CLTV Prediction
##############################################################

#### PROJE ADIMLARI ####
# 1. İş Problemi (Business Problem)
# 2. Gerekli Kütüphane ve Fonksiyonlar
# 3. Veriyi Anlama (Data Understanding)
# 4. Verinin Hazırlanması (Data Preperation)
# 5. CLTV Veri Yapısının Oluşturulması (Metriklerin hazırlanması)
# 6. BG-NBD Modeli ile Expected Number of Transaction
# 7. Gamma-Gamma Modeli ile Expected Average Profit
# 8. BG-NBD ve Gamma-Gamma Modeli ile CLTV'nin Hesaplanması
# 9. CLTV'ye Göre Segmentlerin Oluşturulması
# 10.Çalışmanın fonksiyonlaştırılması









##################################################################################
# 1. İş Problemi (Business Problem)
##################################################################################

# İngiltere merkezli bir e-ticaret şirketi müşterilerini segmentlere ayırıp, bu segmentlere göre pazarlama stratejileri belirlemek istiyor.

# Veri Seti Hikayesi
# https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

# Online Retail II isimli veri seti, İngiltere merkezli online bir satış mağazasının 01/12/2009 - 09/12/2011 tarihleri arasındaki satışlarını içeriyor.
# Bu sirket hediyelik esya satiyor, musterileri genelde kurumsal toptancilar. Kurumsal musterileri segmentlere ayirmak ve buna gore ilgilenmek istiyor.

# Değişkenler
# InvoiceNo:    Fatura numarası. Her işleme yani faturaya ait eşsiz numara. C ile başlıyorsa iptal edilen işlem.
# StockCode:    Ürün kodu. Her bir ürün için eşsiz numara.
# Description:  Ürün ismi
# Quantity:     Ürün adedi. Bir faturada 1den fazla urun yer alabilir.
# InvoiceDate:  Fatura tarihi ve zamanı.
# UnitPrice:    Ürün fiyatı (Sterlin cinsinden)
# CustomerID:   Eşsiz müşteri numarası
# Country:      Ülke ismi. Müşterinin yaşadığı ülke.






##############################################################
# 2. Gerekli Kütüphane ve Fonksiyonlar
##############################################################

# pip install lifetimes
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions


pd.set_option('display.max_columns', None)    # tüm sütunlar gelsin
pd.set_option("display.width", 500)           # tüm sütunlar "yanyana" gelsin
pd.set_option("display.precision", 4)         # float türündeki sayılarda virgül sonrasi 4 basamak olsun
from sklearn.preprocessing import MinMaxScaler


# Bu fonksiyon, belirli bir değişkenin aykırı değerler için alt ve üst sınırlarını hesaplar (şsik deger)
def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)    # Veri setinin belirtilen değişkeninin alt% 1'lik çeyreğini (1. percentile) hesaplar.
    quartile3 = dataframe[variable].quantile(0.99)    # Veri setinin belirtilen değişkeninin üst% 99'luk çeyreğini (99. percentile) hesaplar.
    interquantile_range = quartile3 - quartile1       # Çeyrekler arası aralığı hesaplar.
    up_limit = quartile3 + 1.5 * interquantile_range  # Üst sınırları hesaplar.
    low_limit = quartile1 - 1.5 * interquantile_range # Alt sınırları hesaplar.
    return low_limit, up_limit                        # Hesaplanan alt ve üst sınırları döndürür.


# Bu fonksiyon, belirli bir değişkenin aykırı değerlerini belirlenen alt ve üst sınırlarla değiştirmek için kullanılır.
def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)             # Belirli değişken için alt ve üst sınırları outlier_thresholds fonksiyonundan alır.
    # dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit  # Aykırı değerleri alt sınıra eşitlemek isteniyorsa, yorum satırı kaldırılarak bu satırın etkinleştirilmesi gerekir.
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit      # Aykırı değerler üst sınıra eşitlenir.





##################################################################################
# 3. Veriyi Anlama (Data Understanding)
##################################################################################

df_ = pd.read_excel("/Users/gozdemadendere/Desktop/PycharmProjects/CRM_Analytics/datasets/online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df_.copy()

df.head()
df.describe().T
df.isnull().sum()

# essiz urun sayisi nedir?
df["Description"].nunique()

# essiz fatura sayisi nedir?
df["Invoice"].nunique()


################################################
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

################################################





##############################################################
# 4. Verinin Hazırlanması (Data Preperation)
##############################################################

### 1) Customer ID ve Description da, NaN degerler var.
# Customer ID' si olmayan satirlar burada onemsiz ve Description da cok az eksik deger var. Bunlari ucurabiliriz.
df.dropna(inplace=True)

### 2) invoice C ile baslayanlari (iptal urunleri) disarida birakalim
df = df.loc[~df["Invoice"].str.contains("C", na=False)]   # na=False parametresi, eksik değerlerin (NaN) kontrol edilmemesini sağlar

### 3) Quantity de min -li deger gorunuyor, mantiksiz, 0dan buyuk olanlari alalim
df = df[df["Quantity"] > 0]

### 4) Price da min -li deger gorunuyor, mantiksiz, 0dan buyuk olanlari alalim
df = df[df["Price"] > 0]

### 5) Yukarida hazirladigimiz fonksiyonlari kullanalim:
# Bu fonksiyon, belirli bir değişkenin aykırı değerlerini belirlenen alt ve üst sınırlarla değiştirmek için kullanılır.
replace_with_thresholds(df, "Quantity")
replace_with_thresholds(df, "Price")

df.describe().T
df.isnull().sum()


### 6) TotalPrice sutunu olusturma: ilgili 1 satista, urune totalde ne kadar odenmistir?
df["TotalPrice"] = df["Quantity"] * df["Price"]








##############################################################
# 5. CLTV Veri Yapısının Oluşturulması
##############################################################

# Recency:           Müşteri son satın alma tarihi- Müşteri ilk satın alma tarihi
# Frequency:         Toplam işlem sayısı (fatura sayısı)
# Monetory:          AVERAGE harcama tutarı
# Customer Age (T):  Analiz tarihi - Müşterinin ilk satın alma tarihi

### 1) Analiz tarihini girelim:
today_date = dt.datetime(2011, 12, 11)

### 2) Yeni bir df olustur: Customer lara gore grupla, 4 yeni sutun olustur:
cltv_df = df.groupby('Customer ID').agg(
    {'InvoiceDate': [lambda InvoiceDate: (InvoiceDate.max() - InvoiceDate.min()).days,    # musteriye ait recency
                     lambda InvoiceDate: (today_date - InvoiceDate.min()).days],          # musteri yasi : T
     'Invoice': lambda Invoice: Invoice.nunique(),                                        # frequency
     'TotalPrice': lambda TotalPrice: TotalPrice.sum()})                                  # total price (asagida ortalama kazanci bulacagiz)


# en ustteki level label lari silelim
cltv_df.columns = cltv_df.columns.droplevel(0)

#######################################
# Note!! : Örnek olarak, FLO_CLTV_prediction projesinde, last order date ve first order date ler farklı sütundaydı, orada bu kısmı daha farklı yaptık.
# Ayrıca orada, orijinal dataframe de, Customer id ler her satırda eşsiz, group by a aldırmadan hesaplamalar yaptık, bakılabilir.
#######################################

### 4) monetary: satın alma başına ORTALAMA kazanç idi, total price i islem sayisina bolelim (rfm de toplam kazancti, burada ortalama kazanc !)
cltv_df["TotalPrice"] = cltv_df["TotalPrice"] / cltv_df["Invoice"]

### 5) Olusturdugumuz yeni sutun isimlerini guncelleyelim (suanda:  <lambda_0> <lambda_1> <lambda>   <lambda>)
# recency: musteriye ait recency, T: musteri yasi, frequency: total islem sayisi, monetary: ORTALAMA kazanc
cltv_df.columns = ['recency', 'T', 'frequency', 'monetary']

# frequency integer olmalidir, degilse integer a cevirelim
cltv_df.dtypes

### 6) frequency >1 olmalidir !  df de min 1 gorunuyor.
cltv_df.describe().T
cltv_df = cltv_df[(cltv_df['frequency'] > 1)]

### 7) Recency ve Müşteri Yaşı (T) değerleri haftalık olmalı, haftalık cinse çevirelim: 7'ye bölerek
cltv_df["recency"] = cltv_df["recency"] / 7
cltv_df["T"] = cltv_df["T"] / 7

# degerleri kontrol edelim:
cltv_df.describe().T








##############################################################
# 6. BG-NBD Modelinin Kurulması
##############################################################

# Bu model bir müşterinin beklenen satın alma sayısını tahmin etmek için kullanılır.  (Expected Total Transaction)

# Katsayılara uygulanacak ceza katsayısı: 0.001
bgf = BetaGeoFitter(penalizer_coef=0.001)

# Modeli nihai hale getir:
bgf.fit(cltv_df['frequency'],
        cltv_df['recency'],
        cltv_df['T'])



################################################################
# 1 Haftalık Satın Alma Sayısı Sonuçları
################################################################

# 1 hafta içinde en çok satın alma sayısı beklenen ilk 10 müşteri: (t:1 yani 1 haftalık tahmin yap demek)
bgf.conditional_expected_number_of_purchases_up_to_time(1,
                                                        cltv_df['frequency'],
                                                        cltv_df['recency'],
                                                        cltv_df['T']).sort_values(ascending=False).head(10)


# Veya predict fonksiyonu ile:
bgf.predict(1,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sort_values(ascending=False).head(10)



# Tüm müşteriler için, 1 hafta içinde beklenen satın alma sayısı
cltv_df["expected_purc_1_week"] = bgf.predict(1,
                                              cltv_df['frequency'],
                                              cltv_df['recency'],
                                              cltv_df['T'])


################################################################
# 1 Aylık Satın Alma Sayısı Sonuçları
################################################################

# 1 ay içinde en çok satın alma sayısı beklenen ilk 10 müşteri:
bgf.predict(4,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sort_values(ascending=False).head(10)


# Tüm müşteriler için, 4 hafta içinde beklenen satın alma sayısı
cltv_df["expected_purc_1_month"] = bgf.predict(4 * 3,
                                               cltv_df['frequency'],
                                               cltv_df['recency'],
                                               cltv_df['T'])

# Veya predict fonksiyonu ile:
bgf.predict(4,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sum()



################################################################
# 3 Aylık Satın Alma Sayısı Sonuçları
################################################################


# Tüm müşteriler için, 12 hafta (4 hafta x 3) icerisinde beklenen satın alma sayıları
bgf.predict(4 * 3,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sum()


# veya predict fonksiyonu ile ayni islem:
cltv_df["expected_purc_3_month"] = bgf.predict(4 * 3,
                                               cltv_df['frequency'],
                                               cltv_df['recency'],
                                               cltv_df['T']).sum()


################################################################
# 6 Ayda Tüm Şirketin Beklenen Satış Sayısı Nedir?
################################################################

# Tüm müşteriler için, 24 hafta (4 hafta x 6) içinde beklenen satın alma sayısı
bgf.predict(4 * 6,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sum()


# veya predict fonksiyonu ile ayni islem:
cltv_df["expected_purc_3_month"] = bgf.predict(4 * 6,
                                               cltv_df['frequency'],
                                               cltv_df['recency'],
                                               cltv_df['T']).sum()


# Tahmin Sonuçlarının Değerlendirilmesi
# Bir plot çizdirelim, actual ve model değerleri için karşılaştırma grafiği gelsin
plot_period_transactions(bgf)
plt.show()








##############################################################
# 7. GAMMA-GAMMA Modelinin Kurulması
##############################################################

# GAMMA-GAMMA modeli, bir müşterinin beklenen ortalama karini tahmin etmek için kullanılır. (Expected Average Profit)

# Katsayılara uygulanacak ceza katsayısı: 0.01
ggf = GammaGammaFitter(penalizer_coef=0.01)

# Modeli nihai hale getir:
ggf.fit(cltv_df['frequency'], cltv_df['monetary'])



# Tüm müşteriler için, Expected Average Profit (beklenen kar) i getir
ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                        cltv_df['monetary'])


# Tüm müşteriler için, Expected Average Profit (beklenen kar) i getir
ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                        cltv_df['monetary']).sort_values(ascending=False).head(10)

# Yeni sutuna, Ilk 10 musteri icin, Expected Average Profit (beklenen kar) i getir
cltv_df["expected_average_profit"] = ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                                                             cltv_df['monetary'])


cltv_df.sort_values(by="expected_average_profit", ascending=False).head(10)







##############################################################
# 8. BG-NBD ve GG modeli ile CLTV'nin hesaplanması
##############################################################

# 3 aylık CLTV hesaplayınız.
# Daha önce kurduğumuz ggf modeli ve bgf modeli ile, cltv hesaplayalim  (Buradaki time aylik !)

cltv = ggf.customer_lifetime_value(bgf,
                                   cltv_df['frequency'],
                                   cltv_df['recency'],
                                   cltv_df['T'],
                                   cltv_df['monetary'],
                                   time=3,  # 3 aylık !!
                                   freq="W",  # T'nin frekans bilgisi (W = haftalik)
                                   discount_rate=0.01)   # indirim yapilirsa diye indirim payi

cltv.head()


# index bilgisi ekleyelim, Customer ID bir index degil degisken olsun
cltv = cltv.reset_index()

# cltv_df ile cltv df leri birlestirelim
cltv_final = cltv_df.merge(cltv, on="Customer ID", how="left")

# SONUC: 3 aylik cltv degerleri:
cltv_final.sort_values(by="clv", ascending=False).head(10)


## !! NOTE:
# BG-NBD nin teorisinin en kritik noktasi:
# Recency yüksek olsa da, müşteri düzenli işlem yapıyorsa, eğer churn / drop out olmamışsa, müşterinin recency si arttıkça, satın alma ihtimali yükseliyor der!!
# (Hep kullandığım bir markanın, bayadır gitmediğim mağazasına gitmeye karar vermem gibi..) (Normalde recency az ise bizim için daha iyiydi)




# Örnegin 1. siradaki musteriye bakalim:
# Yorumlar: musteri yasi 51 yani 51 HAFTA dan beri musterimiz (T = musteri yasi haftalikti)
# frequency 73 yani 73 kere islem yapmis, recency 50 yani 50 hafta once en son alisverisini yapmis, monetary 3646 yani 3646 lira kazandirmis
# 1 hafta icinde 1 adet, 1 ay icinde 5 adet, 3 ay icinde 14 adet islem yapmasini bekliyoruz
# 3655 lira kar getirmesini bekliyoruz

# Örnegin altindaki musteriye bakalim:
# frequency 201 yani 201 kere islem yapmis, recency 53 yani 53 hafta once en son alisverisini yapmis, monetary 692 yani 692 lira kazandirmis
# frequency si 1. siradaki musteriye gore dahaa iyi olsaa da, monetary degeri dusuk. Demekki sik alisveris yapan, ama az kar getiren bir musteri

#       Customer ID  recency  T  frequency  monetary  expected_purc_1_week  expected_purc_1_month  expected_purc_3_month  expected_average_profit   clv segment
# 1122        14646       50 51         73      3646                     1                      5                     14                     3655 55741       A
# 1257        14911       53 53        201       692                     3                     12                     37                      692 27377       A









##############################################################
# 9. CLTV'ye Göre Segmentlerin Oluşturulması
##############################################################

# 3 aylık CLTV'ye göre, tüm müşterilerinizi 4 gruba (segmente) ayırınız ve grup isimlerini veri setine ekleyiniz.

# Burada segmentleri otomatik belirledik, gerekirse araliklari kendimiz de ayarlayabiliriz cut fonksiyonu ile vb.
cltv_final["segment"] = pd.qcut(cltv_final["clv"], 4, labels=["D", "C", "B", "A"])
cltv_final.sort_values(by="clv", ascending=False).head(50)

# display.float_format ile bilimsel gösterimdeki sayıları tam sayı olarak görüntülemek
# yani 1.1078e+07 yerine 11077635 gibi   veya   15558.4761 yerine 15558 gibi
pd.set_option('display.float_format', '{:.0f}'.format)

# Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz. (Amac: segmentler arasi cok ucuk farklar varsa, segment sayisini arttirabiliriz)
cltv_final.groupby("segment").agg({"count", "mean", "sum"})


################################################################
# SONUÇ: 3 Aylık CLTV Değerleri:
################################################################

# # Tüm müşteriler için, 3 Aylık CLTV Değerleri:
cltv_final.sort_values(by="clv", ascending=False)

# 3 Aylık CLTV Değerleri en yüksek 50 kişiyi gözlemleyiniz.
cltv_final.sort_values(by="clv", ascending=False).head(50)







##############################################################
# 10. Çalışmanın Fonksiyonlaştırılması
##############################################################


def create_cltv_p(dataframe, month=3):
    # 1. Veri Ön İşleme
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_thresholds(dataframe, "Quantity")
    replace_with_thresholds(dataframe, "Price")
    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]
    today_date = dt.datetime(2011, 12, 11)

    cltv_df = dataframe.groupby('Customer ID').agg(
        {'InvoiceDate': [lambda InvoiceDate: (InvoiceDate.max() - InvoiceDate.min()).days,
                         lambda InvoiceDate: (today_date - InvoiceDate.min()).days],
         'Invoice': lambda Invoice: Invoice.nunique(),
         'TotalPrice': lambda TotalPrice: TotalPrice.sum()})

    cltv_df.columns = cltv_df.columns.droplevel(0)
    cltv_df.columns = ['recency', 'T', 'frequency', 'monetary']
    cltv_df["monetary"] = cltv_df["monetary"] / cltv_df["frequency"]
    cltv_df = cltv_df[(cltv_df['frequency'] > 1)]
    cltv_df["recency"] = cltv_df["recency"] / 7
    cltv_df["T"] = cltv_df["T"] / 7

    # 2. BG-NBD Modelinin Kurulması
    bgf = BetaGeoFitter(penalizer_coef=0.001)
    bgf.fit(cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T'])

    cltv_df["expected_purc_1_week"] = bgf.predict(1,
                                                  cltv_df['frequency'],
                                                  cltv_df['recency'],
                                                  cltv_df['T'])

    cltv_df["expected_purc_1_month"] = bgf.predict(4,
                                                   cltv_df['frequency'],
                                                   cltv_df['recency'],
                                                   cltv_df['T'])

    cltv_df["expected_purc_3_month"] = bgf.predict(12,
                                                   cltv_df['frequency'],
                                                   cltv_df['recency'],
                                                   cltv_df['T'])

    # 3. GAMMA-GAMMA Modelinin Kurulması
    ggf = GammaGammaFitter(penalizer_coef=0.01)
    ggf.fit(cltv_df['frequency'], cltv_df['monetary'])
    cltv_df["expected_average_profit"] = ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                                                                 cltv_df['monetary'])

    # 4. BG-NBD ve GG modeli ile CLTV'nin hesaplanması.
    cltv = ggf.customer_lifetime_value(bgf,
                                       cltv_df['frequency'],
                                       cltv_df['recency'],
                                       cltv_df['T'],
                                       cltv_df['monetary'],
                                       time=month,  # 3 aylık
                                       freq="W",  # T'nin frekans bilgisi.
                                       discount_rate=0.01)

    cltv = cltv.reset_index()
    cltv_final = cltv_df.merge(cltv, on="Customer ID", how="left")
    cltv_final["segment"] = pd.qcut(cltv_final["clv"], 4, labels=["D", "C", "B", "A"])

    return cltv_final


df = df_.copy()

cltv_final2 = create_cltv_p(df)


# Csv dosyası olarak kaydedelim.  (kodu çalıştır, Project'te CRM_Analytics sağ tıkla, Reload from Disk tıkla, dosya orada)
cltv_final2.to_csv("cltv_prediction.csv")













