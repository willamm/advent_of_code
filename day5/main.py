def part_1(crates, lines):
    for line in lines[10:]:
        tokens = line.split(" ")
        move, from_stack, to_stack = int(tokens[1]), int(tokens[3]) - 1, int(tokens[5]) - 1
        for i in range(move):
            crates[to_stack].append(crates[from_stack].pop())
    return "".join([crate[len(crate) - 1] for crate in crates])

def part_2(crates, lines):
    for line in lines[10:]:
        tokens = line.split(" ")
        move, from_stack, to_stack = int(tokens[1]), int(tokens[3]) - 1, int(tokens[5]) - 1
        from_len = len(crates[from_stack]) 
        crates_to_move = crates[from_stack][from_len - move : from_len]
        del crates[from_stack][from_len - move : from_len]
        crates[to_stack].append(crates_to_move)
        crates[to_stack] = [item for sublist in crates[to_stack] for item in sublist]
    return "".join([crate[len(crate) - 1] for crate in crates])

def main():
    crates_str = "DTRBJLWG SWC RZTM DTCHSPV GPTLDZ FBRZJQCD SBDJMFTR LHRBTVM QPDSV"
    temp = crates_str.split(" ")
    crates1 = list(map(list, temp))
    crates2 = list(map(list, temp))
        
    with open("input.txt", "r") as f:
        lines = f.readlines()
        part1 = part_1(crates1, lines)
        part2 = part_2(crates2, lines)
    print(part1)
    print(part2)
main()