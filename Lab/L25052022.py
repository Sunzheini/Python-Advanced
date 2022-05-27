

# multidimentional lists
# mm = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# mm.append([-11])
# print(mm)
#
# mm.pop()
# print(mm)
#
# print(mm[1][2])

# 3D
# cc = [
#     [ #0
#         [1, 2, 3],
#         [2, 3, 4],
#         [4, 5, 6],
#     ],
#     [ #1
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#     ],
# ]

# list of n zeros
# ll = []
# for i in range(5):
#     ll.append(0)
# print(ll)

#matrix of NxM zeros
# mm = []
# for i in range(n):
#     ll = []
#     for j in range(m):
#         ll.append(0)
#
#     mm.append(ll)

# 1
def read_matrix():
    mm = []
    n, m = [int(x) for x in input().split(', ')]

    total = 0

    for i in range(n):
        row = [int(x) for x in input().split(', ')]
        total += sum(row)
        mm.append(row)
    return mm, total


matrix, total_sum = read_matrix()          # !!!

print(total_sum)
print(matrix)

# 2.03.56
























