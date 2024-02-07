##################################################################################
# RFM : Recency, Frequency, Monetary
##################################################################################

# RFM analizi; Recency, Frequency, Monetary metriklerinden faydalanarak, müşteri segmentasyonu için kullanılan bir tekniktir.
# Müşterilerin satın alma alışkanlıkları üzerinden segmentlere ayrılmasını, ve bu segmentler özelinde stratejiler geliştirilmesini sağlar.

# Recency   = Analiz tarihi - Müşterinin son satın alma tarihi
# Frequency = Müşterinin toplam satın alma sayısı   (toplam işlem veya fatura sayısı)
# Monetary  = Müşterinin TOPLAM Harcama tutarı

## KEY NOTES !!!
# Frequency ve ardından Recency daha önemli metriklerdir.
# RFM skorları üzerinden segmentler oluşturulurken, Monetary metriği kullanılmaz! Çünkü zaten Recency ve Frequency varsa, otomatik olarak Monetary de gelir.

# Monetory:   RFM'de TOPLAM harcama tutarı, CLTV'de AVERAGE harcama tutarı şeklinde hesaplanır!
# Frequency:  RFM ve CLTV'de toplam işlem sayısı (fatura sayısı)
# Recency:    RFM'de Analiz tarihi - Müşteri son satın alma tarihi, CLTV'de  Müşteri son satın alma- Müşteri ilk satın alma) (yani CLTV'de müşteri özeline aittir)





##################################################################################
# PROJECT : Customer Segmentation with RFM   (RFM Ile Müşteri Segmentasyonu)
##################################################################################

#### PROJE ADIMLARI ####
# 1. İş Problemi (Business Problem)
# 2. Veriyi Anlama (Data Understanding)
# 3. Veri Hazırlama (Data Preparation)
# 4. RFM Metriklerinin Hesaplanması (Calculating RFM Metrics: Recency, Frequency, Monetary sütunlarını olusturma)
# 5. RFM Skorlarının Hesaplanması (Calculating RFM Scores)
# 6. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi (Creating & Analysing RFM Segments)
# 7. BONUS: Tüm Sürecin Fonksiyonlaştırılması






##################################################################################
# 1. İş Problemi (Business Problem)
##################################################################################

# Bir e-ticaret şirketi müşterilerini segmentlere ayırıp, bu segmentlere göre pazarlama stratejileri belirlemek istiyor.

# Veri Seti Hikayesi
# https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

# Online Retail II isimli veri seti, İngiltere merkezli online bir satış mağazasının 01/12/2009 - 09/12/2011 tarihleri arasındaki satışlarını içeriyor.
# Bu şirket hediyelik eşya satıyor, müşterileri genellikle kurumsal toptancılardır. Kurumsal müşterileri segmentlere ayırmak ve buna göre ilgilenmek istiyor.

# Değişkenler
# InvoiceNo:    Fatura numarası. Her işleme yani faturaya ait eşsiz numara. C ile başlıyorsa iptal edilen işlemdir.
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

# Import libraries
import datetime as dt
import pandas as pd

pd.set_option('display.max_columns', None)    # tüm sütunlar gelsin
pd.set_option("display.width", 500)           # tüm sütunlar "yanyana" gelsin
pd.set_option("display.precision", 3)         # float türündeki sayılarda virgül sonrasi 3 basamak olsun
# pd.set_option('display.max_rows', None)
# pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Read the data from Excel
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

### 1) TotalPrice sutunu olusturma: ilgili 1 satista, urune totalde ne kadar odenmistir?
df["TotalPrice"] = df["Quantity"] * df["Price"]

# Bir faturada, totalde ne kadar odenmistir?  (birkac urune ait total price)
df.groupby("Invoice").agg({"TotalPrice": "sum"}).head()


### 2) Customer ID ve Description da, NaN degerler var.
df.isnull().sum()

# Customer ID' si olmayan satirlar, burada onemsiz ve Description da cok az eksik deger var. Bunlari ucurabiliriz.
df.dropna(inplace=True)  # eksik değer (NaN) içeren satırların silinmesini sağlar
df.isnull().sum()        # tekrar baktigimizda, eksik deger iceren sutun yoktur


### 3)
df.describe().T
# Yorum 1: min quantity ve price 1 veya 1den buyuk olmali, ama quantity ve price da iptal/iadelerden kaynakli aykiri degerler oldugunu goruyoruz

# invoice C ile baslayanlari (iptal urunleri) disarida birakalim
df = df.loc[~df["Invoice"].str.contains("C", na=False)]   # na=False parametresi, eksik değerlerin (NaN) kontrol edilmemesini sağlar

df.describe().T
# Yorum 1: min quantity ve price 1 veya 1den buyuk olmali, totalprice ici min degeri 0, o 1den buyuk olmali

# totalprice >= 1 alalim
df = df.loc[df["TotalPrice"] >= 1, :]

df.describe().T
# Yorum 1: min quantity ve price 1 veya 1den buyuk olmali,artik oyle gorunuyor
# Yorum 2: %75 ile %100 yani max arasinda asiri fark olmamali, kontrol edelim
# Yorum 3: ornegin online'da mean 14, %50lik deger 6, tutarli olabilir





