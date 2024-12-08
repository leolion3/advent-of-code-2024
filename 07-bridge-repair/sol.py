#!/usr/bin/env python3
from itertools import product


with open('example.txt', 'r') as f:
	data = [l.strip().split(' ') for l in list(filter(len, f.readlines()))]


def eval_expr(vals, operators, result):
	combs = product(operators, repeat=len(vals) - 1)
	for comb in combs:
		comb = list(comb)
		vals = [int(x) for x in vals]
		res = vals[0]
		for i, v in enumerate(vals[1:]):
			op = comb[i]
			if op == '+':
				res += v
			elif op == '*':
				res *= v
			else:
				res = int(f'{res}{v}')
		if res == result:
			return True
	return False

def sol_1():
	operators = ['+', '*']
	operators_2 = ['||', '+', '*']
	res = 0
	res2 = 0
	total = len(data)
	for i, line in enumerate(data):
		print(f'Progress: {i+1}/{total}', end='\r')	
		result = int((line[0])[:-1])
		vals = line[1:]
		if eval_expr(vals, operators, result):
			res += result
		if eval_expr(vals, operators_2, result):
			res2 += result
	print()
	print('Solution 1:', res)
	print('Solution 2:', res2)


sol_1()