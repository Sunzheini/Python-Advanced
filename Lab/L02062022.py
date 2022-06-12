# Error Handling


# syntax errors - nevaliden python kod
# exception - obekti pazqt info za konkretnata greshka
#     index error
#     type error
#     name error

# 1
# numbers_list = input().split(", ")
# result = 1
#
# for i in range(len(numbers_list)):
#     number = int(numbers_list[i])
#     if number <= 5:
#         result *= number
#     elif number <= 10:
#         result /= number
#
# print(int(result))

# ----------------------------------------------------------
#example1

# class ValueTooSmallException(Exception):
#     pass
#
#
# value = int(input())
#
# if value < 10:
#     raise ValueTooSmallException(f'{value} less than 10')

# ----------------------------------------------------------
#example2

# class ValueNotOneOrZero(Exception):
#     pass
#
#
# #value should only contain 1 and 0
# str_value = input()
#
# for i in str_value:
#     if i not in ['0', '1']:
#         raise ValueNotOneOrZero('noob')

# ----------------------------------------------------------

# 2
# class ValueCannotBeNegative(Exception):
#     pass
#
#
# for i in range(5):
#     current_number = int(input())
#
#     if current_number < 0:
#         raise ValueCannotBeNegative

# ----------------------------------------------------------
# try-except
# import random
#
#
# def try_raise_exception():
#     chance = 0.7
#     if random.random() < chance:     # ot 0 do 1
#         raise ValueError('Invalid Value')
#
#
# for i in range(10):
#     try:                #this code may raise an exception
#         try_raise_exception()
#         print('No Exception')
#     except ValueError:  #which exception handles the error
#         print('Error handled!!!')

# ----------------------------------------------------------
# finally - izpylnqva se nezavisimo dali imame try ili except

# import random


# def try_raise_exception():
#     chance = 0.7
#     if random.random() < chance:     # ot 0 do 1
#         raise ValueError
#
#
# for i in range(10):
#     try:
#         try_raise_exception()
#         print(f'Try {i} - No Exception!')
#     except ValueError:
#         print(f'Try {i} - Value Error Raised!')
#     finally:
#         print('noob')

# ----------------------------------------------------------
# da se vijda syobshtenieto ot raise ValueError
#nqkolko greshki navednyj
# import random
#
#
# def try_raise_exception():
#     chance = 0.3
#     value = random.random()
#     if value < chance:     # ot 0 do 1
#         raise ValueError('Invalid Value!')
#     elif value < 0.7:
#         raise TypeError('Invalid Type!')
#
#
# for i in range(10):
#     try:
#         try_raise_exception()
#         print(f'Try {i} - No Exception!')
#     except (ValueError, TypeError) as e:
#         print(f'Try {i} - Value Error Raised! {e}{type(e).__name__}')
#         # vijda se syobshtenie ot po-gore

# ----------------------------------------------------------
#nqkolko exceptiona v razlichni blokove
# import random
#
#
# def try_raise_exception():
#     chance = 0.3
#     value = random.random()
#     if value < chance:     # ot 0 do 1
#         raise ValueError('Invalid Value!')
#     elif value < 0.7:
#         raise TypeError('Invalid Type!')
#
#
# for i in range(10):
#     try:
#         try_raise_exception()
#         print(f'Try {i} - No Exception!')
#     except ValueError as e:
#         print(f'Try {i} - Value Error Raised! {e}{type(e).__name__}')
#     except TypeError as e2:
#         print(f'Try {i} - Type Error Raised! {e2}{type(e2).__name__}')

# ----------------------------------------------------------

# 2
# text = input()
#
# try:
#     times = int(input())
#     print(text * times)
# except ValueError:
#     print("Variable times must be an integer")

# ----------------------------------------------------------
# except bez nishto - prihvashta vsqkakvi no ne dava info

# try:
#     pass
# except:
#     print("Exception")
















