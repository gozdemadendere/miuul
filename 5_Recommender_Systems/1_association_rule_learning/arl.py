############################################
# ASSOCIATION RULE LEARNING (BİRLİKTELİK KURALI ÖĞRENİMİ)
############################################

# Birliktelik analizi ile, sık olarak birlikte alınan ürünlere göre öneriler sunulur. (Sepet analizi)
# ARL yöntemi, kullanıcıların puan verme alışkanlıklarına dayanmaz ve sadece ürünler arasındaki ilişkileri baz alır.
# Kullanıcı bilgilerine ihtiyaç yok SepetID x Ürün dataframe'ine ihtiyaç var.

# Örnek: Bebek bezi ve biranın birlikte alınmasının analiz edilmesi. Ürün reyonlarının buna göre düzenlenmesi veya web satışında biranın sunulması.
# Örnek: Kırmızı topuklu ayakkabı satın alan müşterilerin genellikle siyah elbiseler veya metalik aksesuarlar da satın aldığını tespit edebiliriz ve bu ürünleri önerilebiliriz.


# Apriori Algoritması: Sepet analizi yöntemidir. Ürün birlikteliklerini ortaya çıkarır.
# Support(X, Y) = Frequence(X,Y) / bütün işlemler   (X ve Y'nin birlikte görülme olasılığı)
# Confidence(X,Y) = Frequence(X,Y) / Frequence(X)   (X satın alındığında Y'nin de satın alınma olasılığı)
# Lift = Support(X, Y) / Support(X) * Support(Y)    (X satın alındığında Y'nin satın alınma olasılığı lift kadar artar)

# Support (Destek):    Bir kuralın datasette ne kadar sık görüldüğünü ölçer.
# Yüksek support değerleri, kuralın daha yaygın olduğunu ve daha güvenilir olduğunu gösterir.

# Confidence (Güvenilirlik): Bir kuralın ne kadar doğru olduğunu ölçer.
# Yüksek confidence değerleri, kuralın doğruluğunun daha yüksek olduğunu gösterir.

# Lift:  İki ürün arasındaki ilişkinin gücünü ölçer / İki ürün arasındaki bağımlılığı ifade eder.
# Lift değeri > 1 ise bu iki ürün arasında pozitif bir ilişki, 1'e yakınsa, iki ürün arasında bir ilişki yok, < 1 ise, iki ürün arasında negatif bir ilişki olabilir veya birbirlerinden bağımsızdırlar.




# PROJE ADIMLARI
# 1. Veriyi Anlama & Hazırlama
# 2. ARL Veri Yapısını Hazırlama (Invoice-Product Matrix)
# 3. Birliktelik Kurallarının Çıkarılması
# 4. Çalışmanın Scriptini Hazırlama
# 5. Sepet Aşamasındaki Kullanıcılara Ürün Önerisinde Bulunmak




############################################
# 1. Veriyi Anlama & Hazırlama
############################################

# !pip install mlxtend
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

pd.set_option('display.max_columns', None)              # DataFrame'in gösterilecek maksimum sütun sayısını belirler. (None ise tüm sütunlar gelir)
pd.set_option('display.width', 500)                     # Çıktının yanyana gelmesi için genişlik ayarlar.
pd.set_option("display.precision", 2)                   # Float türündeki sayıların gösterilecek ondalık basamak sayısını belirler.
pd.set_option('display.expand_frame_repr', False)       # Geniş Dataframe'lerin tamamını terminal penceresine sığdırmak için kullanılır.
pd.set_option("display.max_rows", 100)                  # DataFrame'in gösterilecek maksimum satır sayısını belirler.

# pip install openpyxl
df_ = pd.read_excel("datasets/online_retail_II.xlsx", sheet_name="Year 2010-2011")    # https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

# Sorun olursa: df_ = pd.read_excel("datasets/online_retail_II.xlsx", sheet_name="Year 2010-2011", engine="openpyxl")

df = df_.copy()
df.head()


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
    print(dataframe.describe([0, 0.05, 0.1, 0.25, 0.50, 0.75, 0.95, 0.99, 1]).T)

# Use the function
check_df(df)

################################################

## Analizler:

# Null value lar var: # Outlier/Aykırı değerleri kırpmalıyız: Invoice başında C olanlarda iadeler var. Quantity ve price da 0 ler var. Onları kaldırmalıyız.
df.isnull().sum().sort_values(ascending=False)
# Customer ID    135080
# Description      1454

