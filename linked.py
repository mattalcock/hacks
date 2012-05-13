from collections import defaultdict

def amplitude ( A ):
    max, min = A[0],A[0]
    for a in A:
        if a >max:
            max=a
        if a <min:
            min=a
    return max-min

if __name__ == '__main__':
    
    print amplitude([45,78,3,12])