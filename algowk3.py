def solve(a):
    max_suffix = 0
    max_span = 0
    for i in a:
        max_suffix = max(0, max_suffix+i)
        max_span = max(max_span, max_suffix)

    return max_span
