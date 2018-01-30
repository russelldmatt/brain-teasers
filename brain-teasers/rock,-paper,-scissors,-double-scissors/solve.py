from sympy import *

def ev1(prob1, prob2):
    x = symbols('x')
    M = [[x, 0.5, 1, 1],
         [1, x, 0, 0.5],
         [0.5, 1, 1, x]]
    expr = 0
    for (i, p1) in enumerate(prob1):
        for (j, p2) in enumerate(prob2):
            expr += p1*p2*M[i][j]
    return solve(Eq(expr, x), x)[0]

def derivatives(x, f, delta):
    # print "fx:", f(x)
    for i in range(len(x)):
        other_non_zero_entries = [z for (j, z) in enumerate(x) if j != i and z != 0]
        n_other_non_zero_entries = len(other_non_zero_entries)
        if n_other_non_zero_entries == 0:
            delta = 0
        else:
            min_other_non_zero_entries = min(other_non_zero_entries)
            delta = min(min(delta, 1 - x[i]), min_other_non_zero_entries * n_other_non_zero_entries)
        y = [ p + delta
              if j == i
              else (p - delta / n_other_non_zero_entries if p != 0 else p)
              for (j, p) in enumerate(x) ]
        # print i, y
        assert(abs(sum(y) - 1.) < 0.00001)
        df = f(y) - f(x)
        # print f(y), df
        if df > 0:
            print("found better strat")
            return y
    return x

prob1 = [1/3., 1/3., 1/3.]
prob2 = [1/3., 1/3., 0., 1/3.]
prob2 = [0, 0, 1., 0]

# print derivatives(prob2, lambda prob2: 1 - ev1(prob1, prob2), 0.01)
# print derivatives(prob1, lambda prob1: ev1(prob1, prob2), 0.01)

print(ev1(prob1, prob2))

delta = 0.03

# for c in range(1000):
#     turn = 1 if c % 2 == 0 else 2
#     print "loop:", c, ": {}'s turn".format(turn)
#     if c % 2 == 0:
#         prob1_ = derivatives(prob1, lambda prob1: ev1(prob1, prob2), delta)
#         if prob1_ == prob1:
#             print "prob1 didnt' change, at nash"
#         prob1 = prob1_
#     else:
#         prob2_ = derivatives(prob2, lambda prob2: 1 - ev1(prob1, prob2), delta)
#         if prob2_ == prob2:
#             print "prob2 didnt' change, at nash"
#         prob2 = prob2_
#     print "prob1", prob1
#     print "prob2", prob2
#     print "ev1:", ev1(prob1, prob2), "ev2:", 1 - ev1(prob1, prob2)

import numpy as np

# find p1's strategy which minimizes score of p2's best response
def all_possibilities(up_to, by):
    return np.concatenate((np.arange(0, up_to, by), [up_to]), 0)

def all_strategies_that_sum_to_one(x, delta):
    def loop(x, left):
        if len(x) == 1: yield [left]
        else:
            for z in all_possibilities(left, delta):
                for l in loop(x[1:], left - z):
                    yield [z] + l
    for z in loop(x, 1.): yield z

def all_pure_strategies(x):
    for i in range(len(x)):
        yield [ 1 if j == i else 0 for j in range(len(x)) ]

def best_response(prob1, delta):
    worst_ev = 1
    best_response = [0, 0, 0, 0]
    for prob2 in all_strategies_that_sum_to_one([0, 0, 0, 0], delta):
        try:
            ev = ev1(prob1, prob2)
            if ev < worst_ev: best_response = prob2
            worst_ev = min(ev, worst_ev)
        except:
            print("failed")
    return (worst_ev, best_response)

def best_response(prob1, delta):
    worst_ev = 1
    best_response = [0, 0, 0, 0]
    for prob2 in all_pure_strategies([0, 0, 0, 0]):
        try:
            ev = ev1(prob1, prob2)
            if ev < worst_ev: best_response = prob2
            worst_ev = min(ev, worst_ev)
        except:
            print("failed")
    return (worst_ev, best_response)

def brute_force(delta): 
    best_ev = 0
    for prob1 in all_strategies_that_sum_to_one([0, 0, 0], delta):
        (worst_ev, best_prob2) = best_response(prob1, delta)
        print("ev1 of:", worst_ev, "with strat of", prob1, "and response of", best_prob2)
        if worst_ev > best_ev:
            print("----------------")
            print("best strat so far for p1:")
            print("ev1:", worst_ev)
            print("prob1", prob1)
            print("best response (prob2):", best_prob2)
            print("----------------")
            best_ev = worst_ev
        
delta = 0.01
# brute_force(delta)
 
        
        

