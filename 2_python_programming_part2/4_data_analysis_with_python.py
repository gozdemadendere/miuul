##########################################################################
# PYTHON ILE VERI ANALIZI (DATA ANALYSIS WITH PYTHON)
##########################################################################

# - NumPy (Numerical Python)
# - Pandas (Panel Data Analysis)
# - Data Visualization: Matplotlib & Seaborn (daha gelişmiştir)
# - Advanced Functional Exploratory Data Analysis (Gelişmiş Fonksiyonel Keşifçi Veri Analizi)




##################################################################################################
# NUMPY (Numerical Python)
# Python'da NumPy dizileri, matematiksel işlemleri hızlı bir şekilde gerçekleştirmek için kullanilan bir kutuphanedir.
# Yuksek boyutlu array ve matrisler uzerinde yuksek performansli calisma imkani saglar.


### Neden Python List yerine Numpy? Veya Numpy neden değerlidir?
# 1) Numpy, Python listelerinden daha hızlıdır (tek tip veri tutar)
# 2) Yüksek seviyeden (vektörel seviyeden) işlem yapılmasını sağlar (daha temiz kod çıktısı, daha iyi performans)


##################################################################################################

# Loading the library
import numpy as np

# Listeler:
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# a ve b elemanlarini carparak bir listeye ekleyelim.
# Normalde Python liste ile yapsaydik:
ab = []

for number in range(0, len(a)):
    ab.append(a[number] * b[number])

ab


# Numpy ile yaparsak:
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a
b

a * b





##########################
# Creating NumPy Arrays
##########################

type(np.array([1, 2, 3, 4, 5]))


np.array([1, 2, 3])  # [1, 2, 3] değerlerini içeren bir NumPy dizisi oluşturur.
np.zeros(5)          # 5 elemanlı, sıfırlardan oluşan bir NumPy dizisi oluşturur.
np.arange(1, 10, 2)  # 1'den başlayarak 10'a kadar (10 hariç) 2'şer adımlarla bir dizi oluşturur. Yani, [1, 3, 5, 7, 9] şeklinde bir dizi oluşturur.
np.empty(3)          # Belirtilen boyutta (3 eleman) ancak herhangi bir spesifik değer atamadan rastgele değerler içeren bir NumPy dizisi oluşturur.
np.random.randint(10, size=5)   # 5 elemanli, rastgele, 0 ile 10 arasinda bir NumPy dizisi oluşturur.



# Bu ifade, 10 elemanı sıfırlardan oluşan bir NumPy dizisi oluşturur. dtype=int parametresi, dizinin veri tipini integer olarak belirtir.
np.zeros(10, dtype=int)

# 0 ile 10 arasında (10 hariç) rastgele tam sayılar üreten bir NumPy dizisi oluşturur. size=10 parametresi, oluşturulacak dizi boyutunu belirtir. Yani, 10 adet rastgele tam sayı içeren bir dizi oluşturur.
np.random.randint(0, 10, size=10)

# ortalamasi 10, standart  sapmasi 4, 3x4 boyutunda bir NumPy dizisi olusturalim
np.random.normal(10, 4, (3, 4))



##########################
# NumPy array ozellikleri
##########################

# ndim: boyut sayisi
# shape: boyut bilgisi (satir sutun sayisi)
# size: toplam eleman sayisi
# dtype: array veri tipi


a = np.random.randint(10, size=5)

a.ndim    # 1   >> tek boyutlu
a.shape   # (5,)     >> 5 elemanli ve tek boyutlu
a.size    # 5     >> 5 elemanli
a.dtype    # int64
a.mean()   # 2.2



arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('1. boyuttaki 2.eleman: ', arr[0, 1])



arr = np.array([1, 2, 3, 4, 5, 6, 7])
#                          -3 -2 -1
print('-3. elemandan(yani 5), -1. elemana kadar(yani 7), -1. eleman dahil degil: ', arr[-3:-1])




array = np.array([1, 2, 3, 4, 5, 6, 7])
filter_array = array % 2 == 0
new_array = array[filter_array]
print(new_array)






##########################
# Reshaping
##########################

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

# veya kalici hale getirmek istersek

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)

# Fortune Cookie Program 🥠
fortune = np.random.randint(0, 4)
fortune

if fortune == 0:
    print("May you one day be carbon neutral")
elif fortune == 1:
    print("You have rice in your teeth")
elif fortune == 2:
    print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
    print("You can only connect the dots looking backwards")
elif fortune == 4:
    print("The fortune you seek is in another cookie")





##########################
# Index Selection
##########################

# Loading the library
import numpy as np

# 0dan 10a kadar, 10 adetlik bir numpy arrayi olusturma
a = np.random.randint(10, size=10)
a

a[0]
a[0:5]  # slicing

# arraydeki degeri degistirme
a[0] = 999
a[0:5]

# 3x5 boyutunda (3 satir 5 sutun), 0-10 arasi rakamlarla bir array
m = np.random.randint(10, size=(3, 5))
m

m[0, 0]
m[1, 1]
m[2, 3]   # 2.satir 3. sutundaki deger

# arraydeki degeri degistirme
m[2, 3] = 88 # 2.satir 3. sutundaki degeri 88 yap
m

