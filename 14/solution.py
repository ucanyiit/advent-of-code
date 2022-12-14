import sys

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]
SAND_START = (500, 0)

def parse_point(s):
    return tuple(map(int, s.split(",")))

def parse_rock(line):
    return list(map(parse_point, line.split("->")))

def parse_rocks(f):
    return list(map(parse_rock, f.readlines()))

def get_filled_points(f):
    rocks = parse_rocks(f)
    filled_points = {}

    for rock in rocks:
        for i in range(len(rock) - 1):
            p1, p2 = rock[i], rock[i + 1]

            x_range = range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
            y_range = range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)

            for x in x_range:
                for y in y_range:
                    filled_points[(x, y)] = True

    return filled_points

def simulate_sand(filled_points, downest_point, part2=False):
    sand_count = 0

    while True:
        sand = SAND_START
        while True:
            if not part2 and sand[1] >= downest_point[1]:
                return sand_count
            if part2 and sand == SAND_START and sand in filled_points:
                return sand_count

            down = (sand[0], sand[1] + 1)
            down_left = (sand[0] - 1, sand[1] + 1)
            down_right = (sand[0] + 1, sand[1] + 1)

            if part2 and sand[1] == downest_point[1] + 1:
                filled_points[sand] = True
                sand_count += 1
                break
            elif not down in filled_points:
                sand = down
            elif not down_left in filled_points:
                sand = down_left
            elif not down_right in filled_points:
                sand = down_right
            else:
                filled_points[sand] = True
                sand_count += 1
                break

def solution(f, part2):
    filled_points = get_filled_points(f)
    downest_point = max(filled_points.keys(), key=lambda p: p[1])

    return simulate_sand(filled_points, downest_point, part2)

def problem1(f):
    return solution(f, False)

def problem2(f):
    return solution(f, True)

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
