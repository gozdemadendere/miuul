
##################################################################################################
# PANDAS CHEATSHEET
##################################################################################################

# The Pandas library is built on NumPy and provides easy-to-use data structures and data analysis tools for Python.

# Import libraries
import pandas as pd
import seaborn as sns

# Upload a dataset
df = sns.load_dataset("titanic")

# Read from CSV
# df = pd.read_csv("file.csv")

# Write to CSV
# df.to_csv("myDataFrame.csv")



# 1) UPDATE DATAFRAME'S PRINT          : pd.set_option("display...", )
# 2) EXPLORE DATAFRAME                 : head(), info(), describe(), df.columns ...
# 3) UPDATE DATAFRAME ROWS / COLUMNS   : astype(), reset_index(), rename(columns={}), replace({}), fillna(), drop(), pd.cut(), pd.qcut()
# 4) DATE & TIME CHANGES               :
# 5) DATA SELECTION & FILTERING        : loc, iloc, isin([]), between(), str.startswith(), str.endswith(), str.contains()
# 6) GROUP THE DATA                    : groupby()
# 7) JOIN DATAFRAMES                   : pd.merge(), pd.concat([])
# 8) APPLYING FUNCTIONS                : apply, lambda






##################################################################################################
# 1) UPDATE DATAFRAME'S PRINT
##################################################################################################

# pd.set_option("",) : Bu fonksiyonu kullanarak yapılabilecek bazı ayarlar:

# display.max_columns: DataFrame'in gösterilecek maksimum sütun sayısını belirler. (None ise tüm sütunlar gelir)
pd.set_option("display.max_columns", None)
df

# display.width: Çıktının yanyana gelmesi için genişlik ayarlar.
pd.set_option("display.width", 500)
df

# display.precision: Float türündeki sayıların gösterilecek ondalık basamak sayısını belirler.
pd.set_option("display.precision", 2)
df

# display.max_rows: DataFrame'in gösterilecek maksimum satır sayısını belirler.
pd.set_option("display.max_rows", 100)
df






##################################################################################################
# 2) EXPLORE DATAFRAME : Retrieving Information
##################################################################################################

##### Data Exploration Function  !
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

explore_dataframe(df)


df.head()  # first x rows
df.tail()  # last x rows
df.info()  # Info on DataFrame
df.describe()  # statistical info on DataFrame
df.describe().T  # Transpozu

df.count()  # Number of non-NA values
df.isnull()  # Is there any Null values?
df.isnull().sum()  # How many are there Null values in each column?
df.isnull().sum().sum() # How many are there Null values in DATAFRAME?
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
# 3) UPDATE DATAFRAME ROWS / COLUMNS
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

# Note: mode u hem kategorik, hem sayisal degiskenler ile kullanabiliriz.
# Note: mean, median i sadece sayisal degiskenler ile kullanabiliriz.

# [0] o sutundaki ilk (yani en sık tekrar eden) değeri seçer.
df["deck"] = df["deck"].fillna(df["deck"].mode()[0]) # "deck" sütunundaki NaN değerleri "deck" sütununun modu (en çok tekrar eden değer) ile doldurur.

# iloc[0] tum dataframe icin, her bir sutundaki ilk (yani en sık tekrar eden) değeri seçer.
df_filled = df.fillna(df.mode().iloc[0])  # DataFrame'deki tüm NaN değerleri ilgili sütunların modu ile doldurur.



# NaN değerleri sütunların medyanı ile doldurma
df["age"] = df["age"].fillna(df["age"].median())
df_filled = df.fillna(df.median())


# NaN değerleri bir önceki değerle doldurma (forward fill)
df_filled = df.fillna(method='ffill')



##### drop()

df.drop("who", axis=1, inplace=True)                  # who degiskenini sutunlardan sil
df.drop(["who", "alive"], axis=1, inplace=True)       # who ve alive degiskenlerini sutunlardan sil
df.drop(['2', '3'], inplace=True)                     # 2 ve 3. indexleri satirlardan sil (axis=0)




##### pd.cut(df[""]  , bins=[] )  : Veriyi kullanıcının belirlediği aralıklara böler. Bu aralıklar eşit büyüklükte olmayabilir ve her bir aralıkta farklı sayıda gözlem olabilir.
##### pd.qcut(df[""] , q=    ) : Veriyi belirli sayıda eşit büyüklükte parçalara böler. Bu parçaların her birinde yaklaşık olarak eşit sayıda gözlem bulunur.
# (2si de sayisal bir degiskeni, kategorik degiskene cevirir)

