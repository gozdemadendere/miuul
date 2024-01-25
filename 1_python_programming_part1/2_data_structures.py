########################################################
# DATA STRUCTURES (Veri Yapıları)
########################################################

### Veri Yapılarına Giriş
# Bir değişken, program tarafından kullanılacak veriyi saklamak için kullanılır.
# Bu veri bir sayı, bir dize, bir mantıksal değer, bir liste veya başka bir veri türü olabilir.
# Python Veri Türleri: Integer / Float (Numeric), Boolean, String, Complex


### Numeric Data Types / Sayısal Veri Türleri

# Integer
x = 46
type(x)

# Float
x = 10.3
type(x)

# Complex
x = 2j + 1
type(x)

## String
x = "Hello AI Era"
type(x)

## Boolean
True
False
type(True)
5 == 4
3 == 3

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Note: List, tuple, set, dictionary gibi veri yapıları, Python Koleksiyonları (Dizileri) olarak adlandırılır.


## List [square brackets]
x = ["btc", "eth", "xrp"]
type(x)


## Dictionary {curly brackets}
x = {"name": "Peter", "Age": 36}   # Key: name , Value: Age
type(x)


## Tuple (round brackets)
x = ("Python", "ml", "ds")
type(x)


## Set {curly brackets} # Küme
x = {"Python", "ml", "ds"}
type(x)






########################################################
### SAYILAR (int, float, complex)
########################################################

##      Arithmetic Operations:

# +    Addition Operator
# -    Subtraction Operator
# *    Multiplication Operator
# /    Division operator
# //   Floor Division
# %    Modulus (Modulo operator)
# **   Exponentiation


## Relational Operations: They are also called comparison operators and they compare values.
## Python has 6 relational operators:

# >     Greater than
# <     Less than
# ==    Equal to
# !=    Not equal to
# >=    Greater than or equal to
# <=    Less than or equal to

a = 5
b = 10.5

a * 3
a / 7
a * b / 7



## Üs Alma (Exponentiation)
a ** 2
print(2**10)
print(8**2)
print(4**0.5)

## Modül Alma (Modulus)
a % 2
print(27 % 3)

## Tipleri Değiştirme
int(b)
float(a)

int(a * b / 10)

c = (a * b / 10)
int(c)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Plus-Equals Operator +=   (Add and assign Operator)
message = ""
message = "abc"
message += "def"
message += "ghi"
print(message)


counter = 0
counter += 5   # add 5
counter += 15  # add 15
print(counter)


# example
total_price = 0
new_sneakers = 50.00
nice_sweater = 39.00
fun_books = 20.00

# Update total_price here:
total_price += new_sneakers
total_price += nice_sweater
total_price += fun_books
print("The total price is", total_price)




########################################################
### STRINGS (Karakter Dizileri) (str)
########################################################

print("John")

name = "John"

a = "Gozde"
b = "Madendere"

print(a + " " + b)


example1 = "Stranger, if you passing meet me and \
desire to speak to me, why \
should you not speak to me? \
And why should \
I not speak to you?"
print(example1)

## Multi-line Strings """ (Cok Satirli Karakter Dizileri)

long_str = """
Stranger, if you passing meet me and
desire to speak to me, why 
should you not speak to me? 
And why should 
I not speak to you?
"""
print(long_str)


## Karakter Dizilerinin Elemanlarına Erişmek
name = "Gözde"
name[0]
name[3]

## Karakter Dizilerinde Dilimleme İşlemi
name[0:2]   # 2'ye kadar, 2 dahil değil
name[0:3]
name[0:10]

## String İçerisinde Karakter Sorgulamak
long_str

"stranger" in long_str
"Stranger" in long_str  # büyük küçük harf algılar! = case sensitive
"stranger" not in long_str



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

########################################################
### STRING Metodları
########################################################

##### Metod: Çeşitli görevleri yerine getiren fonksiyon benzeri yapılarıdır. (Class içinde yer alan fonksiyonlardır.)

## Not: Metod ve fonksiyon aynı şeydir, çeşitli görevleri yerine getirirler.
## Not: Eğer bir fonksiyon Class yapısı içindeyse metoddur, değilse fonksiyondur.

