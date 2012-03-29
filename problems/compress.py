#A function to compress a string.

def compress(st):
    count , last, new = 1,None, ""
    if len(st) ==1:
        return "%s%s%s" % (new,count,st[0])
    else:
        for i in xrange(1, len(st)):
            if st[i] == st[i-1]:
                count +=1
            else:
                new="%s%s%s" % (new,count,st[i-1])
                count = 1
    return "%s%s%s" % (new, count, st[-1])

if __name__ == '__main__':

    print compress("CCCCBBAF")
    print compress("A")
    print compress("AAAA")
    print compress("AB")