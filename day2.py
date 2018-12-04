from util import *

data = get_data(2)


def p1(input):
    twice = 0
    thrice = 0

    for line in input:
        vals_map = defaultdict(int)
        for char in line:
            vals_map[char] += 1

        if 2 in vals_map.values():
            twice += 1
        if 3 in vals_map.values():
            thrice += 1

    return twice * thrice


def p1_alt(lines):
    """
    Part1: Much less efficient, but much shorter solution.
    """
    pairs = [(2 in Counter(line).values(), 3 in Counter(line).values())
             for line in lines]
    return sum(pair[0] for pair in pairs) * sum(pair[1] for pair in pairs)


print("Part 1: ", p1(data), " alt solution: ", p1_alt(data))


def p2(input):
    pos = 1

    for line in input:
        for compr in input[pos:]:
            new_str = ""

            # compare letter by letter, count the diffs
            letter_pairs = zip((c for c in line), (c for c in compr))
            for pair in letter_pairs:
                if pair[0] == pair[1]:
                    new_str += pair[0]

            if len(line) - len(new_str) == 1:
                return new_str
        pos += 1


def p2_alt(input):
    combos = combinations(input, 2)
    for combo in combos:
        if sum(map(lambda x, y: x != y, combo[0], combo[1])) == 1:
            return "".join([x for x, y in zip(combo[0], combo[1]) if x == y])


print("Part 2: ", p2(data), " alt solution: ", p2_alt(data))

# Tests

p1_test_input = [
    "abcdef",
    "bababc",
    "abbcde",
    "abcccd",
    "aabcdd",
    "abcdee",
    "ababab",
]

p1_tests = [
    (p1_test_input, 12)
]
run_tests(p1, p1_tests)

p2_test_input = [
    "abcde",
    "fghij",
    "klmno",
    "pqrst",
    "fguij",
    "axcye",
    "wvxyz",
]

p2_tests = [
    (p2_test_input, "fgij")
]
run_tests(p2, p2_tests)
