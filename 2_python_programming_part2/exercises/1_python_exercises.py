

##### Görev 1:
# Verilen değerlerin veri yapılarını inceleyiniz.
# type() metodunu kullanınız.

x = 8
type(x)        # int

y = 3.2
type(y)        # float

z = 8j + 18
type(z)        # complex

a = "Hello World"
type(a)        # str

b = True
type(b)        # bool

c = 23 < 22
type(c)        # bool !!

l = [1, 2, 3, 4]
type(l)        # list

d = {"Name" : "Jake",
     "Age" : 27,
     "Address" : "Downtown"}

type(d)        # dict

t = ("Machine Learning", "Data Science")
type(t)        # tuple

s = {"Python", "Machine Learning", "Data Science"}
type(s)        # set





##### Görev 2:
# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
# String metodlarını kullanınız.


### 1. YOL : String metodları ile
text = "The goal is to turn data into information, and information into insight."

new_text = text.upper().replace(",", "").replace(".", "").split()
new_text



### 2. YOL : for dongusu ile
text = "The goal is to turn data into information, and information into insight."

new_text = ""

for char in text:
    if char.isalpha():           # char = alfabeden bir harf ise ( isalpha() Python string metodu: Amacı, bir karakterin yalnızca alfabedeki harflerden oluşup oluşmadığını kontrol etmektir.)
        new_text += char.upper()
    elif char == " ":            # char = bosluk ise
        new_text += " "

# Kelime kelime ayirma
new_text = new_text.split()

new_text


### 3. YOL : list comprehension ile
text = "The goal is to turn data into information, and information into insight."

new_text = "".join([char.upper() if char.isalpha() else " " for char in text]).split()
print(new_text)



# VEYA

text = "The goal is to turn data into information, and information into insight."

new_text = "".join([" " if char in [",", "."] else char.upper() for char in text])

# Kelime kelime ayırma
new_text = new_text.split()

print(new_text)






##### Görev 3:
# Verilen listeye aşağıdaki adımları uygulayınız.

list = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]


# Adım1: Verilen listenin eleman sayısına bakınız.
len(list)  #11



# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
list[0]
list[10]



# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Yani 0, 1, 2, 3. indexteki elemanlari alacagiz.

list = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
new_list = []

# list icindeki elemanlardan, 0'dan 4. indexe kadar olan elemanlari al, new_list'e ekle
for char in list:
     if list.index(char) in range(0, 4):
          new_list.append(char)

new_list


list.index("T")



# Adım4: Sekizinci indeksteki elemanı siliniz.
list.pop(8)
list



# Adım5: Yeni bir eleman ekleyiniz.

# elemani listenin en sonuna ekleme
list.append("X")
list



# Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz

# elemani indexi belirterek ekleme
list.insert(8, "N")
list





##### Görev 4:
# Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {"Christian": ["America", 18],
     "Daisy": ["England", 12],
     "Antonio": ["Spain", 22],
     "Dante": ["Italy", 25]
}

dict

# Adım1: Key değerlerine erişiniz.
dict.keys()


# Adım2: Value'lara erişiniz.
dict.values()


# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"] = ["England", 13]
dict

# veya
dict.update({"Daisy": ["England", 13]})
dict



# Adım4: Key değeri Ahmet, value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({"Ahmet": ["Turkey", 24]})    # sozluk var icinde
dict


# Adım5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")
dict




##### Görev 5:
# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.


l = [2, 13, 18, 93, 22]


def function(list):
    even_list = []
    odd_list = []

    for number in list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

    return even_list, odd_list


function(l)





##### Görev 6:
# Aşağıda verilen listede mühendislik ve tıp fakültelerinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken, son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.


ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]
#               0     1        2       3         4        5

for index, ogrenci in enumerate(ogrenciler[0:3], 1):
    print("Muhendislik Fakultesi", index, ". ogrenci:", ogrenci)

for index, ogrenci in enumerate(ogrenciler[3:6], 1):
    print("Tip Fakultesi", index, ". ogrenci:", ogrenci)




# fonksiyon yazarak:
def function(ogrenciler):
     for index, ogrenci in enumerate(ogrenciler[:3], 1):
          print("Muhendislik Fakultesi", index, ". ogrenci:", ogrenci)

     for index, ogrenci in enumerate(ogrenciler[3:6], 1):
          print("Tip Fakultesi", index, ". ogrenci:", ogrenci)

function(ogrenciler)




##### Görev 7:
# Aşağıda 3 adet liste verilmiştir.
# Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır.
# Zip kullanarak ders bilgilerini bastırınız.


# 1. YOL
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

list(zip(ders_kodu, kredi, kontenjan))


# 2. YOL : for dongusu ile

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for kod, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Ders Kodu: {kod}, Kredi: {kredi}, Kontenjan: {kontenjan}")





##### Görev 8:
# Aşağıda 2 adet set verilmiştir.
# Eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını,
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamayiniz.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

kume1.issuperset(kume2)    # kume1 kume2 yi kapsiyor mu?

kume2.difference(kume1)    # kume2 de olup kume1  de olmayanlar

kume1.intersection(kume2)  # kume1 ve kume2 nin kesisimi