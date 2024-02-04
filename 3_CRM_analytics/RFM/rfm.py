
##################################################################################
# RFM : Recency, Frequency, Monetary
##################################################################################

### RFM analizi, müşteri segmentasyonu için kullanılan bir tekniktir.

### Müşterilerin satın alma alışkanlıkları üzerinden segmentlere ayrılmasını ve
# bu segmentler özelinde stratejiler geliştirilebilmesini sağlar.

### RFM : Recency, Frequency, Monetary  (Yenilik, Sıklık, Miktar)
# RFM analizi, bu üç metriği bir araya getirerek müşterileri farklı segmentlere ayırır.



###  Recency (Yenilik)  (Az olan daha iyi)
# Recency = Analiz Tarihi - Müşterinin Son Alışveriş Tarihi
# "Daha yeni etkileşimler" veya satın almalar, genellikle daha değerli müşterileri veya potansiyel olarak daha sadık müşterileri gösterir.

###  Frequency (Sıklık) (Cok olan daha iyi)
# Frequency = Toplam Satın Alma Sayısı (Islem Sayisi / Fatura Sayisi)
# "Daha sık etkileşimler" veya satın almalar, genellikle daha sadık veya daha aktif müşterileri gösterir.

###  Monetary (Miktar) (Cok olan daha iyi)
# Monetary = TOPLAM Harcama tutari
# "Daha yüksek harcamalar" genellikle daha değerli veya daha karlı müşterileri gösterir.


### KEY NOTES !!!
# Frequency ve ardindan Recency daha önemli metriklerdir.
# RFM skorları üzerinden segmentler oluşturulurken, Monetary metriği kullanılmaz !!!
# Cunku zaten Recency ve Frequency varsa, otomatik olarak Monetary de gelir.

# Mesela, Frequency degeri 5 Recency 5 olan musteri: "champions" grubunda, cunku hem sik alisveris var, hem de guncel musteridir.
# Mesela, Frequency degeri 5 Recency 1 olan musteri: "cant lose them" grubunda, cunku sik alisveris yapiyor, ama bayagidir yapmamis!


## !! NOTE :
# Monetory:   RFM de TOPLAM harcama tutari, CLTV da AVERAGE Harcama tutari!
# Frequency:  RFM ve CLTV de toplam islem sayisi (fatura sayisi)
# Recency:    RFM de (analiz tarihi-son satin alma tarihi), CLTV da (musteri son satin alma-ilk satin alma) (yani CLTV de musteri ozelindedir)




##################################################################################
# PROJECT : Customer Segmentation with RFM   (RFM Ile Müşteri Segmentasyonu)
##################################################################################

# 1. İş Problemi (Business Problem)
# 2. Veriyi Anlama (Data Understanding)
# 3. Veri Hazırlama (Data Preparation)
# 4. RFM Metriklerinin Hesaplanması (Calculating RFM Metrics) ('recency', 'frequency', 'monetary' sutunlarini olusturma)
# 5. RFM Skorlarının Hesaplanması (Calculating RFM Scores)
# 6. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi (Creating & Analysing RFM Segments)
# 7. BONUS: Tüm Sürecin Fonksiyonlaştırılması






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

import datetime as dt
import pandas as pd

pd.set_option('display.max_columns', None)    # tüm sütunlar gelsin
pd.set_option("display.width", 500)           # tüm sütunlar "yanyana" gelsin
pd.set_option("display.precision", 3)         # float türündeki sayılarda virgül sonrasi 3 basamak olsun
# pd.set_option('display.max_rows', None)
# pd.set_option('display.float_format', lambda x: '%.3f' % x)

df_ = pd.read_excel("/Users/gozdemadendere/Desktop/PycharmProjects/CRM_Analytics/datasets/online_retail_II.xlsx", sheet_name="Year 2009-2010")
df = df_.copy()

df.head()
df.shape
df.isnull().sum()


# essiz urun sayisi nedir?
df["Description"].nunique()

# hangi urunden kacar adet satilmis?
df["Description"].value_counts().head()

# urun bazinda gruplama: toplam satis adetleri
df.groupby("Description").agg({"Quantity": "sum"}).head()
df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head()

# essiz fatura sayisi nedir?
df["Invoice"].nunique()








##################################################################################
# 3. Veri Hazırlama (Data Preparation)
##################################################################################

### 1) TotalPrice sutunu olusturma: ilgili 1 satista, urune totalde ne kadar odenmistir?
df["TotalPrice"] = df["Quantity"] * df["Price"]

