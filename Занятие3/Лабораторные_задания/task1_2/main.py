# TODO запишите здесь функцию factorial
def factorial(n):
    count = 1
    for i in range(1, n+1):
        count = count * i
    return count



if __name__ == "__main__":
    # TODO распечатать результат выполнения функции factorial от числа 5
    factorial_input = int(input("введите факториал: "))
    print(factorial(factorial_input))
