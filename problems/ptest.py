from collections import defaultdict

def amplitude ( A ):
    max, min = A[0],A[0]
    for a in A:
        if a >max:
            max=a
        if a <min:
            min=a
    return max-min

def nesting ( S ):
    left,right = 0,0
    for s in S:
        if s =='(':
            left+=1
        elif s==')':
            right+=1
    if left==right:
        return 1
    else:
        return 0

def isAnagramOfPalindrome(S):
    counter = defaultdict(int)
    for s in S:
        counter[s]+=1
    even = 0
    for k, v in counter.iteritems():
        if v%2==0:
            even+=1
    if len(counter)==even:
        return 1
    else:
        return 0

def equi(A):
    l = len(A)
    for i in xrange(1, l+1):
        if sum(A[:i])==sum(A[i+1:l]) and i<l:
            return i
    return -1
    
def maxProfit ( A ):
    maxp = 0
    l = len(A)
    for i in xrange(l):
        for j in xrange(i,l):
             if A[j] - A[i] > maxp:
                 #profits = (i, j)
                 maxp = A[j] - A[i]
    return maxp


#from collections import defaultdict
#from operator import itemgetter

def arrLeader ( A ):
    counter = defaultdict(int)
    for a in A:
        counter[a]+=1
        
    s = sorted(counter.iteritems(), key=itemgetter(1), reverse=True)
    leader, count = s[0]
    
    if  count > (len(A))/2:
        return leader
    else:
        return -1

if __name__ == '__main__':
    
    print amplitude([45,78,3,12])
    print nesting("(()(( ))())")
    print isAnagramOfPalindrome("dooernedeevrvn")
    print isAnagramOfPalindrome("octobersky")
    print equi([-7,1,5,2,-4,3,0])
    print maxProfit([23171,21011,21123,21366,21013,21367])
    
    listOne = [4,2,2,3,2,4,2,2,6,4]
    listTwo = [100,50,1,1,1]
    print arrLeader(listOne)
    print arrLeader(listTwo)
    
    