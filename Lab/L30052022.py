

# Functions Advanced

#---------------------------------------------------------
# packigng and unpacking pregovor + dopylnenie

# ll = [1, 2, 3, 4]

# a, b, c, d = ll     # default
# print(a, b, c, d)

# k, l, *r = ll   #izkarai pyrvite 2 a ostanalite v spisyk r
# print(k, l)
# print(r)

# k, *l, r = ll     #bez pyrviq i posledniq gi sloji v l
# print(k, l, r)

# k, *_, r = ll       # ne ni interesuvat srednite
# print(k, r)

#---------------------------------------------------------

# Packing

# we use *args to arguments into tuple
# def some_func(*args):
#     print(args)
#
# some_func(1, 2, 3)                  # (1, 2, 3)
# some_func('Daniel', 'Zorov')        # ('Daniel', 'Zorov')
# some_func(True, False)              # (True, False)
# some_func()                         # ()


# ako e bez * pred args mojem da q izvikame samo s 1 parametyr
# def f(args):
#     print(args)
#
# f(1)
# f([1, 2, 3])
# f({1: 2, 3: 4})
# f({1, 2, 3})

#---------------------------------------------------------

# 1
# def multiply(*args):
#     product = 1
#     for i in args:              # !!! taka vzimame ot tuple-a
#         product *= i
#     return product
#
#
# print(multiply(1))
# print(multiply(1, 2))
# print(multiply(1, 2, 3, 4, 5))

#---------------------------------------------------------

#kwargs - packing arguments into dictionary
# def f(**kwargs):
#     if 'age' in kwargs:
#         kwargs['age'] = None
#     print(kwargs)
#
#
# print(f(name='Daniel', age=19))             # {'name': 'Daniel', 'age': 19}
# print(f(x=1, y=-11))                        # {'x': 1, 'y': -11}
# print(f(values=[1, 2, 3, 4], pair=(7, 6)))  # {'values': [1, 2, 3, 4], 'pair': (7, 6)}

#---------------------------------------------------------
# args + kwargs

# def f(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# f(1, 2, 3)
# f(x=1, y=2, z=3)
# f(1, 2, 3, y=4)

#---------------------------------------------------------

# + positional parmeters

# def f2(x, *args, **kwargs):
#     print(f'x={x}, args={args}, kwargs={kwargs}')
# # poziciqta im ima znachenie
# # trqbva pone da podadem broq na positional parametrite, t.e. pone 1 sega
#
# f2(3)           # x=3, args=(), kwargs={}
# f2(3, 4)        # x=3, args=(4,), kwargs={}
# f2(3, 4, 5)     # x=3, args=(4, 5), kwargs={}
#
# f2(x=11)        # x=11, args=(), kwargs={}
# f2(x=11, y=12)  # x=11, args=(), kwargs={'y': 12}

#---------------------------------------------------------

#packing again

# ll1 = [1, 2, 3, 4]
#
# k, l, *r = ll1
# print(k, l, r)          # 1 2 [3, 4]
#
# ll2 = [1, ll1, -2]
# ll3 = [1, *ll1, -2]     # unpack this list in the middle
# print(ll2)              # [1, [1, 2, 3, 4], -2]
# print(ll3)              # [1, 1, 2, 3, 4, -2]
#
# dd1 = {
#     'x': 1,
#     'y': 2
# }
#
# dd2 = {
#     'z': 3,
#     **dd1,          #** - unpack as a dictionary
# }
#
# print(dd2)          # {'z': 3, 'x': 1, 'y': 2}

#---------------------------------------------------------

# def f(*args, **kwargs):
#     print(f"{args}, {kwargs}")
#
#
# def shame_maimuna(Daniel, **kwargs):
#     print(f"Daniel has {Daniel}. He is superman.")
#
#
# numbers = [1, 2, 3, 4, 5]
# grades = {
#     'Doncho': 3,
#     'Ivan': 4,
#     'Daniel': 6,
#     'Pesho': 4.5,
# }
# # !!!!!!!!!
# shame_maimuna(**grades)     # Daniel has 6. He is superman.
# # syshtotoe  kato:
# shame_maimuna(Doncho=3, Ivan=4, Daniel=6, Pesho=4.5)
#
# f(numbers)              # ([1, 2, 3, 4, 5],), {}
# f(*numbers)             # (1, 2, 3, 4, 5), {}
# f(grades)               # ({'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5},), {}
# f(**grades)             # (), {'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5}
# f(numbers, grades)      # ([1, 2, 3, 4, 5], {'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5}), {}
# f(*numbers, **grades)   # (1, 2, 3, 4, 5), {'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5}

#---------------------------------------------------------

# 2
# def get_info(name, town, age):
#     return f'This is {name} from {town} and he is {age} years old'
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
#

#---------------------------------------------------------

# sorting

# values = [1, 2, 4, 7, 9, -2, -44, 33]
#
# values.sort()               # sorts the list
# print(values)
#
# print(sorted(values))       # new list and doesnt change original
#
# print(sorted(['Maimuna', 'Daniel', 'Maxi', 'Zorov']))
#
# # tuples are sortable
# print(sorted([(1, 7), (-1, 3), (1, 4)]))
#
# print(sorted([1, 2, 4, 7, 9, -2, -44, 33], reverse=True))
#
# print(
#     sorted([1, -2, -44, 33],
#            key=lambda x: x % 5)
# )

