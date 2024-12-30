import re

def find_all_muls(s):
    # find regex with "mul(x,y)"
    # return x * y
    muls = re.findall(r"mul\((\d+),(\d+)\)", s)
    return [int(x) * int(y) for x, y in muls]

def get_answer(s):
    # operations can be "mul(x,y)", "do()", "don't()"
    # return the next operation
    # return None if no operation is found
    r1 = r"mul\((\d+),(\d+)\)"
    r2 = r"do\(\)"
    r3 = r"don't\(\)"
    
    res = 0
    e = True
    
    while s:
        operation = re.search(r1 + "|" + r2 + "|" + r3, s)
        
        if not operation:
            break
        
        s = s[operation.end():]
        
        if operation.group(0) == "do()":
            e = True
        elif not e:
            pass
        elif operation.group(0) == "don't()":
            e = False
        else:
            res += int(operation.group(1)) * int(operation.group(2))
    
    return res

with open("3.in") as f:
    lines = f.readlines()
    
    s = 0
    for line in lines:
        s += sum(find_all_muls(line))
            
    print(s)

with open("3.in") as f:
    lines = f.readlines()
    
    s = 0
    enabled = True
            
    print(get_answer("".join(lines)))