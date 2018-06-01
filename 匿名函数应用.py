def calculate(a,b,c,func):
	result=func(a,b,c)
	print(result)
calculate(2,3,4,lambda x,y,z:x*y*z)
