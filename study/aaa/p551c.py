import sys

def unit_test(ans, result):
	if ans == result:
		return True
	else:
		return False

def binsearch(N, M, A):
	min = 2
	max = sum(A) + N + 1
	last = 0
	n = findEnd(N, A) + 1
	while min <= max:
		mid = (min + max) / 2
		p = possible(n, M, A[0:n], mid)
		#print min, mid, max, p
		if p == True:
			last = mid
			max = mid - 1
		else:
			min = mid + 1

	return last

def empty(N, A, l):
	if (N-1 == l) and (A[l] == 0):
		return True
	else:
		return False

def nextA(N, A, t, l):
	for i in xrange(l, N):
		if t == 0:
			return A, i
		t = t - 1
		if t >= A[i]:
			t = t - A[i]
			A[i] = 0
		else:
			A[i] = A[i] - t
			return A, i
	return A, i

def findEnd(N, P):
	for i in xrange(N-1, -1, -1):
		if P[i] != 0:
			return i
	return 0

def possible(N, M, P, T):
	A = list(P)
	t = T
	s = 0
	for i in xrange(M):
		A, s = nextA(N, A, t-s, s)
		if empty(N, A, s):
			return True
	return False
		
def test():
	C1 = [2,1,[1,1],4]
	C2 = [3,2,[1,0,2],5]
	C3 = [4,100,[3,4,5,4],5]

	print binsearch(C1[0], C1[1], C1[2])
	print binsearch(C2[0], C2[1], C2[2])
	print binsearch(C3[0], C3[1], C3[2])

	#print possible(C1[0], C1[1], C1[2], 4)
	#print possible(C2[0], C2[1], C2[2], 6)
	#print possible(C3[0], C3[1], C3[2], 6)

def unit():
	C1 = [2,1,[1,1],4]
	C2 = [3,2,[1,0,2],5]
	C3 = [4,100,[3,4,5,4],5]
	
	print unit_test(C1[3], solve(C1[0], C1[1], C1[2]))
	print unit_test(C2[3], solve(C2[0], C2[1], C2[2]))
	print unit_test(C3[3], solve(C3[0], C3[1], C3[2]))

def main():

	N, M = sys.stdin.readline().strip().split()
	P = [int(x) for x in sys.stdin.readline().strip().split()]
	#t = time.time()
	print binsearch(int(N), int(M), P)
	#print "elapsed time = ", time.time() - t

if __name__ == '__main__':
	main()