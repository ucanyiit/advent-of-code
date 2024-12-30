
dp = dict()

def blink_single(number):
    if int(number) == 0:
        return ["1"]
    elif len(number) % 2 == 0:
        return [number[:len(number)//2], str(int(number[len(number)//2:]))]
    else:
        return [str(int(number) * 2024)]

def blink_numbers(numbers, times):
    if times == 0:
        return len(numbers)
    
    numbers_hash = hash(tuple(numbers))
    if (numbers_hash, times) in dp:
        # print("hash found: ", numbers, times, dp[(numbers_hash, times)])
        return dp[(numbers_hash, times)]
    
    
    if len(numbers) == 1:
        dp[((numbers_hash, times))] = blink_numbers(blink_single(numbers[0]), times - 1)
    else:
        res = 0
        for number in numbers:
            res += blink_numbers([number], times)
        dp[((numbers_hash, times))] = res
        
    return dp[(numbers_hash, times)]

with open("11.in") as f:

    lines = f.readlines()
    line = lines[0].strip()
    stones = list(line.split())
    
    res = 0
    
    for stone in stones:
        print(stone)
        res += blink_numbers([stone], 75)

    print(res)