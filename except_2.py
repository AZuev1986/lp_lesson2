# -*- coding: utf-8 -*-
def get_summ(num_one, num_two):
	try:
		summ = int(num_one) + int(num_two)
		print('Сумма двух числел', summ)
	except ValueError:
		print('похоже что вы ввели данные в неверном формате, попробуйте еще раз')

num_one = input('введите первое число\n')
num_two = input('введите второе число\n')
get_summ(num_one, num_two)