name = "gözde"
dir(name)  # Bu veri yapısına uygulanabilecek metodları görürüz!




#####################
# len
#####################

type(len)

len(name)
len("gozde")



#####################
# upper & lower
#####################

"Gozde".upper()
"Gozde".lower()


#####################
# replace
#####################

name = "gozde"
name.replace("e", "a")


#####################
# split
#####################

name = "gozde madendere"
name.split()


#####################
# strip: kirpar
#####################

"gozde".strip()
"gozde".strip("z")


#####################
# capitalize : İlk harfi büyütür
#####################

"gozde".capitalize()

# .join() : Bir Python string metodudur. Bir karakter dizisini başka bir dizi içindeki elemanlar arasına yerleştirme işlevine sahiptir. Bu metodun kullanımı şu şekildedir:
string = " "
elements = ["The", "goal", "is", "to", "turn", "data", "into", "information,", "and", "information", "into", "insight."]
new_string = string.join(elements)
print(new_string)

# .isalpha() : Bir Python string metodudur. Bu metodun amacı, bir karakterin yalnızca alfabedeki harflerden oluşup oluşmadığını kontrol etmektir.
character = 'A'
result = character.isalpha()
print(result)  # Çıktı: True



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

########################################################
### List
########################################################

# Elemanları değiştirilebilir.
# Sıralıdır. Index işlemi yapılabilir. (Elemanlara erişilebilir.)
# Kapsayıcıdır. İçinde birden fazla veri yapısını tutabilir.


names = ["a", "b", "c", "d"]

notes = [1 ,2 ,3, 4]
type(notes)

not_names = [1, 2, 3, "a", "b", True, [1, 2, 3]] # Kapsayıcıdır. İçinde birden fazla veri yapısını tutabilir.
type(not_names)

not_names[0]
not_names[5]
not_names[6]
not_names[6][1] # liste içindeki listedeki elemana erişmek için


type(not_names[6])  #list
type(not_names[6][1])  #int


not_names[0] = 99   # Elemanları değiştirilebilir.
not_names


not_names[0:4]   # 0,1,2,3. elemanları çağırır




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#####################
## Liste metodlari (List Methods) :
#  len()
# .append(x)
# .insert(index,x)
# .remove(x)
# .pop(index)
# .sort()
#####################

notes = [1, 2, 3, 4, 4]
dir(notes)  #  Bu veri yapisina uygulanabilecek methodlari cagirir!
dir(list)   # "List" yapisina uygulanabilecek methodlari cagirir!


#####################
# len
#####################
len(notes)


#####################
# append : eleman ekler
#####################

notes
notes.append(100)
notes



#####################
# insert : index e gore eleman ekler
#####################

notes.insert(2, 44)
notes



#####################
# pop : index e gore eleman siler
#####################

notes.pop(2)
notes

#####################
# remove : removes the "first matching element" in a list.
#####################

notes.remove(4)
notes




## Two-Dimensional (2D)

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
heights
print(heights)

heights.append(["Gozde", 65])
print(heights)

heights.remove(["Alexus", 70])
print(heights)



## Accessing 2D Lists

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
print(heights)

heights[0]
heights[0][0]

sams_info = heights[2]
print(sams_info)

sams_height = heights[2][1]
print(sams_height)



## Modifying 2D Lists

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
print(heights)


heights[0] = ["Gozde", 70]
print(heights)

heights[1][0] = "Gamze"
print(heights)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## range
range(10)
range(0, 10)   # usttekinin aynisi
list(range(0, 10))

example_list = range(10)    #0dan 10a kadar, 10 dahil degil
print(example_list)
list(example_list)       #Listeye cevirelim  !!!!!!!!!
print(list(example_list))


example_list = range(5, 10)   #5ten 10a kadar, 10 dahil degil
print(example_list)
print(list(example_list))  #Listeye cevirelim

example_list3 = range(3, 10, 2)    #3ten 10a kadar, 2ser 2ser
list(example_list3)  #Listeye cevirelim




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## slicing
fruits = ["apple", "cherry", "pineapple", "orange", "mango", "banana", "melon", "watermelon"]

