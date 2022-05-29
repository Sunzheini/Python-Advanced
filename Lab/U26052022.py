# 1
# row_index = n - column_index - 1
# mm = []
# size = int(input())
#
# primary_elements = []
# primary_sum = 0
#
# secondary_elements = []
# secondary_sum = 0
#
# for _ in range(size):
#     mm.append([int(x) for x in input().split(', ')])
#
# for i in range(size):
#     for j in range(size):
#         if i == j:
#             primary_elements.append(mm[i][j])
#             primary_sum += mm[i][j]
#         if i == (size - j - 1):
#             secondary_elements.append(mm[i][j])
#             secondary_sum += mm[i][j]
#
# print(f"Primary diagonal:"
#       f" {', '.join(map(str, primary_elements))}. Sum: {primary_sum}")
#
# print(f"Secondary diagonal:"
#       f" {', '.join(map(str, secondary_elements))}. Sum: {secondary_sum}")

# 2
# mm = []
# size = int(input())
#
# primary_elements = []
# primary_sum = 0
#
# secondary_elements = []
# secondary_sum = 0
#
# for _ in range(size):
#     mm.append([int(x) for x in input().split(' ')])
#
# for i in range(size):
#     for j in range(size):
#         if i == j:
#             primary_elements.append(mm[i][j])
#             primary_sum += mm[i][j]
#         if i == (size - j - 1):
#             secondary_elements.append(mm[i][j])
#             secondary_sum += mm[i][j]
#
# difference = abs(primary_sum - secondary_sum)
# print(difference)

# 3
# rows, columns = [int(x) for x in input().split(' ')]
# mm = [list(input().split(' ')) for _ in range(rows)]
# count = 0
#
# for i in range(rows-1):
#     for j in range(columns-1):
#         if mm[i][j] == mm[i][j+1] == mm[i+1][j] == mm[i+1][j+1]:
#             count += 1
#
# print(count)

# 4
# rows, columns = [int(x) for x in input().split()]
# mm = []
# best_sum = float('-inf')
# start_row = 0
# start_column = 0
#
# for _ in range(rows):
#     mm.append([int(x) for x in input().split()])
#
# for i in range(rows-2):
#     for j in range(columns-2):
#         current_sum = mm[i][j] + mm[i][j+1] + mm[i][j+2] + \
#                       mm[i+1][j] + mm[i+1][j+1] + mm[i+1][j+2] + \
#                       mm[i+2][j] + mm[i+2][j+1] + mm[i+2][j+2]
#
#         if current_sum > best_sum:
#             best_sum = current_sum
#             start_row = i
#             start_column = j
#
# print(f"Sum = {best_sum}")
# print(f"{mm[start_row][start_column]} {mm[start_row][start_column+1]} {mm[start_row][start_column+2]}")
# print(f"{mm[start_row+1][start_column]} {mm[start_row+1][start_column+1]} {mm[start_row+1][start_column+2]}")
# print(f"{mm[start_row+2][start_column]} {mm[start_row+2][start_column+1]} {mm[start_row+2][start_column+2]}")

# 5
# r, c = [int(x) for x in input().split()]
# for i in range(r):
#     for j in range(c):
#         current_item = ''
#         current_item += chr(97 + i)
#         current_item += chr(97 + i + j)
#         current_item += chr(97 + i)
#         print(current_item, end=' ')
#     print()

# 6
# def is_outside(row, col, rows, cols):           # validaciq dali sa vytre
#     return row < 0 or col < 0 or row >= rows or col >= cols
#
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# while True:
#     line = input()
#     if line == 'END':
#         break
#
#     line_parts = line.split()
#
#     if len(line_parts) != 5 or line_parts[0] != 'swap':
#         print("Invalid input!")
#         continue
#
#     row1, col1, row2, col2 = [int(x) for x in line_parts[1:]]
#
#     if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
#         print("Invalid input!")
#         continue
#
#     matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#
#     for row in matrix:
#         print(*row, sep=' ')            # moje i taka

# 7
rows, cols = [int(x) for x in input().split()]
word = input()

index = 0

for row in range(rows):
    elements = [None] * cols                # !!!

    if row % 2 == 0:
        for col in range(cols):
            elements[col] = word[index % len(word)]     # 5 % 7 = 5, 7 % 7 = 0, 10 % 7 = 3
            index += 1

    else:
        for col in range(cols-1, -1, -1):
            elements[col] = word[index % len(word)]
            index += 1

    print(''.join(elements))

# 8 -1.25.21
















