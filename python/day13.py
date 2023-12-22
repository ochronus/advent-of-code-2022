import functools


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif b < a:
            return 1
        else:
            return 0
    elif isinstance(a, int):
        return compare([a], b)
    elif isinstance(b, int):
        return compare(a, [b])
    elif not a and b:
        return -1
    elif a and not b:
        return 1
    elif not a and not b:
        return 0
    else:
        q = compare(a[0], b[0])
        if not q:
            return compare(a[1:], b[1:])
        else:
            return q


pairs_text = open("../input/day13.txt").read().split("\n\n")
pairs = []
packets = [[[2]], [[6]]]
for p in pairs_text:
    pairs.append((eval(p.split("\n")[0]), eval(p.split("\n")[1])))
    packets.append(eval(p.split("\n")[0]))
    packets.append(eval(p.split("\n")[1]))

print(sum(i + 1 for i, x in enumerate(pairs) if compare(x[0], x[1]) == -1))

packets_sorted = sorted(packets, key=functools.cmp_to_key(compare))
print((1 + packets_sorted.index([[2]])) * (1 + packets_sorted.index([[6]])))
