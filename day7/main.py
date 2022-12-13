from collections import defaultdict

def main():
    sizes = defaultdict(int)
    max_size = 100000
    filepath = []
    with open("input.txt", "r") as f:
        lines = f.readlines();
        for line in lines:
            if line.startswith("$ cd"):
                directory = line.split()[-1]
                if directory == "..":
                    filepath.pop()
                else:
                    filepath.append(directory)
            elif line.startswith("$ ls"):
                continue
            else:
                size, _ = line.split()
                if size.isdigit():
                    size = int(size)
                    for i in range(len(filepath)):
                        sizes['/'.join(filepath[:i + 1])] += size
                
        # part 1 answer
        total = 0
        for key, value in sizes.items():
            if value <= max_size:
                total += value
        print("part 1: {}".format(total))

        # part 2 answer
        used_space = sizes['/']
        total_space = 70000000
        update = 30000000
        free_space = total_space - used_space
        space_needed = update - free_space
        options = []
        for key, value in sizes.items():
            if value > space_needed:
                options.append(value)
        print("part 2: {}".format(min(options)))

main()