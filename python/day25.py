import sys


def part1():
    addition_table = {
        "2": {"2": "1-", "1": "1=", "0": "02", "-": "01", "=": "00"},
        "1": {"2": "1=", "1": "02", "0": "01", "-": "00", "=": "0-"},
        "0": {"2": "02", "1": "01", "0": "00", "-": "0-", "=": "0="},
        "-": {"2": "01", "1": "00", "0": "0-", "-": "0=", "=": "-2"},
        "=": {"2": "00", "1": "0-", "0": "0=", "-": "-2", "=": "-1"},
    }
    data = [
        list(reversed(line.strip())) for line in open("../input/day25.txt").readlines()
    ]
    total = ["0"]

    for num in data:
        carry = "0"
        for power in range(max(len(num), len(total))):
            if power > len(total) - 1:
                total.append("0")
            if power > len(num) - 1:
                num.append("0")
            carry_a, total[power] = addition_table[total[power]][num[power]]
            carry_b, total[power] = addition_table[total[power]][carry]
            carry = addition_table[carry_b][carry_a][1]
        if carry != "0":
            total.append(carry)

    print("".join(reversed(total)))


part1()
