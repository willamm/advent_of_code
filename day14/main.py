def parse_input(filename):
    data = []
    rock_coords = set()
    with open(filename, "r") as f:
        data = f.read().strip()
        for line in data.split("\n"):
            points = [tuple(map(int, k.split(','))) for k in line.split(' -> ')]
            for i in range(len(points) - 1):
                p1, p2 = points[i], points[i + 1]
                xr = range(min(p1[0], p2[0]), max(p1[0], p2[0] + 1))
                yr = range(min(p1[1], p2[1]), max(p1[1], p2[1] + 1))
                rock_coords.update({(x, y) for x in xr for y in yr})
    
    max_depth = max((y for _, y in rock_coords))
    return rock_coords, max_depth


def part(rock_coords, max_depth, is_part2=False):
    sand_count = 0
    origin = (500, 0)
    (x, y) = origin
    while True:
        if (x, y) in rock_coords:
            (x, y) = origin
        if y > max_depth and not is_part2:
            return sand_count
        if (x, y + 1) not in rock_coords and y <= max_depth:
            y += 1
        elif (x - 1, y + 1) not in rock_coords and y <= max_depth:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in rock_coords and y <= max_depth:
            x += 1
            y += 1
        else:
            sand_count += 1
            rock_coords.add((x, y))
        if (x, y) == origin and is_part2:
            return sand_count

def main():
    print("Hello World!")
    rock_coords, max_depth = parse_input("input.txt")

    ans1 = part(rock_coords.copy(), max_depth)
    ans2 = part(rock_coords.copy(), max_depth, True)
    print(ans1)
    print(ans2)
    

main()