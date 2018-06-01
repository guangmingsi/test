#-*- coding:utf-8 -*-E
business_card=[]#定义一个空的列表来存贮字典
def print_menu():
	print("="*50)
	print("Business Card managemant V1.0")
	print("="*50)
	print("(1)增加一个名片")
	print('(2)删除一个名片')
	print('(3)修改一个名片')
	print('(4)查询名片信息')
	print("其他数字退出系统")
def add_infor():
	new_name=input("输入新的名字：")
	new_qq=input("输入新的qq：")
	new_phone=input("输入新的电话：")
	new_email=input("输入新的邮箱：")
	new_addr=input("输入新的地址：")
	new_infors={}#定义一个空的字典存储信息
	new_infors['names']=new_name
	new_infors['qq']=new_qq
	new_infors['phone']=new_phone
	new_infors['email']=new_email
	new_infors['addr']=new_addr
	global business_card
	business_card.append(new_infors)
	print('名片增加了:%s'%new_infors)
def del_infor():
	global business_card
	delete_infors={}
	delete_name=input("输入你想要删掉的信息的名字：")
	delete_infors['names']=delete_name#定义一个字典存储输入的名字即为字典“names”的value
	for comp in business_card:#遍历一个列表元素实际是一个元组
		if comp.get('names')==delete_infors.get('names'):#get元组nams标签的值，然后比较 相等就删除
			key_confirm=int(input("是否要删除%s信息\n删除请按1\返回请按其他数字:"%comp))
			if key_confirm==1:#确认是否修改
				business_card.remove(comp)
				print("删除了%s的信息:"%delete_name)
			else:
				print('操作取消')
		else:
			print('没有这个人无法删除')
	if business_card==[]:
		print('存储信息为空，请先添加后在删除：')	
def modify_infor():
	modify_name=input("请输入你要修改谁的信息：")#定义一个变量存储输入信息
	modify_infor={}
	modify_infor['names']=modify_name #定义一个字典存储输入的名字即为“names”的value
	for comp1 in business_card:#遍历数组
		if comp1.get('names')==modify_infor.get('names'):
			print("%s的信息如下："%modify_infor.get('names'))
			print(comp1)
			print("(1)修改姓名 (2)修改qq (3)修改电话(4)修改邮箱(5)修改地址(6)不修改")
			while True:
				inputkey=int(input("输入你要执行的操作 "))
				if inputkey==1:
					after_modify_name=input("输入要修改的姓名 ：")
					comp1['names']=after_modify_name
					print("修改完毕")
					print(comp1)
					print(business_card)				
				elif inputkey==2:
					after_modify_qq=input("输入要修改的qq ：")
					comp1['qq']=after_modify_qq
					print("修改完毕")
				elif inputkey==3:
					after_modify_phone=input("输入要修改的电话 ：")
					comp1['phone']=after_modify_phone
					print("修改完毕")
				elif inputkey==4:
					after_modify_email=input("输入要修改的邮箱 ：")
				
					comp1['email']=after_modify_email
					print("修改完毕")
				elif inputkey==5:
					after_modify_addr=input("输入要修改的地址 ：")
				
					comp1['addr']=after_modify_addr
					print("修改完毕")
				else:
					print('取消修改')
					break
		else:
			print("没有这个人无法修改")
	if business_card==[]:
		print("信息库为空，请先输入在修改")
def search_infor():
	while True:
		print('(1)根据姓名查找(2)根据qq查找(3)根据地址查找(4)根据email查找(5)根据电话查找(6)不操作：')
		search_function=int(input("请输入你要查询信息的关键字："))#定义一个变量存储输入信息
		if business_card==[]:
			print("信息库为空，请先输入在查询")
		if search_function==1:
			search_name=input("输入要查找的姓名：")
			for comp2 in business_card:
				if comp2.get("names")==search_name:
					print("查到此人信息\n%s"%comp2)
				else:
					print("没有查到此人信息")
		elif search_function==2:
			search_qq=input("输入要查找的qq：")
			for comp2 in business_card:
				if comp2.get("qq")==search_qq:
					print("查到此人信息\n%s"%comp2)
				else:
					print("没有查到此人信息")
					
		elif search_function==3:
			search_addr=input("输入要查找的地址：")
			for comp2 in business_card:
				if comp2.get("addr")==search_addr:
					print("查到此人信息\n%s"%comp2)
				else:
					print("没有查到此人信息")
		elif search_function==4:
			search_email=input("输入要查找的邮箱：")
			for comp2 in business_card:
				if comp2.get("email")==search_email:
					print("查到此人信息\n%s"%comp2)
				else:
					print("没有查到此人信息")
		elif search_function==5:
			search_phone=input("输入要查找的电话：")
			for comp2 in business_card:
				if comp2.get("phone")==search_phone:
					print("查到此人信息\n%s"%comp2)
				else:
					print("没有查到此人信息")
		else:
			print('取消操作')
			break
while True:
	print_menu()
	key=int(input("输入你的选择："))
	if key==1:
		add_infor()
		
	elif key==2:
		del_infor()		
	elif key==3:
		modify_infor()
			    
	elif key==4:
		search_infor()
	else:
		break