# arraydeki degeri float olarak degistirme
m[2, 3] = 8.7
m  # 8.7 degil 8 olarak ekledi (numpy in hizli olmasi bundan dolayi, tek veri tipi ile calisiyor)

# butun satirlari sec ve 0. sutunu sec
m[:, 0]

# 1. satiri sec ve tum sutunlari sec
m[1, :]

# 0'dan 2. satira git(2.satir dahil degil) ve 0'dan 3. sutuna kadar git(3. sutun dahil degil)
m[0:2, 0:3]






##########################
# Fancy Index
##########################

# Fancy index ile, bir dizideki/arraydeki elemanlara toplu şekilde ulaşmak için bir listeyi veya diziyi kullanabiliriz.

# Basit bir numpy dizisi oluşturalım
arr = np.array([10, 20, 30, 40, 50])  # Çıktı: array([10, 20, 30, 40, 50])

# Fancy index için bir indeks listesi oluşturalım
indices = [1, 3]

# Fancy index kullanarak ilgili indekslerdeki elemanlara ulaşalım
result = arr[indices]    # indices adlı listedeki 1 ve 3 indekslerindeki elemanlara fancy index kullanarak ulaşıyoruz
#      = arr[1, 3]

print(result)  # Çıktı: [20 40]






##########################
# Numpy'da bir array in icinden kosullu eleman secme (Conditions on Numpy)
##########################

# Klasik dongu ile
import numpy as np

v = np.array([1, 2, 3, 4, 5])

ab = []
ab

for i in v:
    if i < 3:
        ab.append(i)
        print(ab)



# Numpy ile

v[v < 3]
v[v == 3]
v[v != 3]
v[v >= 3]





##########################
# Numpy arraylerinde matematiksel islemler
##########################

v = np.array([1, 2, 3, 4, 5])
v

# Matematiksel operatorler ile
v / 5
v * 5 / 10
v ** 2
v - 1

