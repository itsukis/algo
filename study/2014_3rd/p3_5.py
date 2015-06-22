import sys
import time

Pm = [1, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
PmProd = 1

def solve_fast(N, M, K, L):
	global PmProd

	D1 = [0 for x in xrange(0, N+1)]
	D2 = [0 for x in xrange(0, N+1)]
	R = [0 for x in xrange(0, K+2)]
	
	denom = PmProd

	for m in M:
		if m[1] == 1:
			D1[m[0]] = D1[m[0]] + 1
	for k in xrange(2, K+2):
		R[k] = D1[k]

	for l in xrange(1, L):
		for n in xrange(1, N+1):
			D2[n] = 0

		for m in M:
			D2[m[0]] = D2[m[0]] + D1[m[1]]

#		for n in xrange(1, N+1):
#			D2[n] = D2[n] % denom

		for k in xrange(2, K+2):
			R[k] = (R[k] + D2[k]) % Pm[k]

		#print 'L = ', l, ' R = ',  R	

		Dt = D1
		D1 = D2
		D2 = Dt

	return R[2:]

def init():
	global PmProd
	for p in Pm:
		PmProd = PmProd * p

def main():
	t1 = time.time()
	init()
	iters = sys.stdin.readline().strip()
	for i in range(int(iters)):
		sys.stderr.write("Solving test case #" + str(i) + "...\n")
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
	print "elapsed time : ", time.time()-t1

if __name__ == '__main__':
	main()
