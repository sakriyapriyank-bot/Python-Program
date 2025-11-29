no = int(input("Enter no of rows => "))
for i in range(1, no + 1):
    for j in range(i, no + 1):
        print(j, end="")
    print()