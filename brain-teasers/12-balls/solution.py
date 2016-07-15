from enum import Enum

class Weigh_outcome(Enum):
    Left_heavy = 1
    Left_light = 2
    Even = 3
    
    def left_state(self):
        if self == Weigh_outcome.Left_heavy: return S.Maybe_heavy
        elif self == Weigh_outcome.Left_light: return S.Maybe_light
        elif self == Weigh_outcome.Even: return S.Normal
        else: assert(False)

class S(Enum):
    Maybe_heavy = 1
    Maybe_light = 2
    Normal = 3
    No_clue = 4
    
    def other_side_if_left(self):
        if self == S.Maybe_heavy: return S.Maybe_light
        elif self == S.Maybe_light: return S.Maybe_heavy
        elif self == S.Normal: return S.Normal
        else: assert(False)

    def not_weighed_if_left(self):
        if self == S.Maybe_heavy: return S.Normal
        elif self == S.Maybe_light: return S.Normal
        elif self == S.Normal: return S.No_clue
        else: assert(False)

state_reducer = {
    (S.Maybe_heavy, S.Maybe_heavy) : S.Maybe_heavy,
    (S.Maybe_heavy, S.Maybe_light) : S.Normal,
    (S.Maybe_heavy, S.Normal) : S.Normal,
    (S.Maybe_heavy, S.No_clue) : S.Maybe_heavy,

    (S.Maybe_light, S.Maybe_heavy) : S.Normal,
    (S.Maybe_light, S.Maybe_light) : S.Maybe_light,
    (S.Maybe_light, S.Normal) : S.Normal,
    (S.Maybe_light, S.No_clue) : S.Maybe_light,

    (S.Normal, S.Maybe_heavy) : S.Normal,
    (S.Normal, S.Maybe_light) : S.Normal,
    (S.Normal, S.Normal) : S.Normal,
    (S.Normal, S.No_clue) : S.Normal,

    (S.No_clue, S.Maybe_heavy) : S.Maybe_heavy,
    (S.No_clue, S.Maybe_light) : S.Maybe_light,
    (S.No_clue, S.Normal) : S.Normal,
    (S.No_clue, S.No_clue) : S.No_clue,
}    

def reduce_states(state1, state2):
    key = (state1, state2)
    if key in state_reducer:
        return state_reducer[key]
    else:
        assert(False)

def weigh(balls, left, right, indent = ""):
    print "{}Weigh: left = {} vs. right = {}".format(indent, left, right)
    def new_state(new_left_state, idx):
        if idx in left:
            return new_left_state
        elif idx in right:
            return new_left_state.other_side_if_left()
        else:
            return new_left_state.not_weighed_if_left()
    # return 3 possibilities
    return [ (outcome
              , [ reduce_states(balls[x], new_state(outcome.left_state(), x)) for x in range(len(balls)) ])
             for outcome
             in list(Weigh_outcome)
         ]
    
def impossible(balls):
    return balls == [ S.Normal for _ in range(len(balls)) ]

def solved(balls):
    num_normals = len([ x for x in balls if x == S.Normal ])
    return num_normals == len(balls) - 1

class Label(Enum):
    Impossible = 1
    Solved = 2

def label(balls):
    if impossible(balls): return Label.Impossible
    elif solved(balls): return Label.Solved
    else: return None

def human_readable(balls, label):
    if label == Label.Impossible:
        return "Impossible, all balls are equal"
    elif label == Label.Solved:
        (idx, b) = [ (i, b) for (i, b) in enumerate(balls) if b <> S.Normal ][0]
        return "Ball {} is {}".format(idx, b)
    else:
        return "Don't know yet"
        
def print_outcome_balls(outcome, balls, indent = "", assert_solved_or_impossible = False):
    print '{}---------------'.format(indent)
    print "{}{}".format(indent, outcome)
    lbl = label(balls)
    print "{} {} -> {}".format(indent, lbl, human_readable(balls, lbl))
    if assert_solved_or_impossible and lbl is None: assert(False)

def print_all(outcome_and_balls, indent):
    for (outcome, balls) in outcome_and_balls:
        print_outcome_balls(outcome, balls, indent, assert_solved_or_impossible = True)

def three_balls():
    balls = [ S.No_clue for _ in range(3) ]
    print "starting balls:"
    print balls

    balls = weigh(balls, [0], [1])
    for (outcome, new_balls) in balls:
        print_outcome_balls(outcome, new_balls, indent = "")
        x = weigh(new_balls, [0],[2])
        for (outcome, new_balls) in x:
            print_outcome_balls(outcome, new_balls, indent = "  ")

