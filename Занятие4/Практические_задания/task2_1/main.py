if __name__ == "__main__":
    num1 = 12345
    print("число", num1)
    print("список", list(str(num1)))

    # Конструкция для разбития числа на цифры
    digits_list = [int(d) for d in str(num1)]
    print("перевод строк в числа", digits_list)

    join_num = "".join([str(d) for d in digits_list])
    print(int(join_num))
