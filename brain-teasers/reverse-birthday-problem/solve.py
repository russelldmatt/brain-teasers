import math
from memoize import memoize

@memoize
def factorial(n):
    return math.factorial(n)

@memoize
def choose(n, k):
    return factorial(n)/factorial(k)/factorial(n-k)

@memoize
def f(n, k):
    return k**n - sum([choose(k,i) * f(n, i) for i in xrange(1, k)])

def enough(N): return f(N, 365) > 365**N / 2

def tighten(too_low, too_high):
    if too_high - too_low == 1:
        return (too_low, too_high)
    else:
        mid = (too_low + too_high) / 2
        print "trying ", mid
        if enough(mid):
            return tighten(too_low, mid)
        else:
            return tighten(mid, too_high)

print tighten(1,10000)
