#!/usr/bin/env python3


with open('input.txt', 'r') as f:
	data = f.readlines()
	v1 = []
	v2 = []
	for val in data:
		n1, n2 = val.strip().split('   ')
		v1.append(int(n1))
		v2.append(int(n2))


def sol_1():
	v1.sort()
	v2.sort()
	s = sum([abs(v2[i] - v1[i]) for i in range(len(v1))])
	print('Solution 1:', s)


def sol_2():
	sol = sum([v2.count(key) * key for key in v1])
	print('Solution 2:', sol)

sol_1()
sol_2()