import sys
import itertools

def is_pdna(S):
	if len(S) % 2 == 0:
		N = len(S)/2
	else:
		N = (len(S)-1)/2

	for i in range(0, N):
		if S[i] != S[-(i+1)]:
			return False

	return True

def permutate_dna(A):
	N = len(A)
	perm_list = list(itertools.permutations(range(N), N))
	perm_set = set()
	
	for perm in perm_list:
		dna = ''
		for idx in perm:
			dna = dna + A[idx]
		if is_pdna(dna):
			perm_set.add(dna)
	return sorted(list(perm_set))[0]

def test():
	print permutate_dna(["aa", "att", "aaa"])
	print permutate_dna(["ac", "tgt", "ac", "caca"])

def _main():
	iters = sys.stdin.readline().strip()
	for i in range(0, int(iters)):
		A = []
		S = sys.stdin.readline().strip().split()
		
		for j in range(1, int(S[0])+1):
			A.append(S[j])
		
		print permutate_dna(A)
	
def main():
	_main()

if __name__=="__main__":
	main()