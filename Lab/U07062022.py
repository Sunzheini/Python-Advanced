# Exercise: File Handling

# 1
# target_symbols = ["-", ",", ".", "!", "?"]
#
# with open('./text.txt', 'r') as file:
#     for index, line in enumerate(file):
#         if index % 2 == 0:

#             # reverse the line:
#             result = ' '.join(line.strip().split()[::-1])
#
#             for symbol in target_symbols:
#                 result = result.replace(symbol, '@')
#
#             print(result)

# 2
# from string import punctuation      # !!!
#
#
# def count_symbols(line):
#     punctuation_symbols = set(punctuation)
#     letters_count = 0
#     punctuation_count = 0
#
#     for symbol in line:
#         if symbol.isalpha():
#             letters_count += 1
#         elif symbol in punctuation_symbols:
#             punctuation_count += 1
#
#     return letters_count, punctuation_count
#
#
# # open several files as links
# with open('./text.txt', 'r') as file, open('./output.txt', 'w') as result:
#     for index, line in enumerate(file):
#         letters, punctuations = count_symbols(line)
#         result.write(f'Line {index + 1}: {line.strip()} ({letters})({punctuations})\n')

# 3
while 1:
    line = input()
    if line == 'End':
        break

    explode = line.split('-')
    command, file_name = explode[0], explode[1]

    if command == 'Create':
        with open(f'./{file_name}', 'w') as file:
            pass

    elif command == 'Add':
        content = explode[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(content + '\n')

    elif command == 'Replace':
        old_string, new_string = explode[2], explode[3]
        with open(f'./{file_name}', 'r+') as file:      # !!!
            file_content = file.read().replace(old_string, new_string)

            file.truncate(0)        # delete content
            file.write(file_content)

    else:
        pass

# -57.13















