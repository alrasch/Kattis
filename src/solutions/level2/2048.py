lines = [[int(x) for x in input().split()] for i in range(4)]
direction = int(input())

def shift_left(line):
    for i in range(3, 0, -1):
        if line[i] != 0 and line[i-1] == 0:
            line[i-1], line[i] = line[i], line[i-1]

def merge_left(line):
    for i in range(3):
        if line[i] != 0 and line[i] == line[i+1]:
            line[i] = 2 * int(line[i])
            line[i+1] = 0

def is_left_shifted(line):
    for i in range(3):
        if line[i] == 0 and line[i+1] != 0: return False
    return True

def rotate_left(lines):
    new_lines = [[0]*4 for _ in range(4)]
    for x in range(4):
        for y in range(4):
            new_lines[3-y][x] = lines[x][y]
    return new_lines

def solve_left(lines):
    for line in lines:
        shift_left(line)
        merge_left(line)
        while not is_left_shifted(line):
            shift_left(line)
    return lines


if direction == 0: #left
    lines = solve_left(lines)

if direction == 1: #up
    lines = rotate_left(lines)
    lines = solve_left(lines)
    lines = rotate_left(lines)
    lines = rotate_left(lines)
    lines = rotate_left(lines)

if direction == 2: #right
    lines = rotate_left(lines)
    lines = rotate_left(lines)
    lines = solve_left(lines)
    lines = rotate_left(lines)
    lines = rotate_left(lines)

if direction == 3: #down
    lines = rotate_left(lines)
    lines = rotate_left(lines)
    lines = rotate_left(lines)
    lines = solve_left(lines)
    lines = rotate_left(lines)

for line in lines:
    print(line[0], line[1], line[2], line[3])
