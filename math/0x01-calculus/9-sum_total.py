#!/usr/bin/env python3
'''basic sigma notation in python'''

def summation_i_squared(n):
	'''basic sigma noation in pyhthon'''
	if n < i:
		return None
	my_list = list(range(1, n))
	my_list2 = [x ** 2 for x in my_list]
	return(sum(x for x in my_list2))
