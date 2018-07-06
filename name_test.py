name = "chen xiao"#定义name
print (name.lower()) #打印name并且使用全部小写（lower（））
first_name = "xiao"#定义first_name
last_name = "chen"#定义last_name
full_name = first_name + " " + last_name#定义full_name为first_name和空格和last_name
print (full_name.title())#打印full_name并且使用首字母大写的方式
print ("hello " + full_name.title() + " welcome to use our software!")#打印hello和full_name首字母大写+空格和文字
message = "fuck you " + full_name.title() + " you are son of bitch!"#定义message
print (message.lower())#打印message并且使用全部小写
print ("Python")#打印python
print ("\tPython")#打印python并且使用制表符在前面
print ("i \n\tlove \n\t\tyuxuan".title())#打印这一段字并且用层叠效果（\n是制表符 \t是跳转到下一行
xxx = " python "
print (xxx.rstrip())#rstrip指的是去掉尾部的空格
print (xxx.lstrip())#lstrip指的是去掉头部的空格
print (xxx.strip())#strip指的是去掉头尾部的空格
print ('shuaigeshiwo')
print (3 + 1)
print (0.01 + 0.002)
age = 23
message = "happy " + str(age) + " rd birthday!"#只有在变量中调用数字变量的时候需要使用str（变量） 否则单独调用的时候就不需要去使用str
print (message)
print (age)
#import this#python之禅
#7/6 0:35 奋斗的我