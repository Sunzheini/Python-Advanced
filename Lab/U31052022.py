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
def even_odd(*args):
    result = []
    filter = args[-1]
    parity = 0 if filter == 'even' else 1       # !!!

    for i in range(len(args)-1):
        if args[i] % 2 == parity:
            result.append(args[i])

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# -2.33.03














































