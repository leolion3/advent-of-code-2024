#!/usr/bin/env python3
from matrix_operations import MatrixManipulation


with open('input.txt', 'r') as f:
	matrix = list(filter(len, [x.strip() for x in f.readlines()]))
	matrix = MatrixManipulation(matrix)


def sol_1():
	global matrix
	total = 0
	for row in matrix.get_rows():
		total += row.count('XMAS')
		total += row[::-1].count('XMAS')
	for col in matrix.get_cols():
		total += col.count('XMAS')
		total += col[::-1].count('XMAS')
	for diag in matrix.get_diagonals():
		total += diag.count('XMAS')
		total += diag[::-1].count('XMAS')
	print('Solution 1:', total)


def sol_2():
	global matrix
	total = 0
	matrix = matrix.get_rows()
	for i in range(1, len(matrix) - 1):
		for j in range(1, len(matrix[i]) - 1):
			if matrix[i][j] == 'A':
				_matches = 0
				for r_sym, c_sym in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
					if (
						matrix[i + r_sym][j + c_sym] == 'M' and
						matrix[i - r_sym][j - c_sym] == 'S'
					):
						_matches += 1
				if _matches == 2:
					total += 1
	print('Solution 2:', total)

sol_1()
sol_2()