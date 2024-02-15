###########################################################################################################
# A/B TESTING
###########################################################################################################

# Hipotez testi: Bir inanışı/bir savı test etmek için kullanılan bir istatistiksel analiz yöntemidir.
# A/B Testing:   2 grup arasında bir değişikliğin etkisini ölçmek veya 2 gruba ait ortalama / oran karşılaştırması için kullanılır.
# Grup karşılaştırmalarında temel amaç, olası farklılıkların şans eseri ortaya çıkıp çıkmadığını test etmektir.


# 1) A/B Testing (Bağımsız İki Örneklem T Testi) : 2 grup ortalaması arasında karşılaştırma yapmak için kullanılır.
# 2) A/B Testing (İki Örneklem Oran Testi)       : 2 grup oranları arasında karşılaştırma yapmak için kullanılır.
# 3) A/B Testing (Ki-Kare Testi)                 : 2 kategorik değişken arasındaki ilişkiyi belirlemek için kullanılır.
# 4) ANOVA (Analysis of Variance)                : 2'den fazla grup ortalamasını karşılaştırmak için kullanılır.


# A/B Testing Örnek:
# Veri Seti: Bir Web sitesinin eski ve yeni tasarımına ait veriler bulunmaktadır.
# Gruplar:   Eski tasarım (Kontrol Grubu) ve yeni tasarım (Deney Grubu) olmak üzere 2 farklı grup bulunmaktadır.

# Bağımsız İki Örneklem T Testi: 2 grubun eski ve yeni tasarım altında, geçirdikleri sürelerin ortalama değerlerinin karşılaştırılması
# Yani bu test, sayısal bir değişken olan "geçirilen süre"yi karşılaştırır.
# H0: 2 grubun eski ve yeni tasarım altında, geçirdikleri ortalama süre arasında istatistiksel olarak anlamlı bir fark yoktur. (Yani, ortalama süreler hemen hemen aynıdır.)

# Ki-Kare Testi: 2 grubun eski ve yeni tasarım altında, "satın al" düğmesine tıklama oranlarının birbirinden farklı olup olmadığı
# Yani bu test, kategorik bir değişken olan "satın al" düğmesine tıklama oranlarını karşılaştırır.
# H0:  İki grup arasında, eski ve yeni tasarım altında, "satın al" düğmesine tıklama oranları arasında istatistiksel olarak anlamlı bir fark yoktur. (Yani, tıklama oranları hemen hemen aynıdır.)




############################################################################################################
# 1) A/B Testing (Bağımsız İki Örneklem T Testi)
############################################################################################################

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
# Sadece normallik varsayımı sağlanıyorsa, varyans homojenliği varsayımı sağlanmıyorsa,  düzeltilmiş bağımsız iki örneklem t testi uygularız ama argüman girerek bunu belirtiriz. (Welch'in t-testi, equal_var=True)
# Argüman girişi şu şekilde: test_stat, pvalue = ttest_ind(df_control['Purchase'], df_test['Purchase'], equal_var=True)
# Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.





############################
# Uygulama 1) Sigara İçenler ve İçmeyenlerin Hesap Ortalamaları Arasında İstatistiksel Olarak Anlamlı bir Fark var mı?
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
# Uygulama 2) Titanic Kadın ve Erkek Yolcuların Yaş Ortalamaları Arasında İstatistiksel Olarak Anl. bir Fark. var mıdır?
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
# Uygulama 3) Diyabet Hastası Olan ve Olmayanların Yaş Ort. Arasında İst. Ol. Anl. Fark var mıdır?
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
# Uygulama 4) İş Problemi: Kursun Büyük Çoğunluğunu İzleyenler ile İzlemeyenlerin Puanları Birbirinden Farklı mı?
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







############################################################################################################
# 2) A/B Testing (İki Örneklem Oran Testi)
############################################################################################################

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





############################################################################################################
# 4) ANOVA (Analysis of Variance)
############################################################################################################

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