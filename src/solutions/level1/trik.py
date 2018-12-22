move_sequence = input()

current_position = {1: True, 2: False, 3: False}

for move in move_sequence:
    if move == 'A':
        current_position[1], current_position[2] = current_position[2], current_position[1]
    elif move == 'B':
        current_position[2], current_position[3] = current_position[3], current_position[2]
    elif move == 'C':
        current_position[1], current_position[3] = current_position[3], current_position[1]

for key, value in current_position.items():
    if current_position[key]:
        print(key)
        break
