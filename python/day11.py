from math import lcm
from copy import deepcopy


data = open("../input/day11.txt").read().strip()

MONKEYS = []
OPERATIONS = []
TESTS = []
THROWS = []
for monkey in data.split("\n\n"):
    _, items, op, test, true, false = monkey.split("\n")
    MONKEYS.append([int(i) for i in items.split(":")[1].split(",")])
    op = "".join(op.split()[-3:])  # Operation: new = old * 13 --> old * 13
    OPERATIONS.append(lambda old, op=op: eval(op))
    TESTS.append(int(test.split()[-1]))
    THROWS.append([int(false.split()[-1]), int(true.split()[-1])])

START = deepcopy(MONKEYS)

# Want to know for each item if it is divisible by e.g. 23,19,13,17
# If we just wanted to know if its divisible by 23, we can just keep track of the number modulo 23.
# x+a is divisible by 23 iff (x%23)+a is divisible by 23
# x*a is divisible by 23 iff (x%23)*a is divisible by 23
# We can keep track of the number modulo 23*19*13*17

LCM = lcm(*TESTS)

for part in [1, 2]:
    C = [0 for _ in range(len(MONKEYS))]
    MONKEYS = deepcopy(START)
    for t in range(20 if part == 1 else 10000):
        for i in range(len(MONKEYS)):
            C[i] += len(
                MONKEYS[i]
            )  # this monkey inspects len(M[i]) items in this round
            while MONKEYS[i]:
                item = OPERATIONS[i](MONKEYS[i].pop()) % LCM
                if part == 1:
                    item = item // 3
                MONKEYS[THROWS[i][(item % TESTS[i] == 0)]].append(item)

    print(sorted(C)[-1] * sorted(C)[-2])
