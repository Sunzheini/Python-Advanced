

# 1. Ramen Shop
# from collections import deque
#
# ramen = [int(x) for x in input().split(', ')]
# customers = deque([int(x) for x in input().split(', ')])
#
# while ramen and customers:
#
#     current_ramen_bowl = ramen.pop()
#     current_customer = customers.popleft()
#
#     if current_ramen_bowl == current_customer:
#         continue
#
#     if current_ramen_bowl > current_customer:
#         current_ramen_bowl -= current_customer
#         ramen.append(current_ramen_bowl)
#         continue
#
#     if current_ramen_bowl < current_customer:
#         current_customer -= current_ramen_bowl
#         customers.appendleft(current_customer)
#         continue
#
# if not customers:
#     print("Great job! You served all the customers.")
#     if ramen:
#         print(f"Bowls of ramen left: {', '.join(map(str, ramen))}")
# else:
#     print("Out of ramen! You didn't manage to serve all customers.")
#     if customers:
#         print(f"Customers left: {', '.join(map(str, customers))}")



# 2. North Pole Challenge
def y_square(matrix, r, c):
    row, col = 0, 0
    for j in range(r):
        for k in range(c):
            if matrix[j][k] == 'Y':
                row = j
                col = k
    return row, col


rows, columns = [int(x) for x in input().split(', ')]
workshop_matrix = []
items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}
collected_all = False

for i in range(rows):
    current_line = input().split(' ')
    workshop_matrix.append(current_line)

player_row, player_col = y_square(workshop_matrix, rows, columns)

while 1:

    if collected_all:
        print("Merry Christmas!")
        workshop_matrix[player_row][player_col] = 'Y'
        break

    command = input()
    if command == "End":
        workshop_matrix[player_row][player_col] = 'Y'
        break

    explode = command.split('-')
    direction = explode[0]
    steps = int(explode[1])

    workshop_matrix[player_row][player_col] = 'x'

# --------------------------------------------------------------------------------------------------

    if direction == 'left':

        for step in range(steps):

            if collected_all:
                break

            player_col -= 1
            if player_col < 0:
                player_col = columns - 1

            if workshop_matrix[player_row][player_col] == 'D':
                items['Christmas decorations'] += 1
            elif workshop_matrix[player_row][player_col] == 'G':
                items['Gifts'] += 1
            elif workshop_matrix[player_row][player_col] == 'C':
                items['Cookies'] += 1

            workshop_matrix[player_row][player_col] = 'x'

            collected_all = True
            for check_row in range(rows):
                for check_col in range(columns):
                    if workshop_matrix[check_row][check_col] in "GCD":
                        collected_all = False


# --------------------------------------------------------------------------------------------------

    if direction == 'right':
        for step in range(steps):

            if collected_all:
                break

            player_col += 1
            if player_col > columns - 1:
                player_col = 0

            if workshop_matrix[player_row][player_col] == 'D':
                items['Christmas decorations'] += 1
            elif workshop_matrix[player_row][player_col] == 'G':
                items['Gifts'] += 1
            elif workshop_matrix[player_row][player_col] == 'C':
                items['Cookies'] += 1

            workshop_matrix[player_row][player_col] = 'x'

            collected_all = True
            for check_row in range(rows):
                for check_col in range(columns):
                    if workshop_matrix[check_row][check_col] in "GCD":
                        collected_all = False

# --------------------------------------------------------------------------------------------------

    if direction == 'up':
        for step in range(steps):

            if collected_all:
                break

            player_row -= 1
            if player_row < 0:
                player_row = rows - 1

            if workshop_matrix[player_row][player_col] == 'D':
                items['Christmas decorations'] += 1
            elif workshop_matrix[player_row][player_col] == 'G':
                items['Gifts'] += 1
            elif workshop_matrix[player_row][player_col] == 'C':
                items['Cookies'] += 1

            workshop_matrix[player_row][player_col] = 'x'

            collected_all = True
            for check_row in range(rows):
                for check_col in range(columns):
                    if workshop_matrix[check_row][check_col] in "GCD":
                        collected_all = False

# --------------------------------------------------------------------------------------------------

    if direction == 'down':
        for step in range(steps):

            if collected_all:
                break

            player_row += 1
            if player_row > rows - 1:
                player_row = 0

            if workshop_matrix[player_row][player_col] == 'D':
                items['Christmas decorations'] += 1
            elif workshop_matrix[player_row][player_col] == 'G':
                items['Gifts'] += 1
            elif workshop_matrix[player_row][player_col] == 'C':
                items['Cookies'] += 1

            workshop_matrix[player_row][player_col] = 'x'

            collected_all = True
            for check_row in range(rows):
                for check_col in range(columns):
                    if workshop_matrix[check_row][check_col] in "GCD":
                        collected_all = False


print("You've collected:")
for key in items.keys():
    print(f"- {items[key]} {key}")


for line in workshop_matrix:
    print(f"{' '.join(line)}")







