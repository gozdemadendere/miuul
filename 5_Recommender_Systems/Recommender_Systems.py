############################################
# RECOMMENDER SYSTEMS
############################################
# Tavsiye sistemlerini bir kelime ile ifade etsek: Filtreleme. Çok bol bir içerikten, kullanıcıya o kullanıcının ilgileneceği bir alt küme sunuyoruz.

# 1. Simple Recommender Systems: Kategorinin en yüksek puanlı ürünleri, trend olanlar, efsaneler vb.
# 2. Association Rule Learning:  Birliktelik analizi ile, sık olarak birlikte alınan ürünlere göre öneriler sunulur. (Sepet analizi)
# 3. Content Based Filtering:    Kullanıcının geçmiş tercihlerine benzer içeriklere sahip öneriler sunulur.
# 4. Collaborative Filtering:    Topluluğun kullanıcı veya ürün bazında ortak kanaatlerini yansıtan öneriler sunulur. User Based, Item Based, Model Based(Hybrid System)







############################################
# Association Rule Based Recommender
############################################
# Birliktelik analizi ile, sık olarak birlikte alınan ürünlere göre öneriler sunulur. (Sepet analizi)
# ARL yöntemi, kullanıcıların puan verme alışkanlıklarına dayanmaz ve sadece ürünler arasındaki ilişkileri baz alır.
# Kullanıcı bilgilerine ihtiyaç yok SepetID x Ürün dataframe'ine ihtiyaç var.

# Örnek: Bebek bezi ve biranın birlikte alınmasının analiz edilmesi. Ürün reyonlarının buna göre düzenlenmesi veya web satışında biranın sunulması.
# Örnek: Kırmızı topuklu ayakkabı satın alan müşterilerin genellikle siyah elbiseler veya metalik aksesuarlar da satın aldığını tespit edebiliriz ve bu ürünleri önerilebiliriz.

# Apriori Algoritması: Sepet analizi yöntemidir. Ürün birlikteliklerini ortaya çıkarır.


### Recap
# Apriori Algoritması: Sepet analizi yöntemidir. Ürün birlikteliklerini ortaya çıkarır.

# Örneğin, X ürünü alındığında, 3 ürünün de satın alınma olasılığını arttırıyorsa,  X ürününün fiyatını azaltabiliriz, X ürününü raflarda ve  web sitesinde öne çıkarabiliriz.

# Armut case'inde olduğu gibi, şirket hizmet satıyorsa sepet yok, fatura yok >> müşterilerin hizmet satın alım tarihlerine göre, time based bir sepet tanımı/sepet ID oluştururuz.


### Mülakat Soruları
# E-ticaret sitesiyiz, login yapmış kullanıcılarımız da var. Sadece giriş bilgileri, geçmiş sepet bilgileri var. Hangi recommender yöntemini neden kullanmalıyız?
# Association Rule Based Recommender tercih etmeliyiz, çünkü sepet senaryosu var:
# Kullanıcıların geçmiş alışveriş sepetlerini analiz ederek, ürünler arasındaki ilişkileri belirleyebiliriz. Sık olarak birlikte alınan ürünlere göre öneriler sunabiliriz.
# Elimizde kullanıcıların ürünlere verdikleri puan bilgileri yok. ARL yöntemi de kullanıcıların puan verme alışkanlıklarına dayanmaz ve sadece ürünler arasındaki ilişkileri baz alır.

# !! Örneğin, çok kategorili bir e-ticaret şirketindeysek, 10.000 tane ürün var, Apriori uygulayacağız, neye göre seçeceğiz, hangi ürüne odaklanacağız?
# Alt küme seçeriz: Gelirin %80'ini oluşturan ürünlerin %20'sini alırız, o ürünlere odaklanırız. (Pareto Analizi olarak da bilinen 80/20 kuralı)





############################################
### Content-Based Recommender
############################################
# Kullanıcının geçmiş tercihlerine bakarak, ürün içerikleri üzerinden tavsiyeler sunar.
# Ürünlerin sahip olduğu özelliklere ve içeriğe odaklanır. Örneğin, bu özellikler film açıklaması, film türü, oyuncular, yönetmenler, kitap açıklaması, kitap yazarı, konu vb. olabilir.
# Düşük veri gereksinimine sahiptir ve kullanıcı tercihlerini anlama konusunda iyidir; sadece ürün özelliklerine dayalıdır.

# Örnek: Trendyol'da Smeg kahve makinesi satın alan bir kullanıcıya, benzer tarzda kahve makineleri veya aynı markanın diğer ürünleri gibi benzer içeriklere sahip ürünler önerilebilir.



