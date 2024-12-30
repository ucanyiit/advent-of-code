CHECK_WORD = "XMAS"


checks = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, -1), (0, -2), (0, -3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
    [(0, 0), (1, -1), (2, -2), (3, -3)],
    [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
]

def check(grid, x, y, limx, limy):
    s = 0
    for check in checks:
        word = ""
        for c in check:
            if c[0] + x < 0 or c[1] + y < 0 or c[0] + x >= limx or c[1] + y >= limy:
                break
            word += grid[y + c[1]][x + c[0]]
        if word == CHECK_WORD:
            s += 1
    return s

with open("4.in") as f:
    lines = f.readlines()
    
    s = 0
    grid = []
    
    for line in lines:
        grid.append(line.strip())
            
    for i in range(len(grid)):
        for j in range(len(line)):
            s += check(grid, i, j, len(line), len(grid))
            
    print(s)
        
CHECK_WORD_2 = "MAS"

checks = [
    [
        [(0, 0), (1, 1), (2, 2)], 
        [(2, 0), (1, 1), (0, 2)]
    ],
    [
        [(0, 0), (1, 1), (2, 2)], 
        [(0, 2), (1, 1), (2, 0)]
    ],
    [
        [(0, 0), (-1, 1), (-2, 2)],
        [(-2, 0), (-1, 1), (0, 2)]
    ],
    [
        [(0, 0), (-1, 1), (-2, 2)],
        [(0, 2), (-1, 1), (-2, 0)]
    ],
    [
        [(0, 0), (1, -1), (2, -2)],
        [(2, 0), (1, -1), (0, -2)]
    ],
    [
        [(0, 0), (1, -1), (2, -2)],
        [(0, -2), (1, -1), (2, 0)]
    ],
    [
        [(0, 0), (-1, -1), (-2, -2)],
        [(-2, 0), (-1, -1), (0, -2)]
    ],
    [
        [(0, 0), (-1, -1), (-2, -2)],
        [(0, -2), (-1, -1), (-2, 0)]
    ],
]

def check_2(grid, x, y, limx, limy):
    s = 0
    for check_group in checks:
        cs = 0
        for (i, check) in enumerate(check_group):
            word = ""
            for c in check:
                if c[0] + x < 0 or c[1] + y < 0 or c[0] + x >= limx or c[1] + y >= limy:
                    break
                word += grid[y + c[1]][x + c[0]]
            if word == CHECK_WORD_2:
                cs += 1
        print(cs, x, y)
        if cs == 2:
            s += 1
    return s

with open("4.in") as f:
    lines = f.readlines()
    
    s = 0
    grid = []
    
    for line in lines:
        grid.append(line.strip())
            
    for i in range(len(grid)):
        for j in range(len(line)):
            s += check_2(grid, i, j, len(line), len(grid))
            # break
        # break
            
    print(s)
        
