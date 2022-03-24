a = int(input('Введите число А: '))
b = int(input('Введите число В: '))

kvadrat_sum = (a + b) ** 2
sum_kvadratov = a ** 2 + b ** 2

print ("квадрат суммы  = ", kvadrat_sum)
print ("сумма квадратов  = ", sum_kvadratov)

if kvadrat_sum > sum_kvadratov:
    print("Квадрат суммы больше чем сумма квадратов")
else:
    print("сумма квадратов больше чем квадрат суммы")