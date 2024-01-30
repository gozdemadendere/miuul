#############################################
# MÜŞTERİ SEGMENTASYON ANALİZİ (CUSTOMER SEGMENTATION PROCESS)
# KURAL TABANLI SINIFLANDIRMA İLE POTANSİYEL MÜŞTERİ GETİRİSİ HESAPLAMA ()
#############################################

# Müşteri segmentasyonu; benzer özelliklere, ihtiyaçlara ve davranışlara sahip müşterileri gruplara ayırma,
# ve bu gruplara özgü pazarlama stratejileri oluşturma sürecidir.

# Bu süreçte müşteriler, şirketin elinde bulunan verilere dayalı olarak segmentlere ayrılır.

# Projenin amacı, pazarlama stratejilerini desteklemek
# ve yeni müşterilerin hangi segmentte yer aldığını belirleyerek, bu müşterilerin ortalama getiri beklentisini hesaplamaktır.





#############################################
# İŞ PROBLEMI / PROJE HEDEFİ
#############################################
# Bir oyun şirketi, müşteri özelliklerine dayanarak, seviye tabanlı yeni müşteri tanımları (persona) oluşturmayı
# ve bu tanımları kullanarak müşterileri segmentlere ayırmayı amaçlıyor.

# Ardından, bu segmentlere dayanarak potansiyel yeni müşterilerin, şirkete ortalama gelir getirisini tahmin etmek istiyor.

# Örneğin: Türkiye’den IOS kullanan 25 yaşındaki bir erkek kullanıcının, ortalama getirisinin belirlenmesi hedefleniyor.





#############################################
# VERİ SETİ HİKAYESİ
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin ürünlerinin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı demografik bilgilerini içeriyor.
# Veri setinde her satış işlemi için bir kayıt bulunuyor, yani tablo tekilleştirilmemiştir.
# Bu, belirli demografik özelliklere sahip bir kullanıcının birden fazla alışveriş yapmış olabileceği anlamına geliyor.


# Price:    Müşterinin yaptığı harcama tutarı
# Source:   Müşterinin kullandığı cihaz türü
# Sex:      Müşterinin cinsiyeti
# Country:  Müşterinin ülkesi
# Age:      Müşterinin yaşı





#############################################
# PROJE AŞAMALARI
#############################################

# Veri setinin incelenmesi ve anlaşılması
# Veri manipülasyonu
# Müşteri tanımlarına göre segmentlerin oluşturulması (Segmentasyon işlemi)
# Her bir segment için ortalama gelir tahmininin yapılması
# Sonuçlara göre, yeni müşterilerin sınıflandırılması ve ne kadar gelir getirebileceğinin tahmin edilmesi


# 1) Dataframe i COUNTRY, SOURCE, SEX, AGE e gore gruplama ve karsisinda ortalama Price lari gorme
# 2) AGE_CAT isimli yeni bir age kategorisi sutunu olusturma
# 3) CUSTOMERS_LEVEL_BASED isimli yeni bir persona tanimlama sutunu olusturma (FRA_ANDROID_FEMALE_24_30 gibi)
# 4) Price ortalamalarina gore yeni bir SEGMENT sutunu olusturma (A,B,C,D segmentleri ile)
# 5)




################# Uygulama Öncesi DataFrame #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# Uygulama Sonrası DataFrame #####################

#       CUSTOMERS_LEVEL_BASED        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


