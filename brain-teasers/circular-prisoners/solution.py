import itertools

x = [0, 1]
ps = list(itertools.product(x, x, x, x))
for p in ps:
    print p

def num_different(p1, p2):
    num_diff = 0
    for x in range(len(p1)):
        if p1[x] != p2[x]: 
            num_diff += 1
    return num_diff

def find_connected(p):
    return [ x for x in ps if num_different(p, x) == 1]

def find_pair(p, j):
    return [ x if i != j else 1 - x for (i, x) in enumerate(p) ]

def score(p, strat):
    num_right = 0
    num_wrong = 0
    num_right = sum([ 1 if hat == guess else 0 for (hat, guess) in zip(p, strat) if guess != None ])
    num_wrong = sum([ 1 if hat != guess else 0 for (hat, guess) in zip(p, strat) if guess != None])
    if num_wrong > 0:
        return -1 
    else:
        return 1 if num_right > 0 else 0

def summarize(state):
    for (strat, p) in state:
        s = score(p, strat)
        if s == -1:
            hs = "incorrect"
        elif s == 1:
            hs = "correct"
        else:
            hs = "no guesses (incorrect)"
        print p, " -> ", strat, " -> ", hs

def total_score(state):
    return sum([score(p, strat) for (strat, p) in state])

print find_connected([1,1,1,1])
print find_pair([1,1,1,1], 3)

def all_possible_moves(state):
    moves = []
    for (i, (strat, p)) in enumerate(state):
        for (j, decision) in enumerate(strat):
            if decision is None: 
                moves.append((i, j, 0))
                moves.append((i, j, 1))
    return moves

def looks_like(i, j):
    pair = find_pair(ps[i], j) 
    idx = [ (idx, p) for (idx, p) in enumerate(ps) if list(p) == pair ][0][0]
    return (idx, j)

print "score:", score([0,0,0,0], [None, None, None, None])
print "TEST score:", score([0, 0, 1, 1], [0, None, None, None])

def filter_moves(moves):
    filtered_moves = []
    do_not_add = set()
    for move in moves:
        if move not in do_not_add:
            (i, j, decision) = move
            (i2, j2) = looks_like(i, j)
            do_not_add.add((i2, j2, decision))
            filtered_moves.append(move)
    return filtered_moves
    
state = [ ([None for _ in p], p) for p in ps ]
summarize(state)

# all_moves = all_possible_moves(state)
# print "moves:", len(all_moves)
# for move in all_moves:
#     print move
#     # (i, j, decision) = move
#     # print "looks like:", looks_like(i, j)

# filtered_moves = filter_moves(all_moves)
# print "filtered moves:", len(filtered_moves)
# for move in filtered_moves:
#     print move

def apply_move(state, move):
    (i, j, decision) = move
    (i2, j2) = looks_like(i, j)
    state[i][0][j] = decision
    state[i2][0][j2] = decision

def unapply_move(state, move):
    (i, j, decision) = move
    (i2, j2) = looks_like(i, j)
    state[i][0][j] = None
    state[i2][0][j2] = None

def make_move(state, level):
    score = total_score(state)
    if score > 7:
        return (True, state)
    moves = filter_moves(all_possible_moves(state))
    print "level", level, " {} moves".format(len(moves))
    
    def try_moves(state, moves, good_enough):
        for move in moves:
            # print "considering move:", move
            apply_move(state, move)
            new_score = total_score(state)
            if good_enough(new_score, score):
                print " " * level, move, " -> ", total_score(state)
                # summarize(state)
                (got_goal, state) = make_move(state, level + 1)
                if got_goal: return (got_goal, state)
            # print summarize(state)
            unapply_move(state, move)
        return None
    
    better_moves = try_moves(state, moves, lambda new_score, score: new_score > score)
    if better_moves is not None: return better_moves
    equal_moves = try_moves(state, moves, lambda new_score, score: new_score >= score)
    if equal_moves is not None: return equal_moves
    return (False, state)

print "starting"
apply_move(state, (0, 0, 1))
apply_move(state, (0, 1, 1))
apply_move(state, (0, 2, 1))
apply_move(state, (0, 3, 1))
print "state:", total_score(state)
summarize(state)
(got_goal, end_state) = make_move(state, level = 0)
print "end_state:", total_score(end_state), " got goal?", got_goal
summarize(end_state)
