##################################################################################
# CUSTOMER LIFETIME VALUE (Müşteri Yaşam Boyu Değeri)
##################################################################################

# Customer Lifetime Value, bir müşterinin bir şirketle olan ilişkisi boyunca, bu şirkete kazandıracağı parasal değerdir.
# Sirketlerin müşterileriyle ilişkilerini yönetmelerine ve pazarlama stratejilerini desteklemelerine yardımcı olur.

# Müşteri yaşam döngüsü optimizasyonları : Müşteriler ile kurulan iletişimi ya da etkileşimi görsel teknikler ile ifade edip
# bunları çeşitli temel performans göstergeleri (KPI) ile takip edilebilir forma getirip takip etme imkânı sağlayan kavramlardir.


### CLV = (Customer Value / Churn Rate) x Profit Margin

# Customer Value = AVERAGE Order Value x Purchase Frequency        (Müşteri Değeri = Ort Sipariş Değeri x Satın Alma Sıklığı)
# Average Order Value = Total Price / Total Transaction              (Ort Sipariş Değeri = Total Harcama / Total İşlem/Fatura Sayisi)
# Purchase Frequency = Total Transaction / Total Number of Customers (Satın Alma Sıklığı = Total İşlem Sayisi/ Total Müşteri Sayısı)

# Churn Rate = 1 - Repeat Rate   (Musteri terk orani) (Churn Rate: tum kitleden gelir, bireysel hesaplanmaz)
# Repeat Rate = 1den fazla alisveris yapan müşteri sayısı / Total Müşteri Sayısı

# Profit Margin = Total Price * 0.10  (0.10 sirketinn belirledigi kar marji)


## !! NOTE :
# Monetory:   RFM de TOPLAM harcama tutari, CLV da AVERAGE Harcama tutari!
# Frequency:  RFM ve CLV de toplam islem sayisi (fatura sayisi)
# Recency:    RFM de (analiz tarihi-son satin alma tarihi), CLV da (musteri son satin alma-ilk satin alma) (yani CLV'de musteri ozelindedir)




##################################################################################
# PROJECT : CUSTOMER LIFETIME VALUE (Müşteri Yaşam Boyu Değeri)
##################################################################################


#### PROJE ADIMLARI ####
# 1. İş Problemi (Business Problem)
# 2. Veriyi Anlama (Data Understanding)
# 3. Veri Hazırlama (Data Preparation) ('total_transaction', 'total_unit', 'total_price' sutunlarini olusturma)
# 4. Average Order Value (average_order_value = total_price / total_transaction)
# 5. Purchase Frequency (total_transaction / total_number_of_customers)
# 6. Repeat Rate & Churn Rate (birden fazla alışveriş yapan müşteri sayısı / tüm müşteriler)
# 7. Profit Margin (profit_margin =  total_price * 0.10)
# 8. Customer Value (customer_value = average_order_value * purchase_frequency)
# 9. Customer Lifetime Value (CLV = (customer_value / churn_rate) x profit_margin)
# 10. Segmentlerin Oluşturulması
# 11. BONUS: Tüm İşlemlerin Fonksiyonlaştırılması






##################################################################################
# 1. İş Problemi (Business Problem)
##################################################################################

# Bir e-ticaret şirketi müşterilerini segmentlere ayırıp,
# bu segmentlere göre pazarlama stratejileri belirlemek istiyor.


# Veri Seti Hikayesi
# https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

# Online Retail II isimli veri seti, İngiltere merkezli online bir satış mağazasının
# 01/12/2009 - 09/12/2011 tarihleri arasındaki satışlarını içeriyor.
# Bu sirket hediyelik esya satiyor, musterileri genelde kurumsal toptancilar.
# Kurumsal musterileri segmentlere ayirmak ve buna gore ilgilenmek istiyor.


