#
# Interesting Substring
#
# Coded by Jiyoung Song
#
# Link : http://codeforces.com/contest/519/problem/D
#

A = {'a' : 1, 
	 'b' : 1,
	 'c' : -1,
	 'x' : 1}

#B = "xabcabccc" # -> 5
#B = "xabcab" # -> 2
B = 'aaa' # -> 2

accMap = {}
# {'a' : [1, 2]}

	
def print_string_value():
	for i in B:
		print i, A[i] 


def find_substring(A, B):
	accValue = 0
	ans = 0

	for i in B:
		if (i, accValue) in accMap:
			ans = ans + accMap[(i, accValue)]
		
		accValue = accValue + A[i]		
		if (i, accValue) in accMap:
			accMap[(i, accValue)] = accMap[(i, accValue)] + 1
		else:
			accMap[(i, accValue)] = 1

		print accMap, accValue

	print ans

def main():
	print_string_value()
	find_substring(A, B)

if __name__ == '__main__':
	main()

