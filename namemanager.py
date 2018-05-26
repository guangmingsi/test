print("input the funthional number to do you whant")
names=[]
while 2>1:
	print("(1)add_studentname")
	print("(2)delete_studentname")
	print("(3)modification_studentname")
	print("(4)search_studentname is in")
	print("(another number)exit the pragrame")
	key=int(input("please enter the funthional nubmer "))
	#if key is not int:
		print('you operation is false')
		#break
	if key==1:
		namesinput_plus=input("please enter the student name: ")
		names.append(namesinput_plus)
		print(names)
	elif key==2:
		namesinput_del=input('plese enter the student names you want to delete: ')
		if namesinput_del in names:
			names.remove(namesinput_del)
			print('the student%s is remove'%namesinput_del)
		else:
			print("the student names is already remove")
	elif key==3:
		namesinput_old_name=input("please enter the student names you want to modification: ")
		if namesinput_old_name in names:
			namesinput_new_name=input("plese enter the new name")	
			names[names.index(namesinput_old_name)]=namesinput_new_name
			print('student names:%s is change to %s '%(namesinput_old_name,namesinput_new_name))
		else:
			print("the sutdent is not in the school")
	elif key==4:
		namesinput_search=input('plese enter the student name that check in school: ')
		if namesinput_search in names:
			studentnumber=names.index(namesinput_search)+1000
			print('you search the studnet numbers is:%s'%studentnumber)
		else:
			print('there is not the student information') 
	else:
		break	
		
						
