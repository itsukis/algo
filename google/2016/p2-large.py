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

def solve(P):
    tP = P
    mLast = 0
    for i in range(len(P)-1, -1, -1):
        if P[i] == '-':
            mLast = i
            if P[0] == '-':
                tP = flipCake(i, P)
                return 1 + solve(tP)

    if mLast != 0:
        tp = flipCake(mLast-1, P)
        return 1 + solve(tp)

    return 0


def main():
    result = []
    T = sys.stdin.readline().strip()
    for i in range(0, int(T)):
        P = sys.stdin.readline().strip().split()
        result.append(solve(str(P[0])))

    for i in range(0, len(result)):
        print("Case #%d:" % (i+1)), result[i]

if __name__=="__main__":
    main()