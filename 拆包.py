def any_argmunt(a,b,*args,**kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)
any_argmunt(1,2,3,4,10,key=10,name=20,lens=10)
A=(1,2,3,4,5)
B={"name":"hong","age":18}
any_argmunt(10,20,*A,**B)
#一个*拆包元组A传给参数args，两个**拆包字典传给kwargs
