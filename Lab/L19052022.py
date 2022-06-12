# Tuples and Sets

# Tuples: immutable but objects inside are mutable
# tt = (1, 2, 3, 4)
# print(tt)
# print(tt[1])
# nqmame append insert pop i tn
# moje prezapisvane tt = (1, 2, 4)

# definiciq
# t = (1, 2, 3)
# t = 1, 2, 3
# t = (1, ) # s edin element
# print(t)

# n = 15
# print(tuple(range(n)))

# ll = [1, 2, 3]
# print(tuple(ll))


# methods
# numbers = (1, 2, 3, 4)
# print(numbers.count(1))

# names = ('maimuna', 'maiz', 'morz')
# print(names.index('morz')) # index (1, 0)
# print(names.index('morz', 1)) # index ('morz', 1) tyrsi morz ot 1vi index nadqsno


# oshte operacii
# tt = (1, 2, 3, 4, 5)
#
# print(1 in tt) # True
#
# for i in tt:
#     print(i)
#
# print(f'{", ".join(map(str, tt))}') # !!!
#
# print(f'{len(tt)}')
#
# print((1, 2) + (3, 4, 5)) # concatenate


# unpacking
# tt = (1, 2, 3)
# x, y, z = tt
# print(x, y, z)
#
# ll = list(range(5, 16))
#
# for (index, value) in enumerate(ll):
#     print(f'll[{index}] = {value}')
#
# dd = {'one': 1, 'two': 2, 'three': 3}
#
# for key, value in dd.items():
#     print(f'dd[{key}]={value}')


# unpacking works for lists too
# ll = [1, 2, 3]
# a, b, c = ll


# 1
# occurences = {}
# numbers = [float(x) for x in input().split()] # nqma tuple comprehension
#
# for i in numbers:
#     if i not in occurences:
#         occurences[i] = 0
#     occurences[i] += 1
#
# for number, count in occurences.items():
#     print(f'{number:.1f} - {count} times')

# 2
# def average(values):
#     return sum(values) / len(values)
#
#
# dd = {}
#
# numbers = int(input())
# for i in range(numbers):
#
#     name, grade = input().split(' ') #unpacking
#     grade = float(grade)
#
#     if name not in dd.keys():
#         dd[name] = []
#     dd[name].append(grade)
#
# for student, grades in dd.items():
#     grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades) # !!!
#     grades_avg = average(grades)
#     print(f'{student} -> {grades_formatted} (avg: {grades_avg:.2f})')


# --------------------------------------------------------------------#
# tt = ([1, 2, 3], {}, (4, 5, 6))
# #tt[0] = 5   # ne stava
# tt[0].append(-4)    #stava
# --------------------------------------------------------------------#


# SETS
# --------------------------------------------------------------------#
# search, add, remove is very fast
# contain only unique values
# unordered (with hash tables)
# mutable

# ss = {1, 2, 3, 4, 5}
# sss = set() # samo taka prazen set
#
# [ss.add(1) for _ in range(1024)]
# print(ss)
#
# ss.add(8)
# ss.remove(4)
# print(4 in ss)      # check if value is in set
# print(len(ss))
# --------------------------------------------------------------------#

# operations
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s3 = {1, 3, 4, 5}
#
# print(f'{s1} union {s2} = {s1 | s2}')   #union = {1, 2, 3, 4, 5}
# print(f'{s1} & {s2} = {s1 & s2}')       #intersection = {3}
# print(f'{s2} < {s3} = {s2 < s3}')       #subset = True
# print(f'{s1} - {s2} = {s1 - s2}')       #difference = {1, 2}


# set comprehension
# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print({x ** 2 for x in ll})         #kato list ama s kydravi skobi

# --------------------------------------------------------------------#

# 3
# n = int(input())
#
# names_set = set()
#
# for _ in range(n):
#     names_set.add(input())
#
# [print(name) for name in names_set]     # !!!

# 4
# number = int(input())
# parking_lot = set()
#
# commands = [input().split(', ') for i in range(number)]
#
# for direction, car_number in commands:
#     if direction == 'IN':
#         parking_lot.add(car_number)
#     elif direction == 'OUT':
#         parking_lot.remove(car_number)
#
# if parking_lot:
#     [print(car_number) for car_number in parking_lot]
# else:
#     print('Parking Lot is Empty')

# 5
# def is_vip(guest):
#     return guest[0].isdigit()
#
#
# n = int(input())
# vip_guests = set()
# regular_guests = set()
#
# for i in range(n):
#     current_guest = input()
#     if is_vip(current_guest):
#         vip_guests.add(current_guest)
#     else:
#         regular_guests.add(current_guest)
#
# while 1:
#     command = input()
#     if command == 'END':
#         break
#
#     if is_vip(command):
#         vip_guests.remove(command)
#     else:
#         regular_guests.remove(command)
#
# print(f'{len(vip_guests) + len(regular_guests)}')
# [print(x) for x in sorted(vip_guests)]
# [print(x) for x in sorted(regular_guests)]

# --------------------------------------------------------------------#
# from random import shuffle
#
# print(shuffle(ll))
# --------------------------------------------------------------------#

# 6 - sam
#1 5 4 2 2 3 1 3 2 -> value
#0 1 2 3 4 5 6 7 8 -> pos

number_sequence = list(map(int, input().split(' ')))
target_sum = int(input())
set_of_numbers = set()
iterations = 0

for i in range(len(number_sequence)):
    for j in range(len(number_sequence)):
        if i < j:
            iterations += 1
            if number_sequence[i] + number_sequence[j] == target_sum:
                print(f'{number_sequence[i]} + {number_sequence[j]} = {target_sum}')

                current_tuple = (number_sequence[i], number_sequence[j])

                set_of_numbers.add(current_tuple)

print(f'Iterations done: {iterations}')
[print(x) for x in set_of_numbers]





