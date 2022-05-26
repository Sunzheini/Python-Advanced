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
# from collections import deque
#
# chocolates = [int(x) for x in input().split(', ')]
# cups_of_milk = deque([int(x) for x in input().split(', ')])
# milkshakes = 0
#
# while chocolates and cups_of_milk and milkshakes < 5:
#     current_chocolate = chocolates.pop()
#     current_cup_of_milk = cups_of_milk.popleft()
#
#     if current_chocolate <= 0 and current_cup_of_milk <= 0:
#         continue
#
#     if current_chocolate <= 0:
#         cups_of_milk.appendleft(current_cup_of_milk)
#         continue
#
#     if current_cup_of_milk <= 0:
#         chocolates.append(current_chocolate)
#         continue
#
#     if current_chocolate == current_cup_of_milk:
#         milkshakes += 1
#
#     else:
#         cups_of_milk.append(current_cup_of_milk)
#         current_chocolate -= 5
#         chocolates.append(current_chocolate)
#
# if milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# if len(chocolates) > 0:
#     print(f"Chocolate: {', '.join(map(str, chocolates))}")
# else:
#     print("Chocolate: empty")
#
# if len(cups_of_milk) > 0:
#     print(f"Milk: {', '.join(map(str, cups_of_milk))}")
# else:
#     print("Milk: empty")

# 4
# from collections import deque
#
# working_bees = deque([int(x) for x in input().split()])
# nectar = [int(x) for x in input().split()]
# process = deque([x for x in input().split()])
# honey = 0
#
# while len(working_bees) > 0 and len(nectar) > 0:
#     current_bee = working_bees.popleft()
#     current_nectar = nectar.pop()
#
#     if current_bee > current_nectar:
#         working_bees.appendleft(current_bee)
#         continue
#
#     if current_nectar == 0:         #zabravih delenie na 0!
#         continue
#
#     current_process = process.popleft()
#
#     if current_process == '+':
#         honey += (current_bee + current_nectar)
#     elif current_process == '-':
#         honey += abs(current_bee - current_nectar)
#     elif current_process == '*':
#         honey += (current_bee * current_nectar)
#     elif current_process == '/':
#         honey += (current_bee / current_nectar)
#
# print(f"Total honey made: {honey}")
#
# if len(working_bees) > 0:
#     print(f"Bees left: {', '.join(map(str, working_bees))}")
# if len(nectar) > 0:
#     print(f"Nectar left: {', '.join(map(str, nectar))}")

# 5
# from collections import deque
#
# materials = [int(x) for x in input().split()]
# magic_levels = deque([int(x) for x in input().split()])
# crafting_table = {150: 'Doll', 250: 'Wooden train',
#         300: 'Teddy bear', 400: 'Bicycle'}
# toys = {}
#
# while materials and magic_levels:
#     current_materials = materials.pop()
#     current_magic_level = magic_levels.popleft()
#
#     if current_materials == 0 and current_magic_level == 0:
#         continue
#
#     if current_materials == 0:
#         magic_levels.appendleft(current_magic_level)
#         continue            #zabravih continue
#
#     if current_magic_level == 0:
#         materials.append(current_materials)
#         continue
#
#     total_magic_level = current_materials * current_magic_level
#
#     if total_magic_level in crafting_table.keys():
#         toy_name = crafting_table[total_magic_level]
#         if toy_name not in toys.keys():
#             toys[toy_name] = 0
#         toys[toy_name] += 1
#         continue
#
#     if total_magic_level < 0:
#         junk = current_materials + current_magic_level
#         materials.append(junk)
#     else:
#         materials.append(current_materials + 15)
#
# if 'Doll' in toys and 'Wooden train' in toys:
#     print("The presents are crafted! Merry Christmas!")
# elif 'Teddy bear' in toys and 'Bicycle' in toys:
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials:
#     print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
# if magic_levels:
#     print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
#
# for i in sorted(toys.keys()):
#     print(f"{i}: {toys[i]}")

# 6
from collections import deque

words = deque(input().split())
main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {'orange', 'purple', 'green'}
collected_colors = []

while words:
    left = words.popleft()
    right = words.pop() if words else ''  #!ako e ostanal element

    result = left + right
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = right + left
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        words.insert(len(words) // 2, left)
    if right:
        words.insert(len(words) // 2, right)

result = []
forming_colors = {'orange': ['red', 'yellow'],
                  'purple': ['red', 'blue'],
                  'green': ['yellow', 'blue']}

for color in collected_colors:
    if color in main_colors:
        result.append(color)
        continue

    is_collected = True
    for helping_color in forming_colors[color]:
        if helping_color not in collected_colors:
            is_collected = False
            break

    if is_collected:
        result.append(color)

print(result)

