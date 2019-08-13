from sys import argv

integer = 0


def find_prime(num):
    number = num
    range_list = [i for i in range(2, number + 1)]
    multiples = []
    for i in range_list:
        for j in range_list:
            multiples.append(i * j)
    if (number in multiples):
        return False
    else:
        return True


if len(argv) == 2:
    try:
        integer = int(argv[1])
        if (find_prime(integer) == True):
            print(f"{integer} is a prime!")
        else:
            print(f"{integer} is not a prime!")
    except ValueError:
        print("Please input an integer")
else:
    print("Please pass an integer on the command line")
