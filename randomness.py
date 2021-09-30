import random

def throwVirtualDice():
  num = int(input("Enter a number of dice to throw: "))

  print("")
  dices = []
  for i in range(1, num + 1):
    die = random.randint(1, 6)
    dices.append(die)
    print("Die", str(i) + ":", die)
  print("")
  print("Average: ", sum(dices) / len(dices))