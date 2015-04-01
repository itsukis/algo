import sys
import itertools

def xor_combin(A):
	n = len(A)

	if n == 1:
		return True
	elif n == 2:
		if (A[0] ^ A[1]) == 0:
			return False
		else:
			return True
	else:
		for c in itertools.combinations(range(0, n), 3):
			list_c = list(c)
			if A[list_c[0]] ^ A[list_c[1]] ^ A[list_c[2]] == 0:
				#print A[list_c[0]], A[list_c[1]], A[list_c[2]]
				return False
		return True

def check_combin(N):
	for l in range(N, 0, -1):
		for c in itertools.combinations(range(1, N+1), l):
			list_c = list(c)
			if xor_combin(list_c) == False:
				continue
			else:
				return list_c

	return []

def xor_series(N):
	for n in range(2, N+1):
		r,c = check_combin(n)
		if r == True:
			print c

def test_main():
	out = check_combin(5)
	print out

if __name__=='__main__':
	ins = []
	out = []
	rl = lambda: sys.stdin.readline().strip()
	t = int(rl())
	for i in xrange(t):
		ins.append(int(rl()))
	for i in ins:
		out = check_combin(i)
		print len(out)
		print ' '.join(str(e) for e in out)