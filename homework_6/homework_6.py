import requests
import pprint

pp = pprint.PrettyPrinter(depth=5)

url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"
respond_text = ''

respond = requests.get(url)

if respond.ok:
    respond_text = respond.text

"""Создать список содержащий все доступные разделы с сайта https://rozetka.com.ua/ua/sport-i-uvlecheniya"""
p = []
array = respond_text.split('/&q;,&q;title&q;:&q;')
for item in array[1::]:
    item.replace('image_header_list&q;,&q;order&q', '')
    p.append(item.split('&q;,&q;order&q;:')[0])
pp.pprint(f"Homework6/1: {p}")

"""Создать словарь содержащий в качестве ключей имя раздела с задачи 1
 и в качестве значений - url адресс раздела (href=url) ."""
array_link = respond_text.split('.jpg&q;,&q;link&q;:&q;')[1::]
link = []
for item in array_link:
    item.replace('image_header_list&q;,&q;order&q', '')
    link.append(item.split('&q;,&q;title&q;:&q;')[0])

dict_p_link = {}
for index in range(len(p)):
    dict_p_link[p[index]] = link[index]
pp.pprint (f"Homework6/2 \n {dict_p_link}")




