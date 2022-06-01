

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

values = [1, 2, 4, 7, 9, -2, -44, 33]

values.sort()               # sorts the list
print(values)

print(sorted(values))       # new list and doesnt change original

print(sorted(['Maimuna', 'Daniel', 'Maxi', 'Zorov']))

# tuples are sortable
print(sorted([(1, 7), (-1, 3), (1, 4)]))

print(sorted([1, 2, 4, 7, 9, -2, -44, 33], reverse=True))

print(
    sorted([1, -2, -44, 33],
           key=lambda x: x % 5)
)

#---------------------------------------------------------





# -1:48:14
















