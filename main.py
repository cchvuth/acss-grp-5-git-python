from factorial import print_factorials
from links import test_link
from randomness import throwVirtualDice
from mazes import Mazes
from collatz import printCollatzSequence

print("This is the program from group #5 !")

choice = ""

while choice.upper() != "Q":
  print("Please select one of the features below, stop by entering Q.\n")
  print("1. Factorials\n2. Links\n3. Randomness\n4. Mazes\n5. Collatz\n")
  choice = input("Enter choice (stop with Q): ")

  if choice == "1":
    print_factorials()
  elif choice == "2":
    test_link()
  elif choice == "3":
    throwVirtualDice()
  elif choice == "4":
    Mazes()
  elif choice == "5":
    printCollatzSequence()
  else: print("Invalid choice")
  
  print("")
  
print("Thank you for using our program!")
