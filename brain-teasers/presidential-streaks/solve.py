indent = ""
verbose = False
def trace(func):
    def wrapper(k, h, t):
        global indent
        global verbose
        if verbose:
            print "{}{}({}, {}, {})".format(indent, func.__name__, k, h, t)
        indent += "  "
        ret = func(k, h, t)
        indent = indent[:-2]
        if verbose:
            print "{}{}({}, {}, {}) = {}".format(indent, func.__name__, k, h, t, ret)
        return ret
    return wrapper

##############################################3
from math import factorial
from memoize import memoize

@memoize
def choose(n, k): 
    if k < 0: return 0
    else: return factorial(n)/factorial(k)/factorial(n-k)

@memoize
# the total number of sequences with h heads and t tails
def total(h, t): return choose(h+t, h)

# 3 functions: lt, ge, e
@trace
@memoize
# number of sequences with h heads and t tails that have a longest
# streak < k
def lt(k, h, t): 
    return total(h, t) - ge(k, h, t)

@trace
@memoize
# number of sequences with h heads and t tails that have a longest
# streak <= k.
def lte(k, h, t): return lt(k+1, h, t)

@trace
@memoize
# number of sequences with h heads and t tails that have a longest
# streak < k and the rightmost coin flip is tails.
def lt_cond_right_is_tails(k, h, t): 
    return lt_cond_right_is_heads(k, t, h)

@trace
@memoize
# number of sequences with h heads and t tails that have a longest
# streak < k and the rightmost coin flip is heads.
def lt_cond_right_is_heads(k, h, t): 
    return lt(k, h-1, t) - eq_cond_right_k_heads(k-1, h-1, t)

@trace
@memoize
# number of sequences with h heads and t tails that have a longest
# streak = k and the rightmost k coin flips are tails.
def eq_cond_right_k_tails(k, h, t): 
    return eq_cond_right_k_heads(k, t, h)

@trace
@memoize
# number of sequences with h heads and t tails that have a longest
# streak = k and the rightmost k coin flips are heads.
def eq_cond_right_k_heads(k, h, t):
    if h < 0 or t < 0: return 0
    elif h < k and t < k: return 0
    else:
        return lt(k+1, h-k, t) - lt_cond_right_is_heads(k+1, h-k, t)

@trace
@memoize
# number of sequences with h heads and t tails that have a longest
# streak >= k.
def ge(k, h, t):
    if h < 0 or t < 0: return 0
    elif h < k and t < k: return 0
    elif k == 0: return total(h, t)
    else:
        return 0 \
            + ge(k, h-1, t) \
            + eq_cond_right_k_heads(k-1, h-1, t) \
            + ge(k, h, t-1) \
            + eq_cond_right_k_tails(k-1, h, t-1)

# probability that a sequence with h heads and t tails has a longest
# streak <= k
def prob_lte(k, h, t):
    return float(lte(k, h, t)) / total(h, t)

##############################
# brute force
import sys
sys.path.append("py-utilities")
import combinatorics

def streak(dems, total):
    longest = 0
    last_d = -1
    d_streak = 1
    for d in dems:
        r_streak = d - last_d - 1
        longest = max(longest, r_streak)
        # print "d:", d, "last_d:", last_d
        if last_d >= 0 and d == last_d + 1: 
            d_streak += 1
        else:
            longest = max(longest, d_streak)
            d_streak = 1
        last_d = d
    r_streak = total - last_d - 1
    longest = max(longest, r_streak)
    longest = max(longest, d_streak)
    return longest

def ge_brute_force(k, h, t):
    count = 0
    total = h + t
    for hs in combinatorics.choose_indices(h, total):
        s = streak(hs, total)
        # print "hs:", hs, "streak:", s
        if s >= k:
            count += 1
    return count

#############
# tests

def test():
    N = 10
    for h in range(N):
        for t in range(N):
            for k in range(0, h + t):
                correct = ge(k, h, t) == ge_brute_force(k, h, t)
                grade_mark = u'\u2713' if correct else u'\u2717'
                print "(k, h, t) = ({}, {}, {})".format(k, h, t), grade_mark
                if not correct: assert(False)

# h = 22
# t = 18
# compare(4, h, t)

# test()

def solve_real(streak):
    h = 22
    t = 18
    less_than_or_equal_to_five = lte(streak, h, t)
    t = total(h, t)
    p = float(less_than_or_equal_to_five) / t
    print "less_than_or_equal_to_five:", less_than_or_equal_to_five
    print "total:", t
    print "P(streak <= 5, 22 repub, 18 dems):", p
    return p

print solve_real(5)

def eq(k, h, t): return lte(k, h, t) - lt(k, h, t)
sum_ = 0
for h in range(101):
    t = 100 - h
    sum_ += ge(10, h, t)

print sum_
total_ways = 2 ** 100
print "P =", float(sum_) / total_ways


# s = set()
# lst = ['h'] * h + ['t'] * t
# for l in combinatorics.permutations(lst):
#     s.add(tuple(l))
# for l in s:
#     print l
