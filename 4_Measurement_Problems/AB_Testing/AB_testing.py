#####################################################
# A/B Testing
#####################################################

# Hipotez testi: Bir inanışı/bir savı test etmek için kullanılan bir istatistiksel analiz yöntemidir.
# A/B Testing:   2 grup arasında karşılaştırma yapmak için kullanılır. (2 gruba ait ortalama / oran karşılaştırması)
# Grup karşılaştırmalarında temel amaç, olası farklılıkların şans eseri ortaya çıkıp çıkmadığını test etmektir.
# Örnek: mobil uygulamada yapılan bir arayüz değişikliıği sonrasında, kullanıcıların uygulamada geçirdikleri günlük ort. süre arttı mı?


# A/B Testing (Bağımsız İki Örneklem T Testi) : 2 grup ortalaması arasında karşılaştırma yapmak için kullanılır.
# A/B Testing (İki Örneklem Oran Testi)       : 2 grup oranları arasında karşılaştırma yapmak için kullanılır.
# ANOVA (Analysis of Variance)                : 2'den fazla grup ortalamasını karşılaştırmak için kullanılır.




######################################################
# Temel İstatistik Kavramları
######################################################

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option("display.width", 500)
pd.set_option("display.precision", 2)
# pd.set_option('display.float_format', lambda x: '%.5f' % x)



############################
# Sampling (Örneklem)
############################

# Popülasyon: Bir araştırma veya inceleme yapmak istediğiniz tüm bireylerin veya öğelerin tamamını temsil eder.
# Örneklem:   Popülasyonun bir alt kümesidir. Popülasyonun temsil ettiği özellikleri veya nitelikleri yansıtmak için seçilir.

populasyon = np.random.randint(0, 80, 10000)   # 0-80 arasında 10.000 adet sayı oluştur
populasyon.mean() # 39.58

np.random.seed(115)

orneklem = np.random.choice(a=populasyon, size=100)   # popülasyon içinden, 100 adet örneklem seç
orneklem.mean()  # 39.14

np.random.seed(10)
orneklem1 = np.random.choice(a=populasyon, size=100)
orneklem2 = np.random.choice(a=populasyon, size=100)
orneklem3 = np.random.choice(a=populasyon, size=100)
orneklem4 = np.random.choice(a=populasyon, size=100)
orneklem5 = np.random.choice(a=populasyon, size=100)
orneklem6 = np.random.choice(a=populasyon, size=100)
orneklem7 = np.random.choice(a=populasyon, size=100)
orneklem8 = np.random.choice(a=populasyon, size=100)
orneklem9 = np.random.choice(a=populasyon, size=100)
orneklem10 = np.random.choice(a=populasyon, size=100)

(orneklem1.mean() + orneklem2.mean() + orneklem3.mean() + orneklem4.mean() + orneklem5.mean()
 + orneklem6.mean() + orneklem7.mean() + orneklem8.mean() + orneklem9.mean() + orneklem10.mean()) / 10    # 40.23




############################
# Descriptive Statistics (Betimsel İstatistikler)
############################

# Mean (Ortalama), parametriktir. Median (Medyan), nonparametriktir.
# Mean ve Median birbirine yakın ise, aykırı değerler yoktur diyebiliriz.

df = sns.load_dataset("tips")
df.describe().T



############################
# Confidence Intervals (Güven Aralıkları)
############################

# Güven aralıkları, istatistiksel sonuçların güvenilirliğini değerlendirmek ve sonuçların anlamlılığını belirlemek için kullanılır.
# Örneğin, "95% güven aralığı (50, 70)" ifadesi, popülasyon parametresinin tahmini değerinin %95 olasılıkla 50 ile 70 arasında olduğunu belirtir.


# Tips Veri Setindeki Sayısal Değişkenler için Güven Aralığı Hesabı:
# total_bill sütununda bulunan örnek verilere dayalı olarak, popülasyonun ortalamasının güven aralığını hesaplar.
sms.DescrStatsW(df["total_bill"]).tconfint_mean()  # 18.66 ve 20.90 arasinda