##################################################################################
# 4. RFM Metriklerinin Hesaplanması (Calculating 3 RFM Metrics)
##################################################################################

# Recency:    Analiz tarihi - Müşterinin son alışveriş tarihi
# Frequency:  Müşterinin toplam satın alma sayısı  (Toplam işlem/fatura sayısı)
# Monetary:   Müşterinin TOPLAM Harcama tutarı


### 1) Analizin yapildigi gunu tanimlayalim, en son satin alma tarihi 11 aralik 2010 ise:
df["InvoiceDate"].max()    # dataframe deki en son satin alma tarihi !!
today_date = dt.datetime(2010, 12, 11)
type(today_date)


### 2) Müşteri özelinde Recency, Frequency ve Monetary metriklerini hesaplayalim.

## Gerekirse Customer ID ye gore gruplayalim, müşterileri tekilleştirelim (Customer ID ler her satirda tek ise, gerek yoktur.)
# today_date - InvoiceDate.max() >> yani bugunun tarihinden, ilgili musterinin en son satin alma tarihini cikar
# Invoice.nunique() >> yani ilgili musteriye ait, essiz fatura sayisini bul
# TotalPrice.sum() >> yani ilgili musteriye ait, toplam price i bul

rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda x: (today_date - x.max()).days,
                                     'Invoice': lambda x: x.nunique(),
                                     'TotalPrice': lambda x: x.sum()})


### 3) Olusturdugumuz yeni metrik isimlerini 'recency', 'frequency', 'monetary' olarak guncelleyelim
rfm = rfm.rename(columns = {"InvoiceDate": "recency", "Invoice": "frequency", "TotalPrice": "monetary"})
# veya  rfm.columns = ['recency', 'frequency', 'monetary']


### 4) Genel olarak degerleri kontrol edelim
rfm.describe().T

# Baktigimizda, monetary min degeri 0 gorunuyor, mantiksiz. Bu 0 li deger(ler)i ucuralim
rfm = rfm.loc[rfm["monetary"] > 0, :]
# veya rfm = rfm[rfm["monetary"] > 0]






##################################################################################
# 5. RFM Skorlarının Hesaplanması (Calculating RFM Scores)
##################################################################################

## RFM metriklerini RFM skorlarına çevirmedeki amaçlar:
# Farklı ölçek türlerine sahip RFM metriklerini aynı ölçek türüne çevirme
# RFM metrikleri üzerinde bir nevi standartlaştırma işlemi uygulama
# RFM metriklerini birbirleri ile kıyaslanabilir formata getirme


# Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevirelim
rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])


# Yeni bir RFM_SCORE sutunu olusturalim: recency_score ve frequency_score degerlerini string olarak yanyana yazdiralim:
rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str))


# Örnek: Aşağıdaki kodun çıktısı bize hangi RFM segmentini verir? : champions! (Recency=5, Frequency=5)
rfm.loc[rfm["RFM_SCORE"] == "55", :]

# Örnek Aşağıdaki kodun çıktısı bize hangi RFM segmentini verir? : hibernating! (Recency=1, Frequency=1)
rfm.loc[rfm["RFM_SCORE"] == "11", :]






##################################################################################
# 6. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi (Creating & Analysing RFM Segments)
##################################################################################

### 1) RFM Score larına göre Segment Map i oluşturma
# regex ile yapacağız  (: raw string demektir)

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
rfm.groupby("segment").agg({"recency": ["mean", "count"], "frequency": ["mean", "count"], "monetary": ["mean", "count"]})
# veya rfm[["recency", "frequency", "monetary", "segment"]].groupby("segment").agg(["mean", "count"])


### 3) csv dosyası olarak kaydedelim.  (kodu çalıştır, Project'te CRM_Analytics sağ tıkla, Reload from Disk tıkla, dosya orada)
rfm.to_csv("rfm.csv")



### Mesela bir departman bizden, cant_loose segmentine ait musterilerin id lerini istediyse:
# segment i cant_loose olanlarin index bilgileri, yani Customer ID leri !!
rfm[rfm["segment"] == "cant_loose"].index

# bir dataframe olusturalim
new_df = pd.DataFrame()
new_df["cant_loose_customer_id"] = rfm[rfm["segment"] == "cant_loose"].index

# id ler float gorunuyor, integer yapalim:
new_df["cant_loose_customer_id"] = new_df["cant_loose_customer_id"].astype(int)

# Bir departmana vb. göndermemiz gerekirse diye, csv dosyası olarak kaydedelim.
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


### NOTES !
# 1) Bu fonksiyon içindeki adımlar, ayrı ayrı fonksiyonlar şeklinde de yazılabilir. return çıktıları sonraki adıma ait fonksiyonda kullanılabilir.
# 2) Bu fonksiyonu örneğin her ay çalıştırıyorsak, dataframe içeriği değişmiş olabileceğinden, çıktıların doğruluğunu mutlaka kontrol etmeliyiz.(fonksiyon öncesi adımlarda da)





