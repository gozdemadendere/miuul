##### Görev 1:
# Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

# Import libraries
import pandas as pd
import seaborn as sns

# Pandas ve Seaborn kütüphanelerinden bazı ayarları yapılandırma
pd.set_option("display.max_columns", None)  # Gösterilecek max sütun sayısını belirleme (None ise tüm sütunlar gelir)
pd.set_option("display.width", 500)         # Çıktının yanyana gelmesi için genişlik ayarı


# Titanic veri setini yükleme
df = sns.load_dataset("titanic")

# DataFrame'in ilk beş satırını gösterme
df.head()






##### Görev 2:
# Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df["sex"].value_counts()



##### Görev 3:
# Her bir sutuna ait unique değerlerin sayısını bulunuz.

df.nunique()

# or
df.nunique().sort_values(ascending=False)





##### Görev 4:
# pclass değişkeninin unique değerlerinin sayısını bulunuz.

df["pclass"].nunique()






##### Görev 5:
# pclass ve parch değişkeninin unique değerlerinin sayısını bulunuz.

df[["pclass", "parch"]].nunique()





##### Görev 6:
# embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

df["embarked"].dtype         # O
str(df['embarked'].dtype)    # Object

df["embarked"] = df["embarked"].astype("category")
print(df['embarked'].dtype)




##### Görev 7:
#  embarked değeri C olanların tüm bilgelerini gösteriniz.

df.loc[df["embarked"] == "C", :]





##### Görev 8:
# embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df.loc[df["embarked"] != "S", :]





##### Görev 9:
# Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df.loc[(df["age"] < 30) & (df["sex"] == "female") , :]





##### Görev 10:
# Fare'i 500'den büyük veya yaşı 70'den büyük yolcuların bilgilerini gösteriniz.

df.loc[(df["fare"] > 500) | (df["age"] > 70)]




##### Görev 11:
# Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().sum()

# or
df.isnull().sum().sort_values(ascending=False)


# tum dataframedeki boş değerlerin toplamını bulunuz.
df.isnull().sum().sum()






##### Görev 12:
# who değişkenini dataframe’den çıkarınız.

df.drop("who", axis=1, inplace=True)





##### Görev 13:
# deck değişkenindeki boş değerleri deck değişkeninin en çok tekrar eden değeri (mode) ile doldurunuz.

df["deck"] = df["deck"].fillna(df["deck"].mode()[0])   # [0] o sutundaki ilk (yani en sık tekrar eden) değeri seçer.

# or
df["deck"].fillna(df["deck"].mode()[0], inplace=True)  # inplace ile atama yapmadan kalici hale getirdik



##### Görev 14:
# age değikenindeki boş değerleri, age değişkeninin medyanı ile doldurunuz.

df["age"] = df["age"].fillna(df["age"].median())


# Her bir değişkendeki boş değerlerin toplamı:
df.isnull().sum().sort_values(ascending=False)




##### Görev 15:
# survived değişkeninin pclass ve cinsiyet değişkenlerine göre kırılımını yapip, sum, count, mean değerlerini bulunuz.

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "mean", "count"]})
df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "mean", "count"]}).reset_index()  # bir DataFrame'in indeksini sıfırlamak veya değiştirmek istiyorsak

# veya
df.groupby(['pclass', 'sex'])['survived'].agg(["sum", "mean", "count"])
df.groupby(['pclass', 'sex'])['survived'].agg(["sum", "mean", "count"]).reset_index()




##### Görev 16:
# 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz.
# apply ve lambda yapılarını kullanınız.


df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)


# or
def create_age_flag(age):
    return 1 if age < 30 else 0

df["age_flag"] = df["age"].apply(lambda x: create_age_flag(x))




##### Görev 17:
# Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

df = sns.load_dataset("Tips")
df.head()




##### Görev 18:
# time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby("time").agg({"total_bill": ["sum", "mean", "min", "max"]})





##### Görev 19:
# Günlere ve time a göre, total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["day", "time"]).agg({"total_bill": ["sum", "mean", "min", "max"]})



##### Görev 20:
# Lunch zamanına ve kadın müşterilere ait,  total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
df.head()

# Adim 1: Lunch zamanına ve kadın müşterilere ait dataframe i filtreleme:
df2 = df.loc[(df["sex"] == "Female") & (df["time"] == "Lunch"), :]

# Adim 2: Gruplama
df2.groupby("day").agg({"total_bill": ["sum", "mean", "min", "max"], "tip": ["sum", "mean", "min", "max"]})





##### Görev 21:
# size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df.head()

# Adim 1: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişleri filtreleme
df2 = df.loc[(df["size"] < 3) & (df["total_bill"] > 10), :]

# Adim 2: Ortalama bulma
df2.agg({"total_bill": "mean"})





##### Görev 22:
# total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği total bill ve tip in toplamını versin.
df.head()

# total_bill_tip_sum adında yeni bir sütun oluşturma
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

df.head()




##### Görev 23:
# total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

df_first_30 = df.sort_values(by="total_bill_tip_sum", ascending=False).head(30)


# 1den baslayacak bir index sutunu ekleyelim    (reset_index() kullansaydik, 0dan baslayan bir index sutunu olurdu)
df_first_30["index"] = range(1, len(df_first_30) + 1)
df_first_30