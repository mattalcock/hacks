def subsetm(S, x, mem={}):
    k = (str(S), x)
    if k not in mem:
        if len(S)==1:
            return x==S[0]
        L, R = S[0], S[1:]
        mem[k] = x==L or (subsetm(R, x - L) or subsetm(R, x))
    return mem

def subsetf(S, x, C):
    if len(S)==1:
        if x==S[0]:
            C.append(x)
            return C
        else:
            return []
    L, R = S[0], S[1:]
    if x==L:
        C.append(L)
        return C
    elif subsetf(R, x - L, C):
        C.append(L)
        return C
    elif subsetf(R, x, C):
        return C
    else:
        return []

def subset(S, x):
    if len(S)==1:
        return x==S[0]
    L, R = S[0], S[1:]
    return x==L or subset(R, x - L) or subset(R, x)

def pos_neg_sum(S):
    P, N = 0, 0
    for e in S:
        if e >= 0:
            P += e
        else:
            N += e
    return P, N

def subset_sum(S, x=0):
    P, N = pos_neg_sum(S)
    if not S or x < N or x > P:
        return False
    n, m = len(S), P - N + 1
    table = [[False] * m for v in xrange(n)]
    table[0][S[0]] = True
    for i in xrange(1, n):
        for j in xrange(N, P+1):
            table[i][j] = S[i] == j or table[i-1][j] or table[i-1][j-S[i]]
    print "Table is %s" % table
    return table[n-1][x]


if __name__ == '__main__':
    R = [1,3,-4,9]
    #print R[:3]

    print  subset(R, 0)
    print  subset(R, 1)
    print  subset(R, 4)
    print  subset(R, -1)
    print  subset(R, 25)
    print  subset(R, -3)
    print  subset(R, -6)
    print  subset(R, 13)

    print "Trying to find"

    print  subsetf(R, 0, [])
    print  subsetf(R, 1, [])
    print  subsetf(R, 4, [])
    print  subsetf(R, -1, [])
    print  subsetf(R, 25, [])
    print  subsetf(R, -3, [])
    print  subsetf(R, -6, [])
    print  subsetf(R, 13, [])
    print  subsetf(R, 5, [])

    R = [3,-4,9, 45, 900, 30, 27, 45]
    print  subsetf(R, 0, [])
    print  subsetf(R, 1, [])
    print  subsetf(R, 4, [])
    print  subsetf(R, -1, [])
    print  subsetf(R, 25, [])
    print  subsetf(R, -3, [])
    print  subsetf(R, -6, [])
    print  subsetf(R, 13, [])
    print  subsetf(R, 5, [])

    print  subsetf(R, 33, [])

    #print "With a memory check"

    #print subsetm(R, 0)
    #print subsetm(R, 1)
    #print subsetm(R, 4)
    #print subsetm(R, -1)
    #print subsetm(R, 25)
    #print subsetm(R, -3)
    #print subsetm(R, -6)

    #print "Dynamic progamming style"

    #print subset_sum(R, 0)
    #print subset_sum(R, 1)
    #print subset_sum(R, 4)
    #print subset_sum(R, -1)
    #print subset_sum(R, 25)
    #print subset_sum(R, -3)
    #print subset_sum(R, -6)
    #print subset_sum(R, -2)