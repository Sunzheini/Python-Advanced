# 1
# set1 = {int(x) for x in input().split(' ')}
# set2 = {int(x) for x in input().split(' ')}
#
# n = int(input())
#
# for i in range(n):
#     command = input().split(' ')
#
#     if 'Add' in command:
#         if command[1] == 'First':
#             while len(command) > 2:
#                 set1.add(int(command.pop()))
#         elif command[1] == 'Second':
#             while len(command) > 2:
#                 set2.add(int(command.pop()))
#
#     if 'Remove' in command:
#         if command[1] == 'First':
#             while len(command) > 2:
#                 next_remove = int(command.pop())
#                 if next_remove in set1:
#                     set1.remove(next_remove)
#         elif command[1] == 'Second':
#             while len(command) > 2:
#                 next_remove = int(command.pop())
#                 if next_remove in set2:
#                     set2.remove(next_remove)
#
#     elif 'Check' in command:
#         if set1.issubset(set2) or set2.issubset(set1):
#             print('True')
#         else:
#             print('False')
#
# print(f"{', '.join(map(str, sorted(list(set1))))}")
# print(f"{', '.join(map(str, sorted(list(set2))))}")

# 2
# from collections import deque
#
# input_string = input().split(' ')
# q = deque()
#
# operations = {'+': lambda a, b: a + b,      # !!!
#               '-': lambda a, b: a - b,
#               '*': lambda a, b: a * b,
#               '/': lambda a, b: a // b,
#               }
#
# for i in input_string:
#     if i in '+-*/':
#         while len(q) > 1:
#             left = q.popleft()
#             right = q.popleft()
#
#             result = operations[i](left, right)    #!!!
#             q.appendleft(result)
#
#     else:
#         q.append(int(i))
#
# print(q.popleft())

# 3
from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])
milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_cup_of_milk = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_cup_of_milk <= 0:
        continue

    if current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup_of_milk)
        continue

    if current_cup_of_milk <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_cup_of_milk:
        milkshakes += 1

    else:
        cups_of_milk.append(current_cup_of_milk)
        current_chocolate -= 5
        chocolates.append(current_chocolate)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolates) > 0:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if len(cups_of_milk) > 0:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")

# 4 -1.45h













