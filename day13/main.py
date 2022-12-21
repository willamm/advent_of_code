from ast import literal_eval
from itertools import zip_longest

def parse(filename):
    packet_pairs = [[]]
    with open(filename, "r") as f:
        data = f.read().strip().splitlines()
        i = 0
        for line in data:
            if len(line) == 0:
                packet_pairs.append([])
                i += 1
                continue
            packet_pairs[i].append(literal_eval(line))
    return packet_pairs


def process_pairs(left, right):
    if left is None:
        return -1
    if right is None:
        return 1

    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    if type(left) == list and type(right) == list:
        for l, r in zip_longest(left, right):
            if (result := process_pairs(l, r)) != 0:
                return result
        return 0
 
    l = [left] if type(left) == int else left
    r = [right] if type(right) == int else right
    return process_pairs(l, r)

def main():
    data = parse("input.txt")
    pairs_in_right_order = set()
    sum = 0
    for x, pair in enumerate(data):
        # Compare each pair recursively
        left = pair[0]
        right = pair[1]
        if process_pairs(left, right) == -1:
            sum += x 
    print(sum)

main()