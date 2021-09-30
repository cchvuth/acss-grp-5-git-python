import random

def printCollatzSequence():
  num = int(input("Enter the starting number: "))
  print("")
  print(num)

  while num != 1:
    num = int((num / 2) if (num % 2 == 0) else ((3 * num) + 1))
    print(num)