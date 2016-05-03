from math import factorial

def g(N, k): return k**N

def choose(n, k): return factorial(n) / (factorial(n-k) * factorial(k))
def P(n, k): return factorial(n) / factorial(n-k)

def f(N, k):
    if k == 1: return 1
#    return (g(N, k) - sum([choose(k, i) * f(N, i) * factorial(i) for i in range(1, k)])) / factorial(k)
    return (g(N, k) - sum([P(k, i) * f(N, i) for i in range(1, k)])) / factorial(k)

for N in range(1, 11):
    for k in range(1, N+1):
        print f(N, k),
    print ""
    for k in range(1, N+1):
        print f(N, k) * factorial(k),
    print ""
    print sum([f(N, k) * factorial(k) * choose(N, k) for k in range(1, N+1)])
    print "#ways for N of {} = {}".format(N, sum([f(N, k) for k in range(1, N+1)]))
    print ""
    
        
        
