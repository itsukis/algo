import sys

def bitwise_or(A):
	print A
	bitwiseOR = 0
	for i in A:
		bitwiseOR = bitwiseOR | i	
	return bitwiseOR

def count_setbit(A):
	bitwiseOR = bitwise_or(A)
	return bin(bitwiseOR).count("1")


def find_max_setbit(A, M):

	max_setbits = 0
	max_bits_count = 0

	print A, M
	if M == 0:
		return bitwise_or(A)

	for i in range(1, len(A)-(M-1)):
		setbits = bitwise_or(A[0:i]) & find_max_setbit(A[i:], M-1)
		setbit_count = bin(setbits).count("1")
		if setbit_count >= max_bits_count:
			max_bits_count = setbit_count
			max_setbits = setbits

	return max_setbits

def starforce(A, M):	
	print count_setbit(find_max_setbit(A, M))


def test_main():
	S = '=========================\n'
	#print S, starforce([9, 12, 6, 3], 2)
	print S, starforce([15, 14, 13, 12], 3)
	#print S, starforce([8, 7, 4, 12 ,2, 1], 3)
	#print S, starforce([4, 2, 1], 2)
	#print S, starforce([255, 8, 7, 4, 1], 2)
	#print S, starforce([65535, 255], 1)
	#print S, starforce([1, 0, 12, 15, 3, 19], 2)

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