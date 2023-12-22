# Part 1 is just a regular depth first search over a graph consisting of paths between useful
# valves and opening those valves.

# For part 2 we do the same thing, completely ignoring the elephant
# until we open a valve. When we open a valve we split off in to two different searches,
# one continuing as normal, and one where our path ends and the elephant performs the same search,
# ignoring all valves that we have already opened.

# This takes 0.02 seconds for part 1 and 165 seconds for part 2 (or 44 seconds using pypy).

# https://gist.githubusercontent.com/liampwll/351fb848f05e8efd257ac87c7d09d1b0/raw/a41ecbd245ccf552fe735a79ac193af00d66d425/day16.py

# Valve DM has flow rate=3; tunnels lead to valves JX, NG, AW, BY, PF

valves = {}

for ln in open("../input/day16.txt").read().splitlines():
    A, B = ln.split("; ")
    _, name, *_, flow_rate = A.split()
    flow_rate = int(flow_rate[5:])
    tunnels = B.split("valve")[1]
    if tunnels.startswith("s "):
        tunnels = tunnels[2:]
    tunnels = tunnels.strip().split(", ")

    valves[name] = {"flow": flow_rate, "tunnels": tunnels, "paths": {}}

keys = sorted([x for x in list(valves.keys()) if valves[x]["flow"] != 0])


def bfs(frontier, end):
    depth = 1
    while True:
        next_frontier = set()
        for x in frontier:
            if x == end:
                return depth
            for y in valves[x]["tunnels"]:
                next_frontier.add(y)
        frontier = next_frontier
        depth += 1


for k in keys + ["AA"]:
    for k2 in keys:
        if k2 != k:
            valves[k]["paths"][k2] = bfs(valves[k]["tunnels"], k2)


def part1():
    best = 0

    def search(opened, flowed, current_room, depth_to_go):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(
                opened.union([current_room]),
                flowed + valves[current_room]["flow"] * depth_to_go,
                current_room,
                depth_to_go - 1,
            )
        else:
            for k in [
                x for x in valves[current_room]["paths"].keys() if x not in opened
            ]:
                search(
                    opened, flowed, k, depth_to_go - valves[current_room]["paths"][k]
                )

    search(set(["AA"]), 0, "AA", 29)
    print(best)


part1()


def part2():
    best = 0

    def search(opened, flowed, current_room, depth_to_go, elephants_turn):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(
                opened.union([current_room]),
                flowed + valves[current_room]["flow"] * depth_to_go,
                current_room,
                depth_to_go - 1,
                elephants_turn,
            )
            if not elephants_turn:
                search(
                    set([current_room]).union(opened),
                    flowed + valves[current_room]["flow"] * depth_to_go,
                    "AA",
                    25,
                    True,
                )
        else:
            for k in [
                x for x in valves[current_room]["paths"].keys() if x not in opened
            ]:
                search(
                    opened,
                    flowed,
                    k,
                    depth_to_go - valves[current_room]["paths"][k],
                    elephants_turn,
                )

    search(set(["AA"]), 0, "AA", 25, False)
    print(best)


part2()
