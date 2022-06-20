# 1. Flower finder
# from collections import deque
#
# rose = "rose"
# tulip = "tulip"
# lotus = "lotus"
# daffodil = "daffodil"
#
# vowels = deque(input().split())
# consonants = input().split()
#
# while (vowels and consonants) and (len(rose) > 0 and len(tulip) > 0 and len(lotus) > 0 and len(daffodil) > 0):
#     current_vowel = vowels.popleft()
#     current_consonant = consonants.pop()
#
#     if current_vowel in rose:
#         rose = rose.replace(current_vowel, "")
#     if current_vowel in tulip:
#         tulip = tulip.replace(current_vowel, "")
#     if current_vowel in lotus:
#         lotus = lotus.replace(current_vowel, "")
#     if current_vowel in daffodil:
#         daffodil = daffodil.replace(current_vowel, "")
#
#     if current_consonant in rose:
#         rose = rose.replace(current_consonant, "")
#     if current_consonant in tulip:
#         tulip = tulip.replace(current_consonant, "")
#     if current_consonant in lotus:
#         lotus = lotus.replace(current_consonant, "")
#     if current_consonant in daffodil:
#         daffodil = daffodil.replace(current_consonant, "")
#
# if len(rose) == 0:
#     print("Word found: rose")
# elif len(tulip) == 0:
#     print("Word found: tulip")
# elif len(lotus) == 0:
#     print("Word found: lotus")
# elif len(daffodil) == 0:
#     print("Word found: daffodil")
# else:
#     print("Cannot find any word!")
#
# if len(vowels) > 0:
#     print(f"Vowels left: {' '.join(vowels)}")
#
# if len(consonants) > 0:
#     print(f"Consonants left: {' '.join(consonants)}")


# 2. Martian explorer
# def get_current_position(matrix):
#     row, col = 0, 0
#     for j in range(6):
#         for k in range(6):
#             if matrix[j][k] == 'E':
#                 row = j
#                 col = k
#     return row, col
#
#
# def check_findings(explorer_row, explorer_col, matrix):
#     current_finding = matrix[explorer_row][explorer_col]
#
#     if current_finding == 'W':
#         resources['water'] = True
#         current_finding = 'Water'
#     elif current_finding == 'M':
#         resources['metal'] = True
#         current_finding = 'Metal'
#     elif current_finding == 'C':
#         resources['concrete'] = True
#         current_finding = 'Concrete'
#     elif current_finding == 'R':
#         pass
#
#     return current_finding
#
#
# mars = []
# resources = {'water': False, 'metal': False, 'concrete': False}
#
# for i in range(6):
#     mars.append(input().split())
#
# # -----------------------------------------------------------------------------
#
# commands = input().split(', ')
# explorer_row, explorer_col = get_current_position(mars)
#
# for move in commands:
#
#     if move == 'up':
#         explorer_row = explorer_row - 1
#
#         if explorer_row < 0:
#             explorer_row = 5
#
#         if check_findings(explorer_row, explorer_col, mars) == "R":
#             print(f"Rover got broken at ({explorer_row}, {explorer_col})")
#             break
#
#         if check_findings(explorer_row, explorer_col, mars) != '-':
#             print(f"{check_findings(explorer_row, explorer_col, mars)} deposit found at ({explorer_row}, {explorer_col})")
#
#     elif move == 'down':
#         explorer_row = explorer_row + 1
#
#         if explorer_row > 5:
#             explorer_row = 0
#
#         if check_findings(explorer_row, explorer_col, mars) == "R":
#             print(f"Rover got broken at ({explorer_row}, {explorer_col})")
#             break
#
#         if check_findings(explorer_row, explorer_col, mars) != '-':
#             print(f"{check_findings(explorer_row, explorer_col, mars)} deposit found at ({explorer_row}, {explorer_col})")
#
#     elif move == 'left':
#         explorer_col = explorer_col - 1
#
#         if explorer_col < 0:
#             explorer_col = 5
#
#         if check_findings(explorer_row, explorer_col, mars) == "R":
#             print(f"Rover got broken at ({explorer_row}, {explorer_col})")
#             break
#
#         if check_findings(explorer_row, explorer_col, mars) != '-':
#             print(f"{check_findings(explorer_row, explorer_col, mars)} deposit found at ({explorer_row}, {explorer_col})")
#
#     elif move == 'right':
#         explorer_col = explorer_col + 1
#
#         if explorer_col > 5:
#             explorer_col = 0
#
#         if check_findings(explorer_row, explorer_col, mars) == "R":
#             print(f"Rover got broken at ({explorer_row}, {explorer_col})")
#             break
#
#         if check_findings(explorer_row, explorer_col, mars) != '-':
#             print(f"{check_findings(explorer_row, explorer_col, mars)} deposit found at ({explorer_row}, {explorer_col})")
#
#
# suitable = True
# for el in resources.keys():
#     if resources[el] == False:
#         suitable = False
#
# if suitable:
#     print("Area suitable to start the colony.")
# else:
#     print("Area not suitable to start the colony.")


