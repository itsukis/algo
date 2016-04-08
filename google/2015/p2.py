import sys

def choose_max(P):
	maxP = max(P)
	return maxP, P.index(maxP)

def eat(P):
	NP = []
	for p in P:
		if (p-1) > 0:
			NP.append(p-1)
	return NP

def cakebalance(P, t, maxT):
	if (not P) or t >= maxT:
		return t

	max_t, max_idx = choose_max(P)
	min_t = []
	for m in range(int(P[max_idx]/2), -1, -1):
		tP = list(P)
		if m != 0:
			tP[max_idx] = P[max_idx] - m
			tP.append(m)		
			min_t.append(cakebalance(tP, t+1, maxT))
		else:
			min_t.append(cakebalance(eat(P), t+1, maxT))

	return min(min_t)

def unitTest():
	print cakebalance([6, 6], 0, max([6, 6]))
	print cakebalance([4], 0, max([4]))
	print cakebalance([3], 0,  max([3]))
	print cakebalance([1, 2, 1, 2], 0, max([1, 2, 1, 2]))

def main():
	result = []
	iters = sys.stdin.readline().strip()
	for i in range(0, int(iters)):
		P = []
		N = sys.stdin.readline().strip()
		S = sys.stdin.readline().strip().split()
		for s in S:
			P.append(int(s))
		result.append(cakebalance(P, 0, max(P)))
	for i in range(0, len(result)):
		print("Case #%d:" % (i+1)), result[i]

if __name__=='__main__':
	#unitTest()
	main()