# tip sütununda bulunan örnek verilere dayalı olarak, popülasyonun ortalamasının güven aralığını hesaplar.
sms.DescrStatsW(df["tip"]).tconfint_mean()   # 2.82 ve 3.17 arasinda


# Titanic Veri Setindeki Sayısal Değişkenler için Güven Aralığı Hesabı
df = sns.load_dataset("titanic")
df.describe().T

# age sütununda bulunan örnek verilere dayalı olarak popülasyonun ortalamasının güven aralığını hesaplar. (once age degiskeni icindeki eksik degerleri ucurduk)
sms.DescrStatsW(df["age"].dropna()).tconfint_mean()   # 28.63 ve 30.76 arasinda

sms.DescrStatsW(df["fare"].dropna()).tconfint_mean()



######################################################
# Correlation (Korelasyon)
######################################################

# 2 değişken arasındaki ilişkinin hem gücünü hem yönünü ifade etmektedir. (-1 ile 1 arasında yer alır)
# Pozitif korelasyon: bir değişkenin değeri artarken, diğer değişkenin değeri de artar.
# Negatif korelasyon: bir değişkenin değeri artarken, diğer değişkenin değeri azalır.


# Bahşiş veri seti:
# total_bill: yemeğin toplam fiyatı (bahşiş ve vergi dahil)
# tip: bahşiş
# sex: ücreti ödeyen kişinin cinsiyeti (0=male, 1=female)
# smoker: grupta sigara içen var mı? (0=No, 1=Yes)
# day: gün (3=Thur, 4=Fri, 5=Sat, 6=Sun)
# time: ne zaman? (0=Day, 1=Night)
# size: grupta kaç kişi var?

df = sns.load_dataset('tips')
df.head()

# Toplam hesaptan, tip i çıkaralım
df["total_bill"] = df["total_bill"] - df["tip"]

# Toplam hesap arttıkça, bahşiş te artıyor mu?
# Pozitif yönlü bir korelasyon var gibi duruyor.
df.plot.scatter("tip", "total_bill")
plt.show()

# Yorum: Toplam hesap ile bahsis arasinda, orta siddetli, pozitif yönlü bir korelasyon vardir.
df["tip"].corr(df["total_bill"])






######################################################
# A/B Testing (Bağımsız İki Örneklem T Testi)
######################################################

# A/B Testing Adımları:

# 1) Hipotezlerin Tanımlanması
# 2) Varsayım Kontrolü
#   - Normallik Varsayımı
#   - Varyans Homojenliği Varsayımı
# 3) Hipotezlerin Test Edilmesi
#   - Varsayımlar sağlanıyorsa  : Bağımsız iki örneklem t testi (parametrik test)
#   - Varsayımlar sağlanmıyorsa : Mann-Whitney U testi (non-parametrik test)
# 4) Sonuçların p-value değerine göre yorumlanması (p < 0.05 ise H0 red)


# Notlar:
# Normallik Varsayımı hem kontrol grubu, hem de test grubu için sağlanmalıdır.
# Normallik Varsayımı sağlanmıyorsa, direkt mannwhitneyu testini uygularız. Sadece Varyans Homojenliği sağlanmıyorsa, iki örneklem t testi uygulanır ama argüman girilir (equal_var=True).
# Argüman girişi şu şekilde: test_stat, pvalue = ttest_ind(df_control['Purchase'], df_test['Purchase'], equal_var=True)
# Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.




############################
# Uygulama 1: Sigara İçenler ve İçmeyenlerin Hesap Ortalamaları Arasında İstatistiksel Olarak Anlamlı bir Fark var mı?
############################

df = sns.load_dataset("tips")
df.head()

df.groupby("smoker").agg({"total_bill": "mean"})

#         total_bill
# smoker
# Yes       20.75634
# No        19.18828


