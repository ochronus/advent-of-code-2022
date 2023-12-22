from math import prod

grid = [
    [int(j) for j in list(i)]
    for i in open("../input/day08.txt", mode="r").read().splitlines()
]


def visibility_check(x, y):
    tree_height = grid[x][y]
    views = []
    views.append([grid[i][y] for i in range(x)][::-1])  # left
    views.append([grid[i][y] for i in range(x + 1, len(grid))])  # right
    views.append([grid[x][i] for i in range(y)][::-1])  # top
    views.append([grid[x][i] for i in range(y + 1, len(grid))])  # bottom

    # True if there is at least one line of sight (left, right, top, bottom) where all trees are shorter
    p1 = any([all([j < grid[x][y] for j in view]) for view in views])

    # Multiply the number of trees shorter in each line of sight
    # next() skips the elements for which the if condition is false (returns the first for which it's true)
    p2 = prod(
        [
            next((c + 1 for c in range(len(view)) if view[c] >= tree_height), len(view))
            for view in views
        ]
    )
    return p1, p2


part1 = 0
part2 = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        p1, p2 = visibility_check(i, j)
        part1 += p1
        if p2 > part2:
            part2 = p2


print(part1)
print(part2)