# Yeni bir price_qcut sutunu: 'fare' sütununu pd.qcut() kullanarak kategorik olarak böl
df['price_qcut'] = pd.qcut(df['fare'], q=3, labels=['low', 'medium', 'high'])

# Yeni bir price_cut sutunu: 'fare' sütununu pd.cut() kullanarak kategorik olarak bölmek ( low: 0-150, medium: 151-300, high: 301-512 )
df['price_cut'] = pd.cut(df['fare'], bins=[0, 151, 301, 512], labels=['low', 'medium', 'high'])



# Yeni bir Segment sutunu olustur, Price i 4 esit parcaya bolerek 4 farkli Segment olustur
df["segment"] = pd.qcut(df["fare"], q=4)    # price a gore 4 farkli segment olusturdu, altta segmentleri bir isim yani label ile adlandiralim
df["segment"] = pd.qcut(df["fare"], q=4, labels=["D", "C", "B", "A"])    # D(en dusuk segment) le basladik cunku en bsataki en kucuk degerdir


# Yeni bir Age sutunu olustur, bu araliklarda:  "0_18", "19_23", "24_30", "31_40", "41_70"
df["age_cat"] = pd.cut(df["age"], bins=[0, 18, 23, 30, 40, 70], labels=["0_18", "19_23", "24_30", "31_40", "41_70"])








##################################################################################################
# 4) DATE & TIME CHANGES
##################################################################################################



##################################################################################################
# 5) DATA SELECTION & FILTERING
##################################################################################################

##### 1) .loc[] : This function used for label based selection.

## Basic Selections:

# satirlar: tümü  &  sütunlar: "age"
df.loc[: , "age"]          # age i direkt "age" olarak yazariz

# satirlar: tümü  &  sütunlar: "age", "embark_town"
df.loc[: , ["age", "embark_town"]]

# satirlar: tümü  &  sütunlar: "age" sutunundan "embark_town" sutununa kadar (bu 2si de dahil)
df.loc[: , "age":"embark_town"]

# satirlar: 1, 2, 3.  &  sütunlar: "age"
df.loc[[1, 2, 3] , "age"]

# satirlar: 1-3 arasi (3 dahil)  &  sütunlar: "age"
df.loc[1:3 , "age"]




## Conditional Selections:

# satirlar: "age" > 30 olanlar  &  sütunlar: hepsi
df.loc[df["age"] > 30, :]     # kosul belirtirken age i df["age"] olarak yazariz

# satirlar: "age" > 30 olanlar  &  sütunlar: "age"
df.loc[df["age"] > 30, "age"]

# satirlar: embark_town = "Southampton", "Cherbourg", "Queenstown"  &  sütunlar: hepsi
df.loc[df["embark_town"].isin(["Southampton", "Cherbourg", "Queenstown"]), :]

# satirlar: "age" > 30 ve embark_town = Southampton olanlar  &  sütunlar: hepsi
df.loc[(df["age"] > 30) & (df["embark_town"] == "Southampton"), :]      # 2 kosul var, kosullari () icinde beirtiriz


### 1'den fazla kosul varsa !!
# 1) Her kosul parantez icine alinmali ()
# 2) Kosul aralarinda & ya da | olmali
# 3) Kosul belirtirken df["age"] denmeli, sutun belirtirken "age" denmeli
# 4) Kosul belirtirken == kullanilmali, mesela: df["sex"] == "male"




##### 2) .iloc[] : This function used for integer based selection.

## Basic Selections:

# satirlar: tümü  &  sütunlar: 3.sütun yani  "age"
df.iloc[: , 3]

# satirlar: tümü  &  sütunlar: 3. ve 12. sütun yani "age", "embark_town"
df.iloc[: , [3, 12]]

# satirlar: tümü  &  sütunlar: 3. sutunundan 12. sutununa kadar (12. sütun dahil degil !!!!!)
df.iloc[: , 3:12]

# satirlar: 0'dan 3.satira kadar (3 dahil degil), sütunlar: 0'dan 3.sutuna kadar (3 dahil degil)
df.iloc[0:3, 0:3]



##### 3) .isin([]) : This function filters data based on a list.

# satirlar: embark_town = "Southampton", "Cherbourg", "Queenstown"  &  sütunlar: hepsi
df.loc[df["embark_town"].isin(["Southampton", "Cherbourg", "Queenstown"]), :]






##### 4) .between() : This function filters rows based on values that fall within a specified range.

