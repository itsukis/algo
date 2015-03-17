def bitwise(A):
	bitand = 0b1111111111111111
	bitor = 0
	for B in A:
		for j in B:
			bitor = bitor | j
		bitand = bitand & bitor
	return bitand
 
def combination1(A, S, M):
	#print A

	if M == 0:
		print A
		return

	for i in range(1, len(A[S])+1):
		C = []
		for j in range(0, S):
			C.append(A[j])
		C.append(A[S][0:i])
		C.append(A[S][i:])
		combination1(C, S+1, M-1)

def main():
	combination1([[1, 2, 3]], 0, 1)
	combination1([[1, 2, 3]], 0, 2)

if __name__ == "__main__":
	main()