# 3. Naughty or nice - 47%

# def naughty_or_nice_list(kids_list, *args, **kwargs):
#
#     nice = []
#     naughty = []
#     not_found = []
#
#     for i in args:
#         args_number, adjective = i.split('-')
#         args_number = int(args_number)
#         current_name = ''
#
#         counter = 0
#         for j in range(len(kids_list)-1, -1, -1):
#             list_number = kids_list[j][0]
#             if list_number == args_number:
#                 current_name = kids_list[j][1]
#                 counter += 1
#
#         if counter == 1:
#             if adjective == "Naughty":
#                 naughty.append(current_name)
#
#                 for n in range(len(kids_list) - 1, -1, -1):
#                     if kids_list[n][1] == current_name and kids_list[n][0] == args_number:
#                         kids_list.remove(kids_list[n])
#                         break
#
#             elif adjective == "Nice":
#                 nice.append(current_name)
#
#                 for n in range(len(kids_list) - 1, -1, -1):
#                     if kids_list[n][1] == current_name and kids_list[n][0] == args_number:
#                         kids_list.remove(kids_list[n])
#                         break
#
#     for el in kwargs.keys():
#
#         counter = 0
#         for j in kids_list:
#             list_name = j[1]
#             if list_name == el:
#                 counter += 1
#
#         if counter == 1:
#             if kwargs[el] == "Naughty":
#                 naughty.append(el)
#
#                 for n in range(len(kids_list) - 1, -1, -1):
#                     if kids_list[n][1] == el:
#                         kids_list.remove(kids_list[n])
#                         break
#
#             elif kwargs[el] == "Nice":
#                 nice.append(el)
#
#                 for n in range(len(kids_list) - 1, -1, -1):
#                     if kids_list[n][1] == el:
#                         kids_list.remove(kids_list[n])
#                         break
#
#     for new in kids_list:
#         not_found.append(new[1])
#
#     if len(nice) > 0 and len(naughty) > 0 and len(not_found) > 0:
#         return f"Nice: {', '.join(nice)}\nNaughty: {', '.join(naughty)}\nNot found: {', '.join(not_found)}"
#     elif len(nice) > 0 and len(naughty) > 0:
#         return f"Nice: {', '.join(nice)}\nNaughty: {', '.join(naughty)}"
#     elif len(nice) > 0 and len(not_found) > 0:
#         return f"Nice: {', '.join(nice)}\nNot found: {', '.join(not_found)}"
#     elif len(naughty) > 0 and len(not_found) > 0:
#         return f"Naughty: {', '.join(naughty)}\nNot found: {', '.join(not_found)}"
#     elif len(nice) > 0:
#         return f"Nice: {', '.join(nice)}"
#     elif len(naughty) > 0:
#         return f"Nice: {', '.join(naughty)}"
#     elif len(not_found) > 0:
#         return f"Nice: {', '.join(not_found)}"
#     else:
#         return 0


# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))

# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))


# 3. Naughty or nice - 100%

def naughty_or_nice_list(kids, *args, **kwargs):

    nice = []
    naughty = []

    for command in args:
        number, status = command.split('-')
        number = int(number)
        name = None

        is_unique = False

        for kid_number, kid_name in kids:
            if kid_number == number and is_unique:
                is_unique = False
                break
            elif kid_number == number:
                is_unique = True
                name = kid_name

        if is_unique:
            kids.remove((number, name))             # remove tuple

            if status == "Nice":
                nice.append(name)
            else:
                naughty.append(name)

    for name, stat in kwargs.items():
        is_unique = False
        n = None
        for kid_number, kid_name in kids:
            if name == kid_name and is_unique:
                is_unique = False
                break
            if name == kid_name:
                is_unique = True
                n = kid_number

        if is_unique:
            kids.remove((n, name))

            if stat == "Nice":
                nice.append(name)
            else:
                naughty.append(name)

    not_found = [name for num, name in kids]        # !!! vzimam chast ot tuple

    result = ''

    if nice:
        result += f"Nice: {', '.join(nice)}\n"

    if naughty:
        result += f"Naughty: {', '.join(naughty)}\n"

    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"

    return result.strip()                           # zaradi \n


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))