# Değişkenler
# InvoiceNo:    Fatura numarası. Her işleme yani faturaya ait eşsiz numara. C ile başlıyorsa iptal edilen işlem.
# StockCode:    Ürün kodu. Her bir ürün için eşsiz numara.
# Description:  Ürün ismi
# Quantity:     Ürün adedi. Bir faturada 1den fazla urun yer alabilir.
# InvoiceDate:  Fatura tarihi ve zamanı.
# UnitPrice:    Ürün fiyatı (Sterlin cinsinden)
# CustomerID:   Eşsiz müşteri numarası
# Country:      Ülke ismi. Müşterinin yaşadığı ülke.







##################################################################################
# 2. Veriyi Anlama (Data Understanding)
##################################################################################

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)    # tüm sütunlar gelsin
pd.set_option("display.width", 500)           # tüm sütunlar "yanyana" gelsin
pd.set_option("display.precision", 5)         # float türündeki sayılarda virgül sonrasi 5 basamak olsun

df_ = pd.read_excel("/Users/gozdemadendere/Desktop/PycharmProjects/CRM_Analytics/datasets/online_retail_II.xlsx", sheet_name="Year 2009-2010")
df = df_.copy()


df.head()
df.shape
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




##################################################################################
# 3. Veri Hazırlama (Data Preparation)
##################################################################################

# invoice C ile baslayanlar iptal edilen islem demekti
df.describe().T   # quantity de min de bu iptal/iadelerden kaynakli aykiri degerler oldugunu goruyoruz

### 1) invoice C ile baslayanlari (iptal urunleri) disarida birakalim
df = df.loc[~df["Invoice"].str.contains("C", na=False)]   # na=False parametresi, eksik değerlerin (NaN) kontrol edilmemesini sağlar


### 2) Quantity de min -li deger gorunuyor, mantiksiz, 0dan buyuk olanlari alalim
df = df[(df['Quantity'] > 0)]

df.describe().T   # daha mantikli gorunuyor


df.isnull().sum()
### 3) Customer ID ve Description da, NaN degerler var.
# Customer ID' si olmayan satirlar, burada onemsiz ve Description da cok az eksik deger var. Bunlari ucurabiliriz.
df.dropna(inplace=True)



### 4) TotalPrice sutunu olusturma: ilgili 1 satista, urune totalde ne kadar odenmistir?
df["TotalPrice"] = df["Quantity"] * df["Price"]


### 5) CLV hesaplayabilmek icin yeni sutunlari olusturalim : Total Transaction, Total Price (gerekirse diye sum of quantity)
### Customer Value = Average Order Value x Purchase Frequency        (Müşteri Değeri = Ort Sipariş Değeri x Satın Alma Sıklığı)
# Average Order Value = Total Price / Total Transaction              (Ort Sipariş Değeri = Total Harcama / Total İşlem Sayisi)
# Purchase Frequency = Total Transaction / Total Number of Customers (Satın Alma Sıklığı = Total İşlem Sayisi/ Total Müşteri Sayısı)


## Customer ID ye gore grupla, 3 yeni sutunu olustur
# Invoice : essiz fatura sayisi (total_transaction)
# Quantity : sum of unit
# TotalPrice: sum of price  (total_price)
clv = df.groupby('Customer ID').agg({'Invoice': lambda x: x.nunique(),
                                     'Quantity': lambda x: x.sum(),
                                     'TotalPrice': lambda x: x.sum()})

# Yani Customer id ye gore gruplandirdik ve musterileri tekillestirdik.
clv.head()


### 6) Olusturdugumuz yeni sutun isimlerini 'total_transaction', 'total_unit', 'total_price' olarak guncelleyelim
clv = clv.rename(columns = {"Invoice": "total_transaction", "Quantity": "total_unit", "TotalPrice": "total_price"})
# veya clv.columns = ['total_transaction', 'total_unit', 'total_price']



### 7) Genel olarak degerleri kontrol edelim
clv.describe().T

