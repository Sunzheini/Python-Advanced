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
text = input()

dd = {}

for i in text:
    if i not in dd.keys():
        dd[i] = 0
    dd[i] += 1

for key, value in sorted(dd.items()):
    print(f"{key}: {value} time/s")

# 5 -1:19:34






