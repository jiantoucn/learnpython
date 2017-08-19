#this one is like your scrips with argv
def print_two(*args):
    arg1, arg2=args
    print "arg1:%r,arg2:%r"%(arg1,arg2)
#大概是用def创建一个函数 后面是名字 *args是一个可容纳XX的什么什么奇怪的东西（*args可以当作可容纳多个变量组成的list 来自百度）
#ok,that *args is actually pointless,we can juse do this
def print_two_again(arg1,arg2):
    print "arg1:%r,arg2:%r"%(arg1,arg2)

#this just takes one argument
def print_one(arg1):
    print"arg1:%r"% arg1

#this one takes no arguments
def print_none():
    print "i got nothin',"


print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first!")
print_none()



