# -*- coding: utf-8 -*-

def age_status(age):
	try:
		age = int(age)
		if age <= 6:
			age_status = 'вы ходите в деский сад'
		elif age <= 17:
			age_status = 'вы ходите в школу'
		elif age <= 23:
			age_status = 'вы учитесь в ВУЗе'
		else:
			age_status = 'вы работаете'
		return age_status
	except (TypeError, ValueError):
		return 'похоже что вы ввели данные не в правильном формате, попробуйте еще раз'

age = input('введите ваш возраст в формате целого числа: ')
result = age_status(age)
print(result)
