import sys

max_t = 0

def min(a, b):
    if (a < b):
        return a
    else:
        return b

def balancePancake(d, P, t, max_t):
    if (d == 0) or (t > max_t):
        return t

    for p in P:
        for i in range(p, 0, -1):



def unit_test():
    print balancePancake(1, [3], 0, max([3]))
    #print balancePancake(4, [1,2,1,2], 0)

def main():
    unit_test()

if __name__=="__main__":
    main()