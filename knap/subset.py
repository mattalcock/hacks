#Returns the True/False if there is at least one subset of the list S that sums to x
def subsetsum(S, x):
    if len(S)==1:
        return x==S[0]
    L, R = S[0], S[1:]
    return x==L or subset(R, x - L) or subset(R, x)

#A modification of the above with some memory storage. Not sure how usefull this is.
#!!Marked For Delete!!
def subsetm(S, x, mem={}):
    k = (str(S), x)
    if k not in mem:
        if len(S)==1:
            return x==S[0]
        L, R = S[0], S[1:]
        mem[k] = x==L or (subsetm(R, x - L) or subsetm(R, x))
    return mem

#Returns the values that sum to x in the list S. 
#Becuase of the functional nature of this C must be passed in. (Unsure why can't be defaulted)
def subsetsum_find(S, x, C):
    if len(S)==1:
        if x==S[0]:
            C.append(x)
            return C
        else:
            return []
    L, R = S[0], S[1:]
    if x==L or subsetsum_find(R, x - L, C):
        C.append(L)
        return C
    elif subsetsum_find(R, x, C):
        return C
    else:
        return []

#Returns the locations of the values that sum to x in the list S.
def subsetsum_loc(S, x, C, i):
    if len(S)==1:
        if x==S[0]:
            C.append(i)
            return C
        else:
            return []
    L, R = S[0], S[1:]
    if x==L or subsetsum_loc(R, x - L, C, i+1):
        C.append(i)
        return C
    elif subsetsum_loc(R, x, C, i+1):
        return C
    else:
        return []

#Returns the True/False if there is at least one subset of the list S that sums to x
def subsetsum(S, x):
    if len(S)==1:
        return x==S[0]
    L, R = S[0], S[1:]
    return x==L or subsetsum(R, x - L) or subsetsum(R, x)

#Returns a tubel of positive and negative values for the list S.
def pos_neg_sum(S):
    P, N = 0, 0
    for e in S:
        if e >= 0:
            P += e
        else:
            N += e
    return P, N

#Generator version of the above but might be slower on large sets due to the double interation
#Interesting comparison with the above. In a dynamic lange is iteration through a generator faster than variable assignment and lookup
#Future comparison is to check the relative speed over these over varrying sizes.

def pos_neg_gen(S):
    P = sum(e for e in S if e>=0)
    return P, sum(S) - P


#An alternative method to find id there is a subset of list S that sums to x.
#I need to speed test this vs the above
#My guess is this is very memory ineffeictint if there is lots of values in S
#Or S containts a spare set of information with large vlaues. E.g [7, 9, 5000]

#I need to expalin why this is a dynamic programming example.

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



#Covert these into tests!

if __name__ == '__main__':
    R = [1,3,-4,9]
    #print R[:3]

    print pos_neg_gen(R)
    print pos_neg_sum(R)

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

    print "With a location check"

    R = [1,3,-9,9]

    print  subsetl(R, 0, [], 0)
    print  subsetl(R, 1, [], 0)
    print  subsetl(R, 4, [], 0)
    print  subsetl(R, -1, [], 0)
    print  subsetl(R, 25, [], 0)
    print  subsetl(R, -3, [], 0)
    print  subsetl(R, -6, [], 0)
    print  subsetl(R, 13, [], 0)
    print  subsetl(R, 5, [], 0)

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