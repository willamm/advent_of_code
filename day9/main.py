def parse(filename):
    data = []
    with open(filename, "r") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            x, y = line.split()
            data.append([x, int(y)])
    return data


def should_tail_move(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return False, ""
    if head[0] == (tail[0] - 1) and head[1] == (tail[1] + 1):
        return False, ""
    if head[0] == (tail[0] + 1) and head[1] == (tail[1] + 1):
        return False, ""
    if head[0] == (tail[0] - 1) and head[1] == (tail[1] - 1):
        return False, ""
    if head[0] == (tail[0] + 1) and head[1] == (tail[1] - 1):
        return False, ""
    # following cases are when the tail should move
    if head[0] == tail[0] and head[1] > tail[1]:
        return True, "U"
    if head[0] == tail[0] and head[1] < tail[1]:
        return True, "D"
    if head[0] > tail[0] and head[1] == tail[1]:
        return True, "R"
    if head[0] < tail[0] and head[1] == tail[1]:
        return True, "L"
    if head[0] < tail[0] and head[1] < tail[1]:
        return True, "LD"
    if head[0] < tail[0] and head[1] > tail[1]:
        return True, "LU"
    if head[0] > tail[0] and head[1] < tail[1]:
        return True, "RD"
    if head[0] > tail[0] and head[1] > tail[1]:
        return True, "RU"

def move_all_pieces(rope_pieces, positions_visited):
    for index in range(len(rope_pieces) - 1):
        move, piece_direction = should_tail_move(rope_pieces[index], rope_pieces[index + 1])
        if move:
            rope_pieces[index + 1] = move_tail_piece(rope_pieces[index + 1], piece_direction)
            if index == len(rope_pieces) - 2:
                positions_visited.add((rope_pieces[index + 1][0], rope_pieces[index + 1][1]))

def move_tail_piece(old_position, direction):
    if direction == "U":
        return [old_position[0], old_position[1] + 1]
    if direction == "D":
        return [old_position[0], old_position[1] - 1]
    if direction == "L":
        return [old_position[0] - 1, old_position[1]]
    if direction == "R":
        return [old_position[0] + 1, old_position[1]]
    # handle diagonal moves here
    if direction == "LD":
        return [old_position[0] - 1, old_position[1] - 1]
    if direction == "LU":
        return [old_position[0] - 1, old_position[1] + 1]
    if direction == "RD":
        return [old_position[0] + 1, old_position[1] - 1]
    if direction == "RU":
        return [old_position[0] + 1, old_position[1] + 1]

   

def process_move(move, rope_pieces, positions_visited):
    direction = move[0]
    distance = move[1]
    for _ in range(distance):
        if direction == "D":
            rope_pieces[0][1] -= 1
            move_all_pieces(rope_pieces, positions_visited)
        elif direction == "U":
            rope_pieces[0][1] += 1
            move_all_pieces(rope_pieces, positions_visited)
        elif direction == "L":
            rope_pieces[0][0] -= 1
            move_all_pieces(rope_pieces, positions_visited)
        elif direction == "R":
            rope_pieces[0][0] += 1
            move_all_pieces(rope_pieces, positions_visited) 



def main():
    data = parse("input.txt")
    head = [0, 0]
    tail = [0, 0]
    positions_visited = {(0, 0)}
    rope_pieces = [head, tail]  # change for part 2
    rope_pieces2 = [[0, 0] for _ in range(10)]
    positions_visited2 = {(0,0)}
    for move in data:
        # part 1
        process_move(move, rope_pieces, positions_visited)
        # part 2
        process_move(move, rope_pieces2, positions_visited2)

    print(len(positions_visited))
    print(len(positions_visited2))
    

main()
