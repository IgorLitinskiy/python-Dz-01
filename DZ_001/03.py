#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
#четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#x=34; y=-30 -> 4
#x=2; y=4 -> 1
#x=-34; y=-30 -> 3
#x=-4; y=30 -> 2
print('Введите координату X ')
x = int(input())
print('Введите координату Y ')
y = int(input())
n = 4
if x > 0 and y > 0:
        n = 1
elif x < 0 and y > 0:
        n = 2
elif x < 0 and y < 0:
        n = 3
elif x > 0 and y < 0:
        n = 4 
print(f'{n} четверть плоскости')