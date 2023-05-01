import telebot
import requests
import json
import datetime

bot = telebot.TeleBot('5787802812:AAGfBlJTVGECXwOtnk8A1jfhHcE9HBszWAM')
API = 'af764beb4f6b7845ea428759076d7711'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Напишите город, а я покажу погоду в нем')



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = int(data["main"]["temp"])
        temp_fl = int(data["main"]["feels_like"])
        wind_sp = int(data["wind"]["speed"])
        cur_data = str(datetime.datetime.fromtimestamp(data["dt"]))
        bot.send_message(message.chat.id, f'{cur_data}\nТемпература на улице: {temp} °C\nОщущается как: {temp_fl}°C\nСкорость ветра: {wind_sp} м/c')
        emoji = '☀' if temp > 5.0 else '⛅'
        bot.send_message(message.chat.id, emoji)
    else:
        bot.send_message(message.chat.id, f'Такого города не существует')


bot.polling(none_stop=True)
