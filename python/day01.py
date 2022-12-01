input = open("../input/day01.txt", "r").read().splitlines()

elves = []

total = 0
for line in input:
    if line == "":
        elves.append(total)
        total = 0
    else:
        total += int(line)

# part 1
print(max(elves))

# part 2
elves.sort()
print(sum(elves[-3:]))
