from itertools import islice

def get_priority(char):
    prio = 0
    if char.islower():
        prio = ord(char) - ord('a') + 1
    elif char.isupper():
        prio = ord(char) - ord('A') + 27
    return prio

def part_1(filename):
    sum = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n")
            line_length = len(line)
            mid = int(line_length/2)
            comp1, comp2 = line[0:mid], line[mid:line_length]
            res = set(comp1).intersection(comp2)
            char = res.pop()
            sum += get_priority(char)
    return sum

def part_2(filename):
    sum = 0
    with open(filename, "r") as f:
        while True:
            group = list(islice(f, 3))
            if not group:
                break
            res = [set(line.strip("\n")) for line in group]
            intersection = res[0].intersection(*res)
            char = intersection.pop()
            sum += get_priority(char)
    return sum



def main():
    print("hello world!")
    print(part_1("input.txt"))
    print(part_2("input.txt"))


main()