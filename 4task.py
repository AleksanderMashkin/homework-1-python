# from decimal import Decimal

# print('Введите число')
# a = float(input())
# print('Введите точность')
# b = float(input())

# nunber = Decimal(b)
# nunber = a

# print('Число с заданной точностью: ', nunber)

# print('Введите число')
# N = int(input())
# Num_list = []
# a = 2
# while a <= N:
#    if N % a == 0:
#        Num_list.append(a)
#        N //= a
#        a = 2
#    else:
#        a += 1
#print(Num_list)
from collections import Counter
print('Введите количество чисел в списке')
number = int(input())
Num_list = []

Num_list = [int(input('Введите элемент списка: ')) for i in range(0, number)]


print(Num_list) 
print(Counter(Num_list).keys())
    
    