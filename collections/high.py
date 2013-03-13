def highest(L, n):
    return sorted(enumerate(L), reverse=True, key=lambda x: x[1])[:n]

if __name__ == '__main__':
    
    M = [102, 56, 2355, 3, 25, 78, 19, 25, 1002, -54, 0, 23, -1]
    r = highest(M,5)
    print r