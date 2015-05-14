# https://code.google.com/codejam/contest/4224486/dashboard#s=p1

import sys

def binary_search(N, b):
	first = 0
	last = min(b) * N
	found = (False, 0, [])

	while first <= last and not found[0]:
		midpoint = (first + last) / 2

		found = find(N, b, midpoint)

		print "->", first, la
		print "-->", midpoint, found

		if found[0] == True:
			i = N - found[1] - 1
			return found[2][i] + 1
		else:
			if N <= found[1]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return -1			

def find(N, b, t):
	cpl = count_completed_cuts(b, t)
	avb, avbl = count_available_bar(b, t)

	#print cpl, avb, avbl

	if N > cpl and N <= cpl + avb:
		return True, cpl, avbl
	else: 
		return False, cpl, []

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

def unit_test():
	#print binary_search(4, [10, 5])
	#print count_available_bar([2, 2, 2], 0)
	print binary_search(3, [2, 2, 2])
	#print binary_search(8, [4, 2, 1])

def input():
	N = int(sys.stdin.readline().strip().split()[1])
	B = [int(i) for i in sys.stdin.readline().strip().split()]

	return N, B

def solve():
    iters = sys.stdin.readline().strip()
    for i in range(0, int(iters)):
    	N, B = input()
    	r = binary_search(N, B)
    	print("Case #%d:" % (i+1)), r	

def main():
	unit_test()
	#solve()

if __name__=='__main__':
	main()