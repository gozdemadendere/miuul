
########################
# NOTLAR:
########################
# Sorting Products'ta Bayesian faktörünü de eklersek, yeni-başarılı-ümit vaadeden ürünler de öne çıkabiliyor, bu nedenle bu faktörü de baz almak sonuçları daha faydalı hale getirir!
# Bayesian Average Rating Score, sadece kullanıcıların verdiği puanları (rating) dikkate alarak ürünleri sıralamak için kullanılan bir yöntemdir.
# Bu yöntem, ürünlerin puanlarını hesaplarken, her ürün için belirli bir alt-üst limit ve bir güven aralığı belirler.  Bu güven aralığı, o ürünün aldığı puanların ne kadar güvenilir olduğunu ifade eder.
# Bayesian sıralama ile mesela, IK cıyız, işe alacağımız kişilere ait 3 özellik seçip, min max scaler ile özellikleri standartlaştırıp, ardından bu 3 özelliğe göre Bayesian score hesaplayabiliriz.


# Sorting Reviews'da, 1. yöntemde yanlılık oluyor, bu nedenle sadece buna göre sıralamak faydalı değil. (1. Up-Down Difference Score = (up ratings) − (down ratings))
# Sorting Reviews'da, en güvenilir sonucu Wilson Lower Bound Score verir ama yine de 3 score türünü de hesaplayarak, şirkete en güvenilir olanın WLB olduğunu anlatıp, WLB üzerinden ilerleyebiliriz.
# Yorum sıralarken, faydalı olan yorumu en üstte vermeye çalışıyoruz, yüksek puanlı yorumu yada olumlu olumsuz yorumu değil !!
# WLB Score, e-ticaret sitelerindeki ürün yorumlarını sıralamak için yaygın olarak kullanılan istatistiksel bir yöntemdir.
# Bu yöntem, yorumların güvenilirliğini ve önemini hesaba katarak yorumları sıralar.
# Yorumlar var elimizde, puanları var, güven aralığı oluştururuz, bu güven aralığı içinde (alt sınır-üst sınır arasında) kalarak, hata payını da belirterek yanılma payına dayanak sağlayarak, skor belirleriz.


# Güven aralığı ile ortalama bir alt ve üst limit belirleyerek, ortalama bir aralık sağlamış oluyoruz. %5 hata ile diyoruz, böylece hata payını da ekliyoruz.


# A/B Testing'de Normallik Varsayımı, hem kontrol hem test grubu 2si için de sağlanmalı!!
# Sadece normallik varsayımı sağlanıyorsa, varyans homojenliği varsayımı sağlanmıyorsa,  düzeltilmiş bağımsız iki örneklem t testi uygularız ama argüman girerek bunu belirtiriz. (Welch'in t-testi, equal_var=True)


# A/B Testing'i en yaygın kullananlar App geliştiriciler veya Web'de bir sayfa tasarlayanlardır, bir sayfanın/tasarımın eski/yeni halini karşılaştırmak için kullanırlar.
# Ayrıca oyun sektöründe devamlı olarak kullanılır, yeni eklemeler devamlı olarak test edilir.
# Örneğin oyundaki karakterin kıyafet rengi, yılbaşı zamanı eklenen bir icon bir fark yaratıyor mu vb, bunlar bile A/B Testing ile test ediliyor.


# Max bidding : Kim max teklif vermişse o reklamı verebiliyor, ben 5 lira teklif ettim o 3 lira teklif etti, o zaman benim reklamım gösterilir. (açık artırma gibi)
# Avg bidding : Reklam platformunun önerdiği ortalama teklife uygun bir teklif sunma stratejisi diyebiliriz.







########################
# SORULAR & CEVAPLAR:
########################

## Rating Products'ta, Optimum sıralama konusunda zaman periyotları nasıl olmalı? (Time-Based Weighted Average için)
# Verinin dağılımına göre değişir, iş kararıdır, iş birimleri karar verir. Amaca uygun aralıklar belirlenir yani.
# Örneğin son 1 haftaya ait spesifik bir araştırma yapıyorsak, sadece son 1 haftayı baz alırız.


## Fenomen etkisi?
# Faydalı bile olabilir, arındırmak gerekmeyebilir, Trendyol bundan faydalanıyor mesela. Tamamen sektöre veya şirkete bağlı karar verilir.
# !! Bir anda trend olan bir ürünün ilk birkaç günlük verileri analizde baz alınmayabilir,  ilk birkaç gün sonrası verilerini almak daha faydalı olabilir.
# O birkaç günlük patlama veriyi yanıltabilir çünkü.


