# -*- coding: utf-8 -*-

def string_comparison(string1, string2):
	if (isinstance(string1, str) and isinstance(string2, str)) == False:
		string_comparison = 0
	elif string1 == string2:
		string_comparison = 1
	elif string2 == 'learn':
		string_comparison = 3
		if len(string1) > len(string2):
			string_comparison = '2 & 3'
	elif len(string1) > len(string2):
		string_comparison = 2
	else:
		string_comparison = 'случай не подходит ни под одно из условий'
	return print(string_comparison)

string_comparison(2, 'bdfijf')
string_comparison(2, 3)
string_comparison('ycducdgv', 'learn')
string_comparison('111', 'learn')
string_comparison('fdjfhfh', 'fef')
string_comparison('dgy', 'euhfufh')