# Bir faturada, totalde ne kadar odenmistir?  (birkac urune ait total price)
df.groupby("Invoice").agg({"TotalPrice": "sum"}).head()


df.isnull().sum()
### 2) Customer ID ve Description da, NaN degerler var.
# Customer ID' si olmayan satirlar, burada onemsiz ve Description da cok az eksik deger var. Bunlari ucurabiliriz.
df.dropna(inplace=True)  # eksik değer (NaN) içeren satırların silinmesini sağlar
df.isnull().sum()        # tekrar baktigimizda, eksik deger iceren sutun yoktur


# invoice C ile baslayanlar iptal edilen islem demekti
df.describe().T   # quantity de min de bu iptal/iadelerden kaynakli aykiri degerler oldugunu goruyoruz

### 3) invoice C ile baslayanlari (iptal urunleri) disarida birakalim
df = df.loc[~df["Invoice"].str.contains("C", na=False)]   # na=False parametresi, eksik değerlerin (NaN) kontrol edilmemesini sağlar


df.describe().T   # iptal edilen urunleri sildigimiz icin, daha mantikli gorunuyor








##################################################################################
# 4. RFM Metriklerinin Hesaplanması (Calculating RFM Metrics)
##################################################################################

# Recency:   analizin yapildigi tarih - alisveris tarihi
# Frequency: toplam satin alma
# Monetary:  toplam harcama tutari


df.head()
df["InvoiceDate"].max()    # dataframe deki en son satin alma tarihi !!


### 1) Analizin yapildigi gunu tanimlayalim, 11 aralik 2010 ise:
today_date = dt.datetime(2010, 12, 11)
type(today_date)


### 2) Customer ID ye gore gruplayalim, ve 'recency', 'frequency', 'monetary' hesaplayalim
# today_date - InvoiceDate.max() >> yani bugunun tarihinden, ilgili musterinin en son satin alma tarihini cikar
# Invoice.nunique() >> yani ilgili musteriye ait, essiz faatura sayisini ver
# TotalPrice.sum() >> yani ilgili musteriye ait, toplam price i ver
rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda InvoiceDate: (today_date - InvoiceDate.max()).days,
                                     'Invoice': lambda Invoice: Invoice.nunique(),
                                     'TotalPrice': lambda TotalPrice: TotalPrice.sum()})

# Yani Customer id ye gore gruplandirdik ve musterileri tekillestirdik.
rfm.head()


### 3) Olusturdugumuz yeni sutun isimlerini 'recency', 'frequency', 'monetary' olarak guncelleyelim
rfm = rfm.rename(columns = {"InvoiceDate": "recency", "Invoice": "frequency", "TotalPrice": "monetary"})
#veya  rfm.columns = ['recency', 'frequency', 'monetary']


### 4) Genel olarak degerleri kontrol edelim
rfm.describe().T

# Baktigimizda, monetary min degeri 0 gorunuyor, mantiksiz. Bu 0 li deger(ler)i ucuralim
rfm = rfm.loc[rfm["monetary"] > 0, :]
# veya rfm = rfm[rfm["monetary"] > 0]




### SONUC:
# recency, frequency, monetary sutunlarini olusturup hesaplatarak, yeni bir dataframe olusturduk.
# customer id ye gore gruplandirdik.










##################################################################################
# 5. RFM Skorlarının Hesaplanması (Calculating RFM Scores)
##################################################################################

## RFM metriklerini RFM skorlarına çevirmedeki amaçlari:
# Farklı ölçek türlerine sahip RFM metriklerini aynı ölçek türüne çevirme
# RFM metrikleri üzerinde bir nevi standartlaştırma işlemi uygulama
# RFM metriklerini birbirleri ile kıyaslanabilir formata getirme

## Recency az olmasi daha iyidir, Frequency ve Monetary cok olmasi daha iyidir.


### 1)  Yeni bir recency_score sutunu olusturalim: 5 parcaya bolelim
rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])

# Ornegin Recency icin 0-100 arasi degerler var ise: labels=[5, 4, 3, 2, 1]  asagidaki gibi gruplanir:
# 0-20, 20-40, 40-60, 60-80, 80-100


### 2)  Yeni bir frequency_score sutunu olusturalim: 5 parcaya bolelim  (labels i recency a gore tam tersi olusturduk!)
# rank(method="first") ile : birden fazla öğe aynı değere sahipse, bu öğelerin sıralamasını veri setindeki ilk göründükleri sıraya göre yapar
rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])


### 3)  Yeni bir monetary_score sutunu olusturalim: 5 parcaya bolelim  (labels i recency a gore tam tersi olusturduk!)
rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])


