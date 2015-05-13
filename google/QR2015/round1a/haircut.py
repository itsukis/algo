# https://code.google.com/codejam/contest/4224486/dashboard#s=p1

import sys

def found(N, b, t):
	cpl = count_completed_cuts(b, t)
	avb, avbl = count_available_bar(b, t)
	if N > cpl and N <= cpl + avb:
		return True, avbl
	else: 
		return False

def count_available_bar(b, t):
	abl = []
	idx = 0
	sum = 0
	for bt in b:
		if t % bt == 0:
			sum = sum + 1
			abl.append(idx)
		idx = idx + 1

	return sum, abl

def count_completed_cuts(b, t):
	sum = 0
	for bt in b:
		c = t / bt
		sum = sum + c

	return sum

def main():
	bl = [4, 2, 1]
	t = 4

	print found(8, bl, 3)
	print count_completed_cuts(bl, t)
	print count_available_bar(bl, t)
#	print count_completed_cuts([4, 2, 1], )

if __name__=='__main__':
	main()