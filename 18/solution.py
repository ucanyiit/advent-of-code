import sys

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]
MAX_INPUT = 22

def parse_point(s):
    return tuple(map(int, s.split(",")))

def out_of_bounds(x, y, z):
    return x <= 0 or y <= 0 or z <= 0 or x >= MAX_INPUT or y >= MAX_INPUT or z >= MAX_INPUT

def apply_function_to_nearby(x, y, z, f):
    result = 0

    for d_x in range(-1, 2):
        for d_y in range(-1, 2):
            for d_z in range(-1, 2):
                if abs(d_x) + abs(d_y) + abs(d_z) != 1:
                    continue

                d_result = f(x + d_x, y + d_y, z + d_z)

                if d_result is not None:
                    result += d_result

    return result

def check_pocket(x, y, z, has_cube, has_pocket):
    if (x, y, z) in has_pocket:
        return has_pocket[(x, y, z)]

    q = [(x, y, z)]
    pocket = {}

    while q:
        x, y, z = q.pop()
        if (x, y, z) in has_cube:
            continue

        pocket[(x, y, z)] = True

        if out_of_bounds(x, y, z):
            for val in pocket:
                has_pocket[val] = False
            return

        else:
            def f(x, y, z):
                if (x, y, z) not in pocket:
                    q.append((x, y, z))

            apply_function_to_nearby(x, y, z, f)

    for val in pocket:
        has_pocket[val] = True

    return


def check_sides(x, y, z, has_cube, part2 = False, has_pocket = {}):
    result = 0

    def f(x, y, z):
        if part2:
            check_pocket(x, y, z, has_cube, has_pocket)
        if (x, y, z) in has_cube:
            return -1

    result += apply_function_to_nearby(x, y, z, f)

    return result

def solution(f, part2):
    cubes = list(map(parse_point, f.readlines()))
    has_cube = {}
    has_pocket = {}
    result = 0

    for x, y, z in cubes:
        has_cube[(x, y, z)] = True

    for x, y, z in cubes:
        result += 6 + check_sides(x, y, z, has_cube, part2, has_pocket)

    if not part2:
        return result

    for x, y, z in has_pocket:
        if has_pocket[(x, y, z)]:
            result += check_sides(x, y, z, has_cube)

    return result

def problem1(f):
    return solution(f, False)

def problem2(f):
    return solution(f, True)

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
