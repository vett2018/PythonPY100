def task(n: int, m: int) -> list:  # TODO указать аннотацию типов
    list_ = [
        i ** 2
        for i in range(n, m+1)
        if i % 2 == 1
    ]  # TODO с помощью list comprehension отфильтровать знаечения
    return list_


if __name__ == "__main__":
    number_n = 5
    number_m = 37
    print(task(5, 37))
