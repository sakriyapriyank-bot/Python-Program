no = int(input("Enter no of rows => "))
for i in range(no, 0, -1):
    print(" " * (no - i), end="")
    print("*" * i)