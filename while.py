# -*- coding: utf-8 -*-
DICT_ANSWER = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Программирую',
    'На чем?': 'На python',
    'Зачем нужны кортежи, если есть списки?': 'Хороший вопрос'
}

def ask_user(user_say):
    while True:
        user_say = input('Спроси что-нибудь\n')
        if user_say in  DICT_ANSWER.keys():
            print(DICT_ANSWER[user_say])
        if user_say == 'Пока':
            print('Ну пока')
            break

ask_user('start')