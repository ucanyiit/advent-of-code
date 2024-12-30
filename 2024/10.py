DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

with open("10.in") as f:

    starts = []
    lines = f.readlines()
    grid = []
    for i in range(len(lines)):
        line = lines[i]
        grid.append(list(line.strip()))
        for j in range(len(line)):
            c = line[j]
            if c == "0":
                # print(i,j,c)
                starts.append((i, j))
                
    total_end_count = 0
    for start in starts:
        visited = {}
        reachable_9_count = 0
        q = [start]
        while len(q) > 0:
            i, j = q.pop(0)
            val = int(grid[i][j])
            
            for direction in DIRECTIONS:
                new_i = i + direction[0]
                new_j = j + direction[1]
                
                if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
                    continue
                
                new_val = int(grid[new_i][new_j])
                
                if (new_i, new_j) in visited or (new_val != val + 1):
                    continue
                
                visited[(new_i, new_j)] = True
                
                if new_val == 9:
                    reachable_9_count += 1
                    continue
                
                q.append((new_i, new_j))
        total_end_count += reachable_9_count
        
    print(total_end_count)
            

def get_distinct_count(i, j, visited, grid):
    if grid[i][j] == "9":
        return 1
    
    if (i, j) in visited:
        return visited[(i, j)]
    
    val = int(grid[i][j])
    count = 0
    for direction in DIRECTIONS:
        new_i = i + direction[0]
        new_j = j + direction[1]
        
        if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
            continue
        
        new_val = int(grid[new_i][new_j])
        
        if new_val == val + 1:
            count += get_distinct_count(new_i, new_j, visited, grid)
            
    visited[(i, j)] = count
    
    return count

with open("10.in") as f:

    starts = []
    lines = f.readlines()
    grid = []
    for i in range(len(lines)):
        line = lines[i]
        grid.append(list(line.strip()))
        for j in range(len(line)):
            c = line[j]
            if c == "0":
                # print(i,j,c)
                starts.append((i, j))
                
    total_end_count = 0
    for start in starts:
        visited = {}
        total_end_count += get_distinct_count(start[0], start[1], visited, grid)
        
    print(total_end_count)