def calculate(a,b,c,func):
	result=func(a,b,c)
	print(result)
func=input("输入一个3个参数的匿名函数来运算3个值：")
func=eval(func)
calculate(2,3,4,func)
