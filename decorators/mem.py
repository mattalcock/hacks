
def memoize(f):
    cache= {}
    def memf(*args, **kw):
        key = (args, tuple(sorted(kw.items())))
        if key not in cache:
            cache[key] = f(*args, **kw)
        return cache[key]
    return memf

class Memoize:

    def __init__(self, f):
        self.f = f
        self.cache = {}

    def __call__(self, *args, **kw):
        key = key = (args, tuple(sorted(kw.items())))
        if not key in self.cache:
            self.cache[key] = self.f(*args, **kw)
        return self.cache[key]