# Baktigimizda, total_price min degeri 0 gorunuyor, mantiksiz. Bu 0 li deger(ler)i ucuralim
# clv = clv.loc[clv["total_price"] > 0, :]


### SONUC:
# 'total_transaction', 'total_unit', 'total_price' sutunlarini olusturup hesaplatarak, yeni bir dataframe olusturduk.
# customer id ye gore gruplandirdik.






##################################################################################
# 4. Average Order Value
##################################################################################

###### CLV = (Customer Value / Churn Rate) x Profit Margin
### Customer Value = Average Order Value x Purchase Frequency        (Müşteri Değeri = Ort Sipariş Değeri x Satın Alma Sıklığı)
# Average Order Value = Total Price / Total Transaction              (Ort Sipariş Değeri = Total Harcama / Total İşlem Sayisi)
# Purchase Frequency = Total Transaction / Total Number of Customers (Satın Alma Sıklığı = Total İşlem Sayisi/ Total Müşteri Sayısı)

clv.head()

### Yeni bir Average Order Value sutunu olusturalim
clv["average_order_value"] = clv["total_price"] / clv["total_transaction"]





##################################################################################
# 5. Purchase Frequency
##################################################################################

# Purchase Frequency = Total Transaction / Total Number of Customers (Satın Alma Sıklığı = Total İşlem Sayisi/ Total Müşteri Sayısı)

clv.head()

# Total Number of Customers
clv.shape    #(4314, 4)  yani 4314 unique Customer ID var !!
clv.shape[0]  # 4314 = total musteri sayisi


### Yeni bir Purchase Frequency sutunu olusturalim
clv["purchase_frequency"] = clv["total_transaction"] / clv.shape[0]





##################################################################################
# 6. Repeat Rate & Churn Rate
##################################################################################


### Churn Rate = 1 - Repeat Rate   (Musteri terk orani)
# Repeat Rate = 1den fazla alisveris yapan müşteri sayısı / Total Müşteri Sayısı


clv.head()

# Total Number of Customers
clv.shape    #(4314, 4)  yani 4314 unique Customer ID var !!
clv.shape[0]  # 4314 = total musteri sayisi

# Total Transaction > 1 olanlar
clv[clv["total_transaction"] > 1]
clv[clv["total_transaction"] > 1].shape   # (2893, 5) yani 2893 adet 1den fazla alisveris yapan musteri var
clv[clv["total_transaction"] > 1].shape[0]   # 2893 musteri

### Yeni bir Repeat Rate sutunu olusturalim
repeat_rate = clv[clv["total_transaction"] > 1].shape[0] / clv.shape[0]

churn_rate = 1 - repeat_rate






##################################################################################
# 7. Profit Margin
##################################################################################

### Profit Margin = Total Price * 0.10

### Yeni bir Profit Margin sutunu olusturalim : her bir musteriye ait profit margin
clv['profit_margin'] = clv['total_price'] * 0.10

clv.head()





##################################################################################
# 8. Customer Value
##################################################################################

### Customer Value = Average Order Value x Purchase Frequency     (Müşteri Değeri = Ort Sipariş Değeri x Satın Alma Sıklığı)


### Yeni bir Customer Value sutunu olusturalim :
clv['customer_value'] = clv['average_order_value'] * clv["purchase_frequency"]

clv.head()




##################################################################################
# 9. Customer Lifetime Value
##################################################################################

### CLV = (Customer Value / Churn Rate) x Profit Margin

### Yeni bir CLV sutunu olusturalim :
clv["clv"] = (clv["customer_value"] / churn_rate) * clv["profit_margin"]


# Verilere genel olarak goz atalim
clv.head()
clv.describe().T


# CLV si ilk 5 ve son 5 musteriye bakalim:
clv.sort_values(by="clv", ascending=False).head()
clv.sort_values(by="clv", ascending=False).tail()


### CLV si en iyi musteriyi yorumlayalim:
#              total_transaction  total_unit  total_price  average_order_value  purchase_frequency  profit_margin  customer_value         clv
# Customer ID
# 18102.0                     89      124216    349164.35           3923.19494             0.02063      34916.435        80.93749  8.57957e+06

