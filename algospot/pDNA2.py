import sys
import itertools

# case 0 -> fail
# case 1 -> ab  ~ cba
# case 2 -> abc ~ ba
def has_min_common_str(A, B):
	if len(A) <= len(B):
		rA = ''.join(reversed(A))
		if A == B[-len(A):]:
			return 1
		elif B[:len(A)] == A:
			return 2
		else:
			return 0

def main():
	print has_min_common_str("ab", "cba")
	print has_min_common_str("abc", "ba")

if __name__=='__main__'
	main()