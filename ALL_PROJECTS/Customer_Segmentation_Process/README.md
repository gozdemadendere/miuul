#### MÜŞTERİ SEGMENTASYON ANALİZİ (CUSTOMER SEGMENTATION PROCESS)
##### KURAL TABANLI SINIFLANDIRMA İLE POTANSİYEL MÜŞTERİ GETİRİSİ HESAPLAMA 

- Müşteri segmentasyonu; benzer özelliklere, ihtiyaçlara ve davranışlara sahip müşterileri gruplara ayırma, ve bu gruplara özgü pazarlama stratejileri oluşturma sürecidir.

- Bu süreçte müşteriler, şirketin elinde bulunan verilere dayalı olarak segmentlere ayrılır.

- Projenin amacı, pazarlama stratejilerini desteklemek ve yeni müşterilerin hangi segmentte yer aldığını belirleyerek, bu müşterilerin ortalama getiri beklentisini hesaplamaktır.

______________________________

#### 1. İŞ PROBLEMI / PROJE HEDEFİ

Bir oyun şirketi, müşteri özelliklerine dayanarak, seviye tabanlı yeni müşteri tanımları (persona) oluşturmayı ve bu tanımları kullanarak müşterileri segmentlere ayırmayı amaçlıyor.

Ardından, bu segmentlere dayanarak potansiyel yeni müşterilerin, şirkete ortalama gelir getirisini tahmin etmek istiyor.

Örneğin: Türkiye’den IOS kullanan 25 yaşındaki bir erkek kullanıcının, ortalama getirisinin belirlenmesi hedefleniyor.


______________________________

#### 2. VERİ SETİ HİKAYESİ
Persona.csv veri seti uluslararası bir oyun şirketinin ürünlerinin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı demografik bilgilerini içeriyor.
Veri setinde her satış işlemi için bir kayıt bulunuyor, yani tablo tekilleştirilmemiştir.
Bu, belirli demografik özelliklere sahip bir kullanıcının birden fazla alışveriş yapmış olabileceği anlamına geliyor.


- Price:    Müşterinin yaptığı harcama tutarı
- Source:   Müşterinin kullandığı cihaz türü
- Sex:      Müşterinin cinsiyeti
- Country:  Müşterinin ülkesi
- Age:      Müşterinin yaşı



______________________________

#### 3. PROJE AŞAMALARI


- Veri setinin incelenmesi ve anlaşılması
- Veri manipülasyonu
- Müşteri tanımlarına göre segmentlerin oluşturulması (Segmentasyon işlemi)
- Her bir segment için ortalama gelir tahmininin yapılması
- Sonuçlara göre, yeni müşterilerin sınıflandırılması ve ne kadar gelir getirebileceğinin tahmin edilmesi


1) Dataframe i COUNTRY, SOURCE, SEX, AGE e gore gruplama ve karsisinda ortalama Price lari gorme
2) AGE_CAT isimli yeni bir age kategorisi sutunu olusturma
3) CUSTOMERS_LEVEL_BASED isimli yeni bir persona tanimlama sutunu olusturma (FRA_ANDROID_FEMALE_24_30 gibi)
4) Price ortalamalarina gore yeni bir SEGMENT sutunu olusturma (A,B,C,D segmentleri ile)

______________________________

#### 4. PROJE SONUÇLARI

#### Uygulama Öncesi DataFrame:
<img width="412" alt="Screen Shot 2024-01-30 at 2 53 37 PM" src="https://github.com/gozdemadendere/miuul_data_science_bootcamp/assets/90986708/328f1002-8a69-4134-b45c-da60bb2fa84d">


#### Uygulama Sonrası DataFrame:
AGE_CAT isimli yeni bir yaş kategorisi sütunu, CUSTOMERS_LEVEL_BASED isimli yeni bir müşteri persona tanımı sütunu, SEGMENT isimli yeni bir müşteri segmenti sütunu oluşturuldu. 

<img width="771" alt="Screen Shot 2024-01-30 at 2 58 10 PM" src="https://github.com/gozdemadendere/miuul_data_science_bootcamp/assets/90986708/2fcc0545-f0d5-4eb2-856d-6b1ad7f03b59">

#### Müşteri Grubu Bazında Ort. Fiyat & Segment Analizi
Her CUSTOMERS_LEVEL_BASED müşteri persona grubu için, ortalama alışveriş fiyatı ve fiyat segmenti görülmektedir.

<img width="441" alt="Screen Shot 2024-01-30 at 3 02 25 PM" src="https://github.com/gozdemadendere/miuul_data_science_bootcamp/assets/90986708/a25a862f-54c7-402a-84b1-1a4339403aa2">

#### Müşteri Segmenti Bazında Fiyat Analizi
Her SEGMENT için, alışveriş fiyat ortalaması, fiyat toplamı, min ve max fiyatlar görülmektedir.

<img width="433" alt="Screen Shot 2024-01-30 at 3 02 55 PM" src="https://github.com/gozdemadendere/miuul_data_science_bootcamp/assets/90986708/6ae280d3-c04e-4fce-b162-f28992f2b9f5">


