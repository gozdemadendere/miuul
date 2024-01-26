

#############################################    SORU 1    #############################################

# Bir fonksiyon tanimlayarak, bir listedeki her bir maasa %20 zam yapip, yeni maaslari bir listeye yazdiralim.
salaries = [1000, 2000, 3000, 4000, 5000]

# 1) for dongusu ile:

def func(list):
    new_salaries = []
    for salary in list:
        new_salaries.append(salary * 20 / 100 + salary)
    return new_salaries

func(salaries)

# % x zam yapmak isterseydik:

salaries = [1000, 2000, 3000, 4000, 5000]

def func(list, rate):
    new_salaries = []
    for salary in list:
        new_salaries.append(salary * rate / 100 + salary)
    return new_salaries

func(salaries, 50)



# 2) list comprehension ile %20 zam yaptiralim:

new_salaries = [salary * 20 / 100 + salary for salary in salaries]
new_salaries


# veya list comprehension icerisinde fonksiyon yazarak:
def func(salary):
    return salary * 20 / 100 + salary


[func(salary) for salary in salaries]






#############################################      SORU 2       ############################################

# Maaslar 3000 den kucukse 2 ile carpalim, degilse %20 zam yapalim. Yeni maaslari yeni bir listeye ekleyelim.
salaries = [1000, 2000, 3000, 4000, 5000]

# 1) for dongusu ile:

new_salaries = []         # !!! fonksiyon tanimlamadik, o nedenle yeni listeyi for dongusu disinda olusturduk.

for salary in salaries:
    if salary < 3000:
        new_salaries.append(salary * 2)
    else:
        new_salaries.append(salary * 20 / 100 + salary)

new_salaries



# 2) list comprehension ile:

new_salaries = [salary * 2 if salary < 3000 else salary * 20 / 100 + salary for salary in salaries]
new_salaries






#############################################      SORU 3       #############################################

# Eger ogrenci stundents_no listesinde ise lower, degilse upper yazdiralim. Yeni bir listeye ekleyelim.
students = ["John", "Mark", "Vanessa", "Mariam"]
students_no = ["John", "Vanessa"]


# 1) for dongusu ile:

new_list = []

for student in students:
    if student in students_no:
        new_list.append(student.lower())
    else:
        new_list.append(student.upper())

new_list



# 2) list comprehension ile:


new_list = [student.lower() if student in students_no else student.upper() for student in students]
new_list







#############################################      SORU 4       #############################################

# 4.A )
# Numbers icindeki her bir degeri 2 ile carpalim ve bir sozluge ekleyelim.
numbers = range(0, 10)

new_dict = {k: k * 2 for k in numbers}
new_dict




# 4.B )
# Her bir value nun karesini aldiralim ve yeni bir sozluk olusturalim.
dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}

# Bazi pratikler:
dictionary  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dictionary.items()  # ([('a', 1), ('b', 2), ('c', 3), ('d', 4)])    # Dictionary nin bir listeye cevrilmis hali.


new_dictionary = {k: v ** 2 for k, v in dictionary.items()}
new_dictionary






#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT
#############################################      SORU 5       #############################################

# Amac: cift sayilarin karesini alarak bir sozluge eklemek
# Key'ler orijinal degerler, value'lar ise degistirilmis degerler olacak.


# 1) for dongusu ile:

numbers = range(0, 10)
new_dict = {}

for number in numbers:
    if number % 2 == 0:
        new_dict[number] = number ** 2

new_dict


# 2) dict comprehension ile:

numbers = range(0, 10)

new_dict = {k: k ** 2 for k in numbers if k % 2 == 0}
new_dict





#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT
#############################################      SORU 6       #############################################

# Bir Listedeki Degisken Isimlerini Degistirmek, Upper yapmak
list = ['total', 'speeding', 'alcohol']



# 1) for dongusu ile:
new_list = []

for element in list:
    new_list.append(element.upper())

new_list


# 2) list comprehension ile:

new_list = [element.upper() for element in list]
new_list







#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT
#############################################      SORU 7       #############################################

# Bir Verisetindeki/ Dataframe deki Degisken Isimlerini Degistirmek, Upper yapmak

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


# 1) for dongusu ile:

list = []

for col in df.columns:
    list.append(col.upper())

list



# 2) list comprehension ile:

[col.upper() for col in df.columns]



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT ******
#############################################      SORU 8       #############################################

# Dataframe'deki degiskenlerin, isminin icinde "ins" olan degiskenlerin basina FLAG, digerlerine NO_FLAG ekleyelim
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


# 1) for dongusu ile:
list = []

for col in df.columns:
    if "ins" in col:
        list.append("FLAG_" + col)
    else:
        list.append("NO_FLAG_" + col)

list


# 2) list comprehension ile:

["FLAG_" + col if "íns" in col else "NO_FLAG_" + col for col in df.columns]

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT
#############################################      SORU 9       #############################################

# Amac: key'i string, value'su asagidaki gibi bir liste olan sozluk olusturmak.
# Bu islemi sadece sayisal degiskenler icin yapmak istiyoruz.

# Output:
# {"total" : ["mean", "min", "max", "var"],
# "speeding" : ["mean", "min", "max", "var"],
# "alcohol" : ["mean", "min", "max", "var"] ...........}

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






#############################################      SORU 10       #############################################

# Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
list = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# kod oncesi pratik: listedeki 4. indexteki elemani gorme:
list[4]