# Methodlar ile
np.add(v, 1)
np.subtract(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

v = np.add(v, 1)  # dersek, v artik bu sekilde baz alinacaktir.





##########################
# Numpy ile 2 bilinmeyenli denklem cozumu
##########################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)









##################################################################################################
# PANDAS
##################################################################################################
# NumPy üzerine kuruludur, daha gelişmiştir, veri analizi ve manipülasyonu için daha yüksek düzeyli işlevsellik sağlar.


### Pandas serisi tek boyutlu dizilerdir. Index bilgisi barindirir.
### Pandas Dataframe i  iki boyutlu bir veri yapısıdır. Tablo benzeridir, satırlar ve sütunlardan oluşur. Index bilgisi barindirir.


### NumPy array i ve Pandas Dataframe i arasındaki fark:
# 1- NumPy'da index yoktur (Pandas'ta attribute olarak index iç özelliktir, numpy'da ise biz kendimiz index tanımlarız)
# 2- Farklı veri tipleriyle çalışırlar. (NumPy dizileri tek boyutlu veya çok boyutlu olabilirken, Pandas DataFrame'leri iki boyutludur, yani satırlar ve sütunlar içerir.)
# 3- NumPy dizileri, matematiksel işlemleri hızlı bir şekilde gerçekleştirmek içindir, Pandas DataFrame'leri ise veri analizi ve manipülasyonu için daha yüksek düzeyli işlevsellik sağlar.



import pandas as pd

# bir pandas serisi olusturalim
s = pd.Series([10, 77, 12, 4, 5])
s  # pandas serisinde index bilgisiyle birlikte elemanlar gelir
type(s)

# index bilgisini görme
s.index  #(start=0, stop=5, step=1)  0dan 5e kadar, 5 dahil degil

# data type i görme
s.dtype  # int64

# eleman sayisini görme
s.size  # 5

# sadece elemanlari görme (numpy arrayi icinde bir liste seklinde döndürüyor)
s.values

# ilk x elemani görme
s.head(3)

# son x elemani görme
s.tail(3)





##########################
# Reading Data
##########################
import pandas as pd

# csv dosyalarini okuma
df = pd.read_csv("/datasets/advertising.csv")
# Projects altinda ilgili dosya uzerine gel, sag tikla,
# Copy Path e tikla, Path From.. tikla, 2 tirnak arasina gel, yapistir

df.head()



##########################
# Quick Look at Data
##########################
# Import libraries
import pandas as pd
import seaborn as sns

# Pandas ve Seaborn kütüphanelerinden bazı ayarları yapılandırma    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
pd.set_option("display.max_columns", None)  # Gösterilecek max sütun sayısını belirleme (None ise tüm sütunlar gelir)
pd.set_option("display.width", 500)         # Çıktının yanyana gelmesi için genişlik ayarı

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")

# DataFrame'in ilk beş satırını gösterme
print(df.head())


##########################
# Retrieving Series/DataFrame Information  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##########################

df.head()  # first x rows
df.tail()  # last x rows
df.info()  # Info on DataFrame
df.describe()  # Detailed info on DataFrame
df.describe().T  # Transpozu
df.count()  # Number of non-NA values
df.isnull().sum()  # How many are there Null values?
df.isnull()  # Is there any Null values?
df.isnull().values.any()  # True: there is at least 1 Null value


df.columns  # Describe DataFrame columns
df.shape  # (891, 15) (rows,columns)
df.index  # (start=0, stop=891, step=1) Describe index

df["sex"].head()  # sex sutununa ait ilk 5 satir
df["sex"].value_counts()  # sex sutununda kac kategori var ve kacar adet degerleri var?






##########################
# Pandas'ta Seçim Islemleri  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##########################

df.index  # 891 index var
df[0:13]  # 0'dan 13. indexe(satira) kadar döndür (13 dahil degil)

# drop: satir veya sutun silmek
df.drop(2, axis=0).head()   # axis=0 ise satirlardan, 2. indexi sil

# 1den fazla index silerken
delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# axis=1 ise sutunlardan, deck isimli sutunu sil
df.drop(["deck"], axis=1)

# Note: df=df.drop()... diyerek dataframe i yeni haliyle sabitleriz. Veya:
# df.drop(delete_indexes, axis=0, inplace=True) diyerek yeni haliyle sabitleriz.
# (inplace=True, bir degisiklik yapilinca bu degisikligi kalici yapan bir parametredir.)




##########################
# Degiskeni(sutunu) indexe cevirmek
##########################

df.index
df["age"].head()  # veya df.age.head()

# age degiskenini indexe atmak icin:
df.index = df["age"]
df.index
df.head()

# age i index yaptik,degisken olarak silmek icin
df.drop("age", axis=1).head()  # axis=1 sutunlardan siler

# age degiskenini "kalici olarak" silmek icin
df.drop("age", axis=1, inplace=True).head()

df.head()

##########################
# Index i degiskene cevirmek
##########################

df.index

# 1. yol
df["age"] = df.index
df.head()

# 2. yol
df.reset_index().head()
df = df.reset_index().head()
df.head()





##########################
# Degiskenler uzerinde islemler (SUTUNLAR)
##########################

import pandas as pd
import seaborn as sns

# set_option: pandasta bir ayar yapmak icin
pd.set_option("display.max_columns", None)  # display.max_columns : gosterilecek max column sayisi olmasin
df = sns.load_dataset("titanic")
df.head()

"age" in df  # age dataframe de var mi?

df["age"].head()  # ilk 5 age, pandas serisi seklide
type(df["age"].head())


df[["age"]].head()  # ilk 5 age, pandas dataframe i seklide
type(df[["age"]].head())

### df[“x”] ve df[[“x”]]  farklı, ilkinde seri seçerken 2.sinde dataframe seçiyoruz
# Sonuç olarak ikisinde sonuç data type i farklı olur (ilki pandas serisi 2.si dataframe i olarak gelir),
# Dikkat ! seriye ve dataframe e uygulanan methodlar farkli olabilmektedir



# bir dataframe de 1den fazla degisken secmek
df[["age", "alive"]]
df[["age", "alive", "adult_male"]]

# veya
col_names = ["age", "alive", "adult_male"]
df[col_names]

# dataframe e yeni degisken ekleme
df["age2"] = df["age"] ** 2
df.head()

df["age3"] = df["age"] / df["age2"]
df.head()

# dataframe den degisken silmek
df.drop("age3", axis=1).head()
df.drop("age3", axis=1, inplace=True) # kalici olmasi icin

# dataframe den cok sayida degisken silmek
col_names = ["age", "alive", "adult_male"]
df.drop(col_names, axis=1).head()

# icinde belirli bir "string ifadeyi" barindiran degiskenleri silmek
# loc: label based secimler icin
df.loc[:, df.columns.str.contains("age")].head()  # tum satirlari al, sutunlarda icinde age olanlari al

# usttekinin tam tersi degerler, yani age harici seyleri al
df.loc[:, ~df.columns.str.contains("age")].head()




import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
df
subset = df.loc[0:1, ['A', 'B']]



data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
df
subset = df.iloc[0:2, [0, 1]]


##########################
# loc : label based selection
# iloc: integer based selection
##########################

# loc : label based selection (This accessor selects rows and columns by labels.)
# Example: df.loc[row_label, column_label]
# Slicing: df.loc['row1_label':'row2_label' , 'column1_label':'column2_label']

df

df.loc[0:3]  # 0'dan 3.satira kadar(3 dahil), tum sutunlar
df.loc[:, 'embark_town':'age3']  # tum satirlar, embark_town daan age3 e sutunlar (age3 dahil)
df.loc[[0, 1, 2], 'embark_town':'age3']  # 0,1,2. satirlar, embark_town daan age3 e sutunlar (age3 dahil)

df.loc[0:3, "age"]  # 0'dan 3.satira kadar(3 dahil degil), age sutunu
df.loc[0:3, col_names]  # 0'dan 3.satira kadar(3 dahil degil), col_names icindeki sutunlar




# iloc: integer based selection (This accessor selects rows and columns by integer location.)
# Example: df.iloc[row_position, column_position]
# Slicing: df.iloc['row1_position':'row2_position','col1_position':'col2_position']


df.iloc[2, 2]  # 2. satirda, 2. sütunda olan deger
df.iloc[0:3]     # 0'dan 3.satira kadar, 3 dahil degil, tum  sutunlar
df.iloc[0:3, :]  # 0'dan 3.satira kadar, 3 dahil degil, tum  sutunlar

df.iloc[0:3, 0:3]  # 0'dan 3.satira kadar(3 dahil degil), 0'dan 3.sutuna kadar(3 dahil degil)







##########################
# Conditional Selection
##########################

import pandas as pd
import seaborn as sns

# set_option: pandasta bir ayar yapmak icin
pd.set_option("display.max_columns", None)  # display.max_columns : gosterilecek max column sayisi
df = sns.load_dataset("titanic")
df.head()




### 1.yol: df[koşul]
df[df["age"] > 50].head()  # age > 50 oldugunda, tum dataframe i getir
df["age"][df["age"] > 50].head()  # age > 50 oldugunda, sadece age sutununu getir
# veya
df[df["age"] > 50]["age"].head() # age > 50 oldugunda, tum dataframe i getir

df["age"][df["age"] > 50].count()  # age > 50 oldugunda, sadece age sutununda, kac kisi var? (yani 64 kisi 50 yastan buyuk)
df[df["age"] > 50].count()  # age > 50 olanlari say



### 2.yol: label based selection
df.loc[df["age"] > 50].head()  # age > 50 oldugunda, tum dataframe i getir
df.loc[df["age"] > 50, "age"].head()  # age > 50 oldugunda, sadece age sutununu getir
df.loc[df["age"] > 50, ["age", "class"]].head()  # age > 50 oldugunda, age ve class sutununu getir  *****



### 1'den fazla kosul varsa !!
# 1) Her kosul parantez icine alinmali ()
# 2) Kosul aralarinda & ya da | olmali
# 3) Kosul belirtirken df["age"] denmeli, sutun belirtirken "age" denmeli
# 4) Kosul belirtirken == kullanilmali, mesela: df["sex"] == "male"

# age > 50 & cinsiyeti erkek oldugunda, age ve class sutununu getir
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()

# age > 50 & cinsiyeti erkek & embark_town Cherbourg oldugunda, age class ve embark_town sutununu getir
df.loc[(df["age"] > 50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg"),
["age", "class", "embark_town"]].head()

# age > 50 & cinsiyeti erkek & embark_town Cherbourg veya Southampton olanlardan, age class ve embark_town sutununu getir
df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
["age", "class", "embark_town"]].head()





##########################
# Aggregation & Grouping (Toplulastirma & Gruplama)
##########################

# groupby()   :  groupby("age")  /  groupby(["age", "fare"])  : 2li degiskenlerde liste var!!
# agg({})     : agg({"age": "mean"})  / agg({"age": ["mean", "sum"]})   /  agg({"age": ["mean", "sum"], "fare": "mean"})
# count()
# first()
# last()
# mean()
# sum()
# median()
# min()
# max()
# std()
# var()

# pivot table


import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# yas ortalamasi
df["age"].mean()


# her bir cinsiyete gore, yas ortalamasi
df.groupby("sex")["age"].mean()
# veya
df.groupby("sex").agg({"age": "mean"})   # agg({})  icinde dictionary var


# cinsiyete gore yas ortalamasi ve yas toplami
df.groupby("sex").agg({"age": ["mean", "sum"]})  # ***** dictionary icinde, liste kullanabiliyorduk

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "embark_town": "count"})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})  # gemideki kadinlarn %74ü hayatta kalmis, erkeklerin %18i

