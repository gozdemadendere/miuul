# FONKSIYONLAR, KOSULLAR, DONGULER, COMPREHENSIVE

##########################################################################
# FUNCTIONS
##########################################################################

# Belirli gorevleri yerine getirmek icin tanimlanan kod parcalaridir.
# Parametre: Fonksiyon tanimlanmasi sirasinda ifade edilen degiskenlerdir.
# Arguman:   Bu fonks lar cagrildiginda, bu parametreler karsiliginda, girilen degerlerdir.


##########################
# FONKSIYON TANIMLAMA
##########################

# Girilen değeri 2 ile çarparak bir fonksiyon yazalım
def calculate(x):  # calculate: fonks ismi, (x): parametre
    print(x * 2)  # fonksiyonun gövdesi / görevi / statement


calculate(5)


# 2 parametreli/argümanlı bir fonksiyon tanımlayalım
def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)
summer(arg1=7, arg2=8)


##########################
# DOCSTRING : Fonsiyonlara ortak bir dil ile bilgi notu eklemedir.
##########################

# Temel olarak 3 bolumden olusur: Kisa bir aciklama, parameters, returns (en alta examples eklenebilir)

def summer(arg1, arg2):
    """
    Sum of two numbers

    Parameters
    ----------
    arg1: int, float
    arg2: int, float

    Returns
    -------
    int, float

    """
    print(arg1 + arg2)



##########################
# FONKSIYON - STATEMENT
##########################

# def function_name(parameters/arguments):
#          statements (function body)


def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")


say_hi()


def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")


say_hi("Gozde")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# Girilen 2 degeri birbiriyle carpip, bir liste icine ekleyecek fonksiyon

list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 8)

add_element(18, 8)

add_element(180, 10)




##########################
# Ön Tanimli Argumanlar/Parametreler (Default Parameters/Arguments)
##########################

def divide(a, b=2):
    print(a / b)


divide(8)


def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")


say_hi()           # on tanimli deger olan "Merhaba" yi yazar
say_hi("mrb")      # girilen "mrb" yi yazar




##########################
# Ne zaman fonksiyona ihtiyacimiz olur?
##########################

# Birbirini tekrar eden islemler yapmamiz gerektiginde, fonksiyon tanimlayarak islemleri otomatik bir sekilde gerceklestiririz.
# DRY(Don’t repeat yourself) kuralına uymak için

def calculate(warm, moisture, charge):
    print((warm + moisture) / charge)


calculate(98, 12, 78)


##########################
# Return: Fonksiyon Ciktilarini Girdi Olarak Kullanmak
##########################

# Return ile fonksiyon ciktisi, girdi olarak kullanima hazir hale gelir.


def calculate(warm, moisture, charge):
    return (warm + moisture) / charge


# Fonksiyonu return ile yazdigimiz icin, 10 ile direkt carpabiliyor.
# Eger print ile yazsaydik, 10 ile carpamaz hata verirdi.
calculate(98, 12, 78) * 10


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def calculate(warm, moisture, charge):
    warm = warm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (warm + moisture) / charge

    return warm, moisture, charge, output


calculate(98, 12, 78)

type(calculate(98, 12, 78))



##########################
# Fonksiyon icerisinden fonksiyon cagirmak
##########################

def calculate(warm, moisture, charge):
    return (warm + moisture) / charge


calculate(90, 12, 12) * 10
type(calculate(90, 12, 12) * 10)


#ciktinin integer olmasini saglayalim
def calculate(warm, moisture, charge):
    return int((warm + moisture) / charge)


calculate(90, 12, 12) * 10
type(calculate(90, 12, 12) * 10)


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

##### Eger bir fonksiyon icinde baska fonksiyonlar tanimliyorsak,
# icteki fonksiyonlarin parametre/argumanlarini da mutlaka tanimlamaliyiz.

def all_calculation(warm, moisture, charge, a, p):
    a = calculate(warm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 19, 12)





##########################
# Lokal & Global Degiskenler (Local & Global Variables)
##########################

list_store = [1, 2]


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 9)

# lokal degisken: c
# global degisken: a, b


# Global Scope: Global etki alanında olan bir değişkendir ve programın herhangi bir bölümünden erişilebilir.

