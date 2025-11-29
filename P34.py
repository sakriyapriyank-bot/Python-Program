no = int(input("Enter no of rows=> "))
for i in range(1, no + 1):
    print(" " * (i - 1), end="")
    for j in range(no, i - 1, -1):
        print(j, end=" ")
    print()