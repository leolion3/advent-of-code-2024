#!/usr/bin/env python3


with open('input.txt', 'r') as f:
	data = f.readlines()


def contains_invalid(vals, _sym, _min, _max):
	last_valid = vals[0]
	for j, v in enumerate(vals[1:]):
			diff = (v - last_valid) * _sym
			if diff < _min or diff > _max:
				return True
			else:
				last_valid = v
	return False


def sol():
	_sum = 0
	_sum_2 = 0

	for line in data:
		_w = 0
		vals = [int(x) for x in line.split(' ')]
		# Get most common change
		symbs = [1 if vals[x] - vals[x-1] > 0 else -1 for x in range(1, len(vals))]
		_sym = 1 if symbs.count(1) > symbs.count(-1) else -1
		_max = 3
		_min = 1
		count = not contains_invalid(vals, _sym, _min, _max)

		for i in range(len(vals)):
			new_vals = vals[0:i] + vals[i+1:]
			if not count and not contains_invalid(new_vals, _sym, _min, _max):
				_sum_2 += 1
				break

		if count:
			_sum += 1
	print(f'Solution 1: {_sum}')
	print(f'Solution 2: {_sum + _sum_2}')


sol()