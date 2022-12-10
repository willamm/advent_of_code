from heapq import nlargest

def main():
    f = open("input", "r")
    lines = f.readlines()
    elves = []
    current = 0
    max1 = 0
    for line in lines:
        if line.find("\n") != 0:
            current += int(line)
        else:
            elves.append(current)
            max1 = max(current, max1)
            current = 0
    

    top3sum = sum(nlargest(3, elves))
    print(top3sum)
    print(max1)

main()