#print('напишите цифру, обозначающую день недели')
#weekend = [6,7]
#working_days = [1,2,3,4,5]
#a = int(input())
#if a in weekend:
#    print('да')
#elif a in working_days:
#    print('нет')
#else:
#    print('Нет такого рабочего дня') 


#print("x y z")
#for W in range(2):
 #   for Z in range(2):
  #      for Y in range(2):
   #         for X in range(2):
    #            if not (W and Z or -Y or -X == -W):
     #               print (X, Y, Z)


#print('Введите значение x')
#x = int(input())
#print('Введите значение y')
#y = int(input())
#if x > 0 and y > 0:
#    print('значение находится в 1 четверти')
#elif x < 0 and y > 0:
#    print('значение находится во 2 четверти')
#elif x < 0 and y < 0:
#    print('значение находится в 3 четверти')
#elif x > 0 and y < 0:
#    print('значение находится в 4 четверти')
#else:
#    print('x и y должны быть не равны 0')

#print('Введите значение четверти')
#period = int(input())
#if period == 1:
#    print('x > 0 and y > 0')
#elif period == 2:
#    print('x < 0 and y > 0')
#elif period == 3:
#    print('x < 0 and y < 0')
#elif period == 4:
#    print('x > 0 and y < 0')
#else:
#     print('Такой четверти не существует')

print('Введите координату x первой точки')
x0 = int(input())
print('Введите y первой точки')
y0 = int(input())
print('Введите координату x второй точки')
x1 = int(input())
print('Введите координату y второй точки')
y1 = int(input())
distance = ((x1-x0)**2+(y1-y0)**2)**0.5
print(distance)


