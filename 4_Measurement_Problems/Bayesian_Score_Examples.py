############################################
# Uygulama: İşe alacağımız kişilere ait üç özellik seçelim ve bu özellikleri Bayesian Score hesaplayıp, kişileri bu score'a göre sıralayalım.
############################################

# Bu proje, deneyim, eğitim seviyesi ve referans sayısı gibi üç özelliğe sahip olan adaylar için bir DataFrame oluşturur.
# Bu özellikleri min-max scaler ile normalleştirir ve Bayesian Average Rating Score'u hesaplar.

# Özelliklerimizi şöyle seçebiliriz: deneyim, eğitim seviyesi ve referans sayısı gibi. # Education: 40%, References 20%, Experience 40%

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Örnek bir DataFrame oluşturma
data = {
    'Experience': [5, 3, 7, 4, 6],   # Deneyim yılları
    'Education': [4, 3, 5, 2, 4],    # Eğitim seviyesi (1-5 arası)
    'References': [3, 2, 4, 1, 3]    # Referans sayısı
}

df = pd.DataFrame(data)


# Education 1-5 aralığında olduğu için, Experience ve References i da 1-5 aralığına ölçeklendirmeliyiz:

# Experience sütunundaki değerleri, Min-Max ölçeklendirme yöntemiyle 1 ile 5 arasında bir aralığa ölçeklendirelim (standartlaştırma işlemi)
df["Experience_scaled"] = MinMaxScaler(feature_range=(1, 5)).fit(df[["Experience"]]).transform(df[["Experience"]])

# References sütunundaki değerleri, Min-Max ölçeklendirme yöntemiyle 1 ile 5 arasında bir aralığa ölçeklendirelim (standartlaştırma işlemi)
df["References_scaled"] = MinMaxScaler(feature_range=(1, 5)).fit(df[["References"]]).transform(df[["References"]])

# float oldukları için, inteğer yapalım
df["Experience_scaled"] = df["Experience_scaled"].astype(int)
df["References_scaled"] = df["References_scaled"].astype(int)

# Yeni bir dataframe oluşturup, standartlaştırılmış yeni değişkenleri ekleyelim (şimdi 3 değişken de 1-5 arasında)
df_scaled = df.loc[:, ["Education", "References_scaled", "Experience_scaled"]]
# df_scaled
#    Education  References_scaled  Experience_scaled
# 0          4                  3                  3
# 1          3                  2                  1
# 2          5                  5                  5
# 3          2                  1                  2
# 4          4                  3                  4


# Bayesian Average Rating Score hesaplama formülü
def bayesian_score(row):
    confidence = 0.95  # Güven aralığı
    n = len(row)  # Özellik sayısı

    # Özelliklerin ağırlıkları (bu kısım tercihe bağlı eklenebilir)
    weights = [0.4, 0.2, 0.4]  # Education: 40%, References 20%, Experience 40% ()

    # Bayesian Average Rating Score formülü
    bayesian_score = (confidence * n) / (n + confidence) * sum(row * weights) + \
                     (1 - confidence) / (n + confidence) * 0.5  # 0.5 = ortalama puan

    return bayesian_score


# Yukarıda oluşturduğumuz fonksiyon ile, Bayesian_Score sütunu oluşturalım
# ! Bu dataframede, sadece bayesian score unu oluşturmak için kullanacağımız sütunlar var. Bu nedenle, sütün isimlerini yazmadık, direkt df e uyguluyoruz formülü.
df_scaled['Bayesian_Score'] = df_scaled.apply(bayesian_score, axis=1)

#    Education  References_scaled  Experience_scaled  Bayesian_Score
# 0          4                  3                  3            2.46
# 1          3                  2                  1            1.45
# 2          5                  5                  5            3.61
# 3          2                  1                  2            1.31
# 4          4                  3                  4            2.75












