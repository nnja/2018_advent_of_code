# Advent of Code Day 6
# https://adventofcode.com/2018/day/6

from util import *


data_split = get_data(6, split=True)


def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return abs(x1 - x2) + abs(y1 - y2)


def p1(lines):
    points_to_area = defaultdict(int)
    infinite = set()
    points = [tuple(map(int, line.split(', '))) for line in lines]

    min_x = min(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_x = max(point[0] for point in points)
    max_y = max(point[1] for point in points)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            distances_to_points = [
                (manhattan_distance((x, y), point), points.index(point)) for point in points]
            min_distance, min_point = min(
                distances_to_points, key=lambda x: x[0])

            if x == max_x or y == max_y or x == min_x or y == min_y:
                infinite.add(min_point)

            distances = [d[0] for d in distances_to_points]
            has_dupes = distances.count(min_distance) > 1
            if not has_dupes:
                points_to_area[min_point] += 1

    areas_not_infinate = [
        item for item in points_to_area.items() if item[0] not in infinite]
    return max([entry[1] for entry in areas_not_infinate])


def p2(lines):
    points = [tuple(map(int, line.split(', '))) for line in lines]

    min_x = min(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_x = max(point[0] for point in points)
    max_y = max(point[1] for point in points)

    count = 0

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):

            total_dist = sum([manhattan_distance((x, y), point) for point in points])

            if total_dist < MAX_REGION:
                count+= 1

    return count


MAX_REGION = 10000
print("Part1: ", p1(data_split))
print("Part2: ", p2(data_split))

p1_test_data = [
    "1, 1",
    "1, 6",
    "8, 3",
    "3, 4",
    "5, 5",
    "8, 9",
]
p1_tests = [
    (p1_test_data, 17)
]

p2_tests = [
    (p1_test_data, 16)
]

MAX_REGION = 32
run_tests(p1, p1_tests)
run_tests(p2, p2_tests)
