

# 1. Collecting Eggs
# from collections import deque
#
# eggs = deque(int(x) for x in input().split(', '))
# pieces_of_paper = [int(x) for x in input().split(', ')]
# boxes = 0
#
# while eggs and pieces_of_paper:
#
#     current_egg = eggs.popleft()
#     current_paper = pieces_of_paper.pop()
#
#     # check if egg is fresh
#     if current_egg <= 0:
#         pieces_of_paper.append(current_paper)
#         continue
#
#     # check if egg is 13
#     if current_egg == 13:
#         pieces_of_paper.append(current_paper)
#         pieces_of_paper[0], pieces_of_paper[-1] = pieces_of_paper[-1], pieces_of_paper[0]
#         continue
#
#     # check if they fit in
#     sum_egg_and_paper = current_egg + current_paper
#     if sum_egg_and_paper <= 50:
#         boxes += 1
#     else:
#         continue
#
# if boxes >= 1:
#     print(f"Great! You filled {boxes} boxes.")
# else:
#     print("Sorry! You couldn't fill any boxes!")
#
# if eggs:
#     print(f"Eggs left: {', '.join(map(str, eggs))}")
#
# if pieces_of_paper:
#     print(f"Pieces of paper left: {', '.join(map(str, pieces_of_paper))}")



# 2. Exit Founder
# player_1, player_2 = input().split(', ')
# moves_counter = 1
# player_1_skip = False
# player_2_skip = False
#
# maze_board = [(list(input().split())) for x in range(6)]
#
# while 1:
#     command = input()
#     current_row, current_col = command[1], command[4]
#     current_row = int(current_row)
#     current_col = int(current_col)
#
#     # check if skipping turn
#     if moves_counter % 2 != 0:
#         if player_1_skip == True:
#             player_1_skip = False
#             moves_counter += 1
#             continue
#     else:
#         if player_2_skip == True:
#             player_2_skip = False
#             moves_counter += 1
#             continue
#
#     # check if exit is found
#     if maze_board[current_row][current_col] == 'E':
#         if moves_counter % 2 != 0:
#             print(f"{player_1} found the Exit and wins the game!")
#             break
#         else:
#             print(f"{player_2} found the Exit and wins the game!")
#             break
#
#     # check if trap is found
#     if maze_board[current_row][current_col] == 'T':
#         if moves_counter % 2 != 0:
#             print(f"{player_1} is out of the game! The winner is {player_2}.")
#             break
#         else:
#             print(f"{player_2} is out of the game! The winner is {player_1}.")
#             break
#
#     # check if wall is hit
#     if maze_board[current_row][current_col] == 'W':
#         if moves_counter % 2 != 0:
#             print(f"{player_1} hits a wall and needs to rest.")
#             player_1_skip = True
#             moves_counter += 1
#             continue
#         else:
#             print(f"{player_2} hits a wall and needs to rest.")
#             player_2_skip = True
#             moves_counter += 1
#             continue
#
#     moves_counter += 1



# 3. Shopping Cart

def shopping_cart(*args):

    my_cart = {"Soup": [], "Pizza": [], "Dessert": []}
    result = ''

    for command in args:
        if command == 'Stop':

            if len(my_cart["Soup"]) == 0 and len(my_cart["Pizza"]) == 0 and len(my_cart["Dessert"]) == 0:
                result += "No products in the cart!"
                return result

            else:
                my_sorting = sorted(my_cart.items(), key=lambda x: (-len(x[1]), x[0]))
                for i in my_sorting:
                    p, q = i
                    q = sorted(q)

                    result += f"{p}:\n"
                    for j in q:
                        result += f" - {j}\n"

                return result.strip()

        else:
            type_of_meal, product_for_the_meal = command

            if type_of_meal == "Soup" and len(my_cart[type_of_meal]) < 3:
                if product_for_the_meal not in my_cart[type_of_meal]:
                    my_cart[type_of_meal].append(product_for_the_meal)
            elif type_of_meal == "Pizza" and len(my_cart[type_of_meal]) < 4:
                if product_for_the_meal not in my_cart[type_of_meal]:
                    my_cart[type_of_meal].append(product_for_the_meal)
            elif type_of_meal == "Dessert" and len(my_cart[type_of_meal]) < 2:
                if product_for_the_meal not in my_cart[type_of_meal]:
                    my_cart[type_of_meal].append(product_for_the_meal)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
