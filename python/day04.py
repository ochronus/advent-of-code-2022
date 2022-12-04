with open("../input/day04.txt", "r") as f:
    pairs = [
        [
            set(range(sec[0], sec[1] + 1))
            for sec in [list(map(int, p.split("-"))) for p in line.split(",")]
        ]
        for line in f.readlines()
    ]

total = 0
[
    total := total + 1
    for pair in pairs
    if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])
]
print(total)


total = 0
[total := total + 1 for pair in pairs if bool(pair[0] & pair[1])]
print(total)
