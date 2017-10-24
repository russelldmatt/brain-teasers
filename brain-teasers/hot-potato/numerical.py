
def f(N, ps, p, this, other):
    if (this + other) == N: return
    if this not in ps: ps[this] = dict()
    if other not in ps[this]: ps[this][other] = 0
    ps[this][other] += p
    denom = 1 + this + other + 1
    p_other = 1. / denom
    p_this = 1 - p_other
    f(N, ps, p * p_this, this + 1, other)
    f(N, ps, p * p_other, other + 1, this)

N = 20
ps = dict()
f(N, ps, 1., 0, 0)

for this in ps.keys():
    for other in ps[this].keys():
        if this < other: ps[other][this] += ps[this][other]
        
for this in ps.keys():
    for other in ps[this].keys():
        if this >= other:
            if this + other == N - 1:
                if this == other: 
                    print this, other, ps[this][other]
                else:
                    print this, other, ps[this][other]/2.
print ps
