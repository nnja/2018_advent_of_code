# Advent of Code Day 11
# https://adventofcode.com/2018/day/11
# Answers:
# Part1: 20,51
# Part2: 230,272,17

from multiprocessing import Pool

from util import *

grid_size = 300
num = 7803


def get_power(num, cell):
    # assert get_power(8, (3, 5)) == 4
    # assert get_power(71, (101, 153)) == 4
    # assert get_power(57, (122, 79)) == -5
    # assert get_power(39, (217, 196)) == 0
    x, y = cell
    rack_id = x + 10
    power_level = rack_id * y
    power_level += int(num)
    power_level *= rack_id
    hundreds_digit = int(str(power_level)[-3]) if len(str(power_level)) >= 3 else 0
    power_level = hundreds_digit - 5
    return power_level


def p1(grid_size=300):
    power_levels = {}

    for x in range(300):
        for y in range(300):
            power_levels[(x, y)] = get_power(num, (x, y))

    max_point = (-1, -1)
    max_power_level = 0

    # Not the most efficient implementation, but it works!
    for x in range(300):
        for y in range(300):
            power_level_sum = 0
            if x < (300 - grid_size) and y < (300 - grid_size):
                for new_x in range(x, x+grid_size):
                    for new_y in range(y, y+grid_size):
                        power_level_sum += power_levels[(new_x, new_y)]
                if power_level_sum > max_power_level:
                    max_power_level = power_level_sum
                    max_point = (x, y)

    return max_point, max_power_level, grid_size


def p2():
    """
    Ran this with pypy3 for a major speedup.
    i.e. $ pypy3 day11.py
    """
    # Guess that the largest area is < 30
    sizes = range(1, 30)
    max_point = (0, 0)
    max_power_level = 0

    with Pool(processes=5) as pool:
        results = pool.map(p1, sizes, 5)

    point, power_level, grid_size = max(results, key=lambda x: x[1])
    return f"Point: {point}, Grid Size: {grid_size}"


p1_point, _, _ = p1(3)
print("Part 1 with puzzle input of 7803, size 300", p1_point)
print("Part 2 with 7803", p2())
