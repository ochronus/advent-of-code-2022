priorities = "🤩abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

part1 = 0
for line in open("../input/day03.txt").read().splitlines():
    mid = len(line) // 2
    part1 += priorities.index((set(line[:mid]) & set(line[mid:])).pop())

print(part1)


def get_group_iter(lines):
    while lines:
        yield (set(lines.pop(0)), set(lines.pop(0)), set(lines.pop(0)))


part2 = 0
for rs1, rs2, rs3 in get_group_iter(open("../input/day03.txt").read().splitlines()):
    part2 += priorities.index((rs1 & rs2 & rs3).pop())

print(part2)
