if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }
    #sum_ = 0
    for fruit in cart:
        print(cart[fruit])  # получаем значение по ключу
        #sum_ = sum_ + cart[fruit]
    print(sum(cart.values()))
    # TODO посчитать через метод values
