## source: https://rosettacode.org/wiki/Sierpinski_triangle#Python

import sys
sys.setrecursionlimit(6000000)

def s(sp, d):
    if not d: return [], []

    t = s(sp, d[1:])
    return [sp+d[0]+sp]+t[0], [d[0]+" "+d[0]]+t[1]

def sierpinski(n):
    c = 0
    for i in range(1,6): c |= 1<<i if i%2 else 0
    d = [chr(c)]
    for i in range(n): d = s(" "*2**i,d)[0] + s(" "*2**i,d)[1]
    return d
