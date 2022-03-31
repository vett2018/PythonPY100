# TODO
A = int(input('Введите число "А" = '))
B = int(input('Введите число "B" = '))
C = int(input('Введите число "C" = '))

result1 = A < 45 and B >= 45 and C >= 45
result2 = A >= 45 and B < 45 and C >= 45
result3 = A >= 45 and B >= 45 and C < 45

if result1 == 1 or result2 == 1 or result3 == 1:
    print("Одно из чисел меньше 45")
else:
    print("Все числа больше или меньше 45")