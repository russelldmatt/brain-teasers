from math import factorial

def choose(n, k): return factorial(n)/factorial(k)/factorial(n-k)

def no_correct(n):
    return sum([(-1)**i * choose(n,i) * factorial(n-i) for i in range(n+1)])

def f(n, k):
    """#ways exactly k are in the right place out of n"""
    if n == k: return 1
    left = n - k
    return choose(n, k) * (factorial(left) - sum([f(left, i) for i in range(1,left+1)]))

def g(n, k):
    return choose(n, k) * no_correct(n-k)

N = 10
for i in range(N + 1):
    print "i:", i, "f:", f(N, i), "g:", g(N, i)

print '-------'
print f(6, 0)
print no_correct(6)

