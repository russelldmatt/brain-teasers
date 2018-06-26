import sys
import numpy as np

def all_possibilities(n):
    if n == 0:
        return [[]]
    else:
        return ([ [0] + x for x in all_possibilities(n-1) ] 
                + [ [1] + x for x in all_possibilities(n-1) ])

def score(p, guess):
    return sum([ x == y for (x, y) in zip(p, guess) ])

def filter(possibilities, guess, score_):
    return [p for p in possibilities if score(p, guess) == score_]

def possible_scores(possibilities, guess):
    return set([score(p, guess) for p in possibilities])

def best_guess(possibilities, all_possibilities):
    best_guess = None
    best_guess_outcome = len(possibilities)
    best_guess_worst_score = None
    for guess in all_possibilities:
        worst_guess_outcome = 0
        worst_score = None
        for score in possible_scores(possibilities, guess):
            num_left = len(filter(possibilities, guess, score))
            if num_left > worst_guess_outcome:
                worst_guess_outcome = num_left
                worst_score = score
        if worst_guess_outcome < best_guess_outcome:
            best_guess_outcome = worst_guess_outcome
            best_guess = guess
            best_guess_worst_score = worst_score
    return (best_guess, best_guess_worst_score)

def loop(possibilities, all_possibilities, n, verbose, guesses):
    if len(possibilities) == 1:
        return (n, guesses)
    if verbose: print "n =", n
    if verbose: print possibilities
    (guess, worst_score) = best_guess(possibilities, all_possibilities)
    if verbose: print "guess: {}".format(guess)
    if verbose: print "worst score: {}".format(worst_score)
    new_possibilies = filter(possibilities, guess, worst_score)
    return loop(new_possibilies, all_possibilities, n+1, verbose, guesses + [guess])

def test(N, verbose):
    print "------------------"
    print "Testing N of {}:".format(N)
    all_ = all_possibilities(N)
    possibilities = all_
    (num_guesses, guesses) = loop(possibilities, all_, 0, verbose, [])
    print "took {} guesses".format(num_guesses)
    print "guesses:"
    for guess in guesses:
        print(guess)
    # guess = [1] * N
    # score_ = 2
    # possibilities = filter(possibilities, guess, score_)

for i in xrange(1, 15):
    test(i, verbose = False)    

# for p in all_possibilities(4):
#     print p, score(p, [1,1,1,1]), score(p, [1,1,0,0]), score(p, [1,0,1,0])
