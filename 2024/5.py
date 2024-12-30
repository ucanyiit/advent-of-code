from functools import cmp_to_key

rules = {}
 
with open("5.in") as f:
    lines = f.readlines()
    mode = 0
    s = 0
    
    for line in lines:
        # remove \n
        line = line[:-1]
        if line == "":
            mode = 1
            continue
        if mode == 0:
            a, b = line.split("|")
            rules[(a, b)] = True
        else:
            numbers = line.split(",")
            f = 0
            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    a, b = numbers[i], numbers[j]
                    if (b, a) in rules:
                        f = 1
                        break
            if f == 0:
                s += int(numbers[len(numbers)//2])
                
    print(s)
    
def compare(item1, item2):
    if (item1, item2) in rules:
        return -1
    else:
        return 1


with open("5.in") as f:
    lines = f.readlines()
    mode = 0
    s = 0
    
    for line in lines:
        # remove \n
        line = line[:-1]
        if line == "":
            mode = 1
            continue
        if mode == 0:
            a, b = line.split("|")
            rules[(a, b)] = True
        else:
            numbers = line.split(",")
            f = 0
            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    a, b = numbers[i], numbers[j]
                    if (b, a) in rules:
                        f = 1
                        break
            if f == 1:
                numbers = sorted(numbers, key=cmp_to_key(compare))
                s += int(numbers[len(numbers)//2])
    print(s)
                