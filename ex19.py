#this one is like your scrips with argv
def print_two(*args):
    arg1, arg2=args
    print "arg1:%r,arg2:%r"%(arg1,arg2)

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



