
###### WEEK 2 | RECAP NOTES ######


### Python'da eleman seçme komutu nedir?
# Python'da eleman seçme işlemi köşeli parantezler [] kullanılarak yapılır.
# Bu köşeli parantezlerin içine satır numarası veya sütun adı yazılabilir, ayrıca fancy index, slicing ve koşullu seçim de yapılabilir.



### Numpy açılımı nedir? Numerical python
### Pandas açılımı nedir? Panel Data Analysis



### Fancy index nedir?
# Fancy index ile, bir dizideki/arraydeki elemanlara toplu şekilde ulaşmak için bir listeyi veya diziyi kullanabiliriz.



### Neden Python List yerine Numpy? Veya Numpy neden değerlidir?
# 1) Numpy, Python listelerinden daha hızlıdır (tek tip veri tutar)
# 2) Yüksek seviyeden (vektörel seviyeden) işlem yapılmasını sağlar (daha temiz kod çıktısı, daha iyi performans)



### Pandas serisi tek boyutlu dizilerdir.
### Pandas Dataframe i  iki boyutlu bir veri yapısıdır. Tablo benzeridir, satırlar ve sütunlardan oluşur.



### Pandas'ta  & ve | kullanılır, and ve or kullanılmaz !



### NumPy bir kütüphanedir
### random bir modüldür (rastgele sayılar üretmek içindir, bir dizi fonksiyon üretir)
### random.randint(): random modülünün bir fonksiyonudur



### Kütüphane nedir: Belirli görevleri gerçekleştirmek için kullanılan hazır fonksiyonları içerir.
### Modül nedir:  Python'da kodun belirli bir amacı gerçekleştirmek için bir araya getirilmiş fonksiyon, sınıf ve değişkenlerin bulunduğu bir dosyadır.
### Attribute nedir: Bir nesnenin özelliklerine veya niteliklerine erişmek veya onları değiştirmek için kullanılan değerlerdir.
#   Bir sınıfın veya bir nesnenin attribute'larına nokta operatörü (.) kullanarak erişilebilir.



### NumPy array i ve Pandas Dataframe i arasındaki fark:
# 1- NumPy'da index yoktur (Pandas'ta attribute olarak index iç özelliktir, numpy'da ise biz kendimiz index tanımlarız)
# 2- Farklı veri tipleriyle çalışırlar. (NumPy dizileri tek boyutlu veya çok boyutlu olabilirken, Pandas DataFrame'leri iki boyutludur, yani satırlar ve sütunlar içerir.)
# 3- NumPy dizileri, matematiksel işlemleri hızlı bir şekilde gerçekleştirmek içindir, Pandas DataFrame'leri ise veri analizi ve manipülasyonu için daha yüksek düzeyli işlevsellik sağlar.



### df[“x”] ve df[[“x”]]  farklı, ilkinde seri seçerken 2.sinde dataframe seçiyoruz
# Sonuç olarak ikisinde sonuç data type i farklı olur (ilki pandas serisi 2.si dataframe i olarak gelir),
# Dikkat ! seriye ve dataframe e uygulanan methodlar farkli olabilmektedir


### apply  : Satir ya da sutunlarda otomatik olarak fonksiyon calistirma imkani saglar. (apply(lambda..) veya apply(def fonks adi...)  )
### lambda : Bir fonksiyon tanimlama seklidir. Kullan-at fonksiyondur.


###  Pie chart : Kategorik değişkenlerde sınıf sayısı fazla ise Pie chart anlamsız olur, bar plot daha mantıklıdır.
###  Boxplot   : Tek bir değişkene ait veri dağılımını ve aykırı değerleri gösterir.


###  Korelasyon: 2 sayisal değişken arasındaki ilişkinin gücünü ve yönünü ölçen bir terimdir.
###  İki değişken arasındaki ilişki ne kadar güçlüyse, korelasyon katsayısı o kadar yaklaşık ±1'e olur.

# Korelasyon katsayısı 0 ise iki değişken arasında bir ilişki yoktur.
# Korelasyon katsayısı -1'e yaklaşıyorsa, iki değişken arasında negatif bir ilişki olduğunu gösterir. Yani, bir değişken artarken diğeri azalır.
# Korelasyon katsayısı +1'e yaklaşıyorsa, iki değişken arasında pozitif bir ilişki olduğunu gösterir. Yani, bir değişken artarken diğeri de artar.

# Ancak, korelasyon katsayısı sadece iki değişken arasındaki ilişkinin doğrusal olup olmadığını ölçer. Diğer türden ilişkileri ölçmez.



## Önümüze bir veri seti geldiğinde izlemeniz gereken adımlar

# 1) Data Exploration (Genel Resim):
# Veri setinin başından ve sonundan birkaç satırı gözden geçirin, kaç sütun ve satır olduğunu kontrol etmek

# 2) Kategorik değişken analizi:
# Kategorik değişkenlerin benzersiz değerlerini ve sıklıklarını incelemek
# Bu, her bir kategorinin veri setinde ne kadar yaygın olduğunu anlamamıza yardımcı olur.

# 3) Sayısal değişken analizi:
# Sayısal değişkenlerin temel istatistiklerini (ortalama, standart sapma, minimum, maksimum, medyan, çeyreklikler) kontrol etmek
# Bu, sayısal değişkenlerin dağılımını anlamamıza ve potansiyel aykırı değerleri belirlemenmize yardımcı olur.

# 4) Hedef değişken analizi:
# Eğer bir hedef değişkeniniz varsa (örneğin, bir tahmin yapmak istediğiniz bir değişken), bu değişkenin dağılımını ve istatistiklerini incelemek
# Hedef değişkenin diğer özelliklerle ilişkisini anlamak için grafikler ve tablolar kullanabiliriz.

# 5) Korelasyon analizi:
# Sayısal değişkenler arasındaki ilişkiyi anlamak için korelasyon matrisini oluşturmak
# Korelasyon, değişkenler arasındaki doğrusal ilişkiyi ölçer ve değişkenlerin birbiriyle nasıl ilişkilendiğini anlamamıza yardımcı olabilir.

# Son olarak: Veri analizi sonuçlarını raporlamak