def count_even_numbers(list_numbers: list) -> int:
     # TODO найти количество четных чисел в списке list_numbers
    #new_list = [kolvo_element for kolvo_element in list_numbers if kolvo_element % 2 == 0]
    #return len(new_list)
    #return len([kolvo_element for kolvo_element in list_numbers if kolvo_element % 2 == 0])
    sum = 0
    for number in list_numbers:
        if number % 2 == 0:
            sum = sum + 1
    return sum






if __name__ == "__main__":
    print(count_even_numbers(list(range(1, 25))))
