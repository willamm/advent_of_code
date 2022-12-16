filename = 'input.txt'

with open(filename, 'r') as file:
    data = [[int(l) for l in line] for line in file.read().strip().split('\n')]

visible = (len(data) - 2) * 2 + (len(data[0]) * 2)
visibles = []


def check_visible(curr_i: int, curr_j: int, dir: str, next_i: int, next_j: int, incr: int, matrix, is_visible: bool) -> bool:
    if 0 > next_i or len(matrix) - 1 < next_i or 0 > next_j or len(matrix) - 1 < next_j:
        return is_visible

    if matrix[next_i][next_j] >= matrix[curr_i][curr_j]:
        return False

    if 'row' == dir:
        return check_visible(curr_i, curr_j, dir, next_i + incr, next_j, incr, matrix, True)

    if 'col' == dir:
        return check_visible(curr_i, curr_j, dir, next_i, next_j + incr, incr, matrix, True)


def get_visible(curr_i: int, curr_j: int, dir: str, next_i: int, next_j: int, incr: int,
                matrix, visible_trees: int) -> int:
    if 0 > next_i or len(matrix) - 1 < next_i or 0 > next_j or len(matrix) - 1 < next_j:
        return visible_trees - 1

    if matrix[next_i][next_j] >= matrix[curr_i][curr_j]:
        return visible_trees

    if 'row' == dir:
        return get_visible(curr_i, curr_j, dir, next_i + incr, next_j, incr, matrix, visible_trees + 1)

    if 'col' == dir:
        return get_visible(curr_i, curr_j, dir, next_i, next_j + incr, incr, matrix, visible_trees + 1)


for i in range(1, len(data) - 1):
    for j in range(1, len(data) - 1):
        if check_visible(curr_i=i, curr_j=j, dir='col', next_i=i, next_j=j - 1, incr=-1, matrix=data,
                         is_visible=None) or \
                check_visible(curr_i=i, curr_j=j, dir='col', next_i=i, next_j=j + 1, incr=1, matrix=data,
                              is_visible=None) or \
                check_visible(curr_i=i, curr_j=j, dir='row', next_i=i - 1, next_j=j, incr=-1, matrix=data,
                              is_visible=None) or \
                check_visible(curr_i=i, curr_j=j, dir='row', next_i=i + 1, next_j=j, incr=1, matrix=data,
                              is_visible=None):
            visible += 1
            visibles.append((i, j))

print(f"Part 1: %d" % visible)

max_visible = [
    get_visible(curr_i=i, curr_j=j, dir='col', next_i=i, next_j=j - 1, incr=-1, matrix=data, visible_trees=1) *
    get_visible(curr_i=i, curr_j=j, dir='col', next_i=i, next_j=j + 1, incr=1, matrix=data, visible_trees=1) *
    get_visible(curr_i=i, curr_j=j, dir='row', next_i=i - 1, next_j=j, incr=-1, matrix=data, visible_trees=1) *
    get_visible(curr_i=i, curr_j=j, dir='row', next_i=i + 1, next_j=j, incr=1, matrix=data, visible_trees=1)
    for i, j in visibles]

print(f"Part 2: %d" % max(max_visible))
