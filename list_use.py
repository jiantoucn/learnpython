chenxiao = ['chen','xiao']#使用[]表示的是他是一个列表
print (chenxiao)#但是打印出来的时候会是包含括号的一些文字
#如果我们需要去只打印一个或者是选择性打印 我们在这边需要会使用到一个叫做"访问列表元素"的东西 下面是例子
print (chenxiao[0])
#即在定义后加上中括号并且选择上你需要用的顺序的数字 即可 但千万记住这边我刚才出的问题在于我全部用成了小括号！ 并且从0开始数 并不是1开头
print (chenxiao[1].title())
print (chenxiao[-1].title() + " love yuxuan forever!")#使用负数的意思是选择倒数第X个数 在这边1就是1 2就是2
#print (chenxiao[-5]) 这一条因为超出了四个 所以会报错！
#接下来测试用
names = ['yuxuan','xiaoran','yiyan']
message = "I Love " + names[0] + " But I Am Really bad,so I Love " + names[1] + " And "  + names[2] + " Too."
print (message.title())
#十分心痛T T
names[2] = 'jingjing'#更换names列表中第三个元素
#print ("but i think " + names[2] + " is very good ".title())
message = "but i think " + names[2] + " is very good "
print (message.title())
#我永远喜欢萱萱 其他的都可以没有。。。
#接下来是在列表末尾/在列表中间增加元素
names.append("yiyan")#在尾部增加yiyan 语法为 列表名.append("要在末尾添加的元素")
print (names)#通过打印可以对比出和之前有什么区别
names.insert(1,"yuxin")#重要 在这边单双引号无所谓！几乎可以的都这么认为 特殊情况暂时不考虑 这一条是指加入yuxin这个元素作为第二位 其他的往后类推    语法为列表名.insert(顺序号,"要添加的元素")
print (names)#打印出即可看出不同
del names[1]#删除列表中的某一个元素 语法是del 列表名[元素序号]
print (names)#打印出即可看出不同