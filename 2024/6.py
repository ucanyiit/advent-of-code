from functools import cmp_to_key

START = "^"

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

visited = {}
patrol_size = 1
with open("6.in") as f:
    lines = f.readlines()
    grid = []
    point = None
    cur_direction = 0

    for i in range(len(lines)):
        line = lines[i].strip()
        grid.append(list(line))
        for j in range(len(line)):
            c = grid[i][j]
            if c == START:
                point = (i, j)
                visited[point] = True
            
    while True:
        new_pos = point[0] + directions[cur_direction][0], point[1] + directions[cur_direction][1]
        if new_pos[0] < 0 or new_pos[0] >= len(grid) or new_pos[1] < 0 or new_pos[1] >= len(grid[0]):
            break
        if grid[new_pos[0]][new_pos[1]] != "#":
            point = new_pos
            visited[point] = True
        else:
            cur_direction = (cur_direction + 1) % 4
            
    print(len(visited))
    
blocks = {}
    
def test_loop(grid, point, cur_direction):
    visited = {}
    
    N = len(grid)
    M = len(grid[0])
    
    while True:
        if (point, cur_direction) in visited and visited[(point, cur_direction)] > 2:
            return True
        visited[(point, cur_direction)] = 1 if (point, cur_direction) not in visited else visited[(point, cur_direction)] + 1
        direction = directions[cur_direction]
        new_pos = point[0] + direction[0], point[1] + direction[1]
        if new_pos[0] < 0 or new_pos[0] >= N or new_pos[1] < 0 or new_pos[1] >= M:
            return False
        if grid[new_pos[0]][new_pos[1]] != "#":
            point = new_pos
        else:
            cur_direction = (cur_direction + 1) % 4


with open("6.in") as f:
    lines = f.readlines()
    grid = []
    point = None
    s = 0
    cur_direction = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        grid.append(list(line))
        for j in range(len(line)):
            c = grid[i][j]
            if c == START:
                point = (i, j)
                visited[point] = True

    N = len(grid)
    M = len(grid[0])
            
    while True:
        direction = directions[cur_direction]
        new_pos = point[0] + direction[0], point[1] + direction[1]
        if new_pos[0] < 0 or new_pos[0] >= N or new_pos[1] < 0 or new_pos[1] >= M:
            break
        if grid[new_pos[0]][new_pos[1]] != "#":
            if grid[new_pos[0]][new_pos[1]] == ".":
                grid[new_pos[0]][new_pos[1]] = "#"
                if new_pos not in blocks:
                    blocks[new_pos] = test_loop(grid, point, cur_direction)
                grid[new_pos[0]][new_pos[1]] = "."
            point = new_pos
            visited[point] = True
        else:
            cur_direction = (cur_direction + 1) % 4
            
    s = 0
    
    for block in blocks:
        if blocks[block]:
            s += 1
            
    print(s)
        