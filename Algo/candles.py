def blown(n, h):
    # Ignore the first input
    # Parse the input heights
    heights = [int(c) for c in h if c.isdigit()]
    # find all the tall candles
    tall_candles = [d for d in heights if d >= max(heights)]
    return len(tall_candles)

blown(4, "3 2 1 3")
