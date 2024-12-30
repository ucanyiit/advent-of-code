import sys

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]

def problem1(file):
    data = file.read().splitlines()
    max_elf = 0
    cur_elf = 0
    for line in data:
        if line == "":
            cur_elf = 0
            continue
        cur_elf += int(line)
        if cur_elf > max_elf:
            max_elf = cur_elf
    return max_elf

def problem2(file):
    data = file.read().splitlines()
    elves = []
    cur_elf = 0
    for line in data:
        if line == "":
            elves.append(cur_elf)
            cur_elf = 0
            continue
        cur_elf += int(line)
    elves.append(cur_elf)
    elves.sort()
    return elves[-1] + elves[-2] + elves[-3]

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
