from sys import argv#允许使用argv这个奇怪的东西
script,user_name=argv#从运行的那鬼东西后面两个 一个名字 一个XXXXXXXXXXXXX
prompt='>'#变量？有待考证的一点

print "hi %s,i'm the %s script." %(user_name,script)
print "i'd like to ask you a few questions."
print "do you like me %s?"%user_name
likes=raw_input(prompt)
print "where do you live %s?" %user_name
lives=raw_input(prompt)
print "what kind of computer do you have?"
computer=raw_input(prompt)#三个变量 prompt是变量 依次
print"""
alright,so you said %r about liking me.
you live in %r.not sure where that is.
and you have a %r computer.nice.
"""%(likes,lives,computer)