## Sıralama yapmak için, örneğin 5 çeşit zaman var, ağırlık verirken neye göre dağılım yapmalıyız?
# Güncel olan daha ağırlıklı olmalı. Bunun dışında yine iş kararına göre değişebilir.
# Sektörde güncel yorumların/puanlamaların etkisi ürünleri öne çıkarıyorsa güncel yorumlar/puanlamalar, ama eski yorumlar/puanlamalar öne çıkıyorsa onlar öne çıkarılabilir. İş amacına göre değişebilir yani.
# !! Örnek: Beyaz eşyada eski yorumlar/puanlamalar daha değerlidir! Çünkü örneğin bir buzdolabı modelinin, yıllar geçtikçe ne kadar iyi bir ürün olduğu ortaya çıkıyor. Burada eski yorumları/puanlamaları baz alabiliriz.
# Benzer ürünleri almış kullanıcıların yorumlarını öne çıkarmak da faydalı olabilir, işe-amaca göre değişir yine..


## A/B Testing neden yaparız?
# Çünkü 2 grup arasındaki ortalama farkı şans eseri mi çıktı, yoksa gerçekten performans farkı mı var, bunu test ederiz.


## A/B Testing yaptık ve sonuçları aldık. Eğer test etmeye devam edeceksek, test etmeyi nerede bırakmalıyız? Sonuçta o da bir maliyet.
# Örneğin gözlem sayısı 40 ise, bu sayıyı arttırabiliriz, yani farklı grupları da test edebiliriz.
# Her farklı grupta devamlı aynı sonuç çıkmaya devam ediyorsa, o noktada A/B Testing sonuçlarını artık kabul edebiliriz.
# Testte tek bir metriği incelediysek (purchase gibi) ek olarak farklı metrikleri de inceleyebiliriz. (click rate, earning gibi)


## Mülakat sorusu! Bağımsız 2 örneklem t testini yapacağımıza nasıl karar veririz?
# 2 koşulumuz var: normallik varsayımı ve varyans homojenliği varsayımı.
## Peki neden bu 2 koşulu istiyor bizden?
# Çünkü hem kontrol hem test grubunun, satın alma davranışlarının, benzer olmasını istiyoruz! Yani aynı ana kitleden gelmelerini istiyoruzki, kıyaslama yapabilelim.
## Peki normal dağılımı sağlamıyorsa, neden sağlamıyordur?
# Aykırı değerlerden dolayı. Bu nedenle teste başlamadan önce box plot yapıp, aykırı değerlere bakabiliriz, bunları temizleyebiliriz.


# Neden bazen ortalama değil medyanı kullanırız?
# Dağılım homojen değildir/ dağılım normal değildir/ aykırı değerler vardır diyebiliriz.


# H0 sadece red veya reddedilemez deriz! H1 ile ilgili kabul vb demeyiz. Neden?
# Çünkü H0'ı referans alırız, H0 reddedince, hata payımı bilirim 0.05 örneğin. H0 odaklı ilerleriz.


# Örneğin sağlık sektöründe, H0 red dedik, yani ilaç faydasız çıktı, naparız? (sağlık sektöründe p value daha küçük kabul edilir, 0.01 gibi)
# Örneklem doğru mu? örneklem genişletilebilir. Testler farklı gruplarda da denenir.



# ANOVA (Analysis of Variance):  2'den fazla grup ortalamasını karşılaştırmak için kullanılır.
# Anova kullanırız, çünkü 2li 2li karşılaştırma yaparsak, genel hata payı artar. O nedenle 2den fazla grup varsa Anova kullanırız.
# Ayrıca, tüm grupları aynı anda kıyaslıyoruz Anova ile. Tek bir test yapıyoruz.
# Yani Her testin kendine özgü hata olasılığı var (0,05 gibi.)
# Üç t testi olduğuna göre hata yapmama olasılığını üç kez kendisiyle çarpalım: 0,95 * 0,95 * 0,95 = 0,857
# 1 - 0,857 = 0,143. Yani Tür 1 hatası yapma olasılığı # 0,05’ten 0,143’e yükseldi. Bu, kabul edilemez.





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
