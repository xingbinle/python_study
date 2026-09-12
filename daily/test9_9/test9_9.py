from operator import truediv

print("hello luna.")
print("Welcome to Python")

""" 
import keyword
print(keyword.kwlist) #打印全部关键字
"""

#变量与常量
#python 中声明变量不需要显示的写数据类型
a=10#将10这个常量赋值给a这个变量
b=3.34
c='hello yuna'
hp=10000
mp=29000
PI=3.14#将变量名全部使用大写字母来表示，暗示这些变量不应该被修改（习惯）
print(a,b,c,hp,mp)#输出多个值

#数据类型
#整数,不同进制的表示，但是都是用十进制输出
"""
a=123
b=0b100
c=0o13
d=0xaa
print(a,b,c,d) 
"""

#浮点数
e=3.22
f=3.22e3
print(e,f)

#复数
g=4+1j
print(g,type(g))#type(变量名)可以验证字符类型
print(g.real,g.imag)#获取实部和虚部

#字符串("""这里面可以换行""")
h="""hel 
luna
。
"""
print(h)#输出单个

#转义字符(Eg:\" 代表打印一个双引号字符)
str="Luna说\"今天天气不错\""
print(str)

#布尔类型
flg=True
print(flg)

#type()函数  可以用于识别变量的数据类型
print(type(flg))
print(type(str))
print(type(g))
print(type(f))

#换行输出和不换行输出（print(内容, end="结尾添加的东西")）
print("he",end='')
print("llo",end='\n')
print("Luna",end='-_-')
print('')#什么都不操作相当于换行

# 常用的输出写法（格式化输出）(print('XXX占位符%d,%s,%f,仅此三种，XXXX占位符'%(变量1，变量2)))
print("初始血量为%d,魔法值为%d"%(hp,mp),end='\t')
print("当前状态:%s"%flg)

#输出写法插值表达式！！！！常用
print(f"初始血量为{hp},魔法值为{mp}")

'''
#输入  变量=input（‘提示信息’）但是用此方法输入的任何值都会被当作字符串变量接收，除非转换
age=eval(input("请输入你的年龄："))
print(f"接受到的年龄为{age+1}")
print(type(age))
'''

#运算符————算术运算符
num1 = 10
num2 = 3
print(num1/num2)# 这里于c/java有很大区别，这里会输出小数而非整数
print(num1//num2) #整除
print(num1**2)#幂运算 10的2次幂

print("$"*10+"hello")#可以输出多个字符，复制多次字符串
#字符串连接
print("he"+"llo")#字符串的连接，+号两边一定得是字符串

#赋值运算符
a=5
#a+=2#等价于a=a+2
#a//=2
a**=2
print(a)

#关系运算符————结果一定是逻辑值
print(a==5)
print(a!=5)
#print(a>5)
#print(a<5)

#逻辑运算符（not取反，and与 有假则假，or或 有真则真）
print(not(a<5))#25小于5false再取反
t=True
t2=False
print(t and t2)
print(not t)
print(t or t2)
