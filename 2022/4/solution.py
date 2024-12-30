import sys

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]

def problem1(f):
    lines = f.readlines()
    result = 0

    for line in lines:
        str_ranges = line.replace("\n", "").split(',')
        ranges = list(map(lambda x: x.split('-'), str_ranges))
        range1 = list(map(int, ranges[0]))
        range2 = list(map(int, ranges[1]))

        if range1[0] <= range2[0] and range1[1] >= range2[1]:
            result += 1
        elif range2[0] <= range1[0] and range2[1] >= range1[1]:
            result += 1

    return result

def problem2(f):
    lines = f.readlines()
    result = 0

    for line in lines:
        str_ranges = line.replace("\n", "").split(',')
        ranges = list(map(lambda x: x.split('-'), str_ranges))
        range1 = list(map(int, ranges[0]))
        range2 = list(map(int, ranges[1]))

        if range1[0] <= range2[0] and range1[1] >= range2[0]:
            result += 1
        elif range2[0] <= range1[0] and range2[1] >= range1[0]:
            result += 1

    return result

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
