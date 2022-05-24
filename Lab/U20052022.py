# 1
# my_set = set()
# n = int(input())
# for i in range(n):
#     name = input()
#     my_set.add(name)
#
# [print(x) for x in my_set]

# 2
# n, m = [int(x) for x in input().split()]
# set1 = {input() for i in range(n)}
# set2 = {input() for j in range(m)}
#
# set3 = set1.intersection(set2)      #taka e po-dobre intersection
# [print(y) for y in set3]

# 3a
# n = int(input())
# ss = set()
#
# for i in range(n):
#     command = input().split()
#     for j in command:
#         ss.add(j)
#
# [print(x) for x in ss]

# 3b
# n = int(input())
# ss = set()
# for i in range(n):
#     command = set(input().split())
#     ss = ss.union(command)      # otnachalo da ima ss =
#
# [print(x) for x in ss]

# 4
# text = input()
#
# dd = {}
#
# for i in text:
#     if i not in dd.keys():
#         dd[i] = 0
#     dd[i] += 1
#
# for key, value in sorted(dd.items()):
#     print(f"{key}: {value} time/s")

# 5
# n = int(input())
# longest_intersection = set()
#
# for i in range(n):
#     first_range, second_range = input().split('-')
#
#     first_start, first_end = [int(x) for x in first_range.split(',')]
#     second_start, second_end = [int(x) for x in second_range.split(',')]
#
#     first_set = set(range(first_start, first_end + 1))
#     second_set = set(range(second_start, second_end + 1))
#
#     current_intersection = first_set.intersection(second_set)
#
#     if len(current_intersection) > len(longest_intersection):
#         longest_intersection = current_intersection
#
# print(f"Longest intersection is {sorted(list(longest_intersection))} "
#       f"with length {len(longest_intersection)}")

# 6
n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    current_name = input()
    current_sum = 0
    for j in current_name:
        current_sum += ord(j)
    current_sum = int(current_sum / i)

    if current_sum % 2 != 0:
        odd_set.add(current_sum)
    else:
        even_set.add(current_sum)

sum1 = sum(odd_set)
sum2 = sum(even_set)

if sum1 == sum2:
    current_union = odd_set.union(even_set)
    print(f"{', '.join(map(str, current_union))}")

elif sum1 > sum2:
    current_difference = odd_set.difference(even_set)
    print(f"{', '.join(map(str, current_difference))}")
else:
    current_difference = odd_set.symmetric_difference(even_set)
    print(f"{', '.join(map(str, current_difference))}")















