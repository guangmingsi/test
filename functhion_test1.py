def sum_parameter(a,b,c):#3个数求和函数
	#print("%d+%d+%d=%d"%(a,b,c,(a+b+c)))
	sum_paremeter=a+b+c
	return sum_paremeter#返回3个数的和
def avarage_func(d,e,f):#3个数求平均值
	summation=sum_parameter(d,e,f)
	result=summation/3
	print("三个数平均值为：%d"%result)
	return result
par1=int(input("输入第一个数字:"))
par2=int(input("输入第二个数字:"))
par3=int(input("输入第三个数字:"))

avarage_func(par1,par2,par3)#调用求平均数
