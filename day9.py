# Advent of Code Day 9
# https://adventofcode.com/2018/day/9
# Answers
# Part1:  429943
# Part2:  3615691746

from util import *

data = get_data(9, split=False)


def p1(line, multiplier=1):
    num_players, max_marble = int(line.split()[0]), int(line.split()[6])

    scores = defaultdict(int)
    circle = deque([0])
    val = 1
    player = 0

    while val < (max_marble * multiplier) + 1:
        if val % 23 == 0:
            circle.rotate(7)  # rotate to the right, by 7
            scores[player] += circle.pop() + val
            circle.rotate(-1)  # then rotate back to the left, by 1
        else:
            circle.rotate(-1)  # rotate to the left, by 1
            circle.append(val)
        val += 1
        player = (player + 1) % num_players

    return max(v for v in scores.values())


print("Part1: ", p1(data))
print("Part2: ", p1(data, multiplier=100))


p1_tests = [
    ("9 players; last marble is worth 25 points", 32),
    ("13 players; last marble is worth 7999 points", 146373),
    ("17 players; last marble is worth 1104", 2764),
    ("10 players; last marble is worth 1618 points", 8317),
]


run_tests(p1, p1_tests, delim=None)
