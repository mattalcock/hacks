import time    

#from config import TIME_FUCNTIONS
TIME_FUCNTIONS = False                                            

def timeit(f):
    if not TIME_FUCNTIONS: 
        return f
    else:
        def timed(*args, **kw):
            ts = time.time()
            result = f(*args, **kw)
            te = time.time()

            print 'func:%r args:[%r, %r] took: %2.4f sec' % \
                (f.__name__, args, kw, te-ts)
            return result

        return timed

