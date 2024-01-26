# soru 7 8 9 12 13 14



# divide_students fonksiyonu yaziniz.
# Cift indexte yer alan ogrencileri bir listeye aliniz, tek indexte yer alan ogrencileri baska bir listeye aliniz.
# Fakat bu 2 liste, tek bir liste olarak return olsun.


student_names = ["John", "Mark", "Venessa", "Maria"]


def divide_students(students):
    lists = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            lists[0].append(student)
        else:
            lists[1].append(student)
    return lists


divide_students(student_names)