# Duplicated value lar var:
df.duplicated().sum()
# 5268

# Sayısal değişkenleri betimleyelim:  # price ve quantity'de - değerler var. Ayrıca %75 ve max değerler arasında çok fark var. Demekki aykırı değerler var.
df.describe().T
df.describe([0, 0.05, 0.1, 0.25, 0.50, 0.75, 0.95, 0.99, 1]).T

df.shape  # (541910, 8)



# Data Cleaning için, bir fonksiyon tanımlayalım:
def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)                    # Veri setindeki eksik değerleri (NaN) içeren satırları kaldırır.
    df['Invoice'] = df['Invoice'].astype(str)         # Invoice datatype ini string yapalım, object olması sonraki adımlarda sorun çıkarıyor.
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)] # 'Invoice' sütununda "C" harfi içermeyen tüm satırları filtreler.
    dataframe = dataframe[dataframe["Quantity"] > 0]  # Quantity' sütununda 0'dan büyük olan satırları filtreler.
    dataframe = dataframe[dataframe["Price"] > 0]     # 'Price' sütununda 0'dan büyük olan satırları filtreler.
    return dataframe                                  # Temizlenmiş veri setini döndürür.

df = retail_data_prep(df)

# Değerleri tekrar check edelim:
# Değerler daha anlamlı, ama hala quantity ve price'da, %75 ve max arasında çok fark var. Yani Outlier/Aykırı değerler hala mevcut.
df.describe().T


# Veri setindeki belirli bir değişken için, alt ve üst eşik değerleri hesaplayacak bir fonksiyon tanımlayalım: (0.01 ve 0.99 değerleri değiştirilebilir)
def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)    # değişkenin %1 inci yüzdelik dilimini hesaplar
    quartile3 = dataframe[variable].quantile(0.99)    # değişkenin %99'uncu yüzdelik dilimini hesaplar
    interquantile_range = quartile3 - quartile1       # bu yüzdelik dilimler arasındaki aralığı bulur
    up_limit = quartile3 + 1.5 * interquantile_range  # Üst eşik değeri hesaplamak için üst yüzdelik dilimi (quartile3) ile aralığın 1.5 katını çarparak ekler.
    low_limit = quartile1 - 1.5 * interquantile_range # Alt eşik değeri hesaplamak için alt yüzdelik dilimi (quartile1) ile aralığın 1.5 katını çıkartarak azaltır.
    return low_limit, up_limit                        # Alt ve üst eşik değerleri döndürür

# Belirli bir değişken için aykırı değerleri, outlier_thresholds fonksiyonundan elde edilen alt ve üst eşik değerleriyle, değiştiren bir fonksiyon:
def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)          # outlier_thresholds fonksiyonu aracılığıyla, alt ve üst eşik değerlerini belirler (low_limit ve up_limit).
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit # veri setindeki değişkenin alt eşik değerinden küçük olan tüm değerleri alt eşik değeriyle değiştirir.
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit   # veri setindeki değişkenin üst eşik değerinden büyük olan tüm değerleri üst eşik değeriyle değiştirir.

# Data Cleaning için tanımladığımız fonksiyona, eşik değer fonksiyonunu da ekleyelim:
def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)  # Veri setindeki tüm eksik değerleri (NaN) kaldırır.
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_thresholds(dataframe, "Quantity")
    replace_with_thresholds(dataframe, "Price")
    return dataframe


df = retail_data_prep(df)
df.isnull().sum().sort_values(ascending=False)  # Null değerler kaldırıldı
df.describe().T   # değerler daha anlamlı
df.shape  # (397885, 8)





############################################
# 2. ARL Veri Yapısını Hazırlama (Invoice-Product Matrix)
############################################

### Adım 1: Invoice-Product Matrisini oluşturalım:
# Nihai olarak varmak istediğimiz dataframe: (satırlarda invoice/transaction/sepetler, sütunlarda ürünler olacak, değerler True veya False olacak)

# Description/Hizmet     Urun1  Urun2  Urun3  Urun4  Urun5
# SepetID/InvoiceID
# 0_2017-08              False  False  False  False  False
# 0_2017-09              False  False  True   False  False
# 0_2018-01              False  False  False  True   False


# Dataframe i France a indirgeyelim
df_fr = df[df['Country'] == "France"]