df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],         # ***** groupby() icinde, liste kullanabiliyoruz
                                        "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})  # ornegin ilk sirada: kadinlarin yas ort 36, ort %97si kurtulmus, 43 kadin.





##########################
# Pivot Table
##########################

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head


# df.pivot_table("degerler", "satirlar", "sutunlar")
# degerler: survived degiskeninin ortalamasi(mean), satir:sex, sütun:embarked
df.pivot_table("survived", "sex", "embarked")


# kesisim(degerler): survived degiskeni icin standart sapma gelir
df.pivot_table("survived", "sex", "embarked", aggfunc="std")


# kesisim(degerler): survived degiskeninin ortalamasi(mean), satir:sex, sütun:embarked ve class
df.pivot_table("survived", "sex", ["embarked", "class"])






## NOTE:
# pd.cut  : Veriyi kullanıcının belirlediği aralıklara böler. Bu aralıklar eşit büyüklükte olmayabilir ve her bir aralıkta farklı sayıda gözlem olabilir.
# pd.qcut : Veriyi belirli sayıda eşit büyüklükte parçalara böler. Bu parçaların her birinde yaklaşık olarak eşit sayıda gözlem bulunur.

# Örnek veri oluşturma
data = {'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
df = pd.DataFrame(data)

# 'Value' sütununu 4 aralığa bölmek
df['Bins'] = pd.cut(df['Value'], bins=4)
print(df)

# 'Value' sütununu 4 aralığa bölmek
df['Bins'] = pd.qcut(df['Value'], q=4)
print(df)

# Yeni bir Segment sutunu olustur, Price i 4 esit parcaya bolerek 4 farkli Segment olustur
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], q=4, labels=["D", "C", "B", "A"])




##########################
# Sayisal degiskenleri, kategorik degiskenlere cevirme
##########################

# age kategorisi olusturalim:
# .cut ve .qcut: sayisal degiskenleri, kategorik degiskenlere cevirmek icin kullanilir
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
df.head()


# sutunlar: age kategorisi
df.pivot_table("survived", "sex", "new_age")

df.pivot_table("survived", "sex", ["new_age", "class"])

# Ciktinin yanyana gelmesi icin:  !!!!!!!!!!!
pd.set_option("display.width", 500)
df.head()






