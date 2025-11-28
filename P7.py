row= int(input("Enter limit => "))
k=1
for i in range(row,0,-1):
    for j in range(1, i+1):
        print(k, end="")
        k=k+2
    print("")