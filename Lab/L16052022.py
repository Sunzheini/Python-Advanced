# Lists as Stacks and Queues

#tova sa stukturi ot danni
#stack: lifo
#queue: filo
#priority queue -> most optimal element out

#data structure types:
#linear data structures: list, queue, stack (linear are on 1 line)
#hash sets: dictionaries, sets
#trees: binary, RBT, A* trees
#graphs

#stack - on top of each other, and only can access the last one / top one

# push --> add element to top of stack
# pop --> removes top elements
# peek --> vryshta no ne iztriva top element
# len --> count of elements in stack

# in pyhton we use lists as stacks - mylist = []
# push - append()
# pop - pop()
# peek - print(mylist[-1])
# len - len(mylist)

# primer - stack implemented as list, resizing array
# s = []
# s.append(1)
# s.append(2)
# s.append(3)
# s.append(4)
# print(s[-1])
# s.pop()
# print(s[-1])
# s.append(9)
# print(s[-1])

#other variant - stack implemented as linked list

# s = [1, 2, 3, 4, 5]
# s.insert(2, 11) # not a stack operation
# also the operations reverse, count, sort, pop(0), s[0]

#----------------------------------------------------------------#

# class Stack:
#     def __init__(self):
#         self.values = []
#
#     def push(self, value):
#         self.values.append(value)
#
#     def pop(self):
#         return self.values.pop()
#
#     def peek(self):
#         return self.values[-1]
#
#     def count(self):
#         return len(self.values)
#
# s = Stack()
#
# for i in range(5, 10):
#     s.push(i)
#
# print(s.pop())
# print(s.peek())
# print(s.count())

#----------------------------------------------------------------#

# 1
# mystring = input()
#
# s = []
# for i in mystring:
#     s.append(i)
#
# reversed_string = ''
#
# while s:
#     reversed_string += s.pop()
#
# print(reversed_string)

# 2
# '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
# expression = input()
# s = []
#
# for i in range(len(expression)):
#     if expression[i] == '(':
#         s.append(i)
#     elif expression[i] == ')':
#         start_index = s.pop()
#         end_index = i + 1
#         print(expression[start_index:end_index])

# raznovidnosti na 2:
# is expression valid - stack should be empty at the end
# when '(' + 1, when ')' -1 and if t the end is 0 then exp is valid

#----------------------------------------------------------------#
# import time
#
# start = time.time()

#QUEUES - FIFO
#----------------------------------------------------------------#

# from collections import deque
# #for queues we have deque
# q = deque()
#
# # enqueue
# q.append(2) #append right
# # ili q.appendleft(3)
#
# # dequeue
# q.popleft()
# # ili q.pop() #pop right
#
# # peek
# print(q[0])
#
# # count

# 3
# from collections import deque
#
# q = deque()
#
# while 1:
#     command = input()
#     if command == 'End':
#         print(f'{len(q)} people remaining.')
#         break
#     elif command == 'Paid':
#         while q:
#             print(q.popleft())
#     else:
#         q.append(command)

# 4
# from collections import deque
#
# people = deque()
# water_quantity = int(input())
#
# while 1:
#     command = input()
#     if command == 'Start':
#         break
#     else:
#         people.append(command)
#
# while 1:
#     command = input()
#     if command == 'End':
#         break
#
#     elif 'refill' in command:
#         explode = command.split(' ')
#         water_quantity += int(explode[1])
#
#     else:
#         needed_liters = int(command)
#         if needed_liters <= water_quantity:
#             print(f'{people.popleft()} got water')
#             water_quantity -= needed_liters
#         else:
#             print(f'{people.popleft()} must wait')
#
# print(f'{water_quantity} liters left')

#----------------------------------------------------------------#

#command.startswith('fff') # proverqva dali zapochva s tova
#command.endswith

#----------------------------------------------------------------#

# 5
# import collections
#
# kids = collections.deque()
#
# list_of_people = input().split(' ')
# tosses_count = int(input())
#
# for i in list_of_people:
#     kids.append(i)
#
# current_count = 0
# while len(kids) > 1:
#     current_count += 1
#     kid = kids.popleft()
#     if current_count < tosses_count:
#         kids.append(kid)
#     else:
#         print(f'Removed {kid}')
#         current_count = 0
#
# print(f"Last is {kids[0]}")

#----------------------------------------------------------------#

#import collections

#d = collections.deque([1, 2, 3, 4, 5, 6, 7, 8])
#d.rotate(4) # vyrti pyrvite 4 elementa
#print(d)
# deque([5, 6, 7, 8, 1, 2, 3, 4])