print(fruits)
print(fruits[3])

print(fruits[0:3])   # 0dan 3e kadar, 3 dahil degil
print(fruits[:3])    # usttekinin aynisi
print(fruits[3:])    # 3ten itibaren, 3 dahil, son elemana kadar
print(fruits[3:5])   # 3 ve 4. elamanlar
print(fruits[:-3])   # son 3 elemani alma ?


## sorting
fruits = ["apple", "cherry", "pineapple", "orange", "mango"]

fruits.sort()
fruits



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

########################################################
### Dictionary
########################################################

# Elemanları değiştirilebilir.
# Sırasızdır. (3.7 sürümü sonrası sıralıdır.)
# Kapsayıcıdır. Farklı veri tiplerini içinde tutabilir.


# key-value değerlerini girelim
dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]


# Sözlük içinde liste oluşturabiliyoruz! # Kapsayıcıdır.

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}


#####################
## Key sorgulama
#####################

"REG" in dictionary
"HELLO" in dictionary


#####################
## Key'e gore Value'ya erismek
#####################

dictionary["REG"]
dictionary["REG"][1]

dictionary.get("REG")



#####################
## Eleman degistirmek
#####################

dir(dictionary)  # bu veri yapisina uygulanabilecek methodlari cagirir!

dictionary.get("REG")

dictionary["REG"] = ["ABC", 10]
dictionary



#####################
## Tum Key'lere erismek
#####################
dictionary.keys()


#####################
## Tum Value'lara erismek
#####################
dictionary.values()


#####################
## Tum Ciftleri Tuple Halinde Listeye Cevirme
#####################

dictionary.items()  # dictionary yi tuple lar halinde listeye cevirdik


#####################
## Key-Value degerini guncellemek   !!!!!!!!!!!!!!!
#####################

dictionary.update({"REG": 11})   # sozluk var icinde
dictionary



#####################
## Yeni Key-Value eklemek   !!!!!!!!!!!!!!!
#####################

dictionary.update({"RF": 10})    # sozluk var icinde
dictionary






#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

########################################################
### Tuple (Demet)
########################################################

# Elemanları değiştirilemez.
# Sıralıdır. Index işlemi yapılabilir. (Elemanlara erişilebilir.)
# Kapsayıcıdır. (Farklı veri tiplerini içinde tutabilir.)


t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

# tuple i liste ye cevirirsek, elemanlari ancak o zaman degistirebiliriz.      !!!!!!!!!!!!!!!!!!
# ardindan da liste yi tuple a cevirebiliriz:
t = list(t)
t[0] = 99
t = tuple(t)

type(t)
t




########################################################
### Set (Küme)
########################################################

# Elemanları değiştirilemez.
# Sırasız & eşsizdir. (Her elemandan bir tane vardır, tekrar etmez)
# Kapsayıcıdır. (Farklı veri tiplerini içinde tutabilir.)



###############
### difference : iki kumenin farki
###############



set1 = set([1, 3, 5])   # Liste var içinde!    # Yazarken set() deriz, sonuç {} içinde gelir!
set2 = set([1, 2, 3])

# difference: set1'de olan, set2'de olmayanlar
set1.difference(set2)    # set1'de olan set2'de olmayanlar
# veya
set1 - set2


# symmetric_difference: İki kümede de birbirlerine göre olmayanlar
set1.symmetric_difference(set2)

# intersection: İki kümenin kesişimi
set1.intersection(set2)

# union: İki kümenin birleşimi
set1.union(set2)

# issubset(): Bir küme, diğer kümenin alt kümesi mi?
set1.issubset(set2)   # set1 set2'nin alt kümesi mi?

# issuperset(): Bir küme, diğer küneyi kapsıyor mu?
set1.issuperset(set2)  # set1 set2'yi kapsıyor mu?

# isdisjoint(): İki kümenin kesişimi boş mu?
# Not: "is" ile başlıyorsa, sonuç True veya False'tur
set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])
set1.isdisjoint(set2)



