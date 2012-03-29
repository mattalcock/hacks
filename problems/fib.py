#!/ms/dist/python/PROJ/core/2.7.1/bin/python

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