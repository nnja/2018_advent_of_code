# Advent of Code Day 5
# https://adventofcode.com/2018/day/5

from util import *


data = get_data(5, split=False)



def p1(lines):
    lines = lines.strip()

    for c in lines:
        lines = lines.replace(c.lower() + c.upper(), "")
        lines = lines.replace(c.upper() + c.lower(), "")

    return len(lines)


def p2(lines):
    lines = lines.strip()

    polymers = set(c.lower() for c in lines)

    return min(p1(lines.replace(p.lower(), "").replace(p.upper(), "")) for p in polymers)


print("Part1: ", p1(data))
print("Part2: ", p2(data))

p1_tests = [
    ("aA", 0),
    ("abBA", 0),
    ("abAB", 4),
    ("aabAAB", 6),
    ("dabAcCaCBAcCcaDA", 10)
]

p2_tests = [
    ("dabAcCaCBAcCcaDA", 4)
]

run_tests(p1, p1_tests, delim=None)
run_tests(p2, p2_tests, delim=None)
