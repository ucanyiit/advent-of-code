import sys
from functools import cmp_to_key

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]

def parse_string_list(s):
    if s[0] == '[' and s[-1] == ']':
        s = s[1:-1]
    else:
        raise ValueError('Invalid string list')

    result = []
    inner_list = ""
    inner_list_stack = 0
    cur_val = ""

    for c in s:
        if c == '[':
            inner_list += '['
            inner_list_stack += 1
        elif c == ']':
            inner_list += ']'
            inner_list_stack -= 1
            if inner_list_stack == 0:
                result.append(parse_string_list(inner_list))
                inner_list = ""
        elif inner_list != '':
            inner_list += c
        elif c == ',':
            if cur_val == '':
                continue
            result.append(int(cur_val))
            cur_val = ''
        else:
            cur_val += c

    if inner_list != '':
        result.append(parse_string_list(inner_list))
    if cur_val != '':
        result.append(int(cur_val))

    return result

def get_list_pairs(f):
    lines = f.readlines()
    lists = []
    cur_list_pair = []

    for line in lines:
        if line == '\n':
            continue

        cur_list_pair.append(parse_string_list(line.strip()))

        if len(cur_list_pair) == 2:
            lists.append(cur_list_pair)
            cur_list_pair = []

    return lists

def get_all_lists(f):
    lines = f.readlines()
    lists = []

    for line in lines:
        if line == '\n':
            continue
        lists.append(parse_string_list(line.strip()))

    return lists

def compare_lists(list1, list2):
    if len(list2) == 0 and len(list1) > 0:
        return 1
    if len(list2) == 0 and len(list1) == 0:
        return 0
    if len(list1) == 0 and len(list2) >= 0:
        return -1

    if isinstance(list1[0], list) or isinstance(list2[0], list):
        list1_item = list1[0]
        list2_item = list2[0]

        if not isinstance(list1_item, list):
            list1_item = [list1_item]
        if not isinstance(list2_item, list):
            list2_item = [list2_item]

        result = compare_lists(list1_item, list2_item)

        if result == 0:
            return compare_lists(list1[1:], list2[1:])

        return result

    if list1[0] > list2[0]:
        return 1
    if list1[0] < list2[0]:
        return -1
    if list1[0] == list2[0]:
        return compare_lists(list1[1:], list2[1:])

    raise ValueError('Invalid comparison')

def problem1(f):
    lists = get_list_pairs(f)

    comparisons = list(map(
        lambda x: compare_lists(x[0], x[1]),
        lists
    ))

    comparison_indexes = list(map(
        lambda x: x[0] + 1,
        filter(lambda x: x[1] != 1 , enumerate(comparisons))
    ))

    return sum(comparison_indexes)

def problem2(f):
    lists = sorted(get_all_lists(f), key=cmp_to_key(compare_lists))
    place2, place6 = -1, -1

    for i, l in enumerate(lists):
        if place2 == - 1 and compare_lists(l, [[2]]) != -1:
            place2 = i + 1
        elif place6 == -1 and compare_lists(l, [[6]]) != -1:
            place6 = i + 2

    return place2 * place6

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
