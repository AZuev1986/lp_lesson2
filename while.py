# -*- coding: utf-8 -*-
DICT_ANSWER = {
	'Как дела': 'Хорошо!',
	'Что делаешь?': 'Программирую',
	'На чем?': 'На python',
	'Зачем нужны кортежи, если есть списки?': 'Хороший вопрос'
}

def ask_user(user_say):
	while True:
		user_say = input('Спроси что-нибудь\n')
		for key in DICT_ANSWER.keys():
			if user_say == key:
				print(DICT_ANSWER[key])
		if user_say == 'Пока':
			print('Ну пока')
			break

ask_user('start')