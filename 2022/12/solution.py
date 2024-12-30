import sys

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]

def search_grid(grid, c):
    for i, line in enumerate(grid):
        for j, cur_c in enumerate(line):
            if cur_c == c:
                return i, j

    raise Exception("Not found")

def get_char_val(c):
    if c == 'S':
        return ord('a')
    elif c == 'E':
        return ord('z')
    else:
        return ord(c)

def check_bounds(x, y, grid):
    return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])

def solution(f, check_for_all_a):
    grid = [line.strip() for line in f.readlines()]

    start = search_grid(grid, "S")
    end = search_grid(grid, "E")

    step_queue = [(end, 0)]
    steps_to = {}

    while len(step_queue) > 0:
        (x, y), step = step_queue.pop(0)
        if (x, y) == start or (check_for_all_a and grid[x][y] == 'a'):
            return step
        if (x, y) in steps_to and steps_to[(x, y)] <= step:
            continue
        steps_to[(x, y)] = step
        cur_val = get_char_val(grid[x][y])
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 and j != 0) or not check_bounds(x + i, y + j, grid):
                    continue
                val = get_char_val(grid[x + i][y + j])
                if val < cur_val - 1:
                    continue
                step_queue.append(((x + i, y + j), step + 1))

    raise Exception("No solution")

def problem1(f):
    return solution(f, False)

def problem2(f):
    return solution(f, True)

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
