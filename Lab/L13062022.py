# Modules


# importirane funkciq ot dr fail
# from test_module import print_list
#
# print_list([1, 2, 3, 4])


# python:
# 1) programming language
# 2) runtime environment

# environments:
# 1) cpython = our
# 2) pypy

# ----------------------------------------------------
# a
# import os
# print(os.listdir('./'))

# b
# from os import listdir
# print(listdir('./'))

# c
# from os import *      # not good
# print(listdir('./'))

# d
# from os import listdir as maimun
# print(maimun('./'))

# ----------------------------------------------------

# from math import log
#
# value = 10
# base = 10
# print(log(value, base))

# ----------------------------------------------------
# pip - package manager

# pip install
# pip freeze      # pokzava koi sa ni 3rd party paketite

# ----------------------------------------------------
# requirements file

# pip freeze > requirements.txt
# pip install -r requirements.txt

# ----------------------------------------------------
#venv

# ----------------------------------------------------

# 1
# from pyfiglet import figlet_format
# from termcolor import colored
#
# print(figlet_format("Daniel", font="isometric1"))
# print(colored("Daniel", 'green', attrs=['underline']))

# ----------------------------------------------------
#custom modules


# packet - 1 file or a folder
# trqbva vytre fail __init__.py

from triangle import print_triangle     # dostypvame v __init__ chrez imeto na direktoriqta
from triangle.line import print_line    # za razlichni ot __ini__

print_triangle()
print_line()

























