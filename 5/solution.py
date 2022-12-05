import sys
import re

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]
SEARCH_TEXT = "move (.+?) from (.+?) to (.+?)"

def create_stacks(stack_lines):
    stacks = []

    for char in stack_lines[-1]:
        if char != ' ' and char != '\n':
            stacks.append([])

    for line in stack_lines[:-1]:
        for i in range(len(line)):
            if (i % 4 == 1) and line[i] != ' ':
                stacks[i // 4].append(line[i])
    
    for i in range(len(stacks)):
        stacks[i] = stacks[i][::-1]

    return stacks


def solve(f, move_function):
    lines = f.readlines()
    stack_lines = []
    stacks = []

    for line in lines:
        if line == "\n":
            stacks = create_stacks(stack_lines)
        elif len(stacks) == 0:
            stack_lines.append(line)
        else:
            match = re.search(SEARCH_TEXT, line)
            from_stack = int(match.group(2)) - 1
            to_stack = int(match.group(3)) - 1
            amount = int(match.group(1))

            stacks = move_function(amount, from_stack, to_stack, stacks)

    result = "".join(list(map(lambda x: x[-1], stacks)))

    return result

def problem1(f):
    def move_function(amount, from_stack, to_stack, stacks):
        for _ in range(amount):
            stacks[to_stack].append(stacks[from_stack].pop())
        
        return stacks

    return solve(f, move_function)

def problem2(f):
    def move_function(amount, from_stack, to_stack, stacks):
        for element in stacks[from_stack][-amount:]:
            stacks[to_stack].append(element)

        for _ in range(amount):
            stacks[from_stack].pop()
        
        return stacks

    return solve(f, move_function)

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
