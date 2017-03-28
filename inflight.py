#O(n**2)
import itertools
def movies(flight_length, movie_lengths):
    for combo in itertools.product(movie_lengths, movie_lengths):
        if combo[0] == combo[1]:
            pass
        else:
            if combo[0]+combo[1] == flight_length:
                return True
    return False

assert(movies(20, [10]) == False)
assert(movies(60, [35, 25]) == True)
assert(movies(55, [45, 25, 10]) == True)
assert(movies(90, [33, 25, 89, 120]) == False)


##O(n) time, O(n) space
def fast_movies(flight_length, movie_lengths):
    movie_lengths_seen = set()
    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    return False

assert(fast_movies(20, [10]) == False)
assert(fast_movies(60, [35, 25]) == True)
assert(fast_movies(55, [45, 25, 10]) == True)
assert(fast_movies(90, [33, 25, 89, 120]) == False)
