no=int(input("Enter no of rows => "))
for i in range(no, 0, -1):
    digit = 2*i - 1
    print(str(digit) * i)