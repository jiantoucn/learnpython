from sys import argv
from os.path import exists#用来调用exists这个命令

script,from_file,to_file = argv#从运行命令读出被复制和复制的文件名

print "copying from %s to %s"%(from_file,to_file)

#we could do these two on one line too,how?
input=open(from_file)#读取大小？
indata=input.read()#读取出来的大小？给赋予一个值

print "the input file is %d bytes long"% len(indata)

print "does the output file exist? %r"%exists(to_file)
print "readu,hit return to continue,ctrl-c  to abort."
raw_input()

output = open(to_file,"w")#打开这个东西 并且写入
output.write(indata)#写入的是读取出来的文件

print "alright,all done."

output.close()#输出关闭
input.close()#输入关闭
