import sys
import pprint

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]
MOVES = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}

def sum_tuples(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

def get_next_position_1_dim(pos1, pos2):
    if pos1 == pos2:
        return pos1
    elif pos1 > pos2:
        return pos1 - 1
    else:
        return pos1 + 1
        
def get_next_position(pos1, pos2):
    next_position_x = get_next_position_1_dim(pos1[0], pos2[0])
    next_position_y = get_next_position_1_dim(pos1[1], pos2[1])
    if pos1[0] > pos2[0] + 1:
        return (pos1[0] - 1, next_position_y)
    elif pos1[0] < pos2[0] - 1:
        return (pos1[0] + 1, next_position_y)
    elif pos1[1] > pos2[1] + 1:
        return (next_position_x, pos1[1] - 1)
    elif pos1[1] < pos2[1] - 1:
        return (next_position_x, pos1[1] + 1)
    else:
        return pos1

def problem1(f):
    lines = f.readlines()
    positions = {(0, 0): True}
    head_position = (0, 0)
    tail_position = (0, 0)

    for _, line in enumerate(lines):
        move = line.split()
        direction = move[0]
        distance = int(move[1])
        for _ in range(distance):
            head_position = sum_tuples(head_position, MOVES[direction])
            tail_position = get_next_position(tail_position, head_position)
            positions[tail_position] = True

    position_count = len(positions)
    return position_count

def problem2(f):
    lines = f.readlines()
    positions = [{(0, 0): True} for _ in range(11)]
    tail_positions = [(0, 0) for _ in range(11)]

    for _, line in enumerate(lines):
        move = line.split()
        direction = move[0]
        distance = int(move[1])
        for _ in range(distance):
            tail_positions[0] = sum_tuples(tail_positions[0], MOVES[direction])
            for i in range(1, 10, 1):
                tail_positions[i] = get_next_position(tail_positions[i], tail_positions[i - 1])
                positions[i][tail_positions[i]] = True

    position_count = len(positions[9])
    return position_count

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
