# https://code.google.com/codejam/contest/4224486/dashboard#s=p1

import sys

def binary_search(N, b):
	first = 0
	last = min(b) * N
	found = False

	while first <= last and not found:
		
		mid = (first + last) / 2
		ub = count_haircuts(b, mid)
		av, avl = count_available_bar(b, mid)

		if N > ub and N <= (ub + av):
			found = True
		else:
			if N <= ub:
				last = mid - 1
			else:
				first = mid + 1
	
	return avl[N-ub-1]+1			

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

def count_haircuts(b, t):
	sum = 0
	for bt in b:
		c = t / bt
		if t % bt == 0:
			sum = sum + c
		else:
			sum = sum + c + 1

	return sum

def count_completed_cuts(b, t):
	sum = 0
	for bt in b:
		c = t / bt
		sum = sum + c

	return sum

def unit_test():
	print binary_search(4, [10, 5])
	print binary_search(12, [7, 7, 7,])
	print binary_search(8, [4, 2, 1])

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
	#unit_test()
	solve()

if __name__=='__main__':
	main()