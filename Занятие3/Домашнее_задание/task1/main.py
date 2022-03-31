"""def input_numbers():
    input_number = int(input("ввод числа ")) # TODO выберите нужный цикл, чтобы получать числа с клавиатуры
    list_number =[]
    while input_number >= 0:
        if 3 <= input_number <= 13:
            list_number.append(input_number)

    return list_number



if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)
"""


def input_numbers():

    list_number = []
    while True:
        input_number = int(input("ввод числа "))  # TODO выберите нужный цикл, чтобы получать числа с клавиатуры

        if input_number < 0:
            break
        if 3 <= input_number <= 13:
            list_number.append(input_number)

    return list_number


if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)
