if __name__ == "__main__":
    list_numbers = list(range(5, 17))
    print("исходный :", list_numbers)
    list_numbers[4] = sum(list_numbers) / len(list_numbers)  # TODO заменить значение 5-го элемента средним арифметическим
    print("полученный список :", list_numbers)
