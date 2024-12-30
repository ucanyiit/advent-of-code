def solve(ax, ay, bx, by, px, py):
    dp = { (px, py): 0 }

    q = [(px, py)]
    
    while len(q) > 0:
        curx, cury = q.pop(0)
        
        # print(curx, cury, dp[curx, cury])

        if curx - ax >= 0 and cury - ay >= 0:
            if (curx - ax, cury - ay) not in dp or dp[curx - ax, cury - ay] < dp[curx, cury] + 3:
                dp[curx - ax, cury - ay] = dp[curx, cury] + 3
                q.append((curx - ax, cury - ay))
            
        if curx - bx >= 0 and cury - by >= 0:
            if (curx - bx, cury - by) not in dp or dp[curx - bx, cury - by] < dp[curx, cury] + 1:
                dp[curx - bx, cury - by] = dp[curx, cury] + 1
                q.append((curx - bx, cury - by))     
                
    # print(dp)   
            
    return 0 if (0, 0) not in dp else dp[(0, 0)]



with open("13.in") as f:
    lines = f.readlines()
    i = 0
    
    res = 0
    
    while i < len(lines):
        a_line = lines[i].strip()
        i+=1
        b_line = lines[i].strip()
        i+=1
        prize_line = lines[i].strip()
        i+=1
        i+=1
        
        a_x = int(a_line.split()[2][2:-1])
        a_y = int(a_line.split()[3][2:])
        b_x = int(b_line.split()[2][2:-1])
        b_y = int(b_line.split()[3][2:])
        prize_x = int(prize_line.split()[1][2:-1])
        prize_y = int(prize_line.split()[2][2:])
        
        res += (solve(a_x, a_y, b_x, b_y, prize_x, prize_y))
        print(a_x, a_y, b_x, b_y, prize_x, prize_y, res)
        
    print(res)