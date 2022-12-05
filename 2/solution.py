import sys

FILE_NAME = sys.argv[1]
SOLUTION_NUMBER = sys.argv[2]

def problem1(file):
    data = file.read().splitlines()
    move_dict = { "A": "X", "B": "Y", "C": "Z" }
    score = 0
    for line in data:
        moves = line.split(" ")
        oppenent = move_dict[moves[0]]
        player = moves[1]
        score += ord(player) - ord("W")
        if oppenent == player:
            score += 3
        elif oppenent == "X" and player == "Y" or oppenent == "Y" and player == "Z" or oppenent == "Z" and player == "X":
            score += 6

    return score

def problem2(file):
    data = file.read().splitlines()
    score = 0
    for line in data:
        moves = line.split(" ")
        oppenent = ord(moves[0]) + 2
        status = moves[1]

        if status == "Y":
            score += (oppenent % 3 + 3 if oppenent % 3 == 0 else oppenent % 3) + 3
        elif status == "X":
            score += ((oppenent - 1) % 3 + 3 if (oppenent - 1) % 3 == 0 else (oppenent - 1) % 3)
        else:
            score += ((oppenent + 1) % 3 + 3 if (oppenent + 1) % 3 == 0 else (oppenent + 1) % 3) + 6
    return score


with open(FILE_NAME, 'r', encoding="UTF-8") as file:
    if SOLUTION_NUMBER == '1':
        print(problem1(file))
    elif SOLUTION_NUMBER == '2':
        print(problem2(file))
