#!/usr/bin/env python3
import re


with open('input.txt', 'r') as f:
	data = ''.join(f.read().split('\n'))


def sol_1():
	_sum = 0
	matches = re.findall(r'mul\([0-9]+,[0-9]+\)', data)
	for match in matches:
		num1, num2 = ''.join(match.split('mul(')[1:]).split(')')[0].split(',')
		_sum += int(num1) * int(num2)
	print(f'Solution 1: {_sum}')
	

def sol_2():
	_sum = 0
	_data = 'do()' + data
	search = re.findall(r'do\(\)[^d]*', _data)
	for _line in search:
		matches = re.findall(r'mul\([0-9]+,[0-9]+\)', _line)
		for match in matches:
			num1, num2 = ''.join(match.split('mul(')[1:]).split(')')[0].split(',')
			_sum += int(num1) * int(num2)

	print(f'Solution 2: {_sum}')


sol_1()
sol_2()