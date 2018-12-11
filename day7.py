# Advent of Code Day 7
# https://adventofcode.com/2018/day/7
# Answers
# Part1: BDHNEGOLQASVWYPXUMZJIKRTFC
# Part2: 1107

from util import *

data_split = get_data(7, split=True)


def p1(lines):
    """
    Got stuck on this one. 
    Solution is based on:
    https://www.reddit.com/r/adventofcode/comments/a3wmnl/2018_day_7_solutions/ebchy1a/
    """

    rules = defaultdict(list)
    for l in lines:
        first, last = l[36], l[5]

        rules[first].append(last)
        if last not in rules:
            rules[last] = []

    result = ''

    while rules:
        lowest_eligible = sorted(k for k, v in rules.items() if len(v) == 0)[0]
        del rules[lowest_eligible]
        for k in rules:
            if lowest_eligible in rules[k]:
                rules[k].remove(lowest_eligible)
        result += lowest_eligible

    return result


def p2(lines, seconds_plus=0, num_workers=2):
    """
    Got stuck here too. 
    Solution based on networkx, and:
    https://www.reddit.com/r/adventofcode/comments/a3wmnl/2018_day_7_solutions/ebgd6oc/
    """
    G = DiGraph()
    for l in lines:
        G.add_edge(l[5], l[36])

    for node in G.nodes:
        G.nodes[node]['work'] = (ord(node) - ord('A')) + 1 + seconds_plus

    time = 0
    while G.nodes:
        eligibles = sorted([n for n in G.nodes if G.in_degree(n) == 0],
                           key=lambda n: G.nodes[n]['work'])

        for worker, node in zip(range(num_workers), eligibles):
            G.nodes[node]['work'] -= 1

            if G.nodes[node]['work'] == 0:
                G.remove_node(node)

        time += 1

    return time


print("Part1: ", p1(data_split))
print("Part2: ", p2(data_split, seconds_plus=60, num_workers=5))

p1_test_data = [
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
]

p1_tests = [
    (p1_test_data, "CABDFE")
]

p2_tests = [
    (p1_test_data, 16)
]

run_tests(p1, p1_tests)
run_tests(p2, p2_tests)
