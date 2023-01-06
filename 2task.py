#print("Введите число")
#num = float(input())
#total = 0
#while num < 0:
#    num*=10
#while num > 0:
#    total+= num % 10
#    num //= 10
#print(total)

#print("Введите число")
#N = int(input())
#start = 1
#for i in range(N):
#    start*= i + 1
#    print(start)

#print("Введите число")
#N = int(input())
#total = 0
#for i in range(1, N + 1):
#    total += round((1 + 1 / i) ** i, 3)
#    print(total)

print("Введите значение, чтобы задать список (N)")
N = int(input())
print("Введите значение для 1 позиции")
position_1 = int(input())
print("Введите значение для 2 позиции")
position_2 = int(input())
numbers_list = list(range(-N, N + 1))
total = numbers_list[position_1 - 1] * numbers_list[position_2 - 1]
print(total)

