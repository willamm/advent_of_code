#!/usr/bin/python3
def part_1(filename):
    player_score = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split(" ")
            opponent_choice, player_choice = tokens[0], tokens[1].strip("\n")
            if opponent_choice == "A":
                if player_choice == "X":
                    player_score += (1 + 3)
                elif player_choice == "Y":
                    player_score += (2 + 6)
                elif player_choice == "Z":
                    player_score += (3 + 0)
            elif opponent_choice == "B":
                if player_choice == "X":
                    player_score += (1 + 0)
                elif player_choice == "Y":
                    player_score += (2 + 3)
                elif player_choice == "Z":
                    player_score += (3 + 6)
            elif opponent_choice == "C":
                if player_choice == "X":
                    player_score += (1 + 6)
                elif player_choice == "Y":
                    player_score += (2 + 0)
                elif player_choice == "Z":
                    player_score += (3 + 3)
    return player_score

def part_2(filename):
    player_score = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split(" ")
            opponent_choice, player_choice = tokens[0], tokens[1].strip("\n")
            if opponent_choice == "A":
                if player_choice == "X":
                    player_score += (3 + 0)
                elif player_choice == "Y":
                    player_score += (1 + 3)
                elif player_choice == "Z":
                    player_score += (2 + 6)
            elif opponent_choice == "B":
                if player_choice == "X":
                    player_score += (1 + 0)
                elif player_choice == "Y":
                    player_score += (2 + 3)
                elif player_choice == "Z":
                    player_score += (3 + 6)
            elif opponent_choice == "C":
                if player_choice == "X":
                    player_score += (2 + 0)
                elif player_choice == "Y":
                    player_score += (3 + 3)
                elif player_choice == "Z":
                    player_score += (1 + 6)
    return player_score


def main():
    print(part_1("input.txt"))
    print(part_2("input.txt"))


main()
