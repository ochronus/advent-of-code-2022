paths = [
    list(map(lambda xy: tuple(map(int, xy.split(","))), path.split(" -> ")))
    for path in open("../input/day14.txt").read().strip().split("\n")
]

rocks = set()
for (x, y), *path in paths:
    rocks.add((x, y))
    for x0, y0 in path:
        while (x != x0) or (y != y0):
            x, y = x + (x0 > x) - (x > x0), y + (y0 > y) - (y > y0)
            rocks.add((x, y))

max_rock_depth = max(max(map(lambda xy: xy[1], path)) + 2 for path in paths)
for x in range(500 - max_rock_depth - 1, 500 + max_rock_depth + 1):
    rocks.add((x, max_rock_depth))

# Now that we've inserted the floor, we can proceed to simulate the falling
# sand particles.
p1 = False
n = 0
SAND_SOURCE = (500, 0)
while True:
    x, y = SAND_SOURCE
    if SAND_SOURCE in rocks:
        # the sand filled up the cave up to the point of sand source
        print("Part 2:", n)
        break

    while True:
        if not p1 and y >= max_rock_depth - 1:
            print("Part 1:", n)  # the first grain of sand arrived at rest at the bottom
            p1 = True

        if (x, y + 1) not in rocks:
            y = y + 1
        elif (x - 1, y + 1) not in rocks:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in rocks:
            x, y = x + 1, y + 1
        else:
            rocks.add((x, y))  # add the sand at rest
            break
    n += 1
