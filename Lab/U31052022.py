# Exercise: Fuctions Advanced

# 1
# def find_them(*args):
#     negative_sum = 0
#     positive_sum = 0
#
#     for i in args:
#         if i < 0:
#             negative_sum += i
#         elif i > 0:
#             positive_sum += i
#
#     return negative_sum, positive_sum
#
#
# sequence = [int(x) for x in input().split()]
# negative_sum, positive_sum = find_them(*sequence)
#
# print(negative_sum)
# print(positive_sum)
#
# if abs(negative_sum) > positive_sum:
#     print("The negatives are stronger than the positives")
# elif abs(negative_sum) < positive_sum:
#     print("The positives are stronger than the negatives")

# 2
# def kwargs_length(**kwargs):
#     return len(kwargs)
#
#
# dictionary = {}
#
# print(kwargs_length(**dictionary))

# 3
# def even_odd(*args):
#     result = []
#     filter = args[-1]
#     parity = 0 if filter == 'even' else 1       # !!!
#
#     for i in range(len(args)-1):
#         if args[i] % 2 == parity:
#             result.append(args[i])
#
#     return result
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# 4
# def even_odd_filter(**kwargs):
#     result = {}
#
#     for key, value in kwargs.items():
#         parity = 0 if key == 'even' else 1
#         filtered_list = [x for x in value if x % 2 == parity]
#         result[key] = filtered_list
#
#     return dict(sorted(result.items(), key=lambda x: -len(x[1])))   # !!!
#     # podchertava go no raboti
#
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
#
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))

# 5
# def concatenate(*args, **kwargs):
#     new_string = ''.join(args)      # !!!
#
#     for key, value in kwargs.items():
#         new_string = new_string.replace(key, value) # !!!
#
#     return new_string
#
#
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
#

# 6
# def func_executor(*args):
#
#     result_list = []
#
#     for func, params in args:               # unpack tuple!!!
#         result_list.append(f'{func.__name__} - {func(*params)}')   # unpack tuple!!!
#         # vzemahme i imeto na funkciqta
#
#     return '\n'.join(result_list)
#
#
# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result
#
#
# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result
#
#
# print(func_executor(
#     (sum_numbers, (1, 2)),
#     (multiply_numbers, (2, 4))
# ))
#
# print(func_executor(
#     (make_upper, ("Python", "softUni")),
#     (make_lower, ("PyThOn",)),
# ))

# 7
# def grocery_store(**kwargs):
#     sorted_dict = sorted(kwargs.items(),
#                          key=lambda x: (-x[1], -len(x[0]), x[0]))   # !!!
#
#     result = []
#
#     for i in sorted_dict:
#         result.append(f'{i[0]}: {i[1]}')
#         # za da vyrnem kakto iskat text
#
#     return '\n'.join(result)
#
#
# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))
#
# print(grocery_store(
#     bread=2,
#     pasta=2,
#     eggs=20,
#     carrot=1,
# ))

# 8
# def age_assignment(*args, **kwargs):
#     result = []
#
#     for key, value in kwargs.items():
#         for i in args:
#             if i[0] == key:
#                 result.append(f"{i} is {value} years old.")
#
#     result = sorted(result, key=lambda x: x)
#
#     return '\n'.join(result)
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

# 9
def palindrome(word, index):
    if index >= len(word) // 2:
        return f'{word} is a palindrome'

    left = word[index]
    right = word[-1-index]

    if left != right:
        return f'{word} is not a palindrome'

    return palindrome(word, index+1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))







