# Yorum: toplam 89 fatura kesilmis,  toplam 124216 adet birim urun satin almis, toplam 349164.35 harcama yapmis





##################################################################################
# 10. Segmentlerin Oluşturulması
##################################################################################

clv.head()
clv.shape  # (4314, 8)  yani 4314 adet unique musteri var


# Yeni bir segment sutunu olusturalim : dataframe i4 parcaya bolelim
clv["segment"] = pd.qcut(clv["clv"], 4, labels=["D", "C", "B", "A"])

# CLV si en iyi olan ilk 5 musteri, A segmentinde mi kontrol edelim
clv.sort_values(by="clv", ascending=False).head()

# CLV si en kotu olan son 5 musteri, D segmentinde mi kontrol edelim
clv.sort_values(by="clv", ascending=False).tail()


# segment bazinda gruplayalim, degerlere goz atalim
# amac: segmentler arasi cok ucuk farklar varsa, segment sayisini arttirabiliriz.
# Yorum: A segmentinin degerlerinin daha iyi oldugunu gorebiliyoruz
clv.groupby("segment").agg({"count", "mean", "sum"})


# csv dosyası olarak kaydedelim.  (kodu çalıştır, Project'te CRM_Analytics sağ tıkla, Reload from Disk tıkla, dosya orada)
clv.to_csv("clv.csv")

# 18102.00000       A
# 14646.00000       A
# 14156.00000       A
# 14911.00000       A
# 13694.00000       A

# Customer ID
# 18102.00000       A
# 14646.00000       A
# 14156.00000       A
# 14911.00000       A
# 13694.00000       A







##################################################################################
# 11. BONUS: Tüm İşlemlerin Fonksiyonlaştırılması
##################################################################################

# Create the Function
def create_clv(dataframe, profit=0.10):

    # Convert "Invoice" column to string type
    dataframe["Invoice"] = dataframe["Invoice"].astype(str)

    # Prepare the data
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[(dataframe['Quantity'] > 0)]
    dataframe.dropna(inplace=True)
    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]
    clv = dataframe.groupby('Customer ID').agg({'Invoice': lambda x: x.nunique(),
                                               'Quantity': lambda x: x.sum(),
                                               'TotalPrice': lambda x: x.sum()})
    clv.columns = ['total_transaction', 'total_unit', 'total_price']
    # avg_order_value
    clv['avg_order_value'] = clv['total_price'] / clv['total_transaction']
    # purchase_frequency
    clv["purchase_frequency"] = clv['total_transaction'] / clv.shape[0]
    # repeat rate & churn rate
    repeat_rate = clv[clv.total_transaction > 1].shape[0] / clv.shape[0]
    churn_rate = 1 - repeat_rate
    # profit_margin
    clv['profit_margin'] = clv['total_price'] * profit
    # Customer Value
    clv['customer_value'] = (clv['avg_order_value'] * clv["purchase_frequency"])
    # Customer Lifetime Value
    clv['clv'] = (clv['customer_value'] / churn_rate) * clv['profit_margin']
    # Segment
    clv["segment"] = pd.qcut(clv["clv"], 4, labels=["D", "C", "B", "A"])

    return clv

clv = create_clv(df)



# Veri setinin ilk hali
df = df_.copy()

# Use the Function
clv = create_clv(df)
clv.head()





### NOTES:

# 1) Bu fonksiyon icindeki adimlar, ayri ayri fonksiyonlar seklinde dey azilabilir.
# return ciktilari sonraki adima ait fonksiyonda kullanilabilir.

# 2) Bu fonksiyonu ornegin her ay calistiriyorsak, dataframe icerigi degismis olabileceginden,
# ciktilarin dogrulugunu mutlaka kontrol etmeliyiz. (fonksiyon olusturma oncesi adimlarda da)



















