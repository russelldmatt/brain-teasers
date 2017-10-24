import random
import sys
sys.setrecursionlimit(15000)

def flip(): return bool(random.getrandbits(1))
debug = False

N_kids = 5

def game():
    kids = set(range(N_kids))
    current = 0
    def loop(current):
        if debug: print "current:", current
        if current in kids: kids.remove(current)
        if len(kids) == 1: return list(kids)[0]
        current += 1 if flip() else (-1)
        current = (current + N_kids) % N_kids
        return loop(current)
    return loop(current)

print game()

N = 100000
wins = dict()
for n in range(N):
    winner = game()
    if debug: print winner
    if winner not in wins: wins[winner] = 0
    wins[winner] += 1

for i in range(N_kids):
    n_wins = wins[i] if i in wins else 0
    print "{}: {}".format(i, n_wins / float(N))


