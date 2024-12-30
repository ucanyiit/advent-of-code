visited = set()
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
grid = []

def get_sides(x, y):
    v = grid[x][y]
    sides = []
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != v:
           sides.append((dx, dy))
           
    return sides

def get_perimeter_and_size(x, y, perimeter, size):
    v = grid[x][y]
    size += 1
    sides = get_sides(x, y)
           
    sides_of_side = []
    for dx, dy in DIRECTIONS[:2]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != v:
            continue
        sides_of_side += get_sides(nx, ny)
                
    for side in sides:
        if side not in sides_of_side:
            perimeter += 1

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
            continue
        if grid[nx][ny] == v:
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                perimeter, size = get_perimeter_and_size(nx, ny, perimeter, size)
    
    
    return perimeter, size

with open("12.in") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        grid.append(list(lines[i].strip()))
        
    total_price = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in visited:
                continue
            visited.add((i, j))
            perimeter, size = get_perimeter_and_size(i, j, 0, 0)
            print(grid[i][j], perimeter, size)
            total_price += perimeter * size
            
    print(total_price)