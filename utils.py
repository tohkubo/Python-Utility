import os
import re
import csv
import sys
import shutil
from collections import defaultdict
from datetime import datetime as dt
from functools import reduce


def count(it, sorted = True):
	'''
	Returns list of two-tuples of the number
	of occurrences for each item in the list
	'''
	d = defaultdict(int)

	for item in it:
		d[item] += 1

	if sorted:
		return sorted(d.items(), key = lambda x : x[1])
	return d.items()


def humansort(lst):
	'''
	Takes in a list of strings and
	sorts them naturally.
	'''
	def atoi(s):
		return int(s) if s.isdigit() else s
	return list(map(atoi, re.split('(\d+)', lst)))

# strings = ['version ' + str(i) for i in range(1, 15)]
# strings.sort(key = humansort)


def prod(iterable):
	'''
	Produce the product of all values in
	the iterable (i.e.: list).
	'''
	return reduce(lambda x,y : x * y, iterable)


def fib(v):
	'''
	The classic recursive approach to tackling
	the fib sequence. Cons: you end up repeating
	many of the same computations.
	'''
	if v == 0:
		return 0
	elif v == 1:
		return 1
	return fib(v - 1) + fib(v - 2)


def fib_(v):
	'''
	Another way to tackle the fib sequence.
	No need for extra computations; just
	use/access what you already have.
	'''
	data = [None for _ in range(v + 1)]
	data[0] = 0
	data[1] = 1

	for i in range(2, v + 1):
		data[i] = data[i - 1] + data[i - 2]
	return data[v]

