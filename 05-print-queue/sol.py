#!/usr/bin/env python3


with open('input.txt', 'r') as f:
	data = list(filter(len, [x.strip() for x in f.readlines()]))
	rules = {}
	pages = []
	for line in data:
		if '|' in line:
			r1, r2 = line.split('|')
			if r1 in rules:
				rules[r1].append(r2)
			else:
				rules[r1] = [r2]
		else:
			pages.append(line.split(','))

wrong_orders = []

def sol_1():
	global rules, pages, wrong_orders
	total = 0
	for page in pages:
		_c = True
		for i, val in enumerate(page):
			if val in rules:
				for r in rules[val]:
					if r in page[:i]:
						_c = False
						break
				if not _c:
					break
		if _c:
			total += int(page[int(len(page) / 2)])
		else:
			wrong_orders.append(page)
	print('Solution 1:', total)


def sol_2():
	global wrong_orders
	total = 0
	for i in range(len(wrong_orders)):
		page = wrong_orders[i]
		incomplete = True
		while incomplete:
			incomplete = False
			for key, ruleset in rules.items():
				if key not in page:
					continue
				for rule in ruleset:
					if rule not in page:
						continue
					if page.index(rule) < page.index(key):
						idx1 = page.index(rule)
						idx2 = page.index(key)
						page[idx1] = key
						page[idx2] = rule
						incomplete = True
		total += int(page[int(len(page) / 2)])
	print('Solution 2:', total)


sol_1()
sol_2()