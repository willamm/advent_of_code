def get_marker(line, window_size):
    count = window_size
    window = list()
    for ch in line[0:window_size]:
        window.append(ch)

    for ch in line[window_size:]:
        window.pop(0);
        window.append(ch)
        count += 1
        if len(set(window)) == len(window):
            return count
    return count

def main():
    ch_count = 0
    start_count = 0
    with open("input.txt", "r") as f:
        lines = f.readlines();
        for line in lines:
            # part 1
            ch_count = get_marker(line, 4)
            # part 2
            start_count = get_marker(line, 14)
    print(ch_count)
    print(start_count)
main()