# Invoice ve Description'a göre gruplayalım  (invoice lar ve description lar satırlarda yanyana gelecek)
df_fr.groupby(['Invoice', 'Description'])['Quantity'].sum()

# notnull() ile: Bir hücrede değer True ise, o sepet için o hizmetin alındığını gösterir; aksi takdirde False olur.
df_fr.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().notnull()




### Adım 2: Invoice-Product Matrisini oluşturan bir fonksiyon oluşturalım:

# id=False ise sütunlarda Description yer alır, id=True ise sütunlarda StockCode yer alır.
def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['Invoice', "StockCode"])['Quantity'].sum().unstack().notnull()
    else:
        return dataframe.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().notnull()


# id=False ise sütunlarda Description yer alır.
fr_inv_pro_df = create_invoice_product_df(df_fr)

# id=True ise sütunlarda StockCode yer alır.
fr_inv_pro_df = create_invoice_product_df(df_fr, id=True)

# check etmek için, id soralim
def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe["StockCode"] == stock_code][["Description"]].values[0].tolist()
    print(product_name)


check_id(df_fr, 10120)







############################################
# 3. Birliktelik Kurallarının Çıkarılması
############################################

# Oluşturduğumuz Invoice-Product Matrisini fonksiyon ile çağıralım: id=False ise sütunlarda Description yer alır.
fr_inv_pro_df = create_invoice_product_df(df_fr)

# Bu kod, verilen dataframe üzerinde Apriori algoritmasını kullanarak sık öğe kümelerini (frequent itemsets) bulur.
frequent_itemsets = apriori(fr_inv_pro_df,
                            min_support=0.01,  # min_support parametresi, sık öğe kümeleri oluştururken kullanılacak destek eşiğini belirler.
                            use_colnames=True) # use_colnames parametresi, öğelerin gerçek adlarını kullanıp kullanmama seçeneğini belirtir.


# Bu kod, birliktelik kurallarını çıkarmak için mlxtend kütüphanesindeki association_rules fonksiyonunu ve yukarıda oluşturduğumuz frequent_itemsets i kullanır.
rules = association_rules(frequent_itemsets,    # Sık öğe kümelerini içeren bir DataFrame.
                          metric="support",     # Burada "support" metriği seçilmiştir, yani destek değerine göre birliktelik kuralları oluşturulur.
                          min_threshold=0.01)   # Destek değeri için minimum eşik değeri 0.01 olarak belirlenmiştir.


# rules df'ini filtreleyelim: destek (support) değeri 0.05'ten büyük olsun. Güven (confidence) değeri 0.1'den büyük olsun. Kaldırma (lift) değeri 5'ten büyük olsun.
rules.loc[(rules["support"] > 0.05) & (rules["confidence"] > 0.1) & (rules["lift"] > 5)]    # veya: rules[(rules["support"]>0.05) & (rules["confidence"]>0.1) & (rules["lift"]>5)]


check_id(df_fr, 21086)

# Sonuç dataframe inde her satır, bir kuralı temsil eder ve bu kuralda iki bileşen bulunur: antecedents (önceden koşul, X) ve consequents (sonuç, Y).
# İki bileşen arasında bir ilişki oluşturulur ve bu kural, alışveriş sepeti verileri üzerinde bulunan bir ilişkiyi ifade eder.
rules[(rules["support"]>0.05) & (rules["confidence"]>0.1) & (rules["lift"]>5)].sort_values("confidence", ascending=False)







############################################
# 4. Çalışmanın Scriptini Hazırlama
############################################

# Veri setindeki belirli bir değişken için, eşik değerleri hesaplayacak bir fonksiyon tanımlayalım: (0.01 ve 0.99 değerleri değiştirilebilir)
def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)    # değişkenin %1 inci yüzdelik dilimini hesaplar
    quartile3 = dataframe[variable].quantile(0.99)    # değişkenin %99'uncu yüzdelik dilimini hesaplar
    interquantile_range = quartile3 - quartile1       # bu yüzdelik dilimler arasındaki aralığı bulur
    up_limit = quartile3 + 1.5 * interquantile_range  # Üst eşik değeri hesaplamak için üst yüzdelik dilimi (quartile3) ile aralığın 1.5 katını çarparak ekler.
    low_limit = quartile1 - 1.5 * interquantile_range # Alt eşik değeri hesaplamak için alt yüzdelik dilimi (quartile1) ile aralığın 1.5 katını çıkartarak azaltır.
    return low_limit, up_limit                        # Alt ve üst eşik değerleri döndürür


