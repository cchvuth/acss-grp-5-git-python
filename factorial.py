
# Part 1—Printing factorials
# Wu Jia ying

def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    return fac


def print_factorial():
    enum = input("Enter a number:")
    n = int(enum)
    if n <= 0:
        print("Invalid input")
    else:
        for i in range(1, n+1):
            print("%d! = %d " % (i, factorial(i)))
            i = i + 1

print_factorial()
