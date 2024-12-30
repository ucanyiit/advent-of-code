def possible_results(numbers):
    results = set({numbers[0]})
    for i in range(1, len(numbers)):
        results2 = set()
        for res in results:
            results2.add(res + numbers[i])
            results2.add(res * numbers[i])
            results2.add(int(str(res) + str(numbers[i])))
        results = results2
        
    return results
    

with open("7.in") as f:
    lines = f.readlines()
    
    s = 0
    for i in range(len(lines)):
        res, line = lines[i].split(":")
        numbers = list(map(int, line.split()))
                    
        results = possible_results(numbers)
        if int(res) in results:
            s += int(res)
            
    print(s)