#---------------------------------------------------------

# sortirane dict

# my_dict = {'Maymuna': 26, 'Daniel': 44, 'Maxi': 55}
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])
# sorted_dict2 = sorted(my_dict.items(), key=lambda x: x[1])
# print(sorted_dict)      # [('Daniel', 44), ('Maxi', 55), ('Maymuna', 26)]
# print(sorted_dict2)     # [('Maymuna', 26), ('Daniel', 44), ('Maxi', 55)]
#
# print(my_dict.items())

#---------------------------------------------------------

#sorting strings

# values = ['Maymuna', 'Maxi', 'Daniel']
#
# print([-ord(x) for x in 'Daniel'])
#
# print(
#     sorted(
#         values,
#         key=lambda x: [ord(c) for c in x],
#     )
# )       # ['Daniel', 'Maxi', 'Maymuna']

#---------------------------------------------------------

# 3
import os


# def sorting_cheeses(**kwargs):
#     sorted_cheeses = sorted(kwargs.items(),
#                             key=lambda x: (-len(x[1]), x[0]),)
#
#     result = []
#
#     for name, pieces_counts in sorted_cheeses:
#         result.append(name)
#         result.extend(sorted(pieces_counts, reverse=True))
#
#     # '\n\r' for Windows
#     # os.linesep
#     return '\n'.join([str(x) for x in result])
#
#
# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )

#---------------------------------------------------------

# nested_functions

# def f1():
#     def f2():
#         print("I am f2")
#
#     print("I am f1")
#     f2()
#
#
# f1()


# def math_operation(operation, *args):
#
#     def add(*args):
#         return sum(args)
#
#     def subtract(*args):
#         return sum(-x for x in args)
#
#     def multiply(*args):
#         result = 1
#         for x in args:
#             result *= x
#         return result
#
#     if operation == '+':
#         return add(*args)
#     elif operation == '-':
#         return subtract(*args)
#     elif operation == '*':
#         return multiply(*args)
#     else:
#         return None
#
# print(math_operation('+', 1, 2, 3, 4))
# print(math_operation('-', 1, 2, 3, 4))
# print(math_operation('*', 1, 2, 3, 4))

#---------------------------------------------------------

# return functions, which are used as normal functions

# def math_operation_factory(operation):
#
#     def add(*args):
#         return sum(args)
#
#     def subtract(*args):
#         return sum(-x for x in args)
#
#     def multiply(*args):
#         result = 1
#         for x in args:
#             result *= x
#         return result
#
#     if operation == '+':
#         return add
#     elif operation == '-':
#         return subtract
#     elif operation == '*':
#         return multiply
#     else:
#         return None
#
#
# add = math_operation_factory('+')
# subtract = math_operation_factory('-')
# print(add(1, 2, 3))
# print(add(1, 2, -4))
# print(subtract(1, 2, -4))
# print(subtract(1, 2, -4))

#---------------------------------------------------------

# closure -
# vryshtame vytreshnata funkciq, koqto
# close-va vynshnata stoinost x

# def f1(x):
#     def inner_f1(y):
#         return x + y
#
#     return inner_f1
#
#
# func1 = f1(5)
# print(func1(6))         # 11
# print(func1(5))         # 10

#---------------------------------------------------------

# 4

# def rectangle(length, width):
#
#     def area():
#         return length * width
#
#     def perimeter():
#         return 2 * (length + width)
#
#     if not isinstance(length, int) or not isinstance(width, int):
#         return 'Enter valid values!'
#             # proverka dalie  int
#
#     return f'''Rectangle area: {area()}
# Rectangle perimeter: {perimeter()}'''
#
#
# print(rectangle(2, 10))
# print(rectangle('2', 10))

# 5
# def operate(operation, *args):
#
#     def add(*args):
#         return sum(args)
#
#     def subtract(x, *args):
#         return x + sum(-y for y in args)
#
#     def multiply(*args):
#         result = 1
#         for x in args:
#             result *= x
#         return result
#
#     def divide(x, *args):
#         result = x
#         for value in args:
#             result /= value
#         return result
#
#     if operation == '+':
#         return add(*args)
#     elif operation == '-':
#         return subtract(*args)
#     elif operation == '*':
#         return multiply(*args)
#     elif operation == '/':
#         return divide(*args)
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))

#---------------------------------------------------------

# Recursion - funckiq koqto vika sebe si

# import time
#
# def f1():
#     print(time.time())
#     time.sleep(1)
#     f1()
#
# f1()


# trqbva da imame neshto koeto da spre rekursiqta

# def reverse_loop(n):
#     if n < 0:               # exit case
#         return
#     print(n)
#     reverse_loop(n - 1)     # recursive call
#
# def loop(n):
#     if n < 0:
#         return
#     loop(n - 1)
#     print(n)
#
# reverse_loop(5)
# loop(5)

#---------------------------------------------------------

# factorial: n! = n * (n - 1)!, 1! = 1, 0! = 1

# def fact(n):
#     if n in (0, 1):
#         return 1
#
#     n_1_fact = fact(n - 1)
#     return n * n_1_fact
#
#
# print(fact(5))

#---------------------------------------------------------

# 6
def recursive_power(number, power):
    if power == 0:
        return 1

    if power == 1:
        return number

    return number * recursive_power(number, power-1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))














