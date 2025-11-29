n=int(input("Enter no of rows=> "))
def pyramid(n):
    for i in range(n, 0, -1):
        row = ""
        for j in range(n, n - i, -1):
            row += str(2*j - 1)
        print(row)
pyramid(n)