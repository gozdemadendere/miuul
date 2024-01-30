
##################################################################################################
# PANDAS CHEATSHEET
##################################################################################################

# Import libraries
import pandas as pd
import seaborn as sns

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")





##################################################################################################
# UPDATE DATAFRAME'S PRINT
##################################################################################################

# pd.set_option("",) : Bu fonksiyonu kullanarak yapılabilecek bazı ayarlar:

# display.max_rows: DataFrame'in gösterilecek maksimum satır sayısını belirler.
pd.set_option("display.max_rows", 100)
df

# display.max_columns: DataFrame'in gösterilecek maksimum sütun sayısını belirler. (None ise tüm sütunlar gelir)
pd.set_option("display.max_columns", None)
df

# display.width: Çıktının yanyana gelmesi için genişlik ayarlar.
pd.set_option("display.width", 500)
df

# display.precision: Float türündeki sayıların gösterilecek ondalık basamak sayısını belirler.
pd.set_option("display.precision", 2)
df






##################################################################################################
# EXPLORE DATAFRAME : Retrieving Information
##################################################################################################

df.head()  # first x rows
df.tail()  # last x rows
df.info()  # Info on DataFrame
df.describe()  # statistical info on DataFrame
df.describe().T  # Transpozu

df.count()  # Number of non-NA values
df.isnull()  # Is there any Null values?
df.isnull().sum()  # How many are there Null values?
df.isnull().values.any()  # True: there is at least 1 Null value

df["age"].value_counts()  # Numbers of unique values for each category


# Parantezsiz yazilanlar:
df.columns  # Describe DataFrame columns
df.shape  # (891, 15) (rows,columns)
df.index  # (start=0, stop=891, step=1) Describe index

# dtype : data dtpe i görme
df["sex"].dtype           # O
str(df["sex"].dtype)      # Object








##################################################################################################
# UPDATE DATAFRAME ROWS / COLUMNS
##################################################################################################

##### astype()
# Pandas DataFrame veya Pandas Serilerinde, datatype i değiştirmek için kullanılır.

df["age"] = df["age"].astype(int)    # df["age"] = seklinde atama yapmayi unutma!
df["age"] = df["age"].astype(float)
df["age"] = df["age"].astype("category")



##### reset_index() : Eğer bir DataFrame'in indeksini sıfırlamak veya değiştirmek istiyorsanız

df.reset_index(inplace=True)




##### rename(columns={ }) : sutun ismini degistirme /  sutun ismini buyuk harfe cevirme
df = df.rename(columns={"sex": "SEX", "age": "AGE"})

# or
df.rename(columns={"sex": "SEX", "age": "AGE"}, inplace=True)




##### replace({ }) : sutundaki verileri degistirme
df["sex"] = df["sex"].replace({"female": "Woman", "male": "Man"})

# or
df["sex"].replace({"female": "Woman", "male": "Man"}, inplace=True)




##### .str.upper() : sutundaki verileri buyuk harfe cevirme
df["sex"] = df["sex"].str.upper()    # df["sex"] = seklinde atama yapmayi unutma!

##### .str.lower() : sutundaki verileri kucuk harfe cevirme
df["sex"] = df["sex"].str.lower()





##### fillna() : Eksik değerleri (NaN) belirli bir değer veya yöntemle doldurmak için kullanılır.

# Tüm NaN değerleri belirli bir değerle doldurma
df["deck"] = df["deck"].fillna(0)   # "deck" sütunundaki NaN değerleri 0 ile doldurur.
df_filled = df.fillna(0)            # DataFrame'deki tüm NaN değerleri 0 ile doldurur.



# NaN değerleri sütunların ortalaması ile doldurma
df["deck"] = df["deck"].fillna(df["deck"].mean())  # deck sütunundaki NaN değerleri, deck sütununun ortalaması ile doldurur.
df_filled = df.fillna(df.mean())                   # DataFrame'deki tüm NaN değerleri ""ilgili sütunların"" ortalamaları ile doldurur.



# NaN değerleri sütunların modu ile doldurma:

# [0] o sutundaki ilk (yani en sık tekrar eden) değeri seçer.
df["deck"] = df["deck"].fillna(df["deck"].mode()[0]) # "deck" sütunundaki NaN değerleri "deck" sütununun modu (en çok tekrar eden değer) ile doldurur.

# iloc[0] tum dataframe icin, her bir sutundaki ilk (yani en sık tekrar eden) değeri seçer.
df_filled = df.fillna(df.mode().iloc[0])  # DataFrame'deki tüm NaN değerleri ilgili sütunların modu ile doldurur.



# NaN değerleri sütunların medyanı ile doldurma
df["age"] = df["age"].fillna(df["age"].median())
df_filled = df.fillna(df.median())


# NaN değerleri bir önceki değerle doldurma (forward fill)
df_filled = df.fillna(method='ffill')





##### pd.cut(df[""]  , bins=[] )  : Veriyi kullanıcının belirlediği aralıklara böler. Bu aralıklar eşit büyüklükte olmayabilir ve her bir aralıkta farklı sayıda gözlem olabilir.
##### pd.qcut(df[""] , q=    ) : Veriyi belirli sayıda eşit büyüklükte parçalara böler. Bu parçaların her birinde yaklaşık olarak eşit sayıda gözlem bulunur.

# Örnek DataFrame oluşturma
import numpy as np
np.random.seed(0)
data = {
    'product': np.random.choice(['A', 'B', 'C'], size=20),
    'price': np.random.randint(10, 100, size=20)
}
df = pd.DataFrame(data)

# Yeni bir Segment sutunu olustur, Price i 4 esit parcaya bolerek 4 farkli Segment olustur
df["Segment"] = pd.qcut(df["price"], q=4)    # price a gore 4 farkli segment olusturdu, altta segmentleri bir isim yani label ile adlandiralim
df["Segment"] = pd.qcut(df["price"], q=4, labels=["D", "C", "B", "A"])    # D(en dusuk segment) le basladik cunku en bsataki en kucuk degerdir


# Yeni bir Age sutunu olustur, bu araliklarda:  "0_18", "19_23", "24_30", "31_40", "41_70"
df["AGE_CAT"] = pd.cut(df["AGE"], bins=[0, 18, 23, 30, 40, 70], labels=["0_18", "19_23", "24_30", "31_40", "41_70"])




# 'price' sütununu pd.cut() kullanarak kategorik olarak bölmek
df['price_cut'] = pd.cut(df['price'], bins=3, labels=['low', 'medium', 'high'])

# 'price' sütununu pd.qcut() kullanarak kategorik olarak bölmek
df['price_qcut'] = pd.qcut(df['price'], q=3, labels=['low', 'medium', 'high'])












##################################################################################################
# GROUP THE DATA
##################################################################################################

##### groupby()

# survived değişkeninin pclass ve cinsiyet değişkenlerine göre kırılımını yapip, sum, count, mean değerlerini bulunuz.
df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "mean", "count"]})
df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "mean", "count"]}).reset_index()  # bir DataFrame'in indeksini sıfırlamak veya değiştirmek istiyorsak



# time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df = sns.load_dataset("Tips")
df.head()

df.groupby("time").agg({"total_bill": ["sum", "mean", "min", "max"]})