# satirlar: "age" 20 40 arasindakiler (20 ve 40 dahil)  &  sütunlar: "age"
df.loc[df["age"].between(20, 40), :]





##### 5) str.startswith(), str.endswith(), str.contains()

# satirlar: class ta "Fir" icerenler  &  sütunlar: tümü
df.loc[df["class"].str.contains("Fir"), :]

# satirlar: class ta "Fir" ile baslayanlar  &  sütunlar: tümü
df.loc[df["class"].str.startswith("Fir"), :]

# satirlar: class ta "st" ile bitenler  &  sütunlar: tümü
df.loc[df["class"].str.endswith("st"), :]


## BONUS !! tek 1 degisken ismi: df["age"] , tüm sütun isimleri: df.columns
df.loc[:, df.columns.str.contains("age")].head()  # tum satirlari al, sutunlarda icinde age olanlari al








##################################################################################################
# 6) GROUP THE DATA
##################################################################################################

##### groupby()

# sex değişkeninin age ortalamasi ve fare toplami
df.groupby("sex").agg({"age": "mean", "fare": "sum"})      # agg({})  icinde dictionary var


# survived değişkeninin pclass ve cinsiyet değişkenlerine göre kırılımını yapip, sum, count, mean değerleri
df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "mean", "count"]})    # groupby() icinde 2 degisken varsa liste kullaniriz
df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "mean", "count"]}).reset_index()  # bir DataFrame'in indeksini sıfırlamak veya değiştirmek istiyorsak









##########################
# 7) JOIN DATAFRAMES
##########################
# DataFrame 1
df1 = pd.DataFrame({
    "employees": ["john", "dennis", "mark", "maria"],
    "group": ["accounting", "engineering", "engineering", "hr"],
    "salary": [60000, 75000, 80000, 55000],
    "experience": [5, 8, 6, 3]
})

# DataFrame 2
df2 = pd.DataFrame({
    "employees": ["mark", "john", "dennis", "maria"],
    "start_date": [2010, 2009, 2014, 2019],
    "vacation_days": [20, 25, 22, 18],
    "performance_score": [8, 7, 9, 6]
})

# DataFrame 3
df3 = pd.DataFrame({
    "group": ["engineering", "hr", "accounting"],
    "department_head": ["Alice", "Bob", "Charlie"],
    "office_location": ["New York", "Los Angeles", "Chicago"]
})




##### 1) pd.merge() : Bu fonksiyon, sütunlarda ortak anahtarlar kullanılarak DataFrame'leri birleştirmek için kullanılır.

## inner join : eşleşen sütun üzerinden her iki DataFrame'den satırları birleştirir
merged_df = pd.merge(df1, df2, on="employees")    # how="inner" default olarak tanimli


## left join : sol DataFrame'den (df1) tüm satırları ve sağ DataFrame'den (df2) eşleşen satırları döndürür. Eşleşme olmadığında, eksik değerleri NaN ile doldurur.
merged_df = pd.merge(df1, df2, how="left", on="employees")


## right join : sağ DataFrame'den (df2) tüm satırları ve sol DataFrame'den (df1) eşleşen satırları döndürür. Eşleşme olmadığında, eksik değerleri NaN ile doldurur.
merged_df = pd.merge(df1, df2, how="right", on="employees")


# 3 DataFrame i tek seferde birleştirme
merged_df = pd.merge(df1, df2, how="inner", on="employees").merge(df3, how="inner", on="group")  # gerekirse en sondaki: left_on="group", right_on="other_column"





##### 2) pd.concat([]) : Bu fonksiyon, DataFrame'leri alt alta birleştirmek için kullanılır

new_df = pd.concat([df1, df2])  # 2 dataframe oldugu icin,[] liste icinde tanimladik

# index leri de birlestirmek icin
new_df = pd.concat([df1, df2], ignore_index=True)










##################################################################################################
# 8) APPLYING FUNCTIONS
##################################################################################################

# apply  : Satir ya da sutunlarda otomatik olarak fonksiyon calistirma imkani saglar. (apply(lambda..) veya apply(def fonks adi...)  )
# lambda : Bir fonksiyon tanimlama seklidir. Kullan-at fonksiyondur.

function = lambda x: x * 2  # Create function
df.apply(function)          # Apply function
df.applymap(function)       # Apply function element-wise


# apply lambda ile, age_category isimli yeni bir sutun olusturalim.  !! Olusturulan kategori isimleri "" icinde belirtilmeli
df["age_category"] = df["age"].apply(lambda x: "0_18" if x <= 18 else ("19_35" if x <= 35 else "36_70"))

