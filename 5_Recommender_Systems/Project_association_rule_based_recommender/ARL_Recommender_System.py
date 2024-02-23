###################################################
# PROJE:Association Rule Based Recommender System
###################################################
import pandas as pd

# Association Rule Based Recommender:  Birliktelik analizi ile, sık olarak birlikte alınan ürünlere göre öneriler sunulur. (Sepet analizi)
# ARL yöntemi, kullanıcıların puan verme alışkanlıklarına dayanmaz ve sadece ürünler arasındaki ilişkileri baz alır.
# Kullanıcı bilgilerine ihtiyaç yok SepetID x Ürün dataframe'ine ihtiyaç var.


# Apriori Algoritması: Sepet analizi yöntemidir. Ürün birlikteliklerini ortaya çıkarır. Büyük veri setlerinde birliktelik kurallarını tespit etmek içindir.
# Support(X, Y) = Frequence(X,Y) / bütün işlemler   (X ve Y'nin birlikte görülme olasılığı)
# Confidence(X,Y) = Frequence(X,Y) / Frequence(X)   (X satın alındığında Y'nin de satın alınma olasılığı)
# Lift = Support(X, Y) / Support(X) * Support(Y)    (X satın alındığında Y'nin satın alınma olasılığı lift kadar artar)



## PROJE ADIMLARI ##
# 1. İş Problemi                        (Business Problem)
# 2. Veriyi Anlama & Hazırlama          (Data Understanding)
# 3. ARL Veri Yapısını Hazırlama (Invoice-Product Matrix)
# 4. Birliktelik Kurallarının Çıkarılması
# 5. Sepet Aşamasındaki Kullanıcılara Ürün Önerisinde Bulunmak





#########################
# 1. İş Problemi
#########################

# Veri Seti Hikayesi
# https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

# Online Retail II isimli veri seti,  İngiltere merkezli bir e-ticaret şirketinin 01/12/2009 - 09/12/2011 tarihleri arasındaki satışlarını içeriyor.
# Bu sirket hediyelik esya satiyor, musterileri genelde kurumsal toptancilardir.

# Sepet bilgilerine en uygun ürün önerisini birliktelik kuralı kullanarak/Association Rule Learning ile yapınız. 

# Değişkenler
# InvoiceNo:    Fatura numarası. Her işleme yani faturaya ait eşsiz numara. C ile başlıyorsa iptal edilen işlem.
# StockCode:    Ürün kodu. Her bir ürün için eşsiz numara.
# Description:  Ürün ismi
# Quantity:     Ürün adedi. Bir faturada 1den fazla urun yer alabilir.
# InvoiceDate:  Fatura tarihi ve zamanı.
# UnitPrice:    Ürün fiyatı (Sterlin cinsinden)
# CustomerID:   Eşsiz müşteri numarası
# Country:      Ülke ismi. Müşterinin yaşadığı ülke.







#########################
# 2. Veriyi Anlama & Hazırlama
#########################
# !pip install mlxtend
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

pd.set_option('display.max_columns', None)              # DataFrame'in gösterilecek maksimum sütun sayısını belirler. (None ise tüm sütunlar gelir)
pd.set_option('display.width', 500)                     # Çıktının yanyana gelmesi için genişlik ayarlar.
pd.set_option("display.precision", 2)                   # Float türündeki sayıların gösterilecek ondalık basamak sayısını belirler.
pd.set_option('display.expand_frame_repr', False)       # Geniş Dataframe'lerin tamamını terminal penceresine sığdırmak için kullanılır.
pd.set_option("display.max_rows", 100)                  # DataFrame'in gösterilecek maksimum satır sayısını belirler.

# Excel'de var olan sheet name leri görelim:
file_path  = pd.ExcelFile("Project_association_rule_based_recommender/online_retail_II.xlsx")
sheet_names = file_path.sheet_names
print("Sheet Names in the Excel File:", sheet_names)

# Adım 1: Online Retail II veri setinden 2010-2011 sheet’ini okutunuz.
df = pd.read_excel("Project_association_rule_based_recommender/online_retail_II.xlsx", sheet_name="Year 2010-2011")  # pip install openpyxl



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


# Adım 2: StockCode’u POST olan gözlem birimlerini drop ediniz. (POST her faturaya eklenen bedeldir, ürünü ifade etmemektedir.)

