import sys

def unit_test(ans, result):
	if ans == result:
		return True
	else:
		return False

def nextA(A, T):
	for i in xrange(len(A)):
		T = T - 1
		if T >= A[i]:
			A[i] = 0
			T = T - A[i]
		else:
			A[i] = A[i] - T
			return A
	return A

def possible(N, M, A, T):
	return
		

def solve(N, M, P):
	i = 0
	t = 1

	while i < N-1 :
		if P[i] <= M:
			P[i+1] = P[i+1] + P[i]
			P[i] = 0
			i = i + 1
		else:
			P[i] = P[i] - M
			P[i+1] = P[i+1] + M 

		t = t + 1
		#print P, t

	if P[N-1] % M == 0:
		t = P[N-1] / M + t
	else:
		t = P[N-1] / M + 1 + t
	
#	print t

	return t

def test():
	A = nextA([1,1], 3)
	print A

def unit():
	C1 = [2,1,[1,1],4]
	C2 = [3,2,[1,0,2],5]
	C3 = [4,100,[3,4,5,4],5]
	
	print unit_test(C1[3], solve(C1[0], C1[1], C1[2]))
	print unit_test(C2[3], solve(C2[0], C2[1], C2[2]))
	print unit_test(C3[3], solve(C3[0], C3[1], C3[2]))

def main():

	test()
	return

	N, M = sys.stdin.readline().strip().split()
	P = [int(x) for x in sys.stdin.readline().strip().split()]

	print solve(int(N), int(M), P)

if __name__ == '__main__':
	main()