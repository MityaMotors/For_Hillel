import requests

url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"
respond_text = ''

respond = requests.get(url)

if respond.ok:
    respond_text = respond.text
# значения для задач 1-3 можно найти в respond_text