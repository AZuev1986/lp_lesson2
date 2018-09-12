#-*- coding: utf-8 -*-
'''list_int = [1, 2, 23, 34, 22, 11, 345, 5, 7, 47]
for list_element in list_int:
	print(int(list_element) + 1)'''
'''string_input = str(input('введите строку: '))
for symbol in string_input:
	print(symbol)'''
list_score = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, {'school_class': '5б', 'scores': [2, 4, 5, 3]}, {'school_class': '11а', 'scores': [5, 5, 5, 5, 5, 5]}]
sum_school = 0
sum_n = 0
for clas in list_score:
	sum_class = 0
	n = len(clas.get('scores'))
	for score in clas.get('scores'):
		sum_class += score
	sum_n += n
	average_score_class = sum_class / n
	sum_school += sum_class
	print('средняя оценка по классу', clas['school_class'], round(average_score_class, 1))
average_score_school = sum_school / sum_n
print('средняя оценка по школе', round(average_score_school, 1))
