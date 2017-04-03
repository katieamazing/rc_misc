maze = [
    "#####",
    "#.###",
    "#..##",
    "##..#",
    "#####"
]

big_maze = [
    "##########",
    "#..##.####",
    "#.###.####",
    "#.##....##",
    "#..##.####",
    "##.##..###",
    "##....####",
    "#####.####",
    "#####....#",
    "##########"
]

def obstacle_at(row, col):
    return big_maze[row][col] == "#"



def directions(start, goal, discovered):
    if start == goal:
        return []
    else:
        last = discovered[goal]
        if last == "north":
            new_goal = (goal[0]+1, goal[1])
        elif last == "south":
            new_goal = (goal[0]-1, goal[1])
        elif last == "west":
            new_goal = (goal[0], goal[1]+1)
        elif last == "east":
            new_goal = (goal[0], goal[1]-1)
        else:
            print("Bad things, very bad.")
        recursive_path = directions(start, new_goal, discovered)
        recursive_path.append(last)
        return recursive_path

def bfs(start, goal):
    processed = set()
    discovered = {}
    q = []
    q.insert(0, start)
    while len(q) > 0:
        v = q.pop() #the one we're focusing on
        processed.add(v)
        #try 4 directions
        if not obstacle_at(v[0]-1, v[1]):         #try north
            if (v[0]-1, v[1]) not in discovered:
                q.insert(0, (v[0]-1, v[1]))
                discovered[(v[0]-1, v[1])] = "north"
        if not obstacle_at(v[0]+1, v[1]):       #try south
            if (v[0]+1, v[1]) not in discovered:
                q.insert(0, (v[0]+1, v[1]))
                discovered[(v[0]+1, v[1])] = "south"
        if not obstacle_at(v[0], v[1]-1):       #try west
            if (v[0], v[1]-1) not in discovered:
                q.insert(0, (v[0], v[1]-1))
                discovered[(v[0], v[1]-1)] = "west"
        if not obstacle_at(v[0], v[1]+1):       #try east
            if (v[0], v[1]+1) not in discovered:
                q.insert(0, (v[0], v[1]+1))
                discovered[(v[0], v[1]+1)] = "east"

    if goal in processed:
        return " ".join(directions(start, goal, discovered))
    else:
        return "No path found. Eaten by a Minotaur."

print(bfs((1, 1), (8, 8)))
# assert(obstacle_at(0,0))
# assert(not obstacle_at(1,1))
#
# assert(directions((1, 1), (1, 1), {}) == [])
# assert(directions((1, 1), (2, 1), {(2, 1):"south"}) == ["south"])
# assert(directions((1, 1), (1, 2), {(1, 2):"east"}) == ["east"])
# assert(directions((2, 1), (1, 1), {(1, 1):"north"}) == ["north"])
# assert(directions((1, 2), (1, 1), {(1, 1):"west"}) == ["west"])
# assert(directions((1, 1), (1, 3), {(1, 2):"east", (1, 3):"east"}) == ["east", "east"])
#
# assert(bfs((1, 1), (2, 2)) == "south east")
# assert(bfs((1, 1), (1, 1)) == "")
# assert(bfs((2, 2), (1, 1)) == "west north")