##########################
# apply  : Satir ya da sutunlarda otomatik olarak fonksiyon calistirma imkani saglar. (apply(lambda..) veya apply(def fonks adi...)  )
# lambda : Bir fonksiyon tanimlama seklidir. Kullan-at fonksiyondur.
##########################

import pandas as pd
import seaborn as sns

# Örnek 1
# Her kişinin yaşını kategoriye (genç, orta yaşlı veya yaşlı) göre sınıflandırmak istiyoruz.
# Genç, 30 yaşından küçük olanlar, orta yaşlılar 30 ile 60 yaş arasındakiler ve yaşlılar 60 yaşından büyük olanlar olarak kabul edilecektir.
# İpucu: lambda ifadesi ve apply yöntemini kullanın.

veri = {
              'İsim': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Ali'],
               'Yaş': [25, 35, 60, 55, 70]
}

df = pd.DataFrame(veri)
df

df['Yaş Kategorisi'] = df["Yaş"].apply(lambda x: "Genç" if x < 30 else ("Orta Yaşlı" if x <= 60 else "Yaşlı"))
df




# Örnek 2
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5


# tek tek yaparsak:
(df["age"] / 10).head()
(df["age2"] / 10).head()
(df["age3"] / 10).head()

# for dongusu ile:
for col in df.columns:  # df in sutunlarinda gez
    if "age" in col:  # eger age o sutundaysa
        df[col] = df[col] / 10  # bunu yazdir

df.head()


# ustteki islemi kolaylastiracak bir kullan-at fonksiyon tanimlayalim
df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()

# fonksiyonu daha programatik hale getirelim
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()

# age sutunlarinda bir normallestirme/standartlastirma islemi uygulatalim
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()


# veya ayni islemi, def fonksiyon tanimlayarak da apply ile uygulatabiliriz
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()


df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()  # yani apply ile def fonksiyonu da kullanabiliriz/

# üstteki islemi kaydetmek icin:
df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# veya daha otomatik sekilde yapalim:
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()





##########################
# Join (Birlestirme islemleri)
##########################

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))    # 5x3 boyutunda
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])  # pandas dataframe i olustur, m i kullan ve sutunlara var1 var2 var3 isimlerini ver
df2 = df1 + 99


# 1) pd.concat : 2 dataframe i alt alta birlestirmek
pd.concat([df1, df2])  # 2 dataframe oldugu icin,[] liste icinde tanimladik

# index leri de birlestirmek icin
pd.concat([df1, df2], ignore_index=True)



# 2) pd.merge
df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["mark", "john", "dennis", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})


df3 = pd.merge(df1, df2, how="inner", on="employees")
df3



# Amac: her calisanin mudur bilgisine de  erismek
df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})


df5 = pd.merge(df3, df4, how="inner", on="group")
df5


# veya tek seferde 2 merge yapmak
df6 = pd.merge(df1, df2, how="inner", on="employees").merge(df4, how="inner", left_on="group", right_on="group")
df6








##########################################################################
# DATA VISUALIZATION WITH PYTHON : MATPLOTLIB & SEABORN
##########################################################################

#############################################
# MATPLOTLIB
#############################################

# Katmanli bir sekilde, veri gorsellestirme saglar (ust uste 2 farkli veriyi farkli cizgilerle grafik yapabilir)

# Kategorik degisken var ise:   Sütun grafik, Countplot bar
# Sayisal degisken var ise:     Histogram, Boxplot


#####################################
# Kategorik Degisken Gorsellestirme : Sütun grafik, Countplot bar
#####################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

# bu df de, kategorik degiskenler var: sex, embarked, class, who

# kategorik degiskenlerle ilgilenirken: value_counts() kullanalim
df["sex"].value_counts()
df["sex"].value_counts().plot(kind="bar")
plt.show()

# matplotlib guncelleme: Python Console terminaline yaz:
# pip install matplotlib  veya  pip install --upgrade matplotlib


#####################################
# Sayisal Degisken Gorsellestirme : Histogram, Boxplot(kutu grafik)
#####################################


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

# Histogram cizelim:
plt.hist(df["age"])  # 20-30 yas arasinda yigilma var
plt.show()

# Boxplot cizelim:
plt.boxplot(df["fare"])  # aykiri degerleri gorebiliriz, genel dagilim disindaki degerleri gorebiliriz
plt.show()









#################################################
# Matplotlib Ozellikleri
#################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

### 1) plot

x = np.array([1, 8])
y = np.array([0, 150])

# iki numpy arrayini gorsellestirelim
plt.plot(x, y)  # x: 0,8 arasinda ve y: 0,150 arasinda
plt.show()

# cizgi yerine nokta seklinde de gosterebiliriz
plt.plot(x, y, "o")  # 2ser adet veri old icin, 2 adet nokta var
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y, "o")  # 5er adet veri old icin, 5 adet nokta var
plt.show()

### 2) marker

y = np.array([13, 28, 11, 100])

plt.plot(y, marker="o")  # marker: nokta
plt.show()

plt.plot(y, marker="o")  # marker: yildiz
plt.show()

### 3) line graph (marker'siz)
x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.plot(x)
plt.plot(y)

plt.plot(y, linestyle="dashed")  # kesikli cizgi
plt.plot(y, linestyle="dotted")  # noktali cizgi
plt.plot(y, linestyle="dashed", color="r")  # red / kirmizi renkli grafik

