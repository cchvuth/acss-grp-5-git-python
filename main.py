from randomness import throwVirtualDice

print("This is the program from group #5 !")

choice = 0

while choice != "Q":
  print("Please select one of the features below, stop by entering Q.\n")
  print("1. Factorials\n2. Links\n3. Randomness\n4. Mazes\n5. Collatz\n")
  choice = input("Enter choice (stop with Q): ")

  if choice == "1":
    pass
  elif choice == "2":
    pass
  elif choice == "3":
    throwVirtualDice()
  elif choice == "4":
    pass
  elif choice == "5":
    pass
  else: print("Invalid choice")
  
  print("")
  
print("Thank you for using our program!")