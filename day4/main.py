def part_1(pairs):
    count = 0
    for pair in pairs:
        first_str, second_str = pair[0].split('-'), pair[1].split('-')
        first, second = [int(i) for i in first_str], [int(i) for i in second_str]
        if (first[0] <= second[0] and first[1] >= second[1]) or (second[0] <= first[0] and second[1] >= first[1]):
            count += 1
    return count

def part_2(pairs):
    count = 0
    for pair in pairs:
        first_str, second_str = pair[0].split('-'), pair[1].split('-')
        first, second = [int(i) for i in first_str], [int(i) for i in second_str]
        if second[0] <= first[1] and first[0] <= second[1]:
            count += 1
    return count


def main():
    count = 0
    count_overlap = 0
    with open("input.txt", "r") as f:
        pairs = [line.strip("\n").split(',') for line in f.readlines()]
        count = part_1(pairs)
        count_overlap = part_2(pairs)
    print(count)
    print(count_overlap)
    

main()