### 4) Multiple Lines

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

### 5) Labels

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x, y)

# Baslik
plt.title("Ana baslik", fontsize=20)

# X eksenini isimlendirme
plt.xlabel("X eksenini isimlendirme", fontsize=15)

# Y eksenini isimlendirme
plt.ylabel("Y eksenini isimlendirme", fontsize=15)

# Grafik arkasi izgara ekleme
plt.grid()
plt.show()

### 6) Subplots

## Yanyana 3 adet grafik olusturalim
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)  # 1 satirda 3 adetlik grafik olustur, 1.si bu
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 2)  # 1 satirda 3 adetlik grafik olustur, 2.si bu
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)  # 1 satirda 3 adetlik grafik olustur, 3.sü bu
plt.title("3")
plt.plot(x, y)

plt.show()









#################################################
# SEABORN
#################################################

# Yüksek seviye bir kutuphanedir. Yani daha az cabayla, daha cok is yapar.
# Dolayisiyla Matplotlib e gore daha kullanislidir.

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("tips")
df.head()



### 1) countplot: Kategorik degiskenler icin (Yine kategorik degisken icin value_counts kullanalim)
df["sex"].value_counts()

sns.countplot(data=df,
              x="sex",
              palette="OrRd")   # x: hangi kategoriyi gosterelim, data: hangi dataframe
plt.show()


# veya
sns.countplot(x=df["sex"],
              palette="OrRd")   # x: hangi kategoriyi gosterelim, data: hangi dataframe

# matplotlibde soyle olurdu:
df["sex"].value_counts().plot(kind="bar")
plt.show()


### 2) boxplot: Sayisal degiskenler icin
sns.boxplot(data=df,
            x="total_bill")
plt.show()

# veya
sns.boxplot(x=df["total_bill"])
plt.show()


### 3) histogram:  pandas icerisinde yer alan histogram fonksiyonu
df["total_bill"].hist()
plt.show()












##########################################################################
# ADVANCED FUNCTIONAL EDA
##########################################################################

### 1) Genel Resim
### 2) Kategorik Degisken Analizi (Analysis of Categorical Variables)
### 3) Sayisal Degisken Analizi (Analysis of Numerical Variables)
### 4) Hedef Degisken Analizi (Analysis of Target Variables)
### 5) Korelasyon Analizi (Analysis of Correlation)


#############################################
### 1) Genel Resim
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

df.head()
df.tail()
print(df.shape)
df.info()
print(df.columns)
print(df.index)
df.describe().T
df.isnull().values.any()
df.isnull().sum()
# veya
df.isnull().sum().sort_values(ascending=False)




# Functional Data Exploration : EDA fonksiyonu olusturalim    ****************************************************************************************************************************************

