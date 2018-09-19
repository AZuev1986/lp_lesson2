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

def talk_to_me(bot, update):
    update.message.reply_text('Введите название планеты СС (за исключением Земли) на английском языке в формате: /planet Name_planet')

def user_planet(bot, update, args):
#   запись в переменную сегодняшней даты в формате год/месяц/день
    today = datetime.datetime.today().strftime('%Y/%m/%d')
    print(today)
    user_text = update.message.text
#       создаем список слов из строки при помоще разделителя пробела
    user_text_list = user_text.split()
    print(user_text_list)
    if len(user_text_list) > 1:
#       предполагаем что пользователь все правильно ввел и верим в то что в срезе списка лежит название планеты
        try:
            planet_name = user_text_list[1]
            print(planet_name)
#           передаем название планеты в качестве атрибута ephem и затем получаем кортеж ('краткое название', 'полное название'')
            answer_text = ephem.constellation(getattr(ephem, planet_name)(today))
            print(answer_text)
            update.message.reply_text('{0} in {1}'.format(planet_name, answer_text[1]))
        except (TypeError, AttributeError):
            update.message.reply_text('Похоже что вы ввели данные в неверном формате, попробуйте еще раз')
    else:
        update.message.reply_text('Вы скорее всего забыли ввести название планеты после команды')

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY1)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', user_planet, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()
