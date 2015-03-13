## https://algospot.com/judge/problem/read/STARFORCE

import sys
'''
N = 6
M = 2
A = [8, 7, 4, 12, 2, 1]

N = 3
M = 2
A = [4, 2, 1]
'''

def bitwise_or(A):
	bitwiseOR = 0
	for i in A:
		bitwiseOR = bitwiseOR | i	
	return bitwiseOR

def count_bitwise_or(A):
	bitwiseOR = bitwise_or(A)
	return bitwiseOR.bit_length()

def possible_max_bit(bit, A, M):
	if M == 0:
		return True;

	if (M == 1) and (bitwise_or(A).bit_length() == bit):
		return True

	bitwise = A[0]
	for i in range(0, len(A)-1):
		#print 'bit : ', (bitwise & bitwise_or(A[i+1:])).bit_length()
		if ((bitwise & bitwise_or(A[i+1:])).bit_length() == bit):
			return possible_max_bit(bit, A[i+1:], M-1)
		else:
			bitwise = bitwise | A[i]

	return False

def starforce(A, M):
	max_bit = count_bitwise_or(A)
	#print 'max : ', max_bit

	for i in range(max_bit, 0, -1):
		if possible_max_bit(i, A, M):
			return i
	return 0

def test_main():
	print starforce(A, M)

def main():
	iters = sys.stdin.readline().strip()
	for i in range(0, int(iters)):
		A = []
		N, M = sys.stdin.readline().strip().split()
		
		for j in range(0, int(N)):
			A.append(int(sys.stdin.readline().strip()))
	
		print starforce(A, int(M))

if __name__ == '__main__':
	main()
	