def recursion(num):
	if num>1:
		return num*recursion(num-1)
	else:
		return num
i=recursion(4)
print(i)
