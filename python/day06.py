datastream = open("../input/day06.txt").read().strip()


def solve(n):
    for index in range(len(datastream[:-4])):
        if len(set(datastream[index : index + n])) == n:
            return index + n
            break


print(solve(4))
print(solve(14))
