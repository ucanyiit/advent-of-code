def get_first_unsafe(num_array):
    increasing = num_array[1] > num_array[0]
    if increasing:
        for i in range(1, len(num_array)):
            if num_array[i] <= num_array[i - 1] or abs(num_array[i] - num_array[i - 1]) > 3:
                return i
    else:
        for i in range(1, len(num_array)):
            if num_array[i] >= num_array[i - 1] or abs(num_array[i] - num_array[i - 1]) > 3:
                return i
            
    return False

with open("2.in") as f:
    lines = f.readlines()
    
    s = 0
    for line in lines:
        num_array = list(map(int, line.split()))
        if get_first_unsafe(num_array) == False:
            s += 1
            
    print(s)

with open("2.in") as f:
    lines = f.readlines()
    
    s = 0
    for line in lines:
        num_array = list(map(int, line.split()))
        unsafe = get_first_unsafe(num_array)
        if unsafe == False:
            s += 1
        else:
            new_array = num_array[:unsafe] + num_array[unsafe + 1:]
            new_array_2 = num_array[:unsafe - 1] + num_array[unsafe:]
            new_array_3 = num_array[:unsafe - 2] + num_array[unsafe - 1:] # very hacky
            print(num_array, new_array, new_array_2)
            if get_first_unsafe(new_array) == False or get_first_unsafe(new_array_2) == False or get_first_unsafe(new_array_3) == False:
                s += 1
            
    print(s)
    