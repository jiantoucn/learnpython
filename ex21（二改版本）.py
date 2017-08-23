# -*- coding: utf-8 -*-
#add chinese support
from sys import argv#调用argv

script,input_file=argv#python 脚本名 输出文件名

def print_all(f):#新增函数
    print f.read()#打印 读取出来的文件里面的奇怪东西
    #话说你是谁！QWQ

def rewind(f):#新增函数 （f）过会找下什么意思哈
    f.seek(0)#不知道 过会处理～

def print_a_line(line_count,f):
    print line_count,f.readline()#打印这个函数里 line_conunt和定义的这个f的值

current_file=open(input_file)

print "first let's print the whole file:\n"#单纯打印+一个换行

print_all(current_file)#打印所有符合标准的files

print "now let's rewind,kind of like a tape."#打印这段话而已

rewind(current_file)#rewind命令再说 反正现在不会QWQ

print "let's print three lines:"#更多打印

current_line=1#赋值
print_a_line(current_line,current_file)#打印？？？

current_line=current_line+1#不知道 
print_a_line(current_line,current_file)#不知道

current_line=current_line+1#不知道
print_a_line(current_line,current_file)#不知道
