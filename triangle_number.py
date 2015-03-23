import timeit
import math

triangle_list = []

def find_triangle_sum(K):
	for i in triangle_list:
		for j in triangle_list:
			for k in triangle_list:
				if (i + j + k) == K:
					#print i, j, k, ' = ', K
					return True
	return False

def find_triangle(K):
	found = False
	triangle = 0
	for i in range(1, int(math.sqrt(K*2))+1):
		triangle = triangle + i
		#print 'T(', i, ') = ', triangle
		triangle_list.append(triangle)
		#if K == triangle:
		#	return 0

	if find_triangle_sum(K) == True:
		return 1
	else:
		return 0

def main():
	
	#t = timeit.Timer(stmt="find_triangle(10")
	t = timeit.Timer(stmt="find_triangle(1000)", setup="from __main__ import find_triangle")
	print t.timeit(number=2)/2
	#print t.repeat(repeat=10, number=1)

	#print find_triangle(10)
	#print find_triangle(20)
	#print find_triangle(1000)
	#print find_triangle(1000)

if __name__=='__main__':
	main()