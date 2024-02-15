
######################################################
# Temel İstatistik Kavramları
######################################################

# Diyelim ki Kadıköy ilçesinin yaş dağılımına bakmak istiyoruz.

# Popülasyon:
# Kadıköy ilçesi sınırları içinde yaşayan tüm insanları kapsar.

# Örneklem (Sample):
# Kadıköy ilçesinin nüfusunu temsil etmek için seçilen ve dikkate alınan bir alt kümedir. (Popülasyonun bir alt kümesidir.)
# Araştırmacı, örnekleminde farklı yaş grupları, cinsiyet dağılımı, gelir düzeyleri ve meslek grupları gibi çeşitli demografik özellikleri temsil etmesine özen gösterir.

# Ortalama:
# Ortalama yaşa bakarsak, genel bir yaş ortalaması görebiliriz. Örneğin, Kadıköy ilçesindeki 1000 kişilik bir örneklemin yaş ortalaması 48 olsun, bu durumda Kadıköy ilçesindeki ortalama yaş 48 olacaktır.
# Örnek: Kadıköy ilçesindeki 1000 kişilik bir örneklemin yaş dağılımı şu şekildedir: 20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 55, 60, 65, 70, 75, 80, 85
# Bu durumda: Ortalama yaş: (20 + 22 + 25 + ... + 85) / 20 = 48.5

# Medyan:
# Kadıköy ilçesindeki bireylerin yaşlarının medyanı, yaşlara göre sıralandığında ortada bulunan değeri ifade eder.
# Eğer Kadıköy ilçesindeki 1000 kişilik örneklemin yaşlarını sıraladığınızda, ortada 500. sırada bulunan yaş 38 çıkıyorsa, bu durumda Kadıköy ilçesindeki medyan yaş 38 olacaktır.
# Örnek: Kadıköy ilçesindeki 1000 kişilik bir örneklemin yaş dağılımı şu şekildedir: 20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 55, 60, 65, 70, 75, 80, 85
# Bu durumda: Medyan yaş: 45 (Çünkü yaşlar sıralandığında ortada bulunan değer)

# Standart sapma:
# Dağılımın ortalamadan ne kadar uzaklaştığı. 'Ortalamadan sapmaların genel bir dağılımı' da diyebiliriz.
# Standart sapma, yaşların ortalama etrafında ne kadar yayıldığını gösterir. Yaş ortalaması 48 ise, standart sapma bize diğer yaşların bu ortalama etrafında nasıl dağıldığını gösterir.
# Yaşlar 48'in sağ tarafında mı daha çok yoksa 80'in sol tarafında mı? Örneğin, yaş ortalaması 48, standart sapma 5 ise, diğer yaşların 48'e uzaklıklarının ortalaması 5'tir.
# Standart sapma = √((20-48.5)² + (22-48.5)² + ... + (85-48.5)²) / 20

# Varyans:
# Standart sapmanın karesini alırsak varyans elde ederiz. Standart sapma, negatif ve pozitif yönde etkileri dengeleyerek ortalama etrafında yayılan verilerin ölçüsüdür.
# Varyans = 20² = 40. Daha düşük bir varyans, yaş dağılımının ortalama etrafında daha yoğun bir şekilde gruplandığını, daha yüksek bir varyans ise yaş dağılımının daha fazla dağıldığını ve ortalama etrafında daha fazla değişkenlik olduğunu gösterecektir.

# Güven Aralığı:
# Güven aralığı, bir parametrenin (örneğin, yaş ortalaması) tahmini değerinin gerçek değerinin bir aralık içinde olma olasılığını ifade eder.
# Örneğin, 95% güven aralığı, parametrenin gerçek değerinin, yapılan örnekleme dayanarak hesaplanan aralığın içinde olma olasılığını ifade eder.
# Yaş 95% güven aralığı ile 36-48 arasındadır gibi. 5% hata payı ile yanılma payımızı da eklemiş oluruz.

# Yani standart sapma nicelik bilgisi verirken, güven aralığı %sel bir ihtimalle bir alt ve üst sınır içinde bize aralık verir.
# Yani güven aralığı ile, bir örneklem çektiğimde, değer %95 olasılıkla bu alt ve üst sınır arasında gelecektir.
# Mean ve Median birbirine yakın ise, aykırı değerler yoktur diyebiliriz.
# Normal dağılım? : Medyanla ortalamanın yakın değerler olmasıdır, grafikte çan şekline benzer.
# Veri setinde aykırı değerler çoksa, medyanı baz almak daha doğru sonuç verebilir mean e göre.




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

# Popülasyon: Bir araştırma veya inceleme yapmak istediğiniz tüm bireylerin veya öğelerin tamamını temsil eder. (Ana Kitle)
# Örneklem:   Popülasyonun bir alt kümesidir. Popülasyonun temsil ettiği özellikleri veya nitelikleri yansıtır.

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