# Vahit Hoca'nin fonksiyonu:
def check_df(dataframe, head=5):
    print("###################### Head ######################")
    print(dataframe.head(head))
    print("###################### Tail ######################")
    print(dataframe.tail(head))
    print("###################### Shape ######################")
    print(dataframe.shape)
    print("###################### Info ######################")
    print(dataframe.info())
    print("###################### Types ######################")
    print(dataframe.dtypes)
    print("###################### NA ######################")
    print(dataframe.isnull().sum().sort_values(ascending=False))
    print("###################### Quantiles ######################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


# Gözde'nin fonksiyonu:
def explore_dataframe(dataframe, head=5):
    print("###################### First 5 Rows ######################")
    print(dataframe.head(head))
    print("###################### Last 5 Rows ######################")
    print(dataframe.tail(head))
    print("###################### Shape: Rows x Columns ######################")
    print(dataframe.shape)
    print("###################### General Info ######################")
    print(dataframe.info())
    print("###################### Null Values ######################")
    print(dataframe.isnull().sum().sort_values(ascending=False))
    print("###################### Statistical Info ######################")
    print(dataframe.describe().T)




df = sns.load_dataset("titanic")
check_df(df)

df = sns.load_dataset("tips")
check_df(df)




#############################################
### 2) Kategorik Degisken Analizi (Analysis of Categorical Variables)
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

# tek bir degisken analiz etmek istersek:
df["embarked"].value_counts()  # kategori bazli  sayilara erisiriz (sinif sayilarina)
df["sex"].unique()  # unique siniflara erisiriz : female, male
df["sex"].nunique()  # number of unique degerlere erisiriz: sex degiskeni icinde 2 essiz sinif var(female, male)


# Cok sayida degisken analiz etmek icinse, bir fonksiyon olusturalim           ***************************************************************************************************************************
df.info()
df.columns
df["sex"].dtypes
str(df["sex"].dtypes)
# Note: Kategorik degiskenler: category, object, bool (dtype sutununda yer alirlar )
# survived: integer(int64) yani numerik ama aslinda kategorik bir degisken (0 veya 1 yani 2 kategori var)


### ADIMLAR:
# 1.Adim:  + kategorik olan degiskenler : cat_cols
# 2.Adim:  + numerik gorunen ama kategorik olan degiskenler : num_but_cat
# 3.Adim:  - kategorik gorunen ama kategorik olmayan degiskenler : cat_but_car
# 4.Adim:    cat_cols + num_but_cat
# 5.Adim:    cat_cols - cat_but_car


##### 1 )))
# oncelikle, dtype i "category", "object", "bool" olanlari cagiralim
# list comprehesion kullanalim:

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

cat_cols



##### 2 )))
# dtype i numerik gorunen  ama kategorik olan degiskenleri cagiralim
# yani 10dan kucuk kategori sayisi (essiz sinif sayisi) olacak ve int64 veya float olacak (10 sayisi, datasete gore degisebilir, biz belirliyoruz)

num_but_cat = [col for col in df.columns if df[col].dtypes in ["int", "float"] and df[col].nunique() < 10]

num_but_cat



##### 3 )))
# Kategorik gorunen ama kategorik olmayan degiskenler
# dtype i object veya category olan, ama alt sinif sayisi cok fazla olan degiskenleri cagiralim

cat_but_car = [col for col in df.columns if str(df[col].dtypes) in ["category", "object"] and df[col].nunique() > 20]

cat_but_car



##### 4 )))
# tum kategorik degiskenleri biraraya toplayalim
cat_cols = cat_cols + num_but_cat

cat_cols



##### 5 )))
# Kategorik olmayan degiskenleri, yani cat_but_car dan gelenleri cikaralim
cat_cols = [col for col in cat_cols if col not in cat_but_car]

cat_cols


# sonuc1: tum kategorik degiskenler. dataframe inin columnlari
df[cat_cols].columns


# Her kategorik sutunda, kac alt sinif var?
df[cat_cols].nunique()


# sonuc2: tum sayisal (yani kategorik olmayan) degiskenler
[col for col in df.columns if col not in cat_cols]





##### Bir degiskende(sutunda), alt kategoriler (alt siniflar) % kac paya sahip, fonksiyon yazalim: *******************************************************************************************************

df["survived"].value_counts()  # survived alt siniflarindan kacar adet var?
len(df)
100 * df["survived"].value_counts() / len(df)  # % olarak nedir?



def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("################################################")


# sonuc:
cat_summary(df, "sex")


##### Her degiskende(sutunda), alt siniflar % kac paya sahip, fonksiyon yazalim:
# ustteki islemi, tum degiskenler(sutunlar) icin uygulatalim
# cat_cols da col larda gez, ustteki fonksiyonu her col a uygula
for col in cat_cols:
    cat_summary(df, col)



##### Bu fonksiyon icine, grafik ekletelim
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


# foksiyonu 1 degisken icin deneyelim
cat_summary(df, "sex", plot=True)

# foksiyonu tum degiskenler icin calistiralim.
# tip bilgisi bool ise hata verdiginden, bool ise ekrana printi yazdirir
for col in cat_cols:
    if df[col].dtypes == "bool":
        print("fcdfsdfwdfwfwf")
    else:
        cat_summary(df, col, plot=True)

# adult_male degiskeninde bool larda hata vermisti, bool gelirse donusturmesi icin sunu yazalim:
df["adult_male"].astype(int)

# 1den cok degisken bool larda hata verirse diye bir fonksiyon yazalim
# bool ise integer a donustursun
# cat_summary fonks: kendisine girilen degiskenleri ozetliyor.
for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot=True)








#############################################
### 3) Sayisal Degisken Analizi (Analysis of Numerical Variables)
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

# sayisal 1 veya 2 degiskeni inceleyelim
df["age"].describe().T
df[["age", "fare"]].describe().T



# Numerik degiskenleri bulan fonksiyon                 ******************************************************************************************************
# Kategorik degiskenleri yukarida bu sekilde bulmustuk:
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]
cat_cols


# numerik column lari getirelim:
num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
num_cols

# num cols ta olup, cat_cols ta olmayan degiskenleri secelim
num_cols = [col for col in num_cols if col not in cat_cols]
num_cols


# numerik degiskenleri sistematik bir sekilde secen bir fonksiyon yazalim
def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)



num_summary(df, "age")

# num_cols taki tum degiskenlere fonksiyonu uygulatalim
for col in num_cols:
    num_summary(df, col)


# plot cizdirelim
def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


# plot iceren fonksyonu deneyelim
num_summary(df, "age", plot=True)

# !! plot iceren fonksyonu, tum numerik column lar icin uygulatalim
for col in num_cols:
    num_summary(df, col, plot=True)







#############################################
### Degiskenlerin yakalanmasi ve Islemlerin gerceklestirilmesi
# (Capturing Variables and Generalizing Operations)
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()
df.info()


# Fonksiyon: kategorik degisken listesi, numerik degisken listesi, kategorik gorunen ama cardinal listesini versin   ********************************************************************
# bir degisken sayisal olsa da, alt kategori sayisi 10dan kucuk ise, kategoriktir muamelesi yapalim
# bir degisken kategorik olsa da, alt kategori sayisi 20den buyukse, cardinal degiskendir diyelim

