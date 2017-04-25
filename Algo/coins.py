
def change(amount, denoms):
    if amount < 0 or denoms == []:
        return 0
    elif amount == 0:
        return 1

    count = 0
    for d in denoms:
        count += change(amount-d, denoms)

    return count

def ways(amount, denoms):
    if amount < 0 or denoms == []:
        return []
    elif amount == 0:
        return [[]]

    count = []
    for d in denoms:
        subprob = ways(amount-d, denoms)
        for i in subprob:
            i.append(d)
            count.append(i)


    return count

print(ways(5, [1,2,3]))