# Belirli satırlara ait indexleri seçmek
post_rows = df.loc[df["StockCode"] == "POST"].index

# Seçilen satırları veri çerçevesinden kaldırmak
df.drop(post_rows, axis=0, inplace=True)



# Adım 3: Boş değer içeren gözlem birimlerini drop ediniz. (Customer ID ve Description' dan Null value lar var)
df.isnull().sum().sort_values(ascending=False)

df.dropna(inplace=True)



# Adım 4: Invoice içerisinde C bulunan değerleri veri setinden çıkarınız. (C faturanın iptalini ifade etmektedir.)

# Belirli satırlara ait indexleri seçmek
c_rows = df.loc[df["Invoice"].str.contains("C")].index

# Seçilen satırları veri çerçevesinden kaldırmak
df.drop(c_rows, axis=0, inplace=True)



# Adım 5:  Price ve Quantity değişkenlerinin aykırı değerlerini inceleyiniz, gerekirse baskılayınız.
df.describe().T
df.describe([0, 0.05, 0.1, 0.25, 0.50, 0.75, 0.95, 0.99, 1]).T      # price ve quantity'de %99 ve %100 arasında çok fark var, aykırı değerler var


#  Bu fonksiyon, dataframe'deki belirli bir değişken için, alt ve üst sınırları / eşik değerleri hesaplar. (0.01 ve 0.99 değerleri değiştirilebilir)
def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)    # değişkenin %1 inci yüzdelik dilimini hesaplar
    quartile3 = dataframe[variable].quantile(0.99)    # değişkenin %99'uncu yüzdelik dilimini hesaplar
    interquantile_range = quartile3 - quartile1       # bu yüzdelik dilimler arasındaki aralığı bulur
    up_limit = quartile3 + 1.5 * interquantile_range  # Üst eşik değeri hesaplamak için üst yüzdelik dilimi (quartile3) ile aralığın 1.5 katını çarparak ekler.
    low_limit = quartile1 - 1.5 * interquantile_range # Alt eşik değeri hesaplamak için alt yüzdelik dilimi (quartile1) ile aralığın 1.5 katını çıkartarak azaltır.
    return low_limit, up_limit                        # Alt ve üst eşik değerleri döndürür


# Bu fonksiyon, dataframe'deki belirli bir değişken için aykırı değerleri, belirlenen alt ve üst sınırlarla / eşik değerlerlerle değiştirmek için kullanılır.
def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)          # outlier_thresholds fonksiyonu aracılığıyla, alt ve üst eşik değerlerini belirler (low_limit ve up_limit).
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit # veri setindeki değişkenin alt eşik değerinden küçük olan tüm değerleri alt eşik değeriyle değiştirir.
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit   # veri setindeki değişkenin üst eşik değerinden büyük olan tüm değerleri üst eşik değeriyle değiştirir.

replace_with_thresholds(df, "Quantity")
replace_with_thresholds(df, "Price")


df.describe([0, 0.05, 0.1, 0.25, 0.50, 0.75, 0.95, 0.99, 1]).T    # price ve quantity'de %99 ve %100 arasında artık daha az fark var, aykırı değerleri sildik





############################################
# 3. ARL Veri Yapısını Hazırlama (Invoice-Product Matrix)
############################################

# Adım 1: Aşağıdaki gibi sepet-ürün pivot table’ini oluşturunuz.
# Nihai olarak varmak istediğimiz dataframe: (satırlarda invoice/transaction/sepetler, sütunlarda ürünler olacak, değerler True veya False olacak)

# Description/Hizmet     Urun1  Urun2  Urun3  Urun4  Urun5
# SepetID/InvoiceID
# 0_2017-08              False  False  False  False  False
# 0_2017-09              False  False  True   False  False
# 0_2018-01              False  False  False  True   False

# Invoice ve Description'a göre gruplayalım  (Invoice ve Description değerleri satırlarda yanyana gelecek)
df.groupby(["Invoice", "Description"])["Description"].count()

# unstack ile pivot yaparız, yani 'Invoice' değerleri satırlara, 'Description' değerleri ise sütunlara yerleştirilir
df.groupby(["Invoice", "Description"])["Description"].count().unstack()

# notnull() ile: Bir hücrede değer True ise, o sepet için o hizmetin alındığını gösterir; aksi takdirde False olur.
invoice_product_df = df.groupby(["Invoice", "Description"])["Description"].count().unstack().notnull()
invoice_product_df.head()



