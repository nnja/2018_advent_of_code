# Advent of Code Day 8
# https://adventofcode.com/2018/day/8

from util import *

data = get_data(8, split=False)

Node = namedtuple("Node", ["name", "parent", "children", "metadata", "expected_children", "expected_metadata"])
node_cost = {}

def cost(node):
    if not node.children:
        node_cost[node.name] = sum(node.metadata)
    else:
        node_cost[node.name] = sum(node_cost[node.children[i-1].name] for i in node.metadata if i -1 < len(node.children))
    return cost


def both(lines):
    nums = list(map(int, lines.split(" ")))

    node_name = chr(65)
    n_children, n_md = nums[0], nums[1]
    curr = root = Node(node_name, None, list(), list(), n_children, n_md)

    pos = 2
    meta_data_sum = 0

    while pos < len(nums):
        if len(curr.children) < curr.expected_children:  # next val is a child
            node_name = chr(ord(node_name) + 1)
            n_children, n_metadata = nums[pos], nums[pos+1]
            node = Node(node_name, curr, [], [], n_children, n_metadata)
            curr.children.append(node)
            curr = node
            pos+= 2
        elif len(curr.metadata) < curr.expected_metadata:  # next val is metadata
            metadata = int(nums[pos])
            meta_data_sum += metadata
            curr.metadata.append(metadata)
            pos+= 1
        else:
            cost(curr)
            curr = curr.parent
    
    cost(root)

    part1 = meta_data_sum
    part2 = node_cost[root.name]
    
    return(part1, part2)


print("Part1 and Part2: ", both(data))


both_tests = [
    ("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2", (138, 66)),
]

run_tests(both, both_tests, delim=None)
