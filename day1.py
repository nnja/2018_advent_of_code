from util import *


def p1(vals):
    return sum(map(int, vals))


print("Part1 result: ", p1(get_data(1)))


def p2(vals):
    seen = set()
    curr = 0

    while True:
        seen.add(curr)
        for i in map(int, vals):
            curr += i

            if curr in seen:
                return curr
            else:
                seen.add(curr)


print("Part2 result: ", p2(get_data(1)))

# Tests

p2_tests = [
    ("+1, -1", 0),
    ("+1, -2, +3, +1", 2),
    ("+3, +3, +4, -2, -4", 10),
    ("-6, +3, +8, +5, -6", 5),
    ("+7, +7, -2, -7, -4", 14),
]
run_tests(p2, p2_tests, delim=", ")