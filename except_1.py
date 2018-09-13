# -*- coding: utf-8 -*-
def ask_user(user_say):
	while True:
		try:
			user_say = input('Как дела?\n')
			if user_say == 'Хорошо':
				break
		except KeyboardInterrupt:
			print('Пока')
			break

ask_user('start')