import sys
import time

Pm = [1, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def init(N, M):
	A = [[] for x in range(N+1)]
	for i, j in M:
		A[j].append(i)

	return A

def solve_fast(N, M, K, L):
	i_1 = 0
	i_2 = 1

	D = [[[0 for x in range(0, N+1)] for x in range(0, K+2)] for x in range(2)] 
	R = [0 for x in range(0, K+2)]

	for i in range(0, K+2):
		D[i_1][i][i] = 1

	for l in range(L):
		for k in range(1, K+2):
			for n in range(1, N+1):
				D[i_2][k][n] = 0

		for k in range(1, K+2):
			for m in M:
				D[i_2][k][m[1]] = (D[i_2][k][m[1]] + D[i_1][k][m[0]]) % Pm[k]
				#print k, " -> ", m[1], " : ", D[i_2][k][m[1]]

		for k in range(2, K+2):
			R[k] = (R[k] + D[i_2][k][1]) % Pm[k]

		#print 'L = ', l, ' R = ',  R	

		i_1 = i_2
		i_2 = (i_1 + 1) % 2

	return R[2:]

def solve_slow(N, M, K, L):
	idx = 0
	
	R = [0 for x in range(N+1)]
	P = [[] for x in range(2)]
	P[0] = [1]
	
	A = init(N, M)
	#print A
	
	for lvl in range(1, L+1):
		nidx = (idx + 1) % 2
		#print "size p ", len(P[idx])
		for p in P[idx]:
			for c in range(len(A[p])):
				P[nidx].append(A[p][c])
				R[A[p][c]] = R[A[p][c]] + 1
		#print p, " -> ", P[nidx]
		P[idx] = []
		idx = nidx

	return [R[k] % Pm[k] for k in range(2, K+2)]
	#print "Result : ", R[0][1:]

def unit():
	N = 3
	M = [(2,3), (2,3), (3,1), (3,1), (3,1)]
	K = 2
	L = 2
	print solve_slow(N, M, K, L)

def main():
	iters = sys.stdin.readline().strip()
	ts1 = time.time()
	for i in range(int(iters)):
		N, M, K, L = sys.stdin.readline().strip().split()
		LKM = []
		for j in range(int(M)):
			a, b = sys.stdin.readline().strip().split()
			LKM.append((int(a),int(b)))		
		#print LKM
		result = solve_fast(int(N), LKM, int(K), int(L))
		for r in result:
			print r,
		print
	print "time: ", time.time() - ts1

if __name__ == '__main__':
	main()