# File Handling

#-------------------------------------------------------------
# from io import open
#
#
# def give_contents(file_path):
#     print(f'Opening: "{file_path}"...')
#     file = open(file_path)
#     print(file.read())      # printira sydyrjanieto

# relativen pyt, based on the location of the current file,
# ./ e tekushta direktoriq
#give_contents('./demo.txt')

# ../ e parent direktoriq
#give_contents('../another_demo.txt')


#absolute - based on os file location
#give_contents('D:\Study\Projects\PycharmProjects\Python-Advanced\lab\demo.txt')


# path separator
# windows - D:\\repos\\python-advanced
# linux - /repos/python-advanced

#print(os.sep) # za windows e \

#-------------------------------------------------------------
# opening files errors

# try:
#     open('./demo.txt')          # otvarq fail no ne i direktoriq
#     print('File is found!')
# except FileNotFoundError:       # i pri greshni direktorii
#     print('Not found!')

#-------------------------------------------------------------
# file modes - default e rt

# kakvo shte pravim
# r - read only

# pod kakva forma
# t - text mode
# b - binary mode

# print(open('demo.txt', 'rt').read())
# # normalno - kato text
#
# print(open('demo.txt', 'rb').read()) # chete kartinki v baitove
# # b'I am Daniel\r\nYou are Maimuna\r\nAnd you are Maxi'

#-------------------------------------------------------------
# 1

# def file_opener(file_path):
#     try:
#         open(file_path, 'r')
#         print("File found!")
#     except FileNotFoundError:
#         print("File not found")
#
#
# file_opener('./demo.txt')

#-------------------------------------------------------------
# chetene

# file_path = './demo.txt'
# file = open(file_path, 'r')
# print(file.read(9))     # number of symbols
# print(file.read(8))     # next 8 symbols, ako svyrshi pochva prazni da chete
#                         # noviq red e simvol

# print(file.read())      # whole file
# ako go chetem navednyj celiq text se zarejda v RAM


# kogato ochakvame golqm fail e dobre malko po malko
# file_path = './demo.txt'
# file = open(file_path, 'r')
# while True:
#     chars = file.read(3)
#     if not chars:
#         break
#     print(chars)


# file_path = './demo.txt'
# file = open(file_path, 'r')
# while 1:
#     line = file.readline()      # red po red
#     if not line:
#         break
#     print(line, end='')


# file_path = './demo.txt'
# file = open(file_path, 'r')
# print(file.readline(3)) # ako moje da prochete 3 simvola
# # ot tozi red gi vryshta, ako ne kolkoto ima


# file_path = './demo.txt'
# file = open(file_path, 'r')
# print(file.readlines()) # vsichki redove kato spisyk


# iteraciq2
# file_path = './demo.txt'
# file = open(file_path, 'r')
# for i in file:
#     print(i.strip())

#-------------------------------------------------------------

# 2
# file = open('./demo.txt', 'r')
# the_sum = 0
# for line in file:
#     the_sum += int(line)

#-------------------------------------------------------------
# writing modes

# w - create or overwrite file
# import time
# from os import linesep
#
# file = open('./demo2.txt', 'w')
# file.write('It worksz!')
# file.write(linesep)
# file.write(str(time.time()))
# file.write(linesep)


# a - create or append
# import time
# from os import linesep
#
# file = open('./demo2.txt', 'a')
# file.write('It worksz!')
# file.write(linesep)
# file.write(str(time.time()))
# file.write(linesep)


# x = create new file or raise exception if exists
# import time
# from os import linesep
#
# file = open('./demo2.txt', 'x')
# file.write('It worksz!')
# file.write(linesep)
# file.write(str(time.time()))
# file.write(linesep)

#-------------------------------------------------------------
# closing files

# file1 = open('./demo2.txt', 'w')
# file1.write('noob')
# file1.close()             # s close
# file1.write('ddd')


# pishem samo v with bloka sled tova zatvarq
# with open('./demo2.txt', 'w') as file:
#     file.write('hdhfhwf')


# chetem ot ediniq celiq fail i pishem v drugiq
# for i in range(3):
#     with open('./demo.txt', 'r') as file:
#         text = file.read()
#
#     with open('./demo2.txt', 'a') as file:
#         file.write(text)


# # 3 pyti ot ediniq v drugiq fail
# for i in range(3):
#     with open('./demo.txt', 'r') as file_in:
#         with open('./demo2.txt', 'w') as file_out:
#             for line in file_in:
#                 file_out.write(line)

#-------------------------------------------------------------
# deleting file

# import os
# from os.path import exists
#
# if exists('./todel.txt'):
#     os.remove('./todel.txt')

#-------------------------------------------------------------
# directories
#from os import mkdir, rmdir

#directory_path = './'
#mkdir('./dir_to_del')   # create

#rmdir('./dir_to_del')   # delete

#print(listdir(directory_path))   # ls, samo imenata

# + direktoriite
# files_and_dirs_names = listdir(directory_path)
# files_and_dirs = [join(directory_path, f) for f in files_and_dirs_names]

#-------------------------------------------------------------

# 5
# import re
#
#
# def read_words():
#     with open('./demo.txt') as file:
#         return file.read().split()
#
#
# def count_words_in_file(words):
#     words_counts = {word: 0 for word in words}
#     with open('./demo.txt') as file:
#         for line in file:
#             words_in_line = re.findall(r'\b\S+\b', line)
#             for word in words:
#                 words_in_line[word] += words_in_line.count(word)
#     return words_counts
#
#
# print(count_words_in_file(read_words()))













#-------------------------------------------------------------







