with open("1.in") as f:
    lines = f.readlines()
    
    list1 = []
    list2 = []
    
    for line in lines:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))
        
    list1.sort()
    list2.sort()
    s = 0
    for i in range(len(list1)):
        s += abs(list1[i] - list2[i])
    print(s)
    
with open("1.in") as f:
    lines = f.readlines()
    
    list1 = []
    map2 = {}
    
    for line in lines:
        a, b = line.split()
        list1.append(int(a))
        map2[int(b)] = 1 if int(b) not in map2 else map2[int(b)] + 1
        
    s = 0
    for num in list1:
        s += (0 if num not in map2 else map2[num]) * num
    print(s)
    
