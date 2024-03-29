from ast import literal_eval
from itertools import zip_longest
from functools import cmp_to_key
from math import prod

def parse(filename):
    packet_pairs = []
    with open(filename, "r") as f:
        data = f.read().strip()
        for i, p in enumerate(data.split("\n\n")):
            packet_pairs.append([])
            for k in p.split("\n"):
                packet_pairs[i].append(literal_eval(k))
                
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
    pairs = parse("input.txt")
    
    # part 1
    print(sum(i for i, (l, r) in enumerate(pairs, 1) if process_pairs(l, r) == -1))

    # part 2
    packets = sorted([y for x in pairs for y in x] + [[[2]], [[6]]], key=cmp_to_key(process_pairs))
    print(prod(n for n, packet in enumerate(packets, 1) if packet == [[2]] or packet == [[6]]))

main()