# docstring: fonksiyona dokuman yazmak
def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Fonksiyon veri setindeki kategorik, numerik ve kategorik ama kardinal degiskenlerin isimlerini verir

    Parameters
    ----------
    dataframe: dataframe
        Degisken isimleri alinmak istenen dataframe dir.
    cat_th: int, float
        Numerik fakat kategorik olan degiskenler icin sinif esik degeri
    car_th
        Kategorik fakat kardinal degiskenler icin sinif esik degeri

    Returns
    -------
    cat_cols: list
        Kategorik degisken listesi
    num_cols: list
        Numerik degisken listesi
    cat_but_car: list
        Kategorik gorunumlu kardinal degisken listesi

    Notes
    -------
    cat_cols + num_cols + cat_but_car = toplam degisken sayisi
    num_but_cat cat_cols'un icerisinde.

    """
    # Kategorik degiskenleri yukarida bu sekilde bulmustuk:
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # numerik column lari getirelim:
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"Variables: {len(num_cols)}")
    print(f"Variables: {len(cat_but_car)}")
    print(f"Variables: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


# Fonksiyonun dokumantasyonunu cagiralim
help(grab_col_names)

grab_col_names(df)
cat_cols, num_cols, cat_but_car = grab_col_names(df)


# Kategorik degiskenler ozet
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("################################################")


for col in cat_cols:
    cat_summary(df, col)


# Numerik degiskenler ozet
def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    cat_summary(df, col, plot=True)



# BONUS: veri setini bastan okut
# bool lari bul ve integer a cevir, cat_cummary i daha pratikce kullan
df = sns.load_dataset("titanic")
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

df.info()

cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


for col in cat_cols:
    cat_summary(df, col, plot=True)

for col in num_cols:
    cat_summary(df, col, plot=True)









### 4) Hedef Degisken Analizi (Analysis of Target Variables)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)


def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Fonksiyon veri setindeki kategorik, numerik ve kategorik ama kardinal degiskenlerin isimlerini verir

    Parameters
    ----------
    dataframe: dataframe
        Degisken isimleri alinmak istenen dataframe dir.
    cat_th: int, float
        Numerik fakat kategorik olan degiskenler icin sinif esik degeri
    car_th
        Kategorik fakat kardinal degiskenler icin sinif esik degeri

    Returns
    -------
    cat_cols: list
        Kategorik degisken listesi
    num_cols: list
        Numerik degisken listesi
    cat_but_car: list
        Kategorik gorunumlu kardinal degisken listesi

    Notes
    -------
    cat_cols + num_cols + cat_but_car = toplam degisken sayisi
    num_but_cat cat_cols'un icerisinde.

    """
    # Kategorik degiskenleri yukarida bu sekilde bulmustuk:
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # numerik column lari getirelim:
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"Variables: {len(num_cols)}")
    print(f"Variables: {len(cat_but_car)}")
    print(f"Variables: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(df)

# veri setindeki, analiz etmemiz gereken "hedef degisken" : survived
df["survived"].value_counts()
cat_summary(df, "survived")

# survived olanlar, neden survived oldu, diger degiskenlerin etkisi neydi?

# Hedef degiskenin, kategorik degiskenler ile analizi
df.groupby("sex")["survived"].mean()  # kadinlarin %74u ve erkeklerin % 18i hayatta kalmis


# fonksiyon yazalim
def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET MEAN": dataframe.groupby(categorical_col)[target].mean()}))


target_summary_with_cat(df, "survived", "sex")
target_summary_with_cat(df, "survived", "pclass")

# for dongusu ile tum degiskenleri analize sokalim
for col in cat_cols:
    target_summary_with_cat(df, "survived", col)

# Hedef degiskenin, sayisal degiskenler ile analizi
df.groupby("sex")["age"].mean()  # hayatta kalan kadinlar ort 27 ve erkekler 30 yasinda
df.groupby("sex").agg({"age": "mean"})


def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")


target_summary_with_num(df, "survived", "age")

for col in num_cols:
    target_summary_with_num(df, "survived", col)







### 5) Korelasyon Analizi (Analysis of Correlation)

# 2 degisken arasndaaaki iliskiyi gosterir
# -1 ve 1 arasindadir

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

# csv dosyalarini okuma
df = pd.read_csv("/Users/gozdemadendere/Desktop/PycharmProjects/Python_Programming_Project/datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()

# Amacimiz, yuksek korelasyonlu degiskenlerden bazilarini disarda birakabilmek
# Sadece bir analiz araci olarak kullanmaliyiz.
# Genelde birbiriyle yuksek korelasyonlu degiskenleri beraber kullanmamayi tercih ederiz,
# Cunku zaten ayni seyi ifade ederler !!! Yani modelde yanlilik yaparlar !!!
# Peki hangisini elimine ederim, neye gore?
# Hedef degiskenle korelasyonu daha az olani delimine edebiliriz, veya NAN degeri daha cok olani elimine edebiliriz.


num_cols = [col for col in df.columns
            if df[col].dtype in [int, float]]

num_cols

corr = df[num_cols].corr()
corr

#### Isi haritasi olusturma
sns.set(rc={"figure.figsize": (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

#### Yuksek Korelasyonlu Degiskenlerin Silinmesi
# Korelasyonlari mutlak degerden gecirerek hepsini pozitif hale getiririz
cor_matrix = df.corr().abs()

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))

# korelasyonu 0.90dan buyuk olanlari sil
drop_list = [col for col in upper_triangle_matrix.columns
             if any(upper_triangle_matrix[col] > 0.90)]

cor_matrix[drop_list]
df.drop(drop_list, axis=1)


# fonksiyon tanimlayalim
def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={"figure.figsize": (12, 12)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list

high_correlated_cols(df)
drop_list = high_correlated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)



