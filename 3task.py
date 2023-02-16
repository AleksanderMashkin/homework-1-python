# 1 задача


# from random import randint
# print('Задайте количество чисел в списке')
# count = int(input())
# a = [0] * count
# for i in range(count):
#    a[i] = randint(0,99)

# print(a)
# sum = 0
# for m in range(0, count):
#    if not m % 2:
#        sum += a[m]

#print(sum)   


# 2 задача


# from random import randint
# print('Задайте количество чисел в списке')
# count = int(input())
# a = [0] * count
# count2 = count // 2
# b = [] * count2
# for i in range(count):
#   a[i] = randint(1,9)

# print(a)

# for i in range(0, count-1):
#    if not count % 2:
#        while count-1 > i+1:
#            count = count - 1
#            answer = a[count] * a[i]
#            b.append(answer)
#            i += 1
#    else:
#        while count-1 > i:
#            count = count - 1
#            answer = a[count] * a[i]
#            b.append(answer)
#            i += 1
# print(b)

# 3 задача
#list1 = []
#print('Введите число')
#num = int(input())

#while num:
#    list1.append(num % 2)
#    num //= 2
#print(list1)
#for i in reversed(list1):
#    print(i, end = "")

# 4 задача

import random
print('Введите количество вещественных чисел')
N = int(input())
a = [0] * N
for i in range(N):
    a[i] = round(random.uniform(0.1,10),2)
print(a)
for i in range(N):
    a[i] = round((a[i] % 1),2)
print(a)

max = a[i]
min = a[i]
for i in range(N):
    if a[i] > max:
        max = a[i]
    elif a[i] < min:
        min = a[i]
result = max - min
print('Difference: ', result)
print('Max: ', max)
print('Min: ', min)