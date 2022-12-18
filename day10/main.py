def parse_input(filename):
    data = []
    with open(filename, "r") as f:
        lines = f.read().strip().split("\n")
        data = [line.split(" ") for line in lines]
        for d in data:
            if len(d) == 1:
                d.append(0)
    return data

def main():
    data = parse_input("input.txt")
    register_state = 1
    cycle_count = 1
    signal_sum = 0
    screen = ""
    #for ins, val in data:
        #v = int(val)
        #if ins == "addx": 
            #cycle_count += 1
            #if (cycle_count - 20) % 40 == 0:
                #signal_sum += register_state*cycle_count
            #register_state += v
            #cycle_count += 1
            #if (cycle_count - 20) % 40 == 0:
                #signal_sum += register_state*cycle_count
        #else:
            #cycle_count += 1
            #if (cycle_count - 20) % 40 == 0:
                #signal_sum += register_state*cycle_count
    i = 0
    first = True
    while i < len(data):
        if (cycle_count - 20) % 40 == 0:    
            signal_sum += register_state*cycle_count

        if register_state <= cycle_count % 40 <= register_state + 2:
            screen += "#"
        else:
            screen += "."

        if data[i][0] == "addx":
            if not first:
                register_state += int(data[i][1])
                i += 1
            first = not first
        else:
            i += 1
        cycle_count += 1
    
    for pos, pixel in enumerate(screen, 1):
        if pos % 40 > 0:
            print(pixel, end="")
        else:
            print(pixel)

    print(signal_sum)

main()