# kod oncesi pratik: listedeki "S" elemaninin indexini gorme:    ***********
list.index("S")



# 1) for dongusu ile:
new_list = []

for char in list:
     if list.index(char) in range(0, 4):
          new_list.append(char)

new_list


# 2) dict comprehension ile:
new_list = [char for char in list if list.index(char) in range(0, 4)]
new_list






#############################################      SORU 11       #############################################

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

# fonksiyonu kontrol edelim
function(l)







#############################################      SORU 12       #############################################

# List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# Numeric olmayan değişkenlerin de isimleri büyümeli. Tek bir list comprehension yapısı kullanılmalı.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# Adim 1 : Numerik degiskenleri bulma: dtype i O (Object) olmayan, yani kategorik olmayan degiskenleri getir
[col for col in df.columns if df[col].dtype != "O"]

# Adim 2: Numerik degiskenlerin ismine NUM_ ekle ve col.upper() diyerek column isimlerini buyult,
# Numerik olmayan degiskenlerin sadece isimlerini buyult

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]




#############################################      SORU 13       #############################################
# List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.
# Tüm değişkenlerin isimleri büyük harf olmalı.Tek bir list comprehension yapısı ile yapılmalı.

df.columns

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


#############################################      SORU 14       #############################################
# List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]

new_list = [col for col in df.columns if col not in og_list]

new_df = df[new_list]
new_df



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  PHD MULAKAT sorusu! *****
#############################################      SORU 15       #############################################

# Amac: Asagidaki sekilde string degistiren fonksiyon yazmak
# (Tek indextekiler kucuk harf ile, cift indextekiler buyuk harfle yazdirilacak)

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"


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



# Gozde'nin 1. cozumu:
text = "hi my name is john and i am learning python"

def alternating(string):
    new_string = ""
    for char in string:
        if string.index(char) % 2 == 0:
            new_string += char.upper()
        else:
            new_string += char.lower()
    return new_string


alternating(text)




# Gozde'nin 2. cozumu:

def alternating(string):
    new_string = ""
    for index in range(0, len(string)):
        if index % 2 == 0:
            new_string += string[index].upper()
        else:
            new_string += string[index].lower()
    print(new_string)

alternating("Merhaba ben Gozde")




# Vahit hocanin cozumu:

def alternating(string):
    new_string = ""
    for string_index in range(0, len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")







#############################################      SORU 16       #############################################

# Her ogrenciyi indexi ile birlikte 2 farkli listeye ekle, tek indextekiler bir listeye ve cift indextekiler bir listeye eklensin.
students = ["John", "Mark", "Vanessa", "Mariam"]

# 1. YOL : enumarate olmadan
A = []
B = []

for student in students:
    if students.index(student) % 2 == 0:
        A.append(student)
    else:
        B.append(student)

A
B



# 2. YOL : enumarate ile
A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

students = ["John", "Mark", "Vanessa", "Mariam"]

A
B





#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  UYGULAMA / MULAKAT
#############################################      SORU 17       #############################################

# divide_students fonksiyonu yaziniz.
# Cift indexte yer alan ogrencileri bir listeye aliniz, tek indexte yer alan ogrencileri baska bir listeye aliniz.
# Fakat bu 2 liste, tek bir liste olarak return olsun.


student_names = ["John", "Mark", "Venessa", "Maria"]

# 1. YOL: enumarete olmadan:

def divide_students(students):
    lists = [[], []]
    for student in students:
        if students.index(student) % 2 == 0:
            lists[0].append(student)
        else:
            lists[1].append(student)
    return lists

divide_students(student_names)


# !!!!!Note: [] gibi listeye, .append diyerek ekliyoruz.  "" gibi string ifadesine, +=  diyerek ekliyoruz




# 2. YOL: enumarete ile:
def divide_students(students):
    lists = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            lists[0].append(student)
        else:
            lists[1].append(student)
    return lists


divide_students(student_names)

st = divide_students(student_names)
st

st[0]
st[1]




#############################################      SORU 18       #############################################

# Daha once for loop mulakat sorusunda tanimadigimiz fonksiyonu, enumarete ile yazalim

# Eski hali
def alternating(string):
    new_string = ""
    for char in string:
        if string.index(char) % 2 == 0:
            new_string += char.upper()
        else:
            new_string += char.lower()
    return new_string

string = "hi my name is john and i am learning python"
alternating(string)


# Yeni hali
def alternating(string):
    new_string = ""
    for index, char in enumerate(string):
        if index % 2 == 0:
            new_string += char.upper()
        else:
            new_string += char.lower()
    return new_string

string = "hi my name is john and i am learning python"
alternating(string)


#############################################      SORU 19       #############################################

# Aşağıda verilen listede mühendislik ve tıp fakültelerinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.


students = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]
#             0     1        2       3         4        5


for index, student in enumerate(students[:3], 1):
    print(f"Muhendislik Fakultesi {index} . ogrenci: {student}")

for index, student in enumerate(students[3:6], 1):
    print(f"Tip Fakultesi {index} . ogrenci: {student}")




# fonksiyon yazarak:
def function(students):
    for index, student in enumerate(students[:3], 1):
        print(f"Muhendislik Fakultesi {index} . ogrenci: {student}")

    for index, student in enumerate(students[3:6], 1):
        print(f"Tip Fakultesi {index} . ogrenci: {student}")

function(students)

