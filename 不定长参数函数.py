def any_argmunt(a,b,*args):
	result=a+b
	for i in args:
		result=result+i
	print(result)
any_argmunt(1,2,3,4,10)

