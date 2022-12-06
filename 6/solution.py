import sys
import re

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]

def has_an_element_more_than_once(list1):
    return len(list1) != len(set(list1))

def problem1(f):
    line = f.readlines()[0]

    for i in range(len(line)):
        last_4_chars = line[i-4:i]
        if i > 3 and not has_an_element_more_than_once(last_4_chars):
            return i

def problem2(f):
    line = f.readlines()[0]

    for i in range(len(line)):
        last_14_chars = line[i-14:i]
        if i > 13 and not has_an_element_more_than_once(last_14_chars):
            return i

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
