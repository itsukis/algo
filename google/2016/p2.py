import sys

def reverse(P):
    for i in range(0, len(P)):
        if P[i] == '+':
            P = P[:i] + '-' + P[i+1:]
        else:
            P = P[:i] + '+' + P[i+1:]
    return P

def flipCake(i, P):
    tP = P[0:i+1]
    tP = reverse(tP[::-1])
    tP = tP + P[i+1:]
    return tP

def solve(P, m):
    result = 0
    if ('-' in P) == False:
        return 0

    tP = '+' * len(P)
    for i in range(0, len(tP)):
        ttP = flipCake(0, tP)



    return len(P)

def main():
    result = []
    T = sys.stdin.readline().strip()
    for i in range(0, int(T)):
        P = sys.stdin.readline().strip().split()
        result.append(solve(str(P[0], 0)))

    for i in range(0, len(result)):
        print("Case #%d:" % (i+1)), result[i]

if __name__=="__main__":
    main()