# Local Scope: Bir değişkenin veya fonksiyonun local etki alan tanımlandığı yerde veya daha özel bir kapsam içinde erişilebilir olduğu alandır.









##########################################################################
# CONDITIONS
##########################################################################

# True - False
1 == 1
1 == 2

###################################
# if
###################################

x = 20
y = 20

if x == y:
    print("These numbers are the same")


def number_check(number):
    if number == 10:
        print("number is 10")


number_check(10)



credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
    print("You meet the requirements to graduate!")

if credits >= 120 or gpa >= 2.0:
    print("You have met at least one of the requirements.")

###################################
# else : else statements allow us to elegantly describe what we want our code to do when certain conditions are not met.
###################################

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(15)


if (credits >= 120) and (gpa >= 2.0):
    print("You meet the requirements to graduate!")
else:
    print("You do not meet the requirements to graduate.")

###################################
# elif
###################################


def number_check(number):
    if number == 10:
        print("number is 10")
    elif number < 10:
        print("number is less than 10")
    else:
        print("number is greater than 10")


number_check(15)



grade = 86

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")






##########################################################################
# LOOPS
##########################################################################

###################################
# for loop
###################################


students = ["John", "Mark", "Vanessa", "Mariam"]

students[0]
students[1]
students[2]

for student in students:
    print(student)


for student in students:
    print(student.upper())



ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

print(ingredients)

for i in ingredients:
    print(i)



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

# %20 zam uygulayalim

for salary in salaries:
    print(salary * 20 / 100 + salary)

# integer yapalim
for salary in salaries:
    print(int(salary * 20 / 100 + salary))

# maasa zam yapma fonksiyonu ekleyelim
def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)

# 1500 liralik maasa, %10 zam yapalim
new_salary(1500, 10)

# tum maaslara %10 zam yapilsin

for salary in salaries:
    print(new_salary(salary, 10))

for salary in salaries:
    if salary > 1000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 5))




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT

# Amac: Asagidaki sekilde string degistiren fonksiyon yazmak
# (Tek indextekileri kucult, cift indextekileri buyut)

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

# yani, tek indextekiler(1,3,5,7..) kucuk, cift indextekiler(0,2,4,6..) buyuk harf olacak


# oncelikle bazi pratikler yapalim:
range(0, 5)
range(5)    #usttekinin aynisi

range(0, len("miuul"))
range(len("miuul"))    #usttekinin aynisi

"miuul"[2].lower()

for i in range(0, 5):  # range: 0dan 5e kadar gez, 5 dahil degil
    print(i)

for i in range(0, len("miuul")):   # range: yine 0dan 5e kadar
    print(i)




# Gozde'nin fonksiyonu:

def alternating(string):
    new_string = ""
    for index in range(0, len(string)):
        if index % 2 == 0:
            new_string += string[index].upper()
        else:
            new_string += string[index].lower()
    print(new_string)

alternating("Merhaba ben Gozde")



# Vahit hocanin fonksiyonu:

def alternating(string):
    new_string = ""
    for string_index in range(0, len(string)):
        if string_index % 2 == 0:               # index cift ise buyuk harfe cevir
            new_string += string[string_index].upper()
        else:                                   # index tek ise kucuk harfe cevir
            new_string += string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")




###################################
# break & continue & while
###################################
# break:     Aranan koşula gelinirse döngüyü bitirir, o degeri de almaz.
# continue:  Aranan koşula gelince pas geçer, sadece o degeri almadan devam eder.



salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break  #maas 3000 ise orada durdur, 3000i de alma!
    print(salary)

for salary in salaries:
    if salary == 3000:
        continue
        # maas 3000 ise onu alma, ve devam et
    print(salary)





###################################
# while
###################################


number = 1

# number 1den basla, number i 1er 1er arttirarak 5e kadar git, 5i dahil etme
while number < 5:
    print(number)
    number += 1

# number 1den basla, number i 2ser 2ser arttirarak 10a kadar git, 10u dahil etme
while number < 10:
    print(number)
    number += 2




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

###################################
# Enumerate: Otomatik Counter/Indexer ekleyerek for loop
###################################

