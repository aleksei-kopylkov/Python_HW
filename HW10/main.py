import asyncio

import telebot
from weather_get import getweather

bot = telebot.TeleBot('5750548190:AAF43O_6X_37GtMIV5-CcQppgfQ75q4U7Pc')
# temperature  = asyncio.run(getweather(city))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # global city
    if message.text == "Погода":
        bot.send_message(message.from_user.id, "")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Для выбора города введите /city")
    elif message.text == "/city":
        bot.send_message(message.from_user.id, "/Moscow")
        bot.send_message(message.from_user.id, "/Saint-Petersburg")
        bot.send_message(message.from_user.id, "/Rostov-on-Don")
    elif message.text == "/Moscow":
        temperature = asyncio.run(getweather("Moscow"))
        bot.send_message(message.from_user.id, f"В Москве {temperature}  градусов")
    elif message.text == "/Saint":
        temperature = asyncio.run(getweather("Saint-Petersburg"))
        bot.send_message(message.from_user.id, f"В Санкт-Петербурге {temperature}  градусов")
    elif message.text == "/Rostov":
        temperature = asyncio.run(getweather("Rostov-on-Don"))
        bot.send_message(message.from_user.id, f"В Ростове {temperature}  градусов")

#


bot.polling(none_stop=True, interval=0)