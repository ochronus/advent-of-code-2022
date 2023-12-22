moves = [
    (line.split()[0], int(line.split()[1]))
    for line in open("../input/day09.txt", mode="r").read().splitlines()
]

MOVES_MAP = {
    "x": {"L": -1, "R": 1},
    "y": {"U": -1, "D": 1},
}


def solve(knot_count):
    visits = set([(0, 0)])
    knots_x, knots_y = [0] * knot_count, [0] * knot_count
    for direction, steps in moves:
        for _ in range(steps):  # 1 step at a time
            # move the head
            knots_x[0] += MOVES_MAP["x"].get(direction, 0)
            knots_y[0] += MOVES_MAP["y"].get(direction, 0)
            for knot in range(
                1, knot_count
            ):  # "pull" the rest of the rope (each knot) in the new direction, following the unit step
                x_dist = knots_x[knot] - knots_x[knot - 1]
                y_dist = knots_y[knot] - knots_y[knot - 1]
                if (
                    abs(x_dist) > 1 or abs(y_dist) > 1
                ):  # if the distance from the previous knot (counting backwards from the head) grew, we need to move it
                    knots_x[knot] += 0 if x_dist == 0 else 1 if x_dist < 0 else -1
                    knots_y[knot] += 0 if y_dist == 0 else 1 if y_dist < 0 else -1
            visits.add((knots_x[-1], knots_y[-1]))
    print(len(visits))


solve(2)
solve(10)
