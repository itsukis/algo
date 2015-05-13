# https://code.google.com/codejam/contest/4224486/dashboard#s=p1

import sys

def bin_search():
	return 0

def count_completed_cuts(b, t):
	sum = 0
	for bt in b:
		c = t / bt
		sum = sum + c

	return sum

def main():
	print count_completed_cuts([10, 5], 15)

if __name__=='__main__':
	main()