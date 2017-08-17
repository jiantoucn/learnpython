# -*- coding: utf-8 -*-
#上一个代码用来增加中文支持
from sys import argv

script,filename=argv

print "we're going to erase %r." %filename
print "if you don't what that,hit ctrl-c(^c)."
print "if you do what that,hit return."

raw_input("ENTER OR CTRL-C(^C)")

print "opening the file..."
target=open(filename,'w')#打开文件 W是write的缩写

print "truncating the file.goodbey!"
target.truncate()#清空文件

print "now i'm going to adk you for three lines."
line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")
#写入三行
print "i'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print "and finally,we close it."

target.close()#必须关闭
