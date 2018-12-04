from util import *

data = get_data(3)
non_split_data = get_data(3, split=False)


def print_fabric(fabric, fabric_w):
    for chunk in chunks(fabric, fabric_w):
        log(chunk, "\n")


def p1(input):
    fabric_w = 1000
    fabric_h = 1000

    fabric = [0] * fabric_w * fabric_h
    p = re.compile(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)')

    for line in input:
        m = p.match(line)
        _, x, y, w, h = m.groups()

        x = int(x)
        y = int(y)
        width = int(w)
        height = int(h)

        for h in range(height):
            curr_pos = ((y+h) * fabric_w) + x

            # fill from starting point, width times
            for pos in range(curr_pos, curr_pos + width):
                fabric[pos] += 1

    # how many items in the list are greater than or equal 2?
    return sum([n >= 2 for n in fabric])


def p2(input):
    """
    Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single
    square inch of fabric with any other claim.
    If you can somehow draw attention to it, maybe the Elves will be
    able to make Santa's suit after all!

    For example, in the claims above, only claim 3 is intact after all claims are made.
    """
    fabric_w = 1000
    fabric_h = 1000
    fabric = list() * fabric_w * fabric_h

    fabric = []
    for i in range(fabric_w * fabric_h):
        fabric.append(list())

    p = re.compile(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)')
    claim_ids = set()
    intersections = set()

    for line in input:
        m = p.match(line)
        claim_id, x, y, w, h = m.groups()

        claim_ids.add(claim_id)
        x = int(x)
        y = int(y)
        width = int(w)
        height = int(h)

        for h in range(height):
            curr_pos = ((y+h) * fabric_w) + x

            # fill from starting point, width times
            for pos in range(curr_pos, curr_pos + width):

                if fabric[pos] and claim_id not in fabric[pos]:
                    intersections.add(claim_id)
                    intersections.update(fabric[pos])
                fabric[pos].append(claim_id)

    not_itersected = claim_ids - intersections
    log("Not Intersections", not_itersected)
    return list(not_itersected)[0]


def both_alt(input):
    fabric_size = 1000
    fabric = [list() for _ in range(fabric_size ** 2)]

    p = re.compile(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)')
    matches = re.findall(p, input)

    for match in matches:
        claim_id, x, y, w, h = map(int, match)
        for i in range(h):
            curr_pos = ((y + i) * fabric_size) + x
            for pos in range(curr_pos, curr_pos + w):
                fabric[pos].append(claim_id)

    p1 = len([len(square) for square in fabric if len(square) >= 2])

    all_claim_ids = set([int(match[0]) for match in matches])

    for square in fabric:
        if len(square) > 1:
            all_claim_ids = all_claim_ids - set(square)

    p2 = list(all_claim_ids)[0]
    return p1, p2


alt = both_alt(non_split_data)  # alternate solution

print("Part 1: ", p1(data), " alt: ", alt[0])
print("Part 2: ", p2(data), " alt: ", alt[1])

# Tests

test_input = """
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""

p1_tests = [
    (test_input, 4)
]
run_tests(p1, p1_tests)

p2_tests = [
    (test_input, '3')
]
run_tests(p2, p2_tests)

alt_tests = [
    (test_input, (4, 3))
]
run_tests(both_alt, alt_tests, delim=None)
