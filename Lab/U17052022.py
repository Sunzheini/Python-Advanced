

# 1
# numbers = input().split(' ')
#
# while numbers:
#     print(numbers.pop(), end=' ')

# 2
# s = []
# n = int(input())
#
# for _ in range(n):
#     query = input().split(' ')
#     action = query[0]
#
#     if action == '1':
#         s.append(int(query[1]))
#
#     elif action == '2' and s:   #ako steka ne e prazen inache greshka
#         s.pop()
#
#     elif action == '3' and s:
#         print(max(s))
#
#     elif action == '4' and s:
#         print(min(s))
#
# reversed_stack = []
# while s:
#     reversed_stack.append(str(s.pop()))
#
# print(', '.join(reversed_stack))    #ne raboteshe zashtoto vytre sa chisla a ne string!!!

# 3 sam - queue
# import collections
#
# q = collections.deque()
# food_quantity = int(input())
# order_sequence = [int(x) for x in input().split()]
#
# for i in order_sequence:
#     q.append(i)
#
# print(max(q))
#
# failed = False
#
# while q:
#     current_serving = q[0]
#
#     if current_serving <= food_quantity:
#         food_quantity -= current_serving
#         q.popleft()
#     else:
#         failed = True
#         break
#
# if not failed:
#     print("Orders complete")
# else:
#     print("Orders left:", end=' ')
#     for k in q:
#         print(k, end=' ')


# 4
# stack = [int(x) for x in input().split()]
# base_capacity = int(input())
# rack_counter = 1
# capacity_left = base_capacity
#
# while stack:
#     next_clothes = stack[-1]  # peek operaciq
#
#     if next_clothes > capacity_left:
#         rack_counter += 1
#         capacity_left = base_capacity
#
#     else:
#         capacity_left -= next_clothes
#         stack.pop()
#
# print(rack_counter)

# 5 sys queue -
# from collections import deque
#
# q = deque()
# pumps_count = int(input())
#
# for i in range(pumps_count):
#     q.append([int(x) for x in input().split()])     #vkarvame gi na masivcheta
#
# for attempt in range(pumps_count):
#     tank = 0
#     failed = False
#     for petrol, distance in q:      #unpacking
#         tank = tank + petrol - distance
#         if tank < 0:
#             failed = True
#             break
#
#     if failed:
#         q.append(q.popleft())
#     else:
#         print(attempt)
#         break

#----------------------------------------------------------------#

#for, else
#else se izpylnqva sled kraq na for, ako predi tova nqma break

#----------------------------------------------------------------#

# 6 - -1.28
# stack = []
# sequence = input()
# counter = 0
#
# for i in range(len(sequence)):
#     stack.append(sequence[i])
#
#     if stack[counter] == '}' and stack[counter-1] == '{':
#         stack.pop()
#         stack.pop()
#         counter -= 2
#
#     elif stack[counter] == ']' and stack[counter-1] == '[':
#         stack.pop()
#         stack.pop()
#         counter -= 2
#
#     elif stack[counter] == ')' and stack[counter-1] == '(':
#         stack.pop()
#         stack.pop()
#         counter -= 2
#
#     counter += 1
#
# if len(stack) > 0:
#     print('NO')
# else:
#     print('YES')

# 7 sam na 25%
# from collections import deque
#
# command = input().split(';')
# robots = {}
# for i in command:
#     explode = i.split('-')
#     name = explode[0]
#     processing_time = int(explode[1])
#     robots[name] = [processing_time, 'free', 0]
#
# starting_time = input().split(':')
# hh = int(starting_time[0])
# mm = int(starting_time[1])
# ss = int(starting_time[2])
# elapsed_seconds = 0
#
# waiting_list = deque()
#
# while 1:
#
#     if len(waiting_list) > 0:
#         entry = waiting_list.popleft()
#
#     else:
#         entry = input()
#         if entry == 'End':
#             break
#
#     job_started = False
#     current_product = entry
#     elapsed_seconds += 1
#
#     for k in robots.keys():
#         if robots[k][2] <= elapsed_seconds:
#             robots[k][1] = 'free'
#
#     for j in robots.keys():
#         if robots[j][1] == 'free':
#             robots[j][1] = 'occupied'
#             job_started = True
#
#             robots[j][2] = elapsed_seconds + robots[j][0]
#
#             ss_to_print = ss + elapsed_seconds
#             mm_to_print = mm
#             hh_to_print = hh
#             if ss_to_print > 59:
#                 ss_to_print -= 60
#                 mm_to_print += 1
#             if mm_to_print > 59:
#                 mm_to_print -= 60
#                 hh_to_print += 1
#
#             print(f'{j} - {current_product} [{hh_to_print:02d}:{mm_to_print:02d}:{ss_to_print:02d}]')
#
#             #print(f'{j} - {current_product} [{elapsed_seconds}]')
#             break
#
#     if not job_started:
#         waiting_list.append(current_product)

# 8
from collections import deque

duration_green_light = int(input())
duration_free_window = int(input())
car_queue = deque()
cars_counter = 0
crashed = False

while not crashed:
    command = input()
    if command == "END":
        break

    if command == "green":
        green_left = duration_green_light
        while car_queue and green_left > 0:
            current_car = car_queue.popleft()

            if len(current_car) <= green_left + duration_free_window:
                cars_counter += 1
            else:
                print(f"A crash happened!")
                print(f"{current_car} was hit at {current_car[green_left - duration_free_window]}.")
                crashed = True
                break
            green_left -= len(current_car)

    else:
        car_queue.append(command)

if not crashed:
    print(f"Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")