############################
# 1) Hipotezlerin Tanımlanması
############################

# H0: M1 = M2   (Sigara İçenler ve İçmeyenlerin Hesap Ortalamaları Arasında, İstatistiksel Olarak Anlamlı bir Fark yoktur.)
# H1: M1 != M2  (Sigara İçenler ve İçmeyenlerin Hesap Ortalamaları Arasında, İstatistiksel Olarak Anlamlı bir Fark vardır.)



############################
# 2) Varsayım Kontrolü
#   - Normallik Varsayımı            (shapiro testi)
#   - Varyans Homojenliği Varsayımı  (levene testi)
############################

# Normallik Varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.

# shapiro testi, bir değişkenin dağılımının normal olup olmadığını test eder.
test_stat, pvalue = shapiro(df.loc[df["smoker"] == "Yes", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))   # p-value = 0.0002  < 0.05 HO RED   (H0: Normal dağılım varsayımı sağlanmaktadır.)

test_stat, pvalue = shapiro(df.loc[df["smoker"] == "No", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))   # p-value = 0.0000  < 0.05 HO RED   (H0: Normal dağılım varsayımı sağlanmaktadır.)


# Varyans Homojenliği Varsayımı
# H0: Varyanslar Homojendir.
# H1: Varyanslar Homojen Değildir.

# levene testi, varyans homojenliğini test etmek için kullanılır.
test_stat, pvalue = levene(df.loc[df["smoker"] == "Yes", "total_bill"], df.loc[df["smoker"] == "No", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))   # p-value = 0.0452  < 0.05 HO RED   (H0: Varyanslar Homojendir.)




############################
# 3) Hipotezlerin Test Edilmesi
#   - Varsayımlar sağlanıyorsa  : Bağımsız iki örneklem t testi (parametrik test)
#   - Varsayımlar sağlanmıyorsa : Mann-Whitney U testi (non-parametrik test)

# 4) Sonuçların p-value değerine göre yorumlanması (p < 0.05 ise H0 red)
############################

# Hem Normallik varsayımı hem de Varyans homojenliği varsayımı sağlanmadı : mannwhitneyu non-parametrik testini uygulayalım (ortalama, medyan kıyaslar)

########
# 2 Varsayım da sağlansaydı veya
# Normallik varsayımı sağlanıyorsa ama Varyans homojenliği varsayımı sağlanmıyorsa da, kullan ama equal_var=True gir.
test_stat, pvalue = ttest_ind(df.loc[df["smoker"] == "Yes", "total_bill"],
                              df.loc[df["smoker"] == "No", "total_bill"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
########


# Hem Normallik varsayımı hem de Varyans homojenliği varsayımı sağlanmadı : mannwhitneyu non-parametrik testini uygulayalım (ortalama, medyan kıyaslar)
test_stat, pvalue = mannwhitneyu(df.loc[df["smoker"] == "Yes", "total_bill"],
                                 df.loc[df["smoker"] == "No", "total_bill"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))   # p-value = 0.3413 p !< 0.05 H0 Reddedilemez.

# H0 Reddedilemez. :   H0: M1 = M2   (Sigara İçenler ve İçmeyenlerin Hesap Ortalamaları Arasında, İstatistiksel Olarak Anlamlı Fark yoktur.)






############################
# Uygulama 2: Titanic Kadın ve Erkek Yolcuların Yaş Ortalamaları Arasında İstatistiksel Olarak Anl. bir Fark. var mıdır?
############################

df = sns.load_dataset("titanic")
df.head()

df.groupby("sex").agg({"age": "mean"})
#             age
# sex
# female 27.91571
# male   30.72664



############################
# 1) Hipotezlerin Tanımlanması
############################

# H0: M1 = M2   (Titanic Kadın ve Erkek Yolcuların Yaş Ortalamaları Arasında, İstatistiksel Olarak Anlamlı bir Fark yoktur.)
# H1: M1 != M2  (Titanic Kadın ve Erkek Yolcuların Yaş Ortalamaları Arasında, İstatistiksel Olarak Anlamlı bir Fark vardır.)



############################
# 2) Varsayım Kontrolü
#   - Normallik Varsayımı            (shapiro testi)
#   - Varyans Homojenliği Varsayımı  (levene testi)
############################


# Normallik Varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.

# shapiro testi, bir değişkenin dağılımının normal olup olmadığını test eder.
test_stat, pvalue = shapiro(df.loc[df["sex"] == "female", "age"].dropna())    # dropna amaci, age bos olanlari ucurmak
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))     # p-value = 0.0071 < 0.05 yani H0 red   (H0: Normal dağılım varsayımı sağlanmaktadır.)

