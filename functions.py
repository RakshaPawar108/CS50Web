def square(x):
    return x * x

def cube(x):
    return x * x * x

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

    print("#############################################")

    for i in range(10):
        print("{} cubed is {}".format(i, cube(i)))


if __name__ == "__main__":
    main()
