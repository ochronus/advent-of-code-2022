data = open("../input/day10.txt", mode="r").read().splitlines()

c, x = 0, 1
cycles = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
rows = [[" "] * 40 for _ in range(6)]

for inst in data:
    cycle_count = 1 if inst == "noop" else 2
    for _ in range(cycle_count):
        c += 1
        if c in cycles:
            cycles[c] = x * c

        row, pixel = divmod(c - 1, 40)
        if x - 1 <= pixel <= x + 1:
            rows[row][pixel] = "#"

    if cycle_count == 2:  # was addx
        x += int(inst.split()[1])

print(sum(cycles.values()))
for r in rows:
    print("".join(r))
