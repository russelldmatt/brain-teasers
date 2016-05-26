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

def ev(N, M):
    return sum([i * choose(M, i) * f(N, i) for i in xrange(1, M+1)]) / float(M**N)

def fast(N, M):
    return M * (1 - ((M-1) / float(M))**N)

def compare(N, M):
    print (N, M)
    print "slow: {}".format(ev(N, M))
    print "fast: {}".format(fast(N, M))

compare(2,2)
compare(2,3)
compare (20, 1000)

@memoize
def fact(x):
    print "computing fact for %d" % x
    if x == 0:
        return 1
    else: 
        return x * fact(x-1)

fact(6)
fact(3)




    
    