### Recap
# Metin vektörleştirme (TF-IDF):  Kelimelerin sıklığını ve belirli bir belgede geçme sayısını tespit eder.  ( NLP konusudur)
# Metnin karakteristiğini belirlemek için, nadir kelimeler daha önemlidir.
# TFIDF ile nadir kelimeleri öne çıkarırız ve stop words parametresi ile sık kullanılan kelimeleri eleriz.

# Elimizde 100 tane film var, filmler indexlerde yer alır, içerisindeki unique kelimeler çıkarılır, sütunlara konulur, hangi filmde kaç kere geçtiği yazılır, ve benzerlikleri hesaplanır.
# Böylece film-kelime matrisi ile, filmler arasındaki benzerlikler hesaplanır.


### Mülakat Soruları
# Web sitesinde login yapmış bir kullanıcı yok. Sadece kullanıcının izlediği filmi, cookie ID'sinden görüyoruz. Ürün tavsiyesinde bulunmak istiyoruz. Hangi recommender yöntemini kullanmalıyız?
# Content based recommender, çünkü sadece ürün özelliklerine dayanır. Kullanıcının geçmiş tercihlerine bakarak, ürün içerikleri üzerinden tavsiyeler sunar.







# Collaborative filtering: Topluluğun kullanıcı veya ürün bazında ortak kanaatlerini yansıtan öneriler sunulur.(User based, Item based, Hybrid Model. Korelasyon kullanılır!)

############################################
# Item-Based Recommendation
############################################
# Bir ürünün özelliklerine dayanarak, benzer ürünler önerir.  Kullanıcıların geçmiş tercihlerine bakmak yerine, bir ürünün diğer ürünlerle olan benzerliklerine odaklanır.
# Özetle, content-based recommendation kullanıcıların önceki tercihlerine dayanırken, item-based recommendation ise ürünlerin özelliklerine dayanır.
# Kullanıcı bilgilerine ihtiyaç var: UserID x Ürün dataframe'ine ihtiyaç var.
# Örnek: Trendyol'da "Benzer Ürünler" sunulması: Smeg kahve makinesine bakan bir kullanıcıya, farklı kahve makineleri veya Smeg marka diğer ürünler önerilebilir.


### Mülakat Soruları
# Web sitesinde login yapmış bir kullanıcı yok. Sadece kullanıcının izlediği filmi, cookie ID'sinden görüyoruz. Ürün tavsiyesinde bulunmak istiyoruz. Hangi recommender yöntemini kullanmalıyız?
# Content based recommender, çünkü sadece ürün özelliklerine dayanır. Kullanıcının geçmiş tercihlerine bakarak, ürün içerikleri üzerinden tavsiyeler sunar.

# E-ticaret sitesiyiz, login yapmış kullanıcılarımız da var. Ürünlere verdikleri puanlar da var. Hangi yöntemi neden kullanmalıyız?
# User based / Item based recommender. Çünkü puan bilgileri de var.




############################################
# User-Based Recommendation
############################################
# Benzer kullanıcıların tercihlerine dayanarak bir kullanıcıya öğeler önerir.
# Kullanıcı bilgilerine ihtiyaç var: UserID x Ürün dataframe'ine ihtiyaç var.
# Örnek: Trendyol'da kırmızı topuklu ayakkabı satın alan bir kullanıcıya, benzer alışveriş geçmişine sahip diğer kullanıcıların kırmızı topuklu ayakkabı aldıktan sonra tercih ettiği ürünler önerilebilir.
# Örnek: Trendyol'da "Bu Ürünü Alanlar Bunları da Aldı" başlığı altında ürünler sunulması: Smeg kahve makinesine bakan bir kullanıcıya, bu makineyi alanların aldığı diğer ürünler önerilebilir.





############################################
### Model-Based Collaborative Filtering: Matrix Factorization
############################################
# Matrix Factorization, kullanıcıların ve ürünlerin özelliklerini temsil eden bir matrisi oluşturur ve bu matrisi kullanarak kullanıcıların ürünlere olan ilgisini tahmin eder.
# Bu matrisi, eksik değerleri doldurarak ve kullanıcıların ve ürünlerin gizli özelliklerini (latent features) belirleyerek oluşturabiliriz.
# Bu yöntem, kırmızı topuklu ayakkabı satın alan müşterinin benzer ilgi alanlarına sahip diğer müşterilerin tercihlerinden yararlanarak öneriler sunabilir.







