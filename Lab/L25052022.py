

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
# def read_matrix():
#     mm = []
#     n, m = [int(x) for x in input().split(', ')]
#
#     total = 0
#
#     for i in range(n):
#         row = [int(x) for x in input().split(', ')]
#         total += sum(row)
#         mm.append(row)
#     return mm, total
#
#
# matrix, total_sum = read_matrix()          # !!!
#
# print(total_sum)
# print(matrix)


# Comprehension
#-------------------------------------------------------------------------------------

#matrix = [[0 for j in range(2)] for i in range(3)]
#matrix = [[j for j in range(1, 9)] for i in range(1, 5)]

# mm = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# print(mm)
#
# print(
#     [v + 1 for row in mm for v in row]          #flattening
# )
#
# print(
#     [[v + 1 for v in row] for row in mm]        #new matrix
# )

#-------------------------------------------------------------------------------------

# 2a
# mm = []
# row = int(input())
# for i in range(row):
#     ll = [int(x) for x in input().split(', ')]
#     mm.append(
#         [y for y in ll if y % 2 == 0]
#     )
# print(mm)

# 2b
# n = int(input())
# matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
# print([[y for y in row if y % 2 == 0] for row in matrix])

# 3
# mm = []
# rows = int(input())
# for _ in range(rows):
#     ll = [int(x) for x in input().split(', ')]
#     mm.append(ll)
#
# flattened = [x for row in mm for x in row]
# print(flattened)


# Accessing element
#-------------------------------------------------------------------------------------

# mm = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# print(mm[1])            # [4, 5, 6]
# print(mm[1][0])         # 4
# print(mm[-1])           # posledniq red
#
#
# for i in range(len(mm)):
#     for j in range(len(mm[i])):
#         print(mm[i][j], end=' ')        # 1 2 3 4 5 6 7 8 9


#Input automation
#-------------------------------------------------------------------------------------

# import sys
# from io import StringIO
#
# test_input = '''3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
# '''
#
# sys.stdin = StringIO(test_input)
#
# print(input())
# print(input())
# print(input())
# print(input())

#-------------------------------------------------------------------------------------


# 4
# mm = []
# rows, columns = [int(x) for x in input().split(', ')]
# sum_list = [0 for x in range(columns)]
#
# for _ in range(rows):
#     ll = [int(y) for y in input().split(' ')]
#     mm.append(ll)
#
# for i in range(len(mm)):
#     for j in range(len(mm[i])):
#         sum_list[j] += mm[i][j]
#
# [print(x) for x in sum_list]


# Diagonal - matricite sa s raven broi koloni na vseki red
#-------------------------------------------------------------------------------------

# stoinost e na glavniq diagonal ako:           row_index == column_index
# stoinost e na vtorostepenniq diagonal ako:    row_index = n - column_index - 1
# below main diagonal ako:                      column_index < row_index
# above main ako:                               column_index > row_index

#-------------------------------------------------------------------------------------


# 5
# mm = []
# size = int(input())
# total = 0
#
# for _ in range(size):
#     mm.append([int(x) for x in input().split()])
#
# for i in range(size):
#     for j in range(size):
#         if j == i:
#             total += mm[i][j]
#
# print(total)

# 6
# n = int(input())
# matrix = [list(input()) for _ in range(n)]      # pravi input simvoli na list
# symbol = input()
# found = False
#
# for i in range(n):
#     if found:
#         break
#     for j in range(n):
#         if matrix[i][j] == symbol:
#             print(f"({i}, {j})")
#             found = True
#             break                               # zabravih break i na vynshniq cikyl
#
# if not found:
#     print(f"{symbol} does not occur in the matrix")


#Can have other nested structures











