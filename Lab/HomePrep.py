

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
rows, columns = [int(x) for x in input().split(', ')]
workshop_matrix = []
player_row = 0
player_col = 0

for i in range(rows):
    current_line = input().split(' ')
    workshop_matrix.append(current_line)

while 1:
    command = input()
    if command == "End":
        break

print(workshop_matrix)
















