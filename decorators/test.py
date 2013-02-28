from mem import memoize, Memoize
from timeit import timeit

#Only included here for demorstration purposes.
def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


if __name__ == '__main__':

    r = fib(5)
    print r

    Fib = Memoize(fib)
    r = Fib(5)
    print r

    r = fib(12)
    print r

    mfib = memoize(fib)
    r = mfib(12)
    print r

    timedfib = timeit(fib)
    r = timedfib(35)
    print r

    fib = memoize(fib)
    timedfib = timeit(fib)
    r = timedfib(35)
    print r