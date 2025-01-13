#!/usr/bin/env python3


with open('example.txt', 'r') as f:
	lines = [list(l.strip()) for l in list(filter(len, f.readlines()))]


def find_guard(lines):
	for i, l in enumerate(lines):
		for j, v in enumerate(l):
			if v in ['<', '^', '>', 'v']:
				return i, j
	return -1, -1


def turn_right(guard):
	return {
		'<': '^',
		'^': '>',
		'>': 'v',
		'v': '<'
	}.get(guard)


def get_next(guard):
	return {
		'<': (0, -1),
		'^': (-1, 0),
		'>': (0, 1),
		'v': (1, 0)
	}.get(guard)


def sol_1():
	while True:
		old_y, old_x = find_guard(lines)
		guard = (lines[old_y])[old_x]
		n_y, n_x = get_next(guard)
		x = n_x + old_x
		y = n_y + old_y
		if y >= len(lines) or y < 0 or x >= len(lines[y]) or x < 0:
			(lines[old_y])[old_x] = 'X'
			break
		if (lines[y])[x] == '#':
			(lines[old_y])[old_x] = turn_right(guard)
			continue
		(lines[old_y])[old_x] = 'X'
		(lines[y])[x] = guard
	#print('\n'.join([''.join(l) for l in lines]))
	print('Solution 1:', sum([l.count('X') for l in lines]))


def get_route(lst):
	cache = {}
	while True:
		old_y, old_x = find_guard(lst)
		guard = (lines[old_y])[old_x]
		n_y, n_x = get_next(guard)
		x = n_x + old_x
		y = n_y + old_y
		if y >= len(lines) or y < 0 or x >= len(lines[y]) or x < 0:
			return False
		if (lines[y])[x] == '#':
			(lines[old_y])[old_x] = turn_right(guard)
			continue
		if (lines[y])[x] == guard:
			return True
		(lines[old_y])[old_x] = guard
		(lines[y])[x] = guard

def sol_2():
	traversed = []
	i = 0
	while True:
		old_y, old_x = find_guard(lines)
		guard = (lines[old_y])[old_x]
		for _dir in [guard, turn_right(guard)]:
			n_y, n_x = get_next(guard)
			x = n_x + old_x
			y = n_y + old_y
			if y >= len(lines) or y < 0 or x >= len(lines[y]) or x < 0:
				continue
			lst = copy.deepcopy(lines)
			(lst[old_y])[old_x] = guard
			if get_route(lst):
				i += 1
		(lines[old_y])[old_x] = '.'
		(lines[y])[x] = guard
	print(i)


sol_1()
sol_2()
