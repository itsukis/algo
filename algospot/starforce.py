## https://algospot.com/judge/problem/read/STARFORCE

import sys

def bitwise_or(A):
	bitwiseOR = 0
	for i in A:
		bitwiseOR = bitwiseOR | i	
	return bitwiseOR

def count_setbit(A):
	bitwiseOR = bitwise_or(A)
	return bin(bitwiseOR).count("1")

def find_max_setbit(bit, A, M):

	if M == 0:
		return True

	bitwise = A[0]
	for i in range(0, len(A)-1):
		if (bin(bitwise & bitwise_or(A[i+1:])).count("1") == bit):
			print A[0:i+1], '|', A[i+1:]
			return find_max_setbit(bit, A[i+1:], M-1)
		else:
			bitwise = bitwise | A[i+1]

	if (M == 1) and (bin(bitwise_or(A)).count("1") == bit):
		print A, '|'
		return True	

	return False	

def starforce(A, M):
	
	print_binary(A)

	max_bit = count_setbit(A)
	print 'max : ', max_bit

	for i in range(max_bit, 0, -1):
		print '->', i
		if find_max_setbit(i, A, M):
			return i
	return 0

def print_binary(A):
	for i in A:
		print i, bin(i)

def test_main():
	S = '=========================\n'
	print S, starforce([8, 7, 4, 12 ,2, 1], 3)
	print S, starforce([4, 2, 1], 2)
	print S, starforce([255, 8, 7, 4, 1], 2)
	print S, starforce([65535, 255], 1)
	print S, starforce([1, 0, 12, 15, 3, 19], 2)

def main():
	iters = sys.stdin.readline().strip()
	for i in range(0, int(iters)):
		A = []
		N, M = sys.stdin.readline().strip().split()
		
		for j in range(0, int(N)):
			A.append(int(sys.stdin.readline().strip()))
	
		print starforce(A, int(M))

if __name__ == '__main__':
	test_main()