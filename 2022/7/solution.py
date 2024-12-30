import sys

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]
FILE_SIZE_LIMIT = 100000
FILE_SIZE_NEEDS_TO_BE_LESS_THAN = 40000000

result_1 = 0
directory_sizes = []

def add_to_fs(fs, cur_dir, size, file_name):
    if len(cur_dir) == 0:
        fs[file_name] = size
    else:
        if cur_dir[0] not in fs:
            fs[cur_dir[0]] = {}
        add_to_fs(fs[cur_dir[0]], cur_dir[1:], size, file_name)

def get_filesize_total(fs, lim):
    total = 0

    for key in fs:
        total += fs[key] if isinstance(fs[key], int) else get_filesize_total(fs[key], lim)

    if total <= lim:
        global result_1 
        result_1 += total

    directory_sizes.append(total)

    return total

def create_fs(f):
    lines = f.readlines()

    file_system = {}
    cur_dir = []
    i = 0

    while i < len(lines):
        command = lines[i].split()
        if command[0] != '$':
            break
        if command[1] == 'cd':
            if command[2] == '..':
                cur_dir.pop()
            else:
                cur_dir.append(command[2])
            i += 1
        elif command[1] == 'ls':
            while i + 1 < len(lines):
                i += 1
                command = lines[i].split()

                if command[0] == '$':
                    break
                elif command[0] == 'dir':
                    continue
                else:
                    add_to_fs(file_system, cur_dir, int(command[0]), command[1])

    return file_system

def problem1(f):
    file_system = create_fs(f)

    get_filesize_total(file_system, FILE_SIZE_LIMIT)

    return result_1

def problem2(f):
    file_system = create_fs(f)

    total_size = get_filesize_total(file_system['/'], FILE_SIZE_LIMIT)
    current_min = total_size

    for directory_size in directory_sizes:
        adequeate_size = total_size - directory_size < FILE_SIZE_NEEDS_TO_BE_LESS_THAN
        if adequeate_size and directory_size < current_min:
            current_min = directory_size

    return current_min

with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
