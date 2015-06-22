import sys
import time

def paint(T, lf):
	C = []
	p = lf
	
	while p != 0:
		C.append(p)
		p = T[p]

	C.sort()

	return C

def search(T, q1, q2):
	t = q1

	while t != 0:
		if T[t] == q2:
			return 1
		t = T[t]

	return 0

def color(C, q1, q2):
	for c in C:
		if (q1 in c) and (q2 in c):
			return 1

	return 0

def solve(N, L, Q):
	T = [0 for x in xrange(0, N+1)]
	LF = [1 for x in xrange(0, N+1)]

	for lk in L:
		T[lk[1]] = lk[0]
		LF[lk[0]] = 0

	C = []
	for i in xrange(1, N+1):
		if LF[i] == 1:
			C.append(paint(T, i))

	for q in Q:
		same = color(C, q[0], q[1])
		if same == 1:
			print 1
		else:
			print 0
					
def solve_f(N, L, Q):
	T = [0 for x in xrange(0, N+1)]

	for lk in L:
		T[lk[1]] = lk[0]

	for q in Q:
		r = search(T, q[0], q[1])
		if r == 1: 
			print '1'
		else:
			print search(T, q[1], q[0])


def unit1():
	N = 8
	M = 2
	L = [(1,2), (2,4), (2,5), (1,3), (3,6), (3,7), (3,8)]
	Q = [(1,5), (4,7)]

	return N,M,L,Q

def unit2():
	N = 5
	M = 2
	L = [(1,2), (1,3), (3,4), (3,5)]
	Q = [(2,3), (3,5)]

	return N,M,L,Q

def unit3():
	N = 10
	M = 3
	L = [(9,4), (9,10), (10,3), (8,10), (1,3), (6,8), (5,6), (6,2), (2,7)]	
	Q = [(7,3), (10,1), (6,10)]

	return N,M,L,Q

def unit():
	N,M,L,Q = unit1()
	solve(N, L, Q)

def main():

	ts1 = time.time()
	iters = sys.stdin.readline().strip()
	for i in range(int(iters)):
		N, M = sys.stdin.readline().strip().split()
		N = int(N)
		L = []
		for j in range(int(N)-1):
			a, b = sys.stdin.readline().strip().split()
			L.append((int(a),int(b)))		
		Q = []
		for j in range(int(M)):
			a, b = sys.stdin.readline().strip().split()
			Q.append((int(a), int(b)))

		solve_f(N, L, Q)
	
	print "time: ", time.time() - ts1

if __name__ == '__main__':
	main()