# Belirli bir değişken için aykırı değerleri, outlier_thresholds fonksiyonundan elde edilen alt ve üst eşik değerleriyle değiştiren bir fonksiyon:
def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)          # alt ve üst eşik değerlerini belirler (low_limit ve up_limit) outlier_thresholds fonksiyonu aracılığıyla.
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit # veri setindeki değişkenin alt eşik değerinden küçük olan tüm değerleri alt eşik değeriyle değiştirir.
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit   # veri setindeki değişkenin üst eşik değerinden büyük olan tüm değerleri üst eşik değeriyle değiştirir.


# Data Cleaning için tanımladığımız fonksiyona, eşik değer fonksiyonunu da ekleyelim:
def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)  # Veri setindeki tüm eksik değerleri (NaN) kaldırır.
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_thresholds(dataframe, "Quantity")
    replace_with_thresholds(dataframe, "Price")
    return dataframe

# Invoice-Product Matrisini oluşturan bir fonksiyon oluşturalım:
# id=False ise sütunlarda Description yer alır, id=True ise sütunlarda StockCode yer alır.
def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['Invoice', "StockCode"])['Quantity'].sum().unstack().notnull()
    else:
        return dataframe.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().notnull()


# check etmek için, id soralim
def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe["StockCode"] == stock_code][["Description"]].values[0].tolist()
    print(product_name)


def create_rules(dataframe, id=True, country="France"):
    dataframe = dataframe[dataframe['Country'] == country]   # Belirli bir ülkeye ait olan satış verilerini filtreler.
    dataframe = create_invoice_product_df(dataframe, id)     # Ürünlerin birlikte satın alınma durumlarını gösteren bir tablo oluşturmak için create_invoice_product_df fonksiyonunu kullanır.
    frequent_itemsets = apriori(dataframe, min_support=0.01, use_colnames=True)   # Apriori algoritmasını kullanarak sık öğe kümelerini (frequent_itemsets) belirler.
    rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.01)  # frequent_itemsets üzerinde association_rules fonksiyonunu kullanarak birliktelik kurallarını oluşturur.
    return rules                                             #  Son olarak, oluşturulan kuralları döndürür.

df = df_.copy()

df = retail_data_prep(df)
rules = create_rules(df)


# rules df'ini filtreleyelim: destek (support) değeri 0.05'ten büyük olsun. Güven (confidence) değeri 0.1'den büyük olsun. Kaldırma (lift) değeri 5'ten büyük olsun.
rules[(rules["support"]>0.05) & (rules["confidence"]>0.1) & (rules["lift"]>5)]









############################################
# 5. Sepet Aşamasındaki Kullanıcılara Ürün Önerisinde Bulunmak
############################################

# Örnek: Kullanıcı örnek ürün id: 22492

product_id = 22492
check_id(df, product_id)

sorted_rules = rules.sort_values("lift", ascending=False)   # dilediğimiz değişkene göre sıralarız lift / support/ confidence

recommendation_list = []

# ürünün ilk bulunduğu indexe karşılık, 2. ürünü çekmeye çalışalım
for i, product in enumerate(sorted_rules["antecedents"]):
    for j in list(product):
        if j == product_id:
            recommendation_list.append(list(sorted_rules.iloc[i]["consequents"])[0])

recommendation_list[0:3]

check_id(df, 22326)




# Bu fonksiyon, bir ürün ID'si verildiğinde, bu ürünle "en yüksek lift değerine" sahip ilişki kurallarını bulur ve bu kuralların consequents (sonuç) kısmındaki ürünleri öneri listesine ekler.
# Daha sonra bu öneri listesini, belirtilen sayıda öneri ile sınırlayarak döndürür.
def arl_recommender(rules_df, product_id, rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)   # Yüksek lift değeri, iki ürünün birlikte satın alınma eğiliminin yüksek olduğunu gösterir. confidence'e göre de sıralanabilir insiyatife baglıdır.
    recommendation_list = []                                       # Tavsiye edilecek ürünler için boş bir liste oluşturuyoruz.

    for i, product in enumerate(sorted_rules["antecedents"]):
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"])[0])

    return recommendation_list[0:rec_count]


arl_recommender(rules, 22492, 1)
arl_recommender(rules, 22492, 2)
arl_recommender(rules, 22492, 3)





