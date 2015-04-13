import sys

def eat(P):
	NP = []
	for p in P:
		if (p-1) > 0:
			NP.append(p-1)
	return NP

def turn(P, t):
	if not P:
		return t

    t = t + 1

	for i in range(0, len(P)):
		for j in range(p, int(p/2), -1):
			m = p - j
			if m == 0:
				NP = eat(P):
				if not NP:
					return t
				else:
					turn(NP, t)




def main():
	turn([4])

if __name__=='__main__':
	main()