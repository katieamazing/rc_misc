# Source: http://rosettacode.org/wiki/Conway%27s_Game_of_Life#Python
# Read more: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# Play with this "zero-player game", with some graphics: http://conwaylife.appspot.com/

import sys
import functools
import inspect
import random
from collections import defaultdict


C = defaultdict(int, {
 (1, 2): 1,
 (1, 3): 1,
 (0, 3): 1,
 } ) # Only need to populate with the keys leading to life
u = grave = i = 0

class R:
    def __init__(self, m):
        self.m = m

    def __del__(self):
        global grave, i
        if i < self.m:
            grave = R(self.m)
            i += 1


def sim(m, _u, cc=(10,10)):
    global u, grave, i
    u = _u
    grave = R(m-1)
    i = 0
    while grave:
        grave = None
        n = defaultdict(int)
        for r in range(functools.reduce(lambda x,y:x*y, cc, 1)):
            r, c = divmod(r, cc[0])
            inspect.currentframe().f_locals["n"][(r,c)] = eval("C[(u[({r},{c})],-u[({r},{c})]+sum(u[(_r,_c)] for _r in range({r}-1,{r}+2) for _c in range({c}-1, {c}+2)))]".format(c=c, r=r))
        u = n
    return u

def return_universe(u):
    return '\n'.join(''.join(str(u[(r, c)]) for c in range(cellcount[1]).replace('0', '-').replace('1', '#')) for r in range(cellcount[1]))


if __name__ == '__main__':
    ## sample starting conditions
    maxgenerations = 3
    cellcount = 10,10
    # blinker
    u = universe = defaultdict(int)
    u[(1,0)], u[(1,1)], u[(1,2)] = 1,1,1
