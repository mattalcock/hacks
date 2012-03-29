#!/ms/dist/python/PROJ/core/2.7.1/bin/python
from collections import defaultdict
from operator import itemgetter

#-------Basic Bits-------#

def reverseStr(str):
    return str[::-1]

def func(s):
	print s

#-------Functional Bits-------#
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib = Memoize(fib)

if __name__ == '__main__':
    
    func("Hello World")
    print reverseStr("Hello World")
    
    print fib(6)
    print fib(2)
    print fib(0)
    print fib(1)
    print fib(40)
    
    counter = defaultdict(int)
    for i in xrange(100):
        r = (i + i*10) % 3
        counter[r]+=1
        
    print "Done"
    
    for k,v in counter.iteritems():
        print "key: %s, value:%s" % (k,v)
    print "Done"
        
    for k,v in sorted(counter.iteritems(), key=itemgetter(1), reverse=False):
        print "key: %s, value:%s" % (k,v)

