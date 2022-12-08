import sys

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]

def get_trees(f):
    lines = f.readlines()
    trees = []

    for line in lines:
        tree_line = []
        for char in line:
            if char == '\n':
                continue
            tree_line.append(int(char))
        trees.append(tree_line)

    return trees

def is_visible(trees, y, x):
    tree_value = trees[y][x]

    for i in range(y + 1, len(trees)):
        if trees[i][x] >= tree_value:
            break
    else:
        return 1

    for i in range(y - 1, -1, -1):
        if trees[i][x] >= tree_value:
            break
    else:
        return 1

    for i in range(x + 1, len(trees[0])):
        if trees[y][i] >= tree_value:
            break
    else:
        return 1

    for i in range(x - 1, -1, -1):
        if trees[y][i] >= tree_value:
            break
    else:
        return 1

    return 0

def get_score(trees, y, x):
    score = 1
    tree_value = trees[y][x]

    cur_score = 0
    for i in range(y + 1, len(trees)):
        cur_score += 1
        if trees[i][x] >= tree_value:
            break
    score *= cur_score

    cur_score = 0
    for i in range(y - 1, -1, -1):
        cur_score += 1
        if trees[i][x] >= tree_value:
            break
    score *= cur_score

    cur_score = 0
    for i in range(x + 1, len(trees[0])):
        cur_score += 1
        if trees[y][i] >= tree_value:
            break
    score *= cur_score

    cur_score = 0
    for i in range(x - 1, -1, -1):
        cur_score += 1
        if trees[y][i] >= tree_value:
            break
    score *= cur_score

    return score

def problem1(f):
    trees = get_trees(f)
    result = 0

    for i, tree in enumerate(trees):
        for j, _ in enumerate(tree):
            result += is_visible(trees, i, j)

    return result

def problem2(f):
    trees = get_trees(f)
    result = 0

    for i, tree in enumerate(trees):
        for j, _ in enumerate(tree):
            result = max(get_score(trees, i, j), result)

    return result

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
