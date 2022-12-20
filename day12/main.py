def parse(filename):
    data = [];
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return data

def get_coords(grid, ch):
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == ch:
                return (j, i)

def get_adjacent_squares(grid, current):
    adjacent_squares = []
    x, y = current
    x_max = len(grid) - 1
    y_max = len(grid[0]) - 1
    h = ord(grid[x][y]) - 2
    if x > 0 and h < ord(grid[x - 1][y]):
        adjacent_squares.append((x - 1, y))
    if x < x_max and h < ord(grid[x + 1][y]):
        adjacent_squares.append((x + 1, y))
    if y > 0 and h < ord(grid[x][y - 1]):
        adjacent_squares.append((x, y - 1))
    if y < y_max and h < ord(grid[x][y + 1]):
        adjacent_squares.append((x, y + 1))
    return adjacent_squares


def bfs(grid, start, goal):
    visited = {}
    visited[start] = 0
    queue = [start]
    while len(queue) != 0:
        current = queue.pop(0)
        if current == goal:
            return visited
        for square in get_adjacent_squares(grid, current):
            if square not in visited:
                visited[square] = visited[current] + 1
                queue.append(square)
    return visited


def main():
    data = parse("input.txt")
    grid = [[ch for ch in l] for l in data]
    starts = [(x, y) for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] == 'a']
    # find starting point
    start = get_coords(grid, "S")
    starts.append(start)
    grid[start[0]][start[1]] = 'a' # for ease
    end = get_coords(grid, "E")
    grid[end[0]][end[1]] = 'z'
    paths = bfs(grid, end, start)

    total = [paths.get(p) for p in starts if paths.get(p)]

    # part 1
    print(paths[start])
    # part 2
    print(min(total))

main()