students = ["John", "Mark", "Vanessa", "Mariam"]
print(students)
print(list(students))
print(list(enumerate(students)))     # *****
print(list(enumerate(students, 1)))



students = ["John", "Mark", "Vanessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

for index, student in enumerate(students, 1):    # index 1den baslar
    print(index, student)


A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT

###################################
# Enumerate / Uygulama / MULAKAT
###################################
# divide_students fonksiyonu yaziniz
# Cift indexte yer alan ogrencileri bir listeye aliniz
# Tek indexte yer alan ogrencileri baska bir listeye aliniz
# Fakat bu 2 liste, tek bir liste olarak return olsun


students = ["John", "Mark", "Venessa", "Maria"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


divide_students(students)        # hem printi hem return u döndürür

st = divide_students(students)
st

st[0]
st[1]

# !!!!!Note: [] gibi listeye, .append diyerek ekliyoruz.  "" gibi string ifadesine, +=  diyerek ekliyoruz


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT

###################################
# Daha once for loop mulakat sorusunda tanimadigimiz fonksiyonu, enumarete ile yazalim
###################################

# Eski hali
def function(word):
    new_word = ""
    for index in range(0, len(word)):
        if index % 2 == 0:
            new_word += word[index].upper()
        else:
            new_word += word[index].lower()
    print(new_word)

function("Merhaba ben Gozde")




# Yeni hali
def function2(word):
    new_word = ""
    for index, letter in enumerate(word):
        if index % 2 == 0:
            new_word += letter.upper()
        else:
            new_word += letter.lower()
    print(new_word)

function2("Merhaba ben Gozde")




###################################
# Zip fonksiyonu : Farkli LISTELERI, tek bir liste icinde, tuple lar olarak birlestirir.
###################################
# Zip Function: Merging "LISTS" into Tuples

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



###################################
# lambda, map, filter, reduce
###################################

# lambda: Bir fonksiyon olusturma seklidir, ama kullan-at fonksiyondur
# Kullanim sekli ornegi: lambda arg1, arg2: arg1 + arg2

new_sum = lambda a, b: a + b

new_sum(4, 5)



# map: Döngü yazmaktan kurtarir
# Kullanim sekli ornegi: map(uygulanmak istenen fonksiyon, uygulanmak istenen yer)

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))


list(map(new_salary, salaries))    # yani: salariesdeki tum elemanlara, new_salary fonksiyonunu uygula

# lambda ve map iliskisi:
list(map(lambda x: x * 20 / 100 + x, salaries))  # yani: salariesdeki tum elemanlara, bu lambda fonksiyonunu uygula

list(map(lambda x: x ** 2, salaries))  # yani: salariesdeki tum elemanlara, bu lambda fonksiyonunu uygula


# filter: filtreleme islemleri yapar

salaries = [1000, 2000, 3000, 4000, 5000]

list(filter(lambda x: x % 2 == 0, salaries))  # yani: salariesdeki tum elemanlara, bu filtrelemeyi uygula ve o elemanlari getir









#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

##########################################################################
# COMPREHENSIONS
##########################################################################

###################################
# List Comprehension
###################################

salaries = [1000, 2000, 3000, 4000, 5000]

# Maasa %20 zam yapacak bir fonksiyon yazalim
def new_salary(x):
    return x * 20 / 100 + x

# Her bir maasa fonksiyonu uygulatalim
for salary in salaries:
    print(new_salary(salary))

# Bir listeye, yeni maaslari yazdiralim
null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list

# Eger maas 3000den buyukse,
for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

null_list



# List comprehension ile:

# YAPI:

# [Yapilacak islem            for dongusu]
# [Yapilacak islem            for dongusu           if+sart]
# [Yapilacak islem if+sart else+sart                for dongusu]


# fonksiyonumuz neydi
def new_salary(x):
    return x * 20 / 100 + x

# okuma: salaries de salary leri gez, her salary icin salary * 2
[salary * 2 for salary in salaries]


# okuma: eger salary < 3000 ise, salaries de salary leri gez, her salary icin salary * 2
[salary * 2 for salary in salaries if salary < 3000]


# okuma: salaries de salary leri oku, eger salary 3000den kucukse (new_salary(salary)*2 else...
# sadece if varsa for dongusunun sagina, if else blogu varsa for dongusunun soluna yazilir
[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]