#########################
# 4. Birliktelik Kurallarının Çıkarılması
#########################

# Bu kod, verilen dataframe üzerinde Apriori algoritmasını kullanarak sık öğe kümelerini (frequent itemsets) bulur.
frequent_itemsets = apriori(invoice_product_df,
                            min_support=0.01,  # min_support parametresi, sık öğe kümeleri oluştururken kullanılacak destek eşiğini belirler.
                            use_colnames=True) # use_colnames parametresi, öğelerin gerçek adlarını kullanıp kullanmama seçeneğini belirtir.

# Bu kod, birliktelik kurallarını çıkarmak için mlxtend kütüphanesindeki association_rules fonksiyonunu ve yukarıda oluşturduğumuz frequent_itemsets i kullanır.
rules = association_rules(frequent_itemsets,    # Sık öğe kümelerini içeren bir DataFrame.
                          metric="support",     # Burada "support" metriği seçilmiştir, yani destek değerine göre birliktelik kuralları oluşturulur.
                          min_threshold=0.01)   # Destek değeri için minimum eşik değeri 0.01 olarak belirlenmiştir.

# Sonuç dataframe inde her satır, bir kuralı temsil eder ve bu kuralda iki bileşen bulunur: antecedents (önceden koşul, X) ve consequents (sonuç, Y).
rules.head()
#                              antecedents                            consequents  antecedent support  consequent support  support  confidence   lift  leverage  conviction  zhangs_metric
# 0      (60 CAKE CASES DOLLY GIRL DESIGN)      (PACK OF 72 RETROSPOT CAKE CASES)                0.02                0.06     0.01        0.53   9.59  9.16e-03        2.03           0.91
# 1      (PACK OF 72 RETROSPOT CAKE CASES)      (60 CAKE CASES DOLLY GIRL DESIGN)                0.06                0.02     0.01        0.18   9.59  9.16e-03        1.20           0.95
# 2      (60 CAKE CASES VINTAGE CHRISTMAS)  (SET OF 20 VINTAGE CHRISTMAS NAPKINS)                0.03                0.03     0.01        0.40  15.17  9.45e-03        1.63           0.96




############################################
# 5. Sepet Aşamasındaki Kullanıcılara Ürün Önerisinde Bulunmak
############################################

# Bu fonksiyon, verilen ürün id si için ürün isimlerini bulur.
def check_id(stock_code, dataframe):
    Description = dataframe.loc[dataframe["StockCode"] == stock_code, "Description"].values
    if len(Description) > 0:
        return Description[0]
    else:
        return "Description is not found"



# Bu fonksiyon, bir ürün ID'si verildiğinde, bu ürünle "en yüksek lift değerine" sahip ilişki kurallarını bulur ve bu kuralların consequents (sonuç) kısmındaki ürünleri öneri listesine ekler.
# Daha sonra bu öneri listesini, belirtilen sayıda öneri ile sınırlayarak döndürür.
def arl_recommender(rules_df, product_name, rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)   # Yüksek lift değeri, iki ürünün birlikte satın alınma eğiliminin yüksek olduğunu gösterir. confidence'e göre de sıralanabilir insiyatife baglıdır.
    recommendation_list = []                                       # Tavsiye edilecek ürünler için boş bir liste oluşturuyoruz.

    for i, product in enumerate(sorted_rules["antecedents"]):
        for j in list(product):
            if j == product_name:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"])[0])

    return recommendation_list[0:rec_count]



# En son ürünün id'si: 20712 alan bir kullanıcıya yeni ürün önerisinde bulununuz.
check_id(20712, df)
# 'PACK OF 6 SKULL PAPER CUPS'
arl_recommender(rules, "JUMBO BAG WOODLAND ANIMALS", 5)
# ['JUMBO BAG PINK POLKADOT', 'JUMBO BAG RED RETROSPOT']


# En son ürünün id'si: 20712 alan bir kullanıcıya yeni ürün önerisinde bulununuz.
check_id(22613, df)
# 'PACK OF 20 SPACEBOY NAPKINS'
arl_recommender(rules, "60 CAKE CASES DOLLY GIRL DESIGN", 5)
# ['PACK OF 72 RETROSPOT CAKE CASES']
