def lp(i):
    if i == []:
        return None
    else:
        lp(i[1:])

    def length(l):
        if l == []:
            return 0
        else:
            return length(l[1:])


assert(lp([]) == None)
assert(lp([1]) == 1)
assert(lp([6]) == 6)
assert(lp([0, 8]) == 8)
assert(lp([8, 0]) == 8)
assert(lp([0, 7, 3, -2]) == 21)
