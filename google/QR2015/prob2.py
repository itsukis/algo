import sys

def empty(P):
    for p in P:
        if p != 0:
            return False
    return True

def min(a, b):
    if (a < b):
        return a
    else:
        return b

def balancePancake(P, t, max_t):
    if empty(P) or (t > max_t):
        return t

    for i in range(0, len(P)):
        for j in range(p, 0, -1):
            balancePancake()    



def unit_test():
    print balancePancake(1, [3], 0, max([3]))
    #print balancePancake(4, [1,2,1,2], 0)

def main():
    unit_test()

if __name__=="__main__":
    main()