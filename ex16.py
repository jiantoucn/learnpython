#read code
from sys import argv
script,filename=argv#脚本名 和 要打开文件的名字（不在同一目录需要加目录）
txt=open(filename)#打开这个东西
#print "here's your file %r"%filename
print txt.read()#读取你打开过的这个文件 以txt方式读取
#print "typr the filename again:"
#file_again=raw_input(">")
#txt_again=open (file_again)
#print txt_again.read()
txt=close(filename)#用完记得关！
