

# 1. Christmas Elves (lineini strukturi)
# from collections import deque
#
#
# elves_energy = deque([int(x) for x in input().split()])
# materials_box = [int(x) for x in input().split()]
#
# created_toys = 0
# energy_used = 0
# tries_counter = 0
#
# while elves_energy and materials_box:
#
#     current_elf = elves_energy.popleft()
#     current_materials = materials_box.pop()
#
#     if current_elf < 5:
#         materials_box.append(current_materials)
#         continue
#
#     tries_counter += 1
#
#     if tries_counter % 3 == 0:
#         if current_elf >= (current_materials * 2):
#             current_elf -= (current_materials * 2)
#             energy_used += (current_materials * 2)
#
#             if tries_counter % 5 != 0:
#                 created_toys += 2
#                 current_elf += 1
#
#             elves_energy.append(current_elf)
#
#         else:   # failed to create
#             materials_box.append(current_materials)
#             current_elf *= 2
#             elves_energy.append(current_elf)
#
#     else:
#         if current_elf >= current_materials:
#             current_elf -= current_materials
#             energy_used += current_materials
#
#             if tries_counter % 5 != 0:
#                 created_toys += 1
#                 current_elf += 1
#
#             elves_energy.append(current_elf)
#
#         else:   # failed to create
#             materials_box.append(current_materials)
#             current_elf *= 2
#             elves_energy.append(current_elf)
#
#
# print(f"Toys: {created_toys}")
# print(f"Energy: {energy_used}")
#
# if len(elves_energy) > 0:
#     print(f"Elves left: {', '.join(map(str, elves_energy))}")
#
# if len(materials_box) > 0:
#     print(f"Boxes left: {', '.join(map(str, materials_box))}")


# 2. Pawn Wars (matrici)

# def get_w_position(chess):
#     x, y = 0, 0
#     for row in range(8):
#         for col in range(8):
#             if chess[row][col] == 'w':
#                 x = row
#                 y = col
#     return x, y
#
#
# def get_b_position(chess):
#     x, y = 0, 0
#     for row in range(8):
#         for col in range(8):
#             if chess[row][col] == 'b':
#                 x = row
#                 y = col
#     return x, y
#
#
# chessboard = []
# current_turn = 1
#
# for i in range(8):
#     chessboard.append(input().split())
#
# white_row, white_col = get_w_position(chessboard)
# black_row, black_col = get_b_position(chessboard)
#
# while 1:
#     if current_turn % 2 != 0:   # white's turn
#
#         if black_row == white_row - 1:
#             if (black_col == white_col - 1) or (black_col == white_col + 1):
#                 name, number = chr(97 + black_col), str(8 - black_row)
#                 print(f"Game over! White win, capture on {name}{number}.")
#                 break
#
#         white_row, white_col = white_row - 1, white_col
#
#         if white_row == 0:
#             name, number = chr(97 + white_col), str(8 - white_row)
#             print(f"Game over! White pawn is "
#                   f"promoted to a queen at {name}{number}.")
#             break
#
#     else:                       # black's turn
#
#         if white_row == black_row + 1:
#             if (white_col == black_col - 1) or (white_col == black_col + 1):
#                 name, number = chr(97 + white_col), str(8 - white_row)
#                 print(f"Game over! Black win, capture on {name}{number}.")
#                 break
#
#         black_row, black_col = black_row + 1, black_col
#
#         if black_row == 7:
#             name, number = chr(97 + black_col), str(8 - black_row)
#             print(f"Game over! Black pawn is "
#                   f"promoted to a queen at {name}{number}.")
#             break
#
#     current_turn += 1

# 3 - ... (funkcii)

def words_sorting(*args):
    result = {}
    sorted_result = {}

    for i in args:
        current_sum = 0
        for j in i:
            current_sum += ord(j)
        if i not in result.keys():
            result[i] = 0
        result[i] += current_sum

    values_sum = 0
    for key in result.keys():
        values_sum += result[key]

    if values_sum % 2 == 0:
        sorted_result = sorted(result.items(), key=lambda x: x[0])
    else:
        sorted_result = sorted(result.items(), key=lambda x: -x[1])

    return '\n'.join(f'{p} - {q}' for (p, q) in sorted_result)      # !!!!!!!


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

















