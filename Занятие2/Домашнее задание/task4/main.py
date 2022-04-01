if __name__ == "__main__":
    list_ = [-1, 2, 3]
    max_ = 0
    for i in list_:
        if i > max_:
            max_ = i
    print("максимальный элемент: ", max_, "и его индекс: ", list_.index(max_))
    print("первый элемент массива: ", list_[0])
    max_index = list_.index(max_)
    list_[0], list_[max_index] = list_[max_index], list_[0]
    # list_[0], list_[list_.index(max_)] = list_[list_.index(max_)], list_[0]
    #list_[0] = list_[list_.index(max_)]
    print(list_)
    pass

"""
if __name__ == "__main__":
    list_ = [-1, 2, 3, 10, 5, 6, 7, 0]
    max_ = 0
    for i in range(len(list_)):
        if list_[i] > max_:
            max_ = list_[i]

    print(list_)
    print("максимальный элемент в списке :", max_)
    print("индекс максимального элемента в списке: ", list_.index(max_))

    print(list_)
"""
# test 5657757