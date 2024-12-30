N = 0
M = 0

nodes = {}

def in_bounds(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

def calculate_nodes(i, j, locations):
    for loc in locations:
        new_location = (i + (i - loc[0]), j + (j - loc[1]))
        if in_bounds(new_location[0], new_location[1]) and new_location not in nodes:
            nodes[new_location] = True
        new_location = (loc[0] + (loc[0] - i), loc[1] + (loc[1] - j))
        if in_bounds(new_location[0], new_location[1]) and new_location not in nodes:
            nodes[new_location] = True

def calculate_nodes2(i, j, locations):
    for loc in locations:
        
        dif = (i - loc[0], j - loc[1])
        new_location = (i, j)
        
        while True:
            if not in_bounds(new_location[0], new_location[1]):
                break
            if new_location not in nodes:
                nodes[new_location] = True
            new_location = (new_location[0] + dif[0], new_location[1] + dif[1])
            
        dif = (loc[0] - i, loc[1] - j)
        new_location = (loc[0], loc[1])
        
        while True:
            if not in_bounds(new_location[0], new_location[1]):
                break
            if new_location not in nodes:
                nodes[new_location] = True
            new_location = (new_location[0] + dif[0], new_location[1] + dif[1])

with open("8.in") as f:
    lines = f.readlines()
    grid = []
    letter_map = {}
    
    N = len(lines)
    M = len(lines[0].strip())
    
    s = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        grid.append(list(line))
        for j in range(len(line)):
            c = line[j]
            if c == ".":
                continue
            if c in letter_map:
                calculate_nodes2(i, j, letter_map[c])
                letter_map[c].append((i, j))
            else:
                letter_map[c] = [(i, j)]
            
    print(len(nodes))