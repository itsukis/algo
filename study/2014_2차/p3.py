import sys

Pm = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def init(N, M):
	A = [[] for x in range(N+1)]
	for i, j in M:
		A[j].append(i)

	return A

def solve(N, M, K, L):
	idx = 0
	
	R = [[0 for x in range(N+1)] for x in range(2)]
	P = [[] for x in range(2)]
	P[0] = [1]
	
	A = init(N, M)
	#print A
	
	for lvl in range(1, L+1):
		nidx = (idx + 1) % 2
		print "size p ", len(P[idx])
		for p in P[idx]:
			for c in range(len(A[p])):
				P[nidx].append(A[p][c])
				R[0][A[p][c]] = R[0][A[p][c]] + 1
		#print p, " -> ", P[nidx]
		P[idx] = []
		idx = nidx

	Re = []
	for i in range(0, K):
		Re.append(R[0][i+2]%Pm[i])

	return Re
	#print "Result : ", R[0][1:]

def unit():
	N = 3
	M = [(2,3), (2,3), (3,1), (3,1), (3,1)]
	K = 2
	L = 2
	solve(N, M, K, L)

def main():
	iters = sys.stdin.readline().strip()
	for i in range(0, int(iters)):
		N, M, K, L = sys.stdin.readline().strip().split()
		LKM = []
		for j in range(int(M)):
			a, b = sys.stdin.readline().strip().split()
			LKM.append((int(a),int(b)))		
		#print LKM
		result = solve(int(N), LKM, int(K), int(L))
		for r in result:
			print r,
		print

if __name__ == '__main__':
	main()