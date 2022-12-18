import sys
import re

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]
REGEX_TEXT = "Sensor at x={}, y={}: closest beacon is at x={}, y={}"
TEST_ROW_P1 = 10
INPUT_ROW_P1 = 2000000
TEST_ROW_P2 = 20
INPUT_ROW_P2 = 4000000

def get_row_part1():
    return TEST_ROW_P1 if FILE_NAME == 'sample.in' else INPUT_ROW_P1

def get_row_part2():
    return TEST_ROW_P2 if FILE_NAME == 'sample.in' else INPUT_ROW_P2

def get_beacons(f):
    lines = f.readlines()
    beacons = []
    beacon_map = {}

    for line in lines:
        match = re.match(REGEX_TEXT.format(
            r"(?P<x>-?\d+)", r"(?P<y>-?\d+)", r"(?P<closest_x>-?\d+)", r"(?P<closest_y>-?\d+)"
        ), line)
        if match:
            x = int(match.group("x"))
            y = int(match.group("y"))
            closest_x = int(match.group("closest_x"))
            closest_y = int(match.group("closest_y"))
            beacons.append((
                (x, y),
                abs(x - closest_x) + abs(y - closest_y)
            ))
            beacon_map[(closest_x, closest_y)] = True

    return beacons, beacon_map


def problem1(f):
    beacons, beacon_map = get_beacons(f)
    y = get_row_part1()
    points = {}

    for beacon in beacons:
        x1 = -(beacon[1] - abs(y - beacon[0][1])) + beacon[0][0]
        x2 = +(beacon[1] - abs(y - beacon[0][1])) + beacon[0][0]

        for x in range(x1, x2 + 1):
            if x in points or (x, y) in beacon_map:
                continue
            points[x] = True

    return len(points)

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] + 1 < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged

def problem2(f):
    beacons, beacon_map = get_beacons(f)
    row = get_row_part2()

    for y in range(0, row + 1):
        intervals = []
        for beacon in beacons:
            x1 = -(beacon[1] - abs(y - beacon[0][1])) + beacon[0][0]
            x2 = +(beacon[1] - abs(y - beacon[0][1])) + beacon[0][0]

            intervals.append((x1, x2))

        intervals = merge_intervals(intervals)
        possible_intervals = []
        cur_start = 0

        for interval in intervals:
            if interval[1] < cur_start:
                continue
            if interval[0] > cur_start:
                possible_intervals.append((cur_start, interval[0] - 1))
                cur_start = interval[1] + 1
            else:
                cur_start = interval[1] + 1

        for interval in possible_intervals:
            for x in range(interval[0], interval[1] + 1):
                if (x, y) in beacon_map:
                    continue
                return x * INPUT_ROW_P2 + y

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