### 4)  Yeni bir RFM_SCORE sutunu olusturalim: recency_score ve frequency_score degerlerini string olarak yanyana yazdiralim:
rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str))


rfm.describe().T

rfm[rfm["RFM_SCORE"] == "55"]
#rfm.loc[rfm["RFM_SCORE"] == "55", :]

rfm[rfm["RFM_SCORE"] == "11"]
#rfm.loc[rfm["RFM_SCORE"] == "11", :]




# Aşağıdaki kodun çıktısı bize hangi RFM segmentini verir? : Champions! (Recency=5, Frequency=5)
# rfm [ rfm [“RFM_SCORE”] == “55” ]






##################################################################################
# 6. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi (Creating & Analysing RFM Segments)
##################################################################################
# RFM skorları üzerinden segmentler oluşturulurken, Monetary metriği kullanılmaz !!!
# Cunku zaten Recency ve Frequency varsa, otomatik olarak Monetary gelir.

### 1) RFM Score larina gore Segment olusturma

# regex ile yapacagiz
# r : raw string demektir

seg_map = {
    r'[1-2][1-2]': 'hibernating',           # 1.elemanda 1 veya 2   &   2.elemanda 1 veya 2 varsa
    r'[1-2][3-4]': 'at_Risk',               # 1.elemanda 1 veya 2   &   2.elemanda 3 veya 4 varsa
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',                # 1.elemanda 3          &   2.elemanda 3 varsa
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}


### 2) Yeni bir segment sutunu olustur: RFM_SCORE sutunundaki degiskenleri, seg_map icine bakarak degistir
# regex=True : eğer seg_map içindeki keys & values düzenli ifadeler ise, bu desenleri eşleştir
rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)

# alttaki df i segmente gore gruplayalim, segment mean ve count u gosterelim
rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])


rfm[rfm["segment"] == "cant_loose"].head()

### 3) rfm dataframe ini csv dosyasi olarak kaydedelim
# (kodu calistir, Project te CRM_Analytics sag tikla, Reload from Disk tikla, dosya orada)
rfm.to_csv("rfm.csv")




### Mesela bir departman bizden, cant_loose segmentine ait musterilerin id leri istediyse:
# segment i cant_loose olanlarin index bilgileri, yani Customer ID leri !!
rfm[rfm["segment"] == "cant_loose"].index

# bir dataframe olusturalim
new_df = pd.DataFrame()
new_df["cant_loose_customer_id"] = rfm[rfm["segment"] == "cant_loose"].index

# id ler float gorunuyor, integer yapalim:
new_df["cant_loose_customer_id"] = new_df["cant_loose_customer_id"].astype(int)

# csv dosyasi olarak kaydedelim
# (kodu calistir, Project te CRM_Analytics sag tikla, Reload from Disk tikla, dosya orada)
new_df.to_csv("cant_loose_customers.csv")







##################################################################################
# 7. Tüm Sürecin Fonksiyonlaştırılması (Functionalization)
##################################################################################
df = df_.copy()

# Create the function
def create_rfm(dataframe, csv=False):

    # VERIYI HAZIRLAMA
    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]

    # RFM METRIKLERININ HESAPLANMASI
    today_date = dt.datetime(2011, 12, 11)
    rfm = dataframe.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                                'Invoice': lambda num: num.nunique(),
                                                "TotalPrice": lambda price: price.sum()})
    rfm.columns = ['recency', 'frequency', "monetary"]
    rfm = rfm[(rfm['monetary'] > 0)]

    # RFM SKORLARININ HESAPLANMASI
    rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

    # cltv_df skorları kategorik değere dönüştürülüp df'e eklendi
    rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str))

    # SEGMENTLERIN ISIMLENDIRILMESI
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }

    rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
    rfm = rfm[["recency", "frequency", "monetary", "segment"]]
    rfm.index = rfm.index.astype(int)

    # csv=True ise
    if csv:
        rfm.to_csv("rfm.csv")

    return rfm


# Veri setinin ilk hali
df = df_.copy()

# Use the function
rfm_new = create_rfm(df, csv=True)
rfm_new.head()





### NOTES:

# 1) Bu fonksiyon icindeki adimlar, ayri ayri fonksiyonlar seklinde dey azilabilir.
# return ciktilari sonraki adima ait fonksiyonda kullanilabilir.

# 2) Bu fonksiyonu ornegin her ay calistiriyorsak, dataframe icerigi degismis olabileceginden,
# ciktilarin dogrulugunu mutlaka kontrol etmeliyiz. (fonksiyon olusturma oncesi adimlarda da)






