inputs = [line.strip().split() for line in open("../input/day02.txt").readlines()]

# column 1: A: rock ; B: paper ; C: scissors
# column 2: X: rock ; Y: paper ; Z: scissors

shape_score = {"X": 1, "Y": 2, "Z": 3}  # rock  # paper  # scissors


# A (rock): [Y(win|paper) X(draw|rock) Z(lose|scissors)]
outcome_map = {"A": ["Y", "X", "Z"], "B": ["Z", "Y", "X"], "C": ["X", "Z", "Y"]}

# win, draw, lose
outcome_score = [6, 3, 0]

# part 2
# column 2: X: lose ; Y: dray ; Z: win
strategy_map_scores = {"X": 0, "Y": 3, "Z": 6}

score1 = 0
score2 = 0
for opponent_shape, second_column in inputs:
    outcomes = outcome_map[opponent_shape]
    score1 += shape_score[second_column] + outcome_score[outcomes.index(second_column)]

    # part 2
    strategy_score = strategy_map_scores[second_column]
    my_shape = outcomes[
        outcome_score.index(strategy_score)
    ]  # win == first, draw == second, lose == third
    score2 += shape_score[my_shape] + strategy_score

print(score1)
print(score2)
