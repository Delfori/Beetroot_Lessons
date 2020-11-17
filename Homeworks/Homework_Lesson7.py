#!/usr/bin/env python3

# Task 1
"""
A simple function (prints a given argument)
"""

def favorite_movie(name: str):
	print('My favourite movie is named {name}')

# Task 2
"""
Creating a dictionary
"""
country_capital = {}
def make_country(country: str, capital: str):
	country_capital.update({country: capital})
	print(country_capital)

# Task 3
"""
A simple calculator.
"""
	
import math

def make_operation(operator: str, first_num: int, *numbers: int):
	if operator == '+':
		return first_num + sum(numbers)
	elif operator == '-':
		return first_num - sum(numbers)
	elif operator == '*':
		return first_num * math.prod([_ for _ in numbers])
