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

def test(P, t):

	if not P:
		return t

	tP = list(P)
	max_t, max_idx = choose_max(P)
	for m in range(int(P[max_idx]/2), -1, -1):
		tP[max_idx] = tP[max_idx] - m
		next_max_t = max(tP)
		if (max_t - next_max_t > 1):
			tP.append(m)
			return test(tP, t+1)
	return test(eat(P), t+1)


def main():
	print test([4], 0)
	print test([3], 0)
	print test([1, 2, 1, 2], 0)

if __name__=='__main__':
	main()