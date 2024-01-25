

##### Görev 1:
# List Comprehension yapısı kullanarak car_crashes verisindeki;
# numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM_ ekleyiniz.
# numeric olmayan değişkenlerin isimlerini büyük harfe çeviriniz. Tek bir list comprehension yapısı kullanılmalı.

# import dataframe
import seaborn as sns
df = sns.load_dataset("car_crashes")

# df degiskenleri
df.columns

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

df.info()




##### Görev 2:
# List Comprehension yapısı kullanarak car_crashes verisinde, isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.
# Tüm değişkenlerin isimleri büyük harf olmalı. Tek bir list comprehension yapısı ile yapılmalı.

df.columns

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]






##### Görev 3:
# List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz
# ve yeni bir dataframe oluşturunuz.

## 1.YOL : list comprehension ile
df.columns
og_list = ["abbrev", "no_previous"]

new_list = [col for col in df.columns if col not in og_list]

new_list

# dataframe e cevirelim
new_df = df[new_list]
new_df.head()





## 2.YOL: for dongusu ile:
df.columns
og_list = ["abbrev", "no_previous"]

new_list = []

for col in df.columns:
    if col not in og_list:
        new_list.append(col)

new_list


# dataframe e cevirelim
new_df = df[new_list]
new_df.head()
