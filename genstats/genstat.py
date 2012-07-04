    import random
    from math import sqrt
    from collections import namedtuple

    def stat(gen):
        """Returns the namedtuple Stat as below."""
        Stat = namedtuple('Stat', 'total, sum, avg, sd, max, min')
        it = iter(gen)

        x0 = next(it)
        mx = mn = s = x0
        s2 = x0*x0
        n = 1

        for x in it:
            mx = max(mx, x)
            mn = min(mn, x)
            s += x
            s2 += x*x
            n += 1

        return Stat(n, s, s/n, sqrt(s2/n - s*s/n/n), mx, mn)

    def random_int_list(size=100, start=0, end=1000):
        return (random.randrange(start,end,1) for x in xrange(size))
        
    if __name__ == '__main__':
        r = stat(random_int_list())
        print r  #Stat(total=100, sum=56295, avg=562, sd=294.82537204250247, max=994, min=10)


