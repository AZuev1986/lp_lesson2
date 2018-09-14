# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    print('Вызван /start')
    text = 'попробуйте ввести команду /planet'
    print(text)
    update.message.reply_text(text)

def user_planet(bot, update):
    text = 'Введите название планеты СС (за исключением Земли) на английском языке в формате: planet Name_planet'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
#   запись в переменную сегодняшней даты в формате год/месяц/день
    today = datetime.datetime.today().strftime('%Y/%m/%d')
    print(today)
    user_text = update.message.text
    try:
#       создаем список слов из строки при помоще разделителя пробела
        user_text_list = user_text.split()
        print('user_text_list')
#       предполагаем что пользователь все правильно ввел и верим в то что в срезе списка лежит название планеты
        planet_name = user_text_list[1]
        print(planet_name)
#       передаем название планеты в качестве атрибута ephem и затем получаем кортеж ('краткое название', 'полное название'')
        answer_text = ephem.constellation(getattr(ephem, planet_name)(today))
        print(answer_text)
        update.message.reply_text(answer_text)
    except (TypeError, AttributeError):
        update.message.reply_text('Похоже что вы ввели данные в неверном формате попробуйте еще раз')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY1)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', user_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()