# Eger ogrenci stundents_no listesinde ise lower, degilse upper yazdiralim.
students = ["John", "Mark", "Vanessa", "Mariam"]
students_no = ["John", "Vanessa"]

[student.lower() if student in students_no else student.upper() for student in students]





###################################
# Dict Comprehension
###################################

# k: key, v:value
# numbers icindeki her bir degeri 2 ile carpalim
numbers = range(0, 10)

{k: k ** 2 for k in numbers}




dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}

dictionary

dictionary.keys()
dictionary.values()
dictionary.items()

# k: key, v:value
# her bir value nun karesini aldiralim
{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}






eski_fiyat = {'süt': 1.02, 'kahve': 2.5, 'ekmek': 2.5}

dolar_tl = 0.76
yeni_fiyat = {item: value*dolar_tl for (item, value) in eski_fiyat.items()}
print(yeni_fiyat)



original_dict = {'ahmet': 38, 'mehmet': 48, 'ali': 57, 'veli': 33}

dict2 = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(dict2)



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT

###################################
# Dict Comprehension / Uygulama / Mulakat
###################################

# Amac: cift sayilarin karesini alarak bir sozluge eklemek
# Key'ler orijinal degerler, value'lar ise degistirilmis degerler olacak.


# for dongusu ile:
numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2



# dict comprehension ile:
numbers = range(10)

{n: n ** 2 for n in numbers if n % 2 == 0}


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT

###################################
# List & Dict Comprehension / Uygulama 1
###################################

# Bir Listedeki Degisken Isimlerini Degistirmek

# before:
# ['total', 'speeding', 'alcohol']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL']


list = ['total', 'speeding', 'alcohol']
new_list = []

list[0].upper()


# for döngüsü ile:
for element in list:
    new_list.append(element.upper())

new_list


# list comprehension ile:
[element.upper() for element in list]



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT

# Bir Verisetindeki/ Dataframe deki Degisken Isimlerini Degistirmek

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


# for döngüsü ile:

for col in df.columns:
    print(col.upper())

# bir listeye ekleyerek, kalici hale getirelim
list = []

for col in df.columns:
    list.append(col.upper())

list


# list comprehension ile:
list = []

[col.upper() for col in df.columns]





#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT ******

# Dataframe'deki degiskenlerin, isminin icinde INS olan degiskenlerin basina FLAG, digerlerine NO_FLAG ekleyelim

df.columns


# for döngüsü ile:
list = []

for col in df.columns:
    if "INS" in col:
        list.append("FLAG_" + col)
    else:
        list.append("NO_FLAG_" + col)

list


# list comprehension ile:
list = []

["FLAG_" + col if "ins" in col else "NO_FLAG_" + col for col in df.columns]



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT

# Amac: key'i string, value'su asagidaki gibi bir liste olan sozluk olusturmak.
# Bu islemi sadece sayisal degiskenler icin yapmak istiyoruz.

# Output:
# {"total" : ["mean", "min", "max", "var"],
# "speeding" : ["mean", "min", "max", "var"],
# "alcohol" : ["mean", "min", "max", "var"]}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


# 1) for dongusu ile:

# dtype i O (Object) olmayan, yani kategorik olmayan degiskenleri getir
num_cols = [col for col in df.columns if df[col].dtype != "O"]
num_cols

agg_list = ["mean", "min", "max", "sum"]

dict = {}

for col in num_cols:
    dict[col] = agg_list         # dict[col] : sozlugun key degeri = agg_lsit deki degerler (key : value)

dict



# 2) dict comprehension ile:

num_cols = [col for col in df.columns if df[col].dtype != "O"]
num_cols

agg_list = ["mean", "min", "max", "sum"]

{col: agg_list for col in num_cols}



###### BONUS !!!!!!!!!!!

new_dict = {col: agg_list for col in num_cols}
new_dict


# alttaki kod satiri oncesi basic bir ornek:
df["total"].agg("mean")

# df icindeki num_cols lara, agg fonksiyonu araciligiyla, new_dict icindeki islemleri uygulattik!
df[num_cols].agg(new_dict)