def twelve_balls():
    balls = [ S.No_clue for _ in range(12) ]
    print "starting balls:"
    print balls

    balls1 = weigh(balls, [0,1,2,3], [4,5,6,7], indent = "")
    for (outcome, balls) in balls1:
        print_outcome_balls(outcome, balls, indent = "")
        if outcome == Weigh_outcome.Even:
            balls2 = weigh(balls, left = [0,1,2], right = [8,9,10], indent = "  ")
            for (outcome, balls) in balls2:
                print_outcome_balls(outcome, balls, indent = "  ")
                if outcome == Weigh_outcome.Even:
                    print_all(weigh(balls, left = [11], right = [0], indent = "    "), indent = "    ")
                else:
                    print_all(weigh(balls, left = [8], right = [9], indent = "    "), indent = "    ")
        elif outcome == Weigh_outcome.Left_heavy:
            balls2 = weigh(balls, left = [0, 1, 2, 4], right = [3, 8, 9, 10], indent = "  ")
            for (outcome, balls) in balls2:
                print_outcome_balls(outcome, balls, indent = "  ")
                if outcome == Weigh_outcome.Left_heavy:
                    print_all(weigh(balls, left = [0], right = [1], indent = "    "), indent = "    ")
                elif outcome == Weigh_outcome.Left_light:
                    print_all(weigh(balls, left = [4], right = [11], indent = "    "), indent = "    ")
                elif outcome == Weigh_outcome.Even:
                    print_all(weigh(balls, left = [5], right = [6], indent = "    "), indent = "    ")
                else: assert(False)
        else: 
            balls2 = weigh(balls, left = [0, 1, 2, 4], right = [3, 8, 9, 10], indent = "  ")
            for (outcome, balls) in balls2:
                print_outcome_balls(outcome, balls, indent = "  ")
                if outcome == Weigh_outcome.Left_heavy:
                    print_all(weigh(balls, left = [4], right = [11], indent = "    "), indent = "    ")
                elif outcome == Weigh_outcome.Left_light:
                    print_all(weigh(balls, left = [0], right = [1], indent = "   "), indent = "    ")
                elif outcome == Weigh_outcome.Even:
                    print_all(weigh(balls, left = [5], right = [6], indent = "    "), indent = "    ")
                else: assert(False)

def twelve_balls_web():
    balls = [ S.No_clue for _ in range(12) ]
    print "starting balls:"
    print balls

    balls1 = weigh(balls, [0,1,2,3], [4,5,6,7])
    for (outcome, balls) in balls1:
        print_outcome_balls(outcome, balls, indent = "")
        if outcome == Weigh_outcome.Even:
            balls2 = weigh(balls, left = [5,6,7], right = [8,9,10])
            for (outcome, balls) in balls2:
                print_outcome_balls(outcome, balls, indent = "  ")
                if outcome == Weigh_outcome.Even:
                    print_all(weigh(balls, left = [11], right = [0]), indent = "    ")
                else:
                    print_all(weigh(balls, left = [8], right = [9]), indent = "    ")
        elif outcome == Weigh_outcome.Left_heavy:
            balls2 = weigh(balls, left = [0, 1, 4], right = [2,5,9])
            for (outcome, balls) in balls2:
                print_outcome_balls(outcome, balls, indent = "  ")
                if outcome == Weigh_outcome.Left_heavy:
                    print_all(weigh(balls, left = [0], right = [1]), indent = "    ")
                elif outcome == Weigh_outcome.Left_light:
                    print_all(weigh(balls, left = [2], right = [9]), indent = "    ")
                elif outcome == Weigh_outcome.Even:
                    print_all(weigh(balls, left = [6], right = [7]), indent = "    ")
                else: assert(False)
        else: 
            balls2 = weigh(balls, left = [0, 1, 4], right = [2,5,9])
            for (outcome, balls) in balls2:
                print_outcome_balls(outcome, balls, indent = "  ")
                if outcome == Weigh_outcome.Left_heavy:
                    print_all(weigh(balls, left = [2], right = [9]), indent = "    ")
                elif outcome == Weigh_outcome.Left_light:
                    print_all(weigh(balls, left = [0], right = [1]), indent = "    ")
                elif outcome == Weigh_outcome.Even:
                    print_all(weigh(balls, left = [6], right = [7]), indent = "    ")
                else: assert(False)

# three_balls()
twelve_balls()
# twelve_balls_web()
