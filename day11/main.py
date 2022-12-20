import operator
import copy
from functools import reduce

class Monkey:
    def __init__(self, number, items: "list[int]", operation, test, test_val, if_true, if_false) -> None:
        self.number = number
        self.items = items
        self.operation = operation
        self.test_func = test
        self.test_val = test_val
        self.if_true = if_true
        self.if_false = if_false
        self.inspection_count = 0

def parse(filename):
    data = []
    monkeys = [[]]
    with open(filename, "r") as f:
        i = 0
        data = f.read().splitlines()
        for line in data:
            monkeys[i].append(line.strip())
            if len(line) == 0:
                monkeys.append([])
                i += 1
    return monkeys

def make_operator_function(s):
    tokens = s.split()
    op = operator.add if tokens[3] == "+" else operator.mul
    if tokens[-1] == "old":
        return lambda x: x * x
    #print(tokens)
    return lambda x: op(x, int(tokens[-1]))

def make_test_func(s):
    return lambda x: x % int(s) == 0

def part(monkeys, rounds, part2=False):
    worry_level = 1
    # Calculates the greatest common divisor for the monkeys
    if part2:
        worry_level = reduce(lambda accu, m: accu * m.test_val, monkeys, 1)
    else:
        worry_level = 3
    for i in range(rounds):
        for m in monkeys:
            if len(m.items) == 0:
                continue
            print("Monkey {}:".format(m.number))
            deleted_items = []
            for item in m.items:
                print("\tMonkey inspects an item with a worry level of {}".format(item))
                # Monkey inspects item
                temp = m.operation(item)
                m.inspection_count += 1
                print("\tNew worry level after inspection: {}".format(temp))
                # Monkey gets bored
                temp = temp % worry_level if part2 else temp // worry_level
                if m.test_func(temp):
                    # Remove the item from this monkeys list and append it to anothers
                    monkeys[m.if_true].items.append(temp)
                else:
                    monkeys[m.if_false].items.append(temp)
                deleted_items.append(item)
            for item in deleted_items:
                del m.items[m.items.index(item)]
        print("After round {}, the monkeys are holding items with these worry levels:".format(i))
        for m in monkeys:
            print("Monkey {}: {}".format(m.number, m.items))
    
    inspection_list = []
    for m in monkeys:
        inspection_list.append(m.inspection_count)
    inspection_list.sort()
    return inspection_list[-2]*inspection_list[-1]

def main():
    data = parse("input.txt")
    rounds = 20;
    monkeys = []
    for m in data:
        n = m[0][7]
        items2 = [int(item.strip()) for item in m[1].split(':')[1].split(",")]
        operation = m[2].split(":")[1]
        make_operator_function(operation)
        test = m[3].split()[-1]
        if_true = int(m[4].split()[-1])
        if_false = int(m[5].split()[-1])
        monkeys.append(Monkey(n, items2,
                        make_operator_function(operation),
                        make_test_func(test), int(test), if_true, if_false))

    print(part(copy.deepcopy(monkeys), 20))
    print(part(copy.deepcopy(monkeys), 10000, True))

main()
