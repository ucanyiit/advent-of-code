import sys

def get_char_value(char):
    if char <= 'Z' and char >= 'A':
        return ord(char) - ord('A') + 1 + 26
    elif char <= 'z' and char >= 'a':
        return ord(char) - ord('a') + 1
    return 0

def problem1(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        sum = 0

        for line in lines:
            first_half = line[:len(line)//2]
            second_half = line[len(line)//2:]
            exists_in_first_half = {}
            exists_in_both_halfs = set() 

            for char in first_half:
                exists_in_first_half[char] = True

            for char in second_half:
                if char in exists_in_first_half:
                    exists_in_both_halfs.add(char)
            
            for char in exists_in_both_halfs:
                sum += get_char_value(char)

        return sum

def problem2(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        sum = 0
        i = 0

        while i < len(lines):
            cur_three_lines = lines[i:i+3]
            exists_in_first_line = {}
            exists_in_first_and_second_line = {}
            exists_in_all_three_lines = set()
        
            for char in cur_three_lines[0]:
                exists_in_first_line[char] = True

            for char in cur_three_lines[1]:
                if char in exists_in_first_line:
                    exists_in_first_and_second_line[char] = True

            for char in cur_three_lines[2]:
                if char in exists_in_first_and_second_line:
                    exists_in_all_three_lines.add(char)

            for char in exists_in_all_three_lines:
                sum += get_char_value(char)
            
            i += 3
        
        return sum
    
argv = sys.argv
filename = argv[1]
print(problem2(filename))