num = 1
for i in range(1,4):
	for j in range(1,i+1):
		if num% 2 == 0:
			print("0",end="")
			num = num+1
		else:
			print("1",end="")
			num=num+1
	print()