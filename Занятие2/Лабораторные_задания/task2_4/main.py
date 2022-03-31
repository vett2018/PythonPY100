if __name__ == "__main__":
    phrase = "Hello,world"
    initial_offset = 5  # TODO чему равно начальное смещение?
    for offset, char in enumerate(phrase, start=initial_offset): #TODO как использовать начальное смещение в команде enumerate?
        print(" " * offset, char)