test_stat, pvalue = shapiro(df.loc[df["sex"] == "male", "age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))     # p-value = 0.0000 < 0.05 yani H0 red   (H0: Normal dağılım varsayımı sağlanmaktadır.)


####
# 1. Varsayım sağlansaydı:

# Varyans homojenliğine bakalım:
# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(df.loc[df["sex"] == "female", "age"].dropna(),
                           df.loc[df["sex"] == "male", "age"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
####



############################
# 3) Hipotezlerin Test Edilmesi
#   - Varsayımlar sağlanıyorsa  : Bağımsız iki örneklem t testi (parametrik test)
#   - Varsayımlar sağlanmıyorsa : Mann-Whitney U testi (non-parametrik test)

# 4) Sonuçların p-value değerine göre yorumlanması (p < 0.05 ise H0 red)
############################

# Normallik varsayımı sağlanmadı : mannwhitneyu non-parametrik testini uygulayalım (ortalama, medyan kıyaslar)
test_stat, pvalue = mannwhitneyu(df.loc[df["sex"] == "female", "age"].dropna(),
                                 df.loc[df["sex"] == "male", "age"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))     # p-value = 0.0261  < 0.05 H0 Red


# H0 Red  :   H0: M1 = M2   (Titanic Kadın ve Erkek Yolcuların Yaş Ortalamaları Arasında, İstatistiksel Olarak Anlamlı Fark yoktur.)












############################
# Uygulama 3: Diyabet Hastası Olan ve Olmayanların Yaş Ort. Arasında İst. Ol. Anl. Fark var mıdır?
############################

df = pd.read_csv("datasets/diabetes.csv")
df.head()

df.groupby("Outcome").agg({"Age": "mean"})
#              Age
# Outcome
# 0       31.19000
# 1       37.06716


############################
# 1) Hipotezlerin Tanımlanması
############################

# H0: M1 = M2   (Diyabet Hastası Olan ve Olmayanların Yaş Ortalamaları Arasında, İstatistiksel Olarak Anlamlı Fark yoktur.)
# H1: M1 != M2  (Diyabet Hastası Olan ve Olmayanların Yaş Ortalamaları Arasında, İstatistiksel Olarak Anlamlı Fark vardır.)



############################
# 2) Varsayım Kontrolü
#   - Normallik Varsayımı            (shapiro testi)
#   - Varyans Homojenliği Varsayımı  (levene testi)
############################

# Normallik Varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.

# shapiro testi, bir değişkenin dağılımının normal olup olmadığını test eder.
test_stat, pvalue = shapiro(df.loc[df["Outcome"] == 1, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))               # p-value = 0.0000  < 0.05 H0 Red   (H0: Normal dağılım varsayımı sağlanmaktadır.)

test_stat, pvalue = shapiro(df.loc[df["Outcome"] == 0, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))               # p-value = 0.0000  < 0.05 H0 Red   (H0: Normal dağılım varsayımı sağlanmaktadır.)



############################
# 3) Hipotezlerin Test Edilmesi
#   - Varsayımlar sağlanıyorsa  : Bağımsız iki örneklem t testi (parametrik test)
#   - Varsayımlar sağlanmıyorsa : Mann-Whitney U testi (non-parametrik test)

# 4) Sonuçların p-value değerine göre yorumlanması (p < 0.05 ise H0 red)
############################

# Normallik varsayımı sağlanmadı : mannwhitneyu non-parametrik testini uygulayalım (ortalama, medyan kıyaslar)
test_stat, pvalue = mannwhitneyu(df.loc[df["Outcome"] == 1, "Age"].dropna(),
                                 df.loc[df["Outcome"] == 0, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))   # p-value = 0.0000 < 0.05 H0 red


# H0 Red :  H0: M1 = M2   (Diyabet Hastası Olan ve Olmayanların Yaş Ortalamaları Arasında, İstatistiksel Olarak Anlamlı Fark yoktur.)







###################################################
# İş Problemi: Kursun Büyük Çoğunluğunu İzleyenler ile İzlemeyenlerin Puanları Birbirinden Farklı mı?
###################################################

df = pd.read_csv("datasets/course_reviews.csv")
df.head()

df[(df["Progress"] > 75)]["Rating"].mean()    # 4.86

df[(df["Progress"] < 25)]["Rating"].mean()    # 4.72


############################
# 1) Hipotezlerin Tanımlanması
############################

# H0: M1 = M2  (Kursun Büyük Çoğunluğunu İzleyenler ile İzlemeyenlerin Puanları ortalamaları arasında İstatistiksel Olarak Anlamlı Fark yoktur.)
# H1: M1 != M2 (Kursun Büyük Çoğunluğunu İzleyenler ile İzlemeyenlerin Puanları ortalamaları arasında İstatistiksel Olarak Anlamlı Fark vardır.)


############################
# 2) Varsayım Kontrolü
#   - Normallik Varsayımı            (shapiro testi)
#   - Varyans Homojenliği Varsayımı  (levene testi)
############################

# Normallik Varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.

# shapiro testi, bir değişkenin dağılımının normal olup olmadığını test eder.
test_stat, pvalue = shapiro(df[(df["Progress"] > 75)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))      # p-value = 0.0000 < 0.05 H0 Red


test_stat, pvalue = shapiro(df[(df["Progress"] < 25)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))      # p-value = 0.0000 < 0.05 H0 Red


############################
# 3) Hipotezlerin Test Edilmesi
#   - Varsayımlar sağlanıyorsa  : Bağımsız iki örneklem t testi (parametrik test)
#   - Varsayımlar sağlanmıyorsa : Mann-Whitney U testi (non-parametrik test)

# 4) Sonuçların p-value değerine göre yorumlanması (p < 0.05 ise H0 red)
############################

# Normallik varsayımı sağlanmadı : mannwhitneyu non-parametrik testini uygulayalım (ortalama, medyan kıyaslar)
test_stat, pvalue = mannwhitneyu(df[(df["Progress"] > 75)]["Rating"],
                                 df[(df["Progress"] < 25)]["Rating"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))      # p-value = 0.0000 < 0.05 H0 Red

# H0 Red   :   H0: M1 = M2  (Kursun Büyük Çoğunluğunu İzleyenler ile İzlemeyenlerin Puanları ortalamaları arasında İstatistiksel Olarak Anlamlı Fark yoktur.)







######################################################
# AB Testing (İki Örneklem Oran Testi)
######################################################

############################
# 1) Hipotezlerin Tanımlanması
############################

# H0: p1 = p2     (Yeni Tasarımın Dönüşüm Oranı ile Eski Tasarımın Dönüşüm Oranı Arasında İst. Ol. Anlamlı Farklılık Yoktur.)
# H1: p1 != p2    (Yeni Tasarımın Dönüşüm Oranı ile Eski Tasarımın Dönüşüm Oranı Arasında İst. Ol. Anlamlı Farklılık Vardır.)


basari_sayisi = np.array([300, 250])
gozlem_sayilari = np.array([1000, 1100])

proportions_ztest(count=basari_sayisi, nobs=gozlem_sayilari)

basari_sayisi / gozlem_sayilari



############################
# Uygulama: Kadın ve Erkeklerin Hayatta Kalma Oranları Arasında İst. Olarak An. Farklılık var mıdır?
############################

# H0: p1 = p2    Kadın ve Erkeklerin Hayatta Kalma Oranları Arasında İst. Olarak An. Fark yoktur.
# H1: p1 != p2   Kadın ve Erkeklerin Hayatta Kalma Oranları Arasında İst. Olarak An. Fark vardır.

df = sns.load_dataset("titanic")
df.head()

df.loc[df["sex"] == "female", "survived"].mean()

df.loc[df["sex"] == "male", "survived"].mean()

female_succ_count = df.loc[df["sex"] == "female", "survived"].sum()
male_succ_count = df.loc[df["sex"] == "male", "survived"].sum()

test_stat, pvalue = proportions_ztest(count=[female_succ_count, male_succ_count],
                                      nobs=[df.loc[df["sex"] == "female", "survived"].shape[0],
                                            df.loc[df["sex"] == "male", "survived"].shape[0]])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))





######################################################
# ANOVA (Analysis of Variance)
######################################################

# İkiden fazla grup ortalamasını karşılaştırmak için kullanılır.

df = sns.load_dataset("tips")
df.head()

df.groupby("day")["total_bill"].mean()

############################
# 1) Hipotezlerin Tanımlanması
############################


# HO: m1 = m2 = m3 = m4   (Grup ortalamaları arasında fark yoktur.)
# H1:                     (Grup ortalamaları arasında fark yoktur.)

############################
# 2. Varsayım Kontrolü
#   - Normallik Varsayımı
#   - Varyans Homojenliği Varsayımı
############################

# Normallik Varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.


# H0: Normal dağılım varsayımı sağlanmaktadır.

for group in list(df["day"].unique()):
    pvalue = shapiro(df.loc[df["day"] == group, "total_bill"])[1]
    print(group, 'p-value: %.4f' % pvalue)


# H0: Varyans homojenliği varsayımı sağlanmaktadır.

test_stat, pvalue = levene(df.loc[df["day"] == "Sun", "total_bill"],
                           df.loc[df["day"] == "Sat", "total_bill"],
                           df.loc[df["day"] == "Thur", "total_bill"],
                           df.loc[df["day"] == "Fri", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))



############################
# 3) Hipotezlerin Test Edilmesi
#   - Varsayımlar sağlanıyorsa  : Bağımsız iki örneklem t testi (parametrik test)
#   - Varsayımlar sağlanmıyorsa : Mann-Whitney U testi (non-parametrik test)

# 4) Sonuçların p-value değerine göre yorumlanması (p < 0.05 ise H0 red)
############################

# Hiç biri sağlamıyor.
df.groupby("day").agg({"total_bill": ["mean", "median"]})


# HO: Grup ortalamaları arasında ist ol anl fark yoktur

# parametrik anova testi: one way anova
f_oneway(df.loc[df["day"] == "Thur", "total_bill"],
         df.loc[df["day"] == "Fri", "total_bill"],
         df.loc[df["day"] == "Sat", "total_bill"],
         df.loc[df["day"] == "Sun", "total_bill"])

# Nonparametrik anova testi: kruskal
kruskal(df.loc[df["day"] == "Thur", "total_bill"],
        df.loc[df["day"] == "Fri", "total_bill"],
        df.loc[df["day"] == "Sat", "total_bill"],
        df.loc[df["day"] == "Sun", "total_bill"])

from statsmodels.stats.multicomp import MultiComparison
comparison = MultiComparison(df['total_bill'], df['day'])

# tukey: ANOVA testinde farkı oluşturan grup veya grupları incelemek için kullandığımız test
tukey = comparison.tukeyhsd(0.05)
print(tukey.summary())