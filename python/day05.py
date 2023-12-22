with open("../input/day05.txt") as file:
    raw_stacks, raw_lines = file.read().split("\n\n")
    lines = raw_lines.splitlines()


stacks = [
    [] for _ in range(10)
]  # added an empty list at the start so indexing from 1 works
for row in raw_stacks.splitlines()[-2::-1]:  # reverse the lines and skip the last
    for i, c in enumerate(
        row[1::4], start=1
    ):  # every 4th character on the line [Q] [Q] [B]
        if c != " ":
            stacks[i].append(c)

instructions = []
for line in lines:
    # move n from s to d
    _, n, _, s, _, d = line.split()
    instructions.append(list(map(int, (n, s, d))))

stacks2 = [s.copy() for s in stacks]


for n, s, d in instructions:
    for _ in range(n):
        stacks[d].append(stacks[s].pop())

    stacks2[d].extend(stacks2[s][-n:])
    del stacks2[s][-n:]


p1 = [s[-1] for s in stacks[1:]]
print("Part 1: ", *p1, sep="")
p2 = [s[-1] for s in stacks2[1:]]
print("Part 2: ", *p2, sep="")
