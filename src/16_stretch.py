import math
from sys import argv


def find_prime(num):
  int_num = int(num)
  range_list = [i for i in range(2, int_num + 1)]
  print(range_list)
  multiples = []
  for i in range_list:
    for j in range_list:
      multiples.append(i * j)
  print(multiples)
  if (int_num in multiples):
    return False
  else:
    return True


if len(argv) == 2:
  print("that's right!")
  if (find_prime(argv[1]) == True):
    print(f"{argv[1]} is a prime!")
  else:
    print(f"{argv[1]} is not a prime!")
else:
  print("Please pass an integer on the command line")

