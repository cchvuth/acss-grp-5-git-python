
# Mazes
# by Yuzhi_Chen
def Mazes():
    print(" ")
    print("The width and height should be more than 5 and the height should be an odd number.")
    print("Terminate by enter 0.")
    print(" ")

    w = 1
    while w != 0:
        input_str = input("Enter the width of the maze:")
        w = int(input_str)

        if w == 0:  # terminate
            break

        else:
            input_str = input("Enter the height of the maze:")
            h = int(input_str)

            if (w < 5) or (h < 5) or (h % 2 != 1):  # invalid
                print("Invalid data.")
                print(" ")

            else:
                i = 1
                while i <= h:
                    if (i == 1) or (i == h):  # first and last wall [#####]
                        for j in range(1, w):
                            print(end="#")
                        print("#")
                    elif i == 2:  # entrance [    #]
                        for j in range(1, w):
                            print(end=" ")
                        print("#")
                    elif (i == h - 1) and (i % 4 == 2):  # right exit [#    ]
                        print(end="#")
                        for j in range(2, w):
                            print(end=" ")
                        print(" ")
                    elif (i == h - 1) and (i % 4 == 0):  # left exit [    #]
                        for j in range(1, w):
                            print(end=" ")
                        print("#")
                    elif (i - 2) % 4 == 1:  # right hole [### #]
                        for j in range(1, w - 1):
                            print(end="#")
                        print(end=" ")
                        print("#")
                    elif (i - 2) % 4 == 3:  # left hole [# ###]
                        print(end="#")
                        print(end=" ")
                        for j in range(3, w):
                            print(end="#")
                        print("#")
                    else:  # middle corridor [#   #]
                        print(end="#")
                        for j in range(2, w):
                            print(end=" ")
                        print("#")
                    i = i + 1
                print(" ")

