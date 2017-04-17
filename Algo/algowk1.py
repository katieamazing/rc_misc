"""
Algorithm week 1: Greedy

Interval partitioning

1. sort lectures based on start time from latest to earliest
2. initialize classrooms at 0
3. while lectures are unscheduled:
    pick earliest unscheduled lecture (sorted_lecture[-1])
    look through classrooms and schedule
        if no classrooms, make a new classroom and schedule
    pop sorted_lecture off
4. Return number of classrooms

Sorting costs extra - not using heap/priority queue maybe costs extra
Might be O(n log n) to do this
Just the scheduling is O(3n) = O(n) a search through a list of lists, a push, a pop

"""

def sort_lectures(lectures):
    return sorted(lectures, key=lambda lecture: lecture[1], reverse=True)

def conflicts(a, b):
    return point_in_interval(b[1], b[2], a[1]) or point_in_interval(b[1], b[2], a[2])

def point_in_interval(start, end, point):
    return start < point and point < end

def schedule_lectures(sorted_lectures):
    classrooms = []
    while len(sorted_lectures) > 0:
        class_to_schedule = sorted_lectures[-1]
        done = False
        print(class_to_schedule)        for room in classrooms:
            any_conflict = False
            for prev_scheduled_class in room:
                if conflicts(class_to_schedule, prev_scheduled_class):
                    any_conflict = True
            if not any_conflict:
                room.append(class_to_schedule)
                done = True
        if not done:
            classrooms.append([class_to_schedule])
        sorted_lectures.pop()
    return len(classrooms)


assert(sort_lectures([(2, 700, 1000), (1, 930, 1100)]) == [(1, 930, 1100), (2, 700, 1000)])

assert(conflicts((1, 1500, 1700), (2, 1600, 1800)) == True)
assert(conflicts((1, 900, 1000), (2, 1600, 1800)) == False)
assert(conflicts((1, 900, 1000), (2, 1000, 1200)) == False)

assert(schedule_lectures([(1, 930, 1100)]) == 1)
assert(schedule_lectures([]) == 0)
assert(schedule_lectures([(1, 930, 1100), (2, 700, 1000)]) == 2)
assert(schedule_lectures([(4, 1500, 1700), (3, 1200, 1500), (2, 1000, 1200), (3, 900, 1200)]) == 2)
