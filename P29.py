row = int(input("Enter no of rows => "))
for i in range(row, 0, -1):
    print(" " * (row - i), end="")
    for j in range(i):
        print(i, end=" ")

    print()