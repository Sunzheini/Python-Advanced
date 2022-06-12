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
# from os.path import exists
# from os import remove
#
# while 1:
#     line = input()
#     if line == 'End':
#         break
#
#     explode = line.split('-')
#     command, file_name = explode[0], explode[1]
#
#     if command == 'Create':
#         with open(f'./{file_name}', 'w') as file:
#             pass
#
#     elif command == 'Add':
#         content = explode[2]
#         with open(f'./{file_name}', 'a') as file:
#             file.write(content + '\n')
#
#     elif command == 'Replace':
#         if not exists(f'./{file_name}'):
#             print("An error occurred.")
#             continue
#
#         old_string, new_string = explode[2], explode[3]
#         with open(f'./{file_name}', 'r+') as file:      # !!!
#             file_content = file.read().replace(old_string, new_string)
#
#             file.seek(0)            # pointer at zero position
#             file.truncate(0)        # delete content from pointer
#             file.write(file_content)
#
#     else:
#         if not exists(f'./{file_name}'):
#             print("An error occurred.")
#             continue
#
#         remove(f'./{file_name}')


#-------------------------------------------------------------

# print(listdir('./'))                    # tekushtata direktoriq
# print(listdir('../'))                   # gornata direktoriq
# print(listdir('./{folder2}/{folder3}')) # konkretna direktoriq

#-------------------------------------------------------------

# 4
# from os import listdir
# from os.path import isdir, join
#
#
# def directory_traversal(path, files_by_ext):
#     for element in listdir(path):
#         if isdir(join(path, element)):       # True e fail, False ne e, t.e. e direktoriq
#             directory_traversal(join(path, element), files_by_ext)
#         else:
#             extension = element.split('.')[-1]
#             if extension not in files_by_ext:
#                 files_by_ext[extension] = []
#             files_by_ext[extension].append(element)
#
#
# result = {}
# directory_traversal('./', result)
#
# result = sorted(result.items(), key=lambda x: (x[0], x[1]))
#
# new_dict = {}
#
# for i in result:
#     key = i[0]
#     value = i[1]
#     new_dict[key] = value
#
# with open('./result.txt', 'w') as output_file:
#     for ext, files in new_dict.items():
#         output_file.write(ext + '\n')
#
#         for file in files:
#             output_file.write(f'- - - {file}\n')







