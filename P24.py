no = int(input("Enter number of rows: "))

for i in range(1, no+1):
    for k in range(i, 0, -1):
        print(2*k - 1, end="")
    print()