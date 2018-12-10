# Advent of Code Day 10
# https://adventofcode.com/2018/day/10
# Answers:
# Part1: FPZKLJZG
# Part2: 10867

from util import *

data_split = get_data(10)


def p1(lines):

    points = list(map(extract_ints, lines))
    s = 0
    min_bounding_box = 100000000000000  # probably a cleaner way to do this, but eh...

    while True:
        points_in_second = [(p[0] + (p[2] * s), p[1] + (p[3] * s)) for p in points]

        min_x = min(points_in_second, key=lambda p: p[0])[0]
        min_y = min(points_in_second, key=lambda p: p[1])[1]
        max_x = max(points_in_second, key=lambda p: p[0])[0]
        max_y = max(points_in_second, key=lambda p: p[1])[1]

        bounding_box = (abs(min_x) + max_x) * (abs(min_y) + max_y)

        if bounding_box > min_bounding_box:
            break
        else:
            min_bounding_box = bounding_box
            s += 1

    log("Minimum second:", s)

    # I have an off by 1 error, so subtract 1 from final seconds
    s-= 1

    points_in_second = [(p[0] + (p[2] * s), p[1] + (p[3] * s)) for p in points]

    min_x = min(p[0] for p in points_in_second)
    min_y = min(p[1] for p in points_in_second)

    # Board size is a guess
    max_x = 65
    max_y = 10
    
    row = ['.'] * max_x
    board = [row[:] for _ in range(max_y)]

    for x, y in points_in_second:
        board[y - min_y][x - min_x] = '#'

    print("Part1:")
    print_board(board)
    print("Part2: ", s)


def print_board(board):
    for row in board:
        print("".join(row))


p1(data_split)

p1_input = (
"""
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
"""
)

p1_tests = [
    (p1_input, None)
]

run_tests(p1, p1_tests)
