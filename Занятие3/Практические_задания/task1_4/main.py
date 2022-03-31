PI = 3.14


def square_circle(r):
    return PI * r ** 2


if __name__ == "__main__":
    input_radius = int(input("Ввести радиус круга: "))
    square = square_circle(input_radius)
    print(square)
