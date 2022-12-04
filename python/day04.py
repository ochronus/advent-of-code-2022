def getranges(line):
    pair = line.split(",")
    sec1 = list(map(int, pair[0].split("-")))
    sec2 = list(map(int, pair[1].split("-")))
    return (set(range(sec1[0], sec1[1] + 1)), set(range(sec2[0], sec2[1] + 1)))


with open("../input/day04.txt", "r") as f:
    pairs = [getranges(line) for line in f.readlines()]

total = 0
for pair in pairs:
    if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
        total += 1
print(total)


total = 0
[total := total + 1 for pair in pairs if bool(pair[0] & pair[1])]
print(total)
