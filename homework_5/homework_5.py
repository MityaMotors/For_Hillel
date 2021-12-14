import re
#Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку таким образом
#что бы каждое имя однозначно начиналось с большой буквы.
print("\n Issue N1")
String = "john marta james Morgan Adam Maria huang"
String_1 = [word[0].upper() + word[1:] for word in String.split()]
String = " ".join(String_1)
print(String_1)

#Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. выведите в консоль имена
#каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string.
#Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное
#пространство заполнено скажем символом "*"
print("\n Issue N2")
The_names_list = ["John", "Marta", "James", "Amanda", "Marianna"]

The_Names = "Names".center(48, "*")
format_to_the_right = "{:>48}\n" * len(The_names_list)
all_lines_nf = f'{The_Names}\n{format_to_the_right}'
print_text = all_lines_nf.format("John", "Marta", "James", "Amanda", "Marianna")
print(print_text)
print("\n Issue N3")
#Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro ".
#Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно
#{name: Amanda=sssss, age: 32, salary: 1500, currency: quro}

Str_Y = " name=Amanda=sssss&age=32&&salary=1500&currency=quro "

list_1 = Str_Y.replace(" ", '').split("&")
del list_1[2]

cr_dictionary = {}

for item in list_1:
    list_2 = item.split("=", 1)
    for item2 in list_2:
        cr_dictionary[list_2[0]] = list_2[1]
print(cr_dictionary)

#У вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"]
#преобразовать его в список имен переменных для пайтона в формате снейк
#кейс ["first_item", "friends_list", "my_tuple"]

print("\n Issue N4")

Spisok = ["FirstItem", "FriendsList", "MyTuple"]
Spisok_1 = Spisok[0]
Spisok_2 = Spisok[1]
Spisok_3 = Spisok[2]

Spisok_1 = re.sub(r'(?<!^)(?=[A-Z])', "_", Spisok_1).lower()
Spisok_2 = re.sub(r'(?<!^)(?=[A-Z])', "_", Spisok_2).lower()
Spisok_3 = re.sub(r'(?<!^)(?=[A-Z])', "_", Spisok_3).lower()

print(Spisok_1, Spisok_2, Spisok_3)

#У вас есть текст разбейте текст по предложениям.
# качестве результата вы должны получить список из предложений. Текст -все чтот выше.

print("\n Issue N5")

super_text = """Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы.
Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string. Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*".
Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro ". Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda=sssss, age: 32, salary: 1500, currency: quro}.
У вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"].
У вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений. Текст -все чтот выше."""

text_format = super_text.split(".")
print(text_format)