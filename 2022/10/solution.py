import sys

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]

def addx(x, y, i):
    return x + y, 2

def apply_command(i, x, command):
    if command[0] == 'addx':
        return addx(x, int(command[1]), i)
    return x, 1

def problem1(f):
    lines = f.readlines()
    x = 1
    i = 1
    signal_str = 0
    next_cycle = 20

    for line in lines:
        command = line.split(' ')
        next_x, cycle = apply_command(i, x, command)

        if i + cycle >= next_cycle:
            signal_str += next_cycle * (x if i + cycle > next_cycle else next_x)
            next_cycle += 40

        x = next_x
        i += cycle

    return signal_str

def draw_cycle(current_line, sprite_pos, cur_cycle):
    if abs(sprite_pos - cur_cycle) < 2:
        current_line.append("#")
    else:
        current_line.append(".")
    return cur_cycle + 1

def problem2(f):
    lines = f.readlines()
    crt_lines = []
    cur_cycle = 0
    current_line = []
    sprite_pos = 1
    i = 1

    for line in lines:
        command = line.split(' ')
        next_x, cycle = apply_command(i, sprite_pos, command)

        for i in range(cycle):
            cur_cycle = draw_cycle(current_line, sprite_pos, cur_cycle)
            if cur_cycle == 40:
                cur_cycle = 0
                crt_lines.append(current_line)
                current_line = []

        sprite_pos = next_x

    for line in crt_lines:
        print("".join(line))

    return None

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
