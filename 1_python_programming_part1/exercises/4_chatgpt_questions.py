
##### Zip Function: Merging "LISTS" into Tuples

# Aşağıda 3 adet liste verilmiştir. Zip kullanarak tek bir listede ders bilgilerini bastırınız.
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

### METHOD 1: Zip Fonksiyonunu Doğrudan Kullanma

list(zip(ders_kodu, kredi, kontenjan))       # 3 ayri listeyi, tek bir liste icinde, tuple lar olarak birlestirdi (4 adet tuple)


### METHOD 2: Zip Fonksiyonunu For Döngüsü İle Kullanma

for kod, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Ders Kodu: {kod}, Kredi: {kredi}, Kontenjan: {kontenjan}")



## NOTE !!
# Tek bir listeyle çalışırken:  for number in list
list1 = [5, 3, 8, 2]
[number for number in list1]


# 2 listeyle çalışırken:  for number1, number2 in zip(list1, list2)
list1 = [5, 3, 8, 2]
list2 = [1, 7, 4, 6]
[number1 * number2 for number1, number2 in zip(list1, list2)]      # 2 ayri listeden, karssilikli her bir rakamin carpimlari gelir





##########        SORU 1 | Dictionary icindeki Listelerden Yeni Bir Dictionary Oluşturma         ##########

# cities sözlüğündeki değerleri kullanarak nüfus yoğunluğunu hesaplayın ve yeni bir sözlük oluşturun.
# Nüfus yoğunluğu, nüfusu yüzölçümüne bölerek elde edilir.
# Sonuç olarak, şehir isimleri ve nüfus yoğunlukları içeren dictionary beklenmektedir. (ornek: {Istanbul : 1234, Ankara: 567 ...} )

cities = {
    'city_name': ['Ankara', 'Istanbul', 'Izmir', 'Bursa'],
    'population_info': [5445026, 15519267, 4279677, 2936803],
    'area_info': [2510, 5461, 2024, 1755]
}


# zip ile: dictionary icindeki 3 ayri listeyi alip, tek bir liste icinde birlestirdik >> cities["city_name"] diyerek sozluk icindeki listeyi cagirdik
population_density = {city: population / area for city, population, area in zip(cities["city_name"], cities["population_info"], cities["area_info"])}
print(population_density)







##########        SORU 2 | İki Liste Elemanlarını Toplama         ##########

# İki liste arasındaki karşılıklı elemanları toplayan bir Python kodu yazın.
list1 = [5, 3, 8, 2]
list2 = [1, 7, 4, 6]

result = [number1 + number2 for number1, number2 in zip(list1, list2)]
print(result)


## NOTE !!
# tek bir liste oldugunda, for number in list diyorduk
list1 = [5, 3, 8, 2]
[number for number in list1]    #cikti: [5, 3, 8, 2]


# 2  liste oldugunda, for number1, number2 in zip(list1, list2) diyoruz
list1 = [5, 3, 8, 2]
list2 = [1, 7, 4, 6]
[number1 + number2 for number1, number2 in zip(list1, list2)]    #cikti: [6, 10, 12, 8]





##########        SORU 3 | Ortalama Hesaplama        ##########

# Verilen bir listenin elemanlarının ortalamasını hesaplayan bir Python fonksiyonu yazın.
def calculate_average(lst):
    return sum(lst) / len(lst)

# Örnek kullanım:
sample_list = [10, 20, 30, 40, 50]
print(calculate_average(sample_list))





##########        SORU 4 | Çift Sayıları Filtreleme        ##########

# Verilen bir listede bulunan çift sayıları filtreleyen bir Python kodu yazın.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in my_list if number % 2 == 0]
print(even_numbers)

# Bunu fonksiyon olarak yazın.

def function(list):
    even_numbers = [number for number in list if number % 2 == 0]
    return even_numbers

function(my_list)




##########        SORU 5 | Bir Liste içinde Tekrar Eden Elemanları Bulma       ##########

# Bir listede tekrar eden elemanları bulup, yeni bir listeye ekleyen bir Python kodu yazın.

my_list = [1, 2, 3, 4, 2, 5, 6, 6, 1, 7, 8, 8, 9]

# practise: belirli bir elemanin o listede kac kere tekrar ettigini bulma
my_list.count(8)   #2
my_list.count(3)   #1

# Tekrar eden elemanları bulma: set() yani küme icinde her eleman essizdir, yani 1 kere yer alir tekrar etmez. Bu nedenle set kullaniyoruz
duplicates = set(number for number in my_list if my_list.count(number) > 1)

# küme olarak gelir:
duplicates

# listeye cevirelim:
print(list(duplicates))







##########        SORU 6         ##########

# Verilen bir listenin elemanlarını toplayan bir Python fonksiyonu yazın.

def calculate_sum(list):
    sum = 0
    for number in list:
        sum += number
    return sum

# Örnek kullanım:
my_list = [2, 4, 6, 8]
calculate_sum(my_list)







##########        SORU 7        ##########

# Verilen bir listedeki harfleri yanyana yazan bir Python fonksiyonu yazın.

my_list = ["D", "a", "t", "a", "s"]

def string_function(list):
    new_string = ""
    for char in list:
        new_string += char
    return new_string

string_function(my_list)




##########        SORU 8         ##########

# Bir metni belirli bir sayıda kez yazdıran bir Python fonksiyonu yazın. Metin ve sayı parametre olarak alınmalıdır.

def repeat_function(text, count):
    repeated_text = text * count
    return repeated_text

repeat_function("Hello ", 5)




##########        SORU 9 |        ##########

# Verilen bir listenin elemanlarını karelerine dönüştüren bir Python fonksiyonu yazın.

def square_function(list):
    new_list = []
    for number in list:
        new_list.append(number ** 2)
    return new_list

my_list = [2, 4, 6, 8]
square_function(my_list)



##########        SORU 10         ##########

# Belirli bir aralıktaki sayıları toplayan bir Python fonksiyonu yazın.
# Fonksiyon, başlangıç ve bitiş değerlerini parametre olarak almalıdır.


def calculate_sum_in_range(firstnumber, lastnumber):
    sum = 0
    for number in range(firstnumber, lastnumber+1):
        sum += number
    return sum


calculate_sum_in_range(2, 10)



##########        SORU 11         ##########

# Verilen iki listenin elemanlarını anahtar-değer çiftleri olarak içeren bir sözlük oluşturan bir dictionary comprehension yazın.

keys = ['a', 'b', 'c']
values = [1, 2, 3]

new_dictionary = {k: v for k, v in zip(keys, values)}

new_dictionary



##########        SORU 12         ##########

#  Bir sözlüğün değerlerinin karelerinden oluşan yeni bir sözlük oluşturan bir dictionary comprehension yazın.

original_dict = {'a': 2, 'b': 3, 'c': 4}

original_dict.items()

squared_dict = {k: v ** 2 for k, v in original_dict.items()}

squared_dict






##########        SORU 13         ##########



##########        SORU 14         ##########



##########        SORU 15         ##########