#####基础知识#####
'''
n="hello wld!";
print(n);

name = " AAAAAAfe lovelace";
print(name.lower());

#2-4
firstname =  "kkk";
lastname = "hhh";
fullname = firstname + " " + lastname;
print(fullname);

n="lan :\n\tpython\n\tc++\n\tjs";
print(n);

#删除空白
n="       python      ";
print(n);
print(n.rstrip());
print(n.lstrip());
print(n.strip());

#2-3
n=" mm ";
print("Hello"+ n + "would you like to learn some Python today?")

#Python使用两个乘号表示乘方运算;
3**2==9;

#函数str()，它让Python将非字符串值表示 为字符串;

#Python之禅 
import this 

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1].title())

Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1
索引-2返回倒数第二个列表元素， 索引-3返回倒数第三个列表元素，以此类推。 

#3-1-2
names = ['jack','peter','mike','poly']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
hello = ["I think "," is a good friend! "]
print(hello)
print(hello[0]+names[1]+hello[-1])

#方法append()添加元素
names =['jack','oniny','cc']
print(names)
names.append('hhuly')
print(names)

#方法insert()插入元素
names =['jack','oniny','cc']
print(names)
names.insert(1,'peter')
print(names)

#del语句删除元素
names =['jack','oniny','cc']
print(names)
del names[0]
print(names)

#方法pop()可删除列表末尾的元素，并让你能够接着使用它
names =['jack','oniny','cc']
print(names)
n = names.pop()
print(names)
print(n)

#还可以使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素的位置即可。
names =['jack','oniny','cc']
print(names)
n = names.pop(1)
print(names)
print(n)

#用方法remove()根据值删除元素
#方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要 使用循环来判断是否删除了所有这样的值。
names =['jack','oniny','cc']
print(names)
names.remove('cc')
print(names)

#3-4-5
invitation=['jock','stenwen','mily','mike','jackson']
print(invitation)
n1=invitation.remove('jock')
invitation.insert(0,'peter')
print(invitation)
invitation.pop(2)
invitation.append('rockr')
print(invitation)

#方法 sort()排序   方法.sort(reverse=True) 逆向排序 ，对列表元素排列顺序的修改是永久性
a=[11,23,1,32,2,4,45]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
names=['berter','perter','abwe']
names.sort()
print(names)
names.sort(reverse=True)
print(names)

#函数 sorted()对列表进行临时排序
a=[11,23,1,32,2,4,45]
n=sorted(a)
print(a)
print(n)

#方法reverse 倒着打印列表  永久性
a=[11,23,1,32,2,4,45]
print(a)
a.reverse()
print(a)
a.sort()
a.reverse()
print(a)

#len() 确定列表的长度
a=[11,23,1,32,2,4,45]
n=len(a)
print(n)

#遍历
a=[22,3,22,2221,345,332,3,2,1,2,2]
a.sort()
for b in a:
    print(b)

#4-1
fruits=['apple','banana','orange','potato']
for fruit in fruits:
    print("I like "+fruit+"!")
print("I really love fruits!")

#函数range() 生成一系列的数字
for a in range(5,11):
    print(a)

#使用函数list()将range()的结果直接转换为列表（数组）
a= list(range(1,11))
print(a)
print(a[3])

#range(a,b,c)  a->begin  b->end  c->add
a= list(range(0,11,2))
print(a)

bb=[]
for a in range(1,11,2):
    b=a**2
    bb.append(b)
print(bb)

#找最大值max()  最小值min()  加和sum()
a=[33,432,453,66,43,44,43,4]
print(max(a))
print(min(a))
print(sum(a))

#4-7 3 的倍数
a=[b for b in range(3,31,3)]
print(a)

#4-9 立方解析
a= [b**3 for b in range(1,11)]
print(a)

#处理列表的部分元素——Python称之为切片
a=[1,2,3,4,5,6,7]
print(a[0:2])
print(a[2:5])
print(a[:3])
print(a[4:])
print(a[-3:])

#遍历切片
a=[1,2,3,4,5,6,7,8,9]
for b in a[2:6]:
    print(b)
c=[cc for cc in a[3:8]]
print(c)

#复制列表  [:]
a=[1,2,3,4,5,6,7,8,9]
b=a[:]
print(b)
#而若 b=a  的话，是让，a，b，有同一个地址，类似于js中的对象不可直接赋值

# 元组  Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
a=(1,2,3,4)
print(a[1])
#a[0]=10   便会报错
b=[1,2,3,4]
print(b)
b[0]=10
print(b)  #no error

#不能修改元组的元素 因此，如果要修改，则要重新定义整个元组
a=(1,2,3)
print(a)
a=(4,5,6)
print(a)

# &&-->and  ||-->or  !-->!
weather = [100,500,223,22,45,50,55,234,108]
a=0;b=0;c=0;d=0
for wh in weather:
    if wh<=50:
        a=a+1
    if wh>50 and wh<=150:
        b=b+1
    if wh>150 and wh<=300:
        c=c+1
    if wh>300:
        d=d+1
print(a,b,c,d)

#要判断特定的值是否已包含在列表中，可使用关键字in
if 56 in weather:
    print("true")
else:
    print("flase")

#确定特定的值未包含在列表中,在这种情况下，可使用关键字not in。
weather = [100,500,223,22,45,50,55,234,108]
if 101 not in weather:
    print(1)
else:
    print(2)

#5-1 条件测试
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#if-elif-else 结构   elif 代码可用多个
a=18
if a>19:
    print(1)
elif a<18:
    print(2)
elif a=19:
    print(22)
else:
    print(3)

#总之，如果你只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，就使用一系列独立的if语句。

#5-4 外星人颜色：
a= input()
if a=='green':
    print("you get 5 points")
else:
    print("you get 1 point")

#5-9 处理没有用户的情形
users = []
users.append('helen')
users.append('akkk')
users.sort()
users.reverse()
if users:
    for user in users:
        print("Welcome! " + user)
else:
    print("we need some users!!")

#5-11 序数
a=['1','2','3','4','5','6','7','8','9']
for b in a:
    if b=='1':
        print(b + "st")
    elif b=='2':
        print(b + "nd")
    else:
        print(b + "th")

#创建字典
person={'name':'nike','age':'33','height':190}
#也可以这样创建
person1 = \
    {
    'name':'jack',
    'age':'18',
    'height':'180'
}
#创建空字典
person2={}
#添加键值对
person2['name']='mike'
print(person2)
#修改键值对
person1['age']='20'
print(person1)
print(person1['age'])
#删除键值对
del person1['height']
print(person1)

#遍历字典

#遍历所有的键(key)—值(value)对   .items()
person={'name':'nike','age':'33','height':190}
for key, value in person.items():
    print(key)
    print(value)
#遍历字典中的所有键    .keys()  ,方法keys()并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键
person={'name':'nike','age':'33','height':190}
for key in person.keys():
    print(key)
#遍历字典中的所有值   .values()
person={'name':'nike','age':'33','height':190}
for value in person.values():
    print(value)
#通过对包含重复元素的列表调用set()，可让Python找出列表中独一无二的元素，并使用这些元素来创建一个集合
person={'name':'nike','age':'33','height':190,'weight':190}
for value in set(person.values()):
    print(value)
#嵌套      有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。
#你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#创建10个人，修改前3人的身高
persons = []
for i in range(10):
    newperson = {'name': 'ps', 'age': '19', 'sex': 'male'}
    persons.append(newperson)
print(persons)
for person in persons[0:3]:
    if person['sex'] == 'male':
        person['sex'] = 'female'
print(persons)

#在字典中存储列表
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +
"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
#在字典中存储列表
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

#在字典中存储字典
users = {
    'mike':{
        'sex':'male',
        'location':'xian',
        'hobby':'football'
    },
    'jily':{
        'sex':'female',
        'location':'baoji',
        'hobby':'pingpang'
    }
}
for name,info in users.items():
    print("\n" + name + "'s information:")
    s = info['sex']
    l = info['location']
    h = info['hobby']
    print('\t' + s + "\t" + l + "\t" + h + '\t')

#基础试题1
for i in range(1,100,2):
    print(i)
#基础试题2
a = '你好￥￥￥我正在学python@#@#现在%%%'
b = a.replace('￥￥￥',' ').replace('@#@#',' ').replace('%%%',' ')
print(b)
#基础试题3
for a in range(1,10,1):
    for b in range(1,a+1,1):
        print("%d*%d=%d\t" % (b , a , a*b) , end="")
    print("")
#基础试题4
def fun1( a ):
    a=a*1
    if a<=100000:
        b = a * 0.1
    elif a>100000 and a<=200000:
        b = 10000 + (a - 100000) * 0.075
    elif a>20000 and a<=400000:
        b = 10000 + 7500 + (a-200000)  * 0.05
    else:
        b = 'niubi'
    return b
a = int(input())
b = fun1(a)
#基础试题5
print(b)
import operator
x = {1:2,3:4,4:3,2:1,0:0}
x=sorted(x.items(),key=operator.itemgetter(1))
print(x)

#使用函数input()时，Python将用户输入解读为字符串  SO,使用int()来获取数值输入

#7-3 10 的整数倍
a = int(input())
if a % 10 == 0:
    print('yes')
else:
    print('no')

#输入0结束
a = int(input())
while a != 0:
    print(a)
    a = int(input())

#break
a = int(input())
while True:
    if a != 0:
        print(a)
        a = int(input())
    else:
        break

#continue
a = 0
while a <11:
    a += 1
    if a % 2 != 0:
        continue
    print(a)

#7-5 电影票
a = input('please enter your age: ')
while True:
    if a != 'quit':
        a = int(a)
        if a < 3:
            b = 'free'
        elif a >=3 and a<=12:
            b = '$10'
        else:
            b = '$15'
        print("you should pay : " + b)
        a = input('please enter your age: ')
    else:
        break

#在列表之间移动元素
a = ['peter','mike','lily']
b = []
while a !=[]:
    c = a.pop()
    print(c)
    b.append(c)
print(b)
for i in b:
    print(i.title())
print(a)

#删除包含特定值的所有列表元素
a = [1,1,2,3,1,55,234,22,55,90,6,2,11,1,1]
while 1 in a:
    a.remove(1)
    a.sort()
print(a)

#使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

#7-8 熟食店
sandwich_orders = ['1','2','3','4']
finished_sandwiches = []
#for a in sandwich_orders:
    #print('I made your ' + a + ' sandwich ! ')
    #finished_sandwiches.append(a)
while sandwich_orders:
    a = sandwich_orders.pop()
    print('I made your ' + a + ' sandwich ! ')
    finished_sandwiches.append(a)
print(sandwich_orders)
print(finished_sandwiches)

#定义函数   关键字def
def favorite_book(title):
    print('One of my favorite books is ' + title)
favorite_book('ddd')
favorite_book('lll')

#关键字实参  如计算a/b
def fun1(a,b):
    print(a / b)
fun1(b = 2 , a = 5)

#默认值编写函数时，可给每个形参指定默认值,
#在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值
def fun2(a = 2 , b = 5):
    print(b / a)
fun2(33,44)
fun2()

#返回字典  函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。
def fun(a , b):
    users = {'a' : a , 'b' : b}
    return users
c = fun(1 , 2)
sorted(c)
print(c)

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=18)
print(musician)

#8-7 专辑
def make_album(name , album , num):
    sum = {'name':name , 'album':album}
    if num != '0':
        sum['num'] = num
    return sum
while True:
    n = input('Please enter a name: ')
    al = input('Please enter an album: ')
    num = input('Please enter the numbers: ')
    if n == '0':
        break
    a = make_album(n , al , num)
    sorted(a)
    print(a)

#向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）。
def fun(names):
    for name in names:
        a = 'niubia ' + name
        print(a)
names = ['rr','tt','uu','ii']
fun(names)

#切片表示法[:]创建列表的副本
ms = ['qq','ww','ee','rr']
def show_magicians(ms):
    for m in ms:
        print(m)
    print(ms)
def make_great(ms):
    add = 'the great '
    for i in range(0,ms.__len__()):
        ms[i] = add + ms[i]
    for m in ms:
        print(m)
    print(ms)
make_great(ms[:])                #  [:]  传递列表的副本
show_magicians(ms)

#传递任意数量的实参  (类似于js中的动态数组)
#such as 形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#注意：其他实参必须在任意实参前传入 如(ss,ww,*www)这是对的，而(*www,dd,ss)这样是错的，会导致后两个参数无法传入

#**a中的两个星号让Python创建一个名为a的空字典，并将收到的所有名称—值对都封装到这个字典中。
def fun1(ss,mm,**a):
    b={}
    b['ss']=ss
    b['mm']=mm
    for key,value in a.items():
        b[key]=value
    return b
a = fun1('ss','mm',ee='rr',rr='rrr',ddd='uuu')
print(a)
#结果为{'ddd': 'uuu', 'rr': 'rrr', 'ss': 'ss', 'ee': 'rr', 'mm': 'mm'}

#将函数存储在模块中  导入整个模块
import jc
jc.make_pizza(16, 'pepperoni')
jc.make_pizza(88,'wdw','dwd','ddd')

#导入模中特定的函数  from module_name import function_name
#such as
from jc import add
print(add(1,3))

#使用as 给函数指定别名  from module_name import function_name as fn
from jc import make_pizza as mp
mp(22,'ffff')
#使用as 给模块指定别名   import module_name as mn
import jc as j
print(j.add(22,2515))

#导入模块中的所有函数  使用星号（*）运算符可让Python导入模块中的所有函数：from module_name import *
from jc import *
make_pizza(99,'okkk')

#eval()
print(eval("1*2*3*4"))
print(eval("'e'"))
s = 9
c = 8
print(eval("s + c"))
print(eval(input("请输入数字: "))**2)

#大小写转化
pp = input()
for p in pp:
    if 'A'<= p <='Z':
        print(chr(ord(p)+32))
    if 'a'<= p <='z':
        print(chr(ord(p)-32))

#进度条
import time
s = 10
for i in range(s+1):
    a,b = '***'* i,'...'*(s-i)
    c = (i/s)*100
    print("{}%\t{}->{}".format(c,a,b))
    time.sleep(0.5)

#计算pi
import math
from random import *
from time import *
i = 1000000000
q = i
h = 0
clock()
while i:
    i = i - 1
    x , y = random(),random()
    d = math.sqrt(x ** 2 + y ** 2)
    if d <= 1:
        h = h + 1
pi = 4 * (h / q)
print(pi)
print(clock())

#类
#创建类   根据约定，在Python中，首字母大写的名称指的是类。
class People():
    def __init__(self,name,age):     #初始化方法 我们将通过实参向Dog()传递名字和年龄；self会自动传递，因此我们不需要传递它。每当我们根据Dog类创建实例时，都只需给最后两个形参（name和age）提供值。
        self.name = name  #以self为前缀的变量都可供类中的所有方法使用
        self.age = age
    def eat(self):    #定义新的方法
        print(self.name.title() + " is eating now!")
    def sleep(self):
        print(self.name.title() + " is sleeping now!")
jc = People('jack','18')
print(jc.name)
print(jc.age)
print(jc.eat())   #方法里本来就有print 所以调用时就没必要再加print否则
jc.sleep()        #Jack is eating now!  None   eat中不仅会打印语句还会打印None
                  #Jack is sleeping now!

#在同一个类中可以创建多个对象
mk = People('mike','22')
ls = People('lucas','10')
print(ls.name,mk.name)
ls.eat()
mk.sleep()

#使用类
class People():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.hobby = 'guitar'   #给属性指定默认值
        self.sex = 'male'
    def eat(self):
        b = self.name.title() + " is eating now!"
        return b
    def sleep(self):
        print(self.name.title() + " is sleeping now!")
    def update_hobby(self,hobby):  #通过方法修改属性的值
        self.hobby = hobby
    def increase_age(self,age1):   #通过方法对属性的值进行递增
        self.age += age1
jc = People('jack',18)
print(jc.eat())
print(jc.hobby)
#直接修改属性的值
jc.hobby = 'piano'
print(jc.hobby)
#通过方法修改属性的值
jc.update_hobby('violin')
print(jc.hobby)
#通过方法对属性的值进行递增
jc.increase_age(5)
print(jc.age)


#继承
#创建子类时，父类必须包含在当前文件中，且位于子类前面。
class Son(People):   #创建子类
    def __init__(self,name,age):
        super().__init__(name,age)   #super()是一个特殊函数，帮助Python将父类和子类关联起来。
        self.sex = 'man'   #重写(修改)父类的方法
    def fav_book(self):    #给子类元素添加新的属性
        c = 'python_book'
        return c
    def sleep(self):     #重写(修改)父类的方法
        print(self.name.title() + " don not like sleeping!")
jcson = Son('jccc','2')
print(jcson.age)
print(jcson.eat())
jcson.sleep()
print(jcson.hobby)   #结果为'guitar'即子类继承父类继承的是原始的数据
print(jcson.fav_book())
print(jcson.hobby)
print(jc.sex)
print(jcson.sex)
jc.sleep()
jcson.sleep()

#将类的一部分作为一个独立的类提取出来。将大型类拆分成多个协同工作的小类。
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        self.a = 111
    def describe_battery(self):     #打印一条描述电瓶容量的消息
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self,battery_size):     #给Battery类中的函数加参数可输入参数来改变输出
        range = battery_size * 2.5
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
class ElectricCar(Car):
    def __init__(self, make, model, year):     #初始化父类的属性
        super().__init__(make, model, year)    # 再初始化电动汽车特有的属性
        self.battery = Battery()               #让self.battery等于一个其他的类，便可以调用这个类中的函数，属性等。
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()         #让self.battery等于一个其他的类，便可以调用这个类中的函数，属性等。
print(my_tesla.battery.a)                   #让self.battery等于一个其他的类，便可以调用这个类中的函数，属性等。
my_tesla.battery.get_range(50)              #给Battery类中的函数加参数可输入参数来改变输出


#导入类
#导入单个类
from myclass import Car
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
#从一个模块中导入多个类
from myclass import Car,ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
#导入整个模块
import myclass
my_beetle = myclass.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = myclass.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range(88)
#导入模块中的所有类  from module_name import *

#补充：模块collections中的OrderedDict类。OrderedDict实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。
favorite_languages = {}
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +language.title() + ".")
print('\n')
from collections import OrderedDict
favorite = OrderedDict()
favorite['jen'] = 'python'
favorite['sarah'] = 'c'
favorite['edward'] = 'ruby'
favorite['phil'] = 'python'
for name, language in favorite.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


#文件和异常

#读取整个文件
with open('E:\PYcharm\PythonLearing\pi_digits.txt') as file_object:  #函数open()接受一个参数：要打开的文件的名称。Python在当前执行的文件所在的目录中查找指定的文件
    contents = file_object.read()
    print(contents)
#也可以
#file_path = 'E:\PYcharm\PythonLearing\pi_digits.txt'
#with open(file_path) as file_object:

#逐行读取   要以每次一行的方式检查文件，可对文件对象使用for循环：
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
        #print(line.rstrip())  消除这些多余的空白行，可在print语句中使用rstrip()

#创建一个包含文件各行内容的列表
#使用关键字with时，open()返回的文件对象只在with代码块内可用   如果要在with代码块外访问文件的内容，可在with代码块内将文件的各行存储在一个列表中
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()   #方法readlines()从文件中读取每一行，并将其存储在一个列表中
for line in lines:
    print(line.rstrip())
print(lines)

#使用文件的内容
with open('mytxt.txt') as file:
    lines = file.readlines()
string = ''
for line in lines:
    string += line.rstrip()
print(string)   #3.1415926535  8979323846  2643383279

#strip()
with open('mytxt.txt') as file:
    lines = file.readlines()
string = ''
for line in lines:
    string += line.strip()  #为删除这些空格，可使用strip()
print(string)   #3.141592653589793238462643383279

#注意：读取文本文件时，Python将其中的所有文本都解读为字符串。如果你读取的是数字，并要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数。

#只显示文件的部分内容
with open('mytxt.txt') as file:
    lines = file.readlines()
string = ''
for line in lines:
    string += line.strip()
print(string[:10] + '...')
print('...' + string[20:])
print('...' + string[10:20] + '...')

#在文件中查找关键字
with open('mytxt.txt') as file:
    lines = file.readlines()
string = ''
for line in lines:
    string += line.strip()  #字
key = input('Please enter the key: ')
if key in string:
    print('yes')
else:
    print('no')

#在文件中查找关键词句
with open('mytxt.txt') as file:
    lines = file.readlines()
string = ''
for line in lines:
    string += line.rstrip() #字词句
key = input('Please enter the key: ')
if key in string:
    print('yes')
else:
    print('no')

#写入文件
with open('mytxt.txt','w') as flie:  #  w  为写入模式
    flie.write('3.1415926\n53589793\n238462643383279')  #像显示到终端的输出一样，还可以使用空格、制表符和空行来设置这些输出的格式。
#注意：Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。
#附加到文件（添加新的文件）
with open('mytxt.txt','a') as flie:  #  a  为添加模式
    flie.write('ddd\n')

#异常
#使用try-except 代码块  处理ZeroDivisionError异常
try:  
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
#如果try代码块中的代码运行起来没有问题，Python将跳过except代码块；如果try代码块中的代码导致了错误，Python将查找这样的except代码块，并运行其中的代码

#else 代码块
a = int(input());b = int(input())
try:
    c = a / b
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(c)

#处理FileNotFoundError 异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

#分析文本
try:
    with open('E:\PYcharm\PythonLearing\loveyouerself.txt') as fe:
        ct = fe.read()
except FileNotFoundError:
    msg = "Sorry, the file " + fe + " does not exist."
    print(msg)
else:  #计算文件大致包含多少个单词
    words = ct.split()  #方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
    word = len(words)
    print(word)

#分析多个文本
def fun(fd):
    try:
        with open(fd) as fe:
            ct = fe.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + fe + " does not exist."
        print(msg)
    else:  # 计算文件大致包含多少个单词
        words = ct.split()  # 方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
        word = len(words)
        print(word)
fun('E:\PYcharm\PythonLearing\loveyouerself.txt')
fun('E:\PYcharm\PythonLearing\mytxt.txt')
#用列表分析多个文本
def fun(fd):
    try:
        with open(fd) as fe:
            ct = fe.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + fd + " does not exist."
        print(msg)
    else:  # 计算文件大致包含多少个单词
        words = ct.split()  # 方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
        word = len(words)
        print(word)
fds = ['E:\PYcharm\PythonLearing\loveyouerself.txt','mytxt.txt','99.txt']
for fd in fds:
    fun(fd)

#异常时不报错
a = int(input());b = int(input())
try:
    c = a / b
except ZeroDivisionError:
    pass   #异常不报错
else:
    print(c)

#存储数据

#一种简单的方式是使用模块json来存储数据
#使用json.dump()和json.load()
import json 
numbers = [1,2,3,4,5,6,7,8,9,0]
fe = 'numbers.json'
with open(fe,'w') as fd:
    json.dump(numbers, fd)   #用json.dump()来存储

#用json.load()读取
import json
with open('numbers.json') as fd:
    a = json.load(fd)   #用json.load()读取
print(a)

#用户记忆程序
import json
fe = 'users.json'
try:
    with open(fe) as fd:
        us = json.load(fd)
except FileNotFoundError:
    us = input("Please enter: ")
    with open(fe,'w') as fd:
        json.dump(us , fd)
        print("We'll remember you when you come back, " + us + "!")
else:
    print("Welcome back, " + us + "!")

#重构  代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。这样的过程被称为重构。重构让代码更清晰、更易于理解、更容易扩展。
import json
def get_stored_username():
#"""如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
#"""提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
def greet_user():
#"""问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
greet_user()


#测试代码
#测试函数
#Python标准库中的模块unittest提供了代码测试工具
#要为函数编写测试用例，可先导入模块unittest以及要测试的函数，再创建一个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试。
import unittest
from jc import cityfun
class CcTest(unittest.TestCase):
    def test_CC(self):
        sum = cityfun('xian','shannxi')
        self.assertEqual(sum, 'Xian,Shannxi')  #断言方法。断言方法用来核实得到的结果是否与期望的结果一致
unittest.main()

#测试类

import unittest
from jc import Employee
class TestEe(unittest.TestCase):
    def test1(self):
        tt1 = Employee('aa','bb')
        tt1.giveraise('2000')
    def test3(self):
        tt3 = Employee('aaa','bbb')
        addd = ['100','200','500']
        for ad in addd:
            tt3.giveraise(ad)
unittest.main()

#各种断言方法
#assertEqual(a, b)      核实a == b
#assertNotEqual(a, b)       核实a != b
#assertTrue(x)      核实x为True
#assertFalse(x)         核实x为False
#assertIn(item, list)       核实item在list中
#assertNotIn(item, list)        核实item不在list中

#方法setUp()
#unittest.TestCase类包含方法setUp()，让我们只需创建这些对象一次，并在每个测试方法中使用它们
#即不用每次创建测试方法时，还要新创建对象
import unittest
from jc import Employee
class TestEe(unittest.TestCase):
    def setUp(self):
        name = 'aa'
        xing = 'bb'
        self.tst = Employee(name,xing)
        self.addd = ['200','500','1000']
    def tst1(self):
        self.assertEqual('5000',self.money)          
unittest.main()

#####项目1 外星人入侵#####

#创建Pygame 窗口以及响应用户输入
import sys
import pygame
from jcku import Settings
from jcku import Ship

def run_game():
    pygame.init()     # 初始化游戏并创建一个屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))   # 初始化游戏并创建一个屏幕对象
    pygame.display.set_caption("Alien Invasion")   # 初始化游戏并创建一个屏幕对象
    ship = Ship(screen)
    bg_color = (255, 255, 255)   #设置背景色
    while True:   # 开始游戏的主循环
        for event in pygame.event.get():   # 监视键盘和鼠标事件
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)    #调用方法screen.fill()，用背景色填充屏幕
        ship.blitme()
        pygame.display.flip()    #让最近绘制的屏幕可见
run_game()
#####未完成#####




#####数据可视化#####

#https://matplotlib.org/
#数据可视化指的是通过可视化表示来探索数据，它与数据挖掘紧密相关，而数据挖掘指的是使用代码来探索数据集的规律和关联。

#绘制简单的折线图
import matplotlib.pyplot as plt
squares = [1,4,9,16,25] #创建了一个列表，在其中存储了前述平方数
plt.plot(squares)   #再将这个列表传递给函数plot()
plt.show()  #。plt.show()打开matplotlib查看器，并显示绘制的图形

#修改标签文字和线条粗细
import  matplotlib.pyplot as plt
s = [1,3,9,27,81]
plt.plot(s,linewidth = 5)   #参数linewidth决定了plot()绘制的线条的粗细
plt.title("Always * 3",fontsize = 25)   #。函数title()给图表指定标题
plt.xlabel("Value / 3",fontsize = 15)   #参数fontsize指定了图表中文字的大小
plt.ylabel("Value",fontsize = 15)   #函数xlabel()和ylabel()让你能够为每条轴设置标题
plt.tick_params(axis='both',labelsize = 15) #函数tick_params()设置刻度的样式  其中指定的实参将影响x轴和y轴上的刻度字号的大小
plt.show()

#校正图形  可以给plot()同时提供输入值和输出值
import matplotlib.pyplot as plt
input = [1,2,3,4,5]
output = [1,4,9,16,25]
plt.plot(input,output,linewidth = 5)    #现在plot()将正确地绘制数据，因为我们同时提供了输入值和输出值，它无需对输出值的生成方式作出假设
plt.title("Squares",fontsize = 25)
plt.ylabel("Output",fontsize = 15)
plt.xlabel("Input",fontsize = 15)
plt.tick_params(axis='both',labelsize = 15)
plt.show()

#使用scatter()绘制散点图并设置其样式
#要绘制单个点，可使用函数scatter()，并向它传递一对x和y坐标，它将在指定位置绘制一个点
import matplotlib.pyplot as plt
plt.scatter(5,5,s=200,c='yellow')    # s 为点的大小  c 为点的颜色
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

#使用scatter()绘制一系列点
import matplotlib.pyplot as plt
xinput = [1,2,3,4,5]
youtput = [3,9,27,81,3**5]
plt.scatter(xinput,youtput,s=200,c='red')   #传入一系列点
plt.plot(xinput,youtput,linewidth = 5)
plt.title("**3 Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("**3 of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

#自动计算数据  让Python循环来替我们完成这种计算
import matplotlib.pyplot as plt
xinput = list(range(1,1001))    #创建了一个包含x值的列表，其中包含数字1~1000
youtput = [x**3 for x in xinput]    #接下来是一个生成y值的列表解析，它遍历x值（for x in x_values），计算其立方值（x**3），并将结果存储到列表youtput
plt.scatter(xinput,youtput,s=40,c='orange') #将输入列表和输出列表传递给scatter()
plt.title("**3 Numbers", fontsize=25)
plt.xlabel("Iutput", fontsize=15)
plt.ylabel("Output", fontsize=15)
plt.tick_params(axis='both', labelsize=15)
plt.axis([0,1000,0,10000000])    #函数axis()指定了每个坐标轴的取值范围  函数axis()要求提供四个值：x和y坐标轴的最小值和最大值
plt.show()

#删除数据点的轮廓  matplotlib允许你给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓，在散点图包含的数据点不多时效果很好。
#但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，可在调用scatter()时传递实参edgecolor='none'
import matplotlib.pyplot as plt
xinput = list(range(1,1001))
youtput = [x**3 for x in xinput]
plt.scatter(xinput,youtput,s=40,c=(0,0.9,0),edgecolors='none')   #调用scatter()时传递实参edgecolor='none'
#RGB颜色模式自定义颜色 其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量
plt.title("**3 Numbers",fontsize = 25)
plt.xlabel("Iutput",fontsize = 15)
plt.ylabel("Output",fontsize = 15)
plt.tick_params(axis='both',labelsize = 15)
plt.axis([0,1100,0,1100000])
plt.show()

#使用颜色映射  颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。在可视化中，颜色映射用于突出数据的规律，例如，你可能用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。
import matplotlib.pyplot as plt
xinput = list(range(1,1001))
youtput = [x**3 for x in xinput]
plt.scatter(xinput,youtput,s=40,c=youtput, cmap=plt.cm.Blues,edgecolors='none')
#将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。这些代码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色
plt.title("**3 Numbers",fontsize = 25)
plt.xlabel("Iutput",fontsize = 15)
plt.ylabel("Output",fontsize = 15)
plt.tick_params(axis='both',labelsize = 15)
plt.show()

#自动保存图表
#要让程序自动将图表保存到文件中，可将对plt.show()的调用替换为对plt.savefig()的调用
#例如：plt.savefig('squares_plot.png', bbox_inches='tight')
#第一个实参指定要以什么样的文件名保存图表 这个文件将存储到.py所在的目录中
#第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，可省略这个实参

#随机漫步
#使用Python来生成随机漫步数据
#创建RandomWalk()类
#这个类需要三个属性，其中一个是存储随机漫步次数的变量，其他两个是列表，分别存储随机漫步经过的每个点的x和y坐标。
import matplotlib.pyplot as plt
from random import choice  #为做出随机决策，我们将所有可能的选择都存储在一个列表中，并在每次做决策时都使用choice()来决定使用哪种选择
class RandomWalk():
    def __init__(self,num_points = 5000):   #将随机漫步包含的默认点数设置为5000
        self.num_points = num_points
#创建了两个用于存储x和y值的列表，并让每次漫步都从点(0, 0)出发。
        self.x = [0]
        self.y = [0]
    def fill_walk(self):
        while len(self.x) < self.num_points:
            x_direction = choice([1,-1])    #右走为1，左走为-1
            x_distance = choice([0,1,2,3,4])    #choice([0, 1, 2, 3, 4])随机地选择一个0~4之间的整数，告诉Python 沿指定的方向走多远
            x_step = x_direction * x_distance   #将移动方向乘以移动距离，以确定沿x和y轴移动的距离  如果x_step为正，将向右移动，为负将向左移动，而为零将垂直移动；
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])    #（通过包含0，我们不仅能够沿x轴移动，还能够沿y轴移动。）
            y_step = y_direction * y_distance   #将移动方向乘以移动距离，以确定沿x和y轴移动的距离  如果y_step为正，就意味着向上移动，为负意味着向下移动，而为零意味着水平移动。
            if x_step == 0 and y_step == 0: #如果x_step和y_step都为零，则意味着原地踏步，我们拒绝这样的情况，接着执行下一次循环
                continue
            next_x = self.x[-1] + x_step    #为获取漫步中下一个点的x值，我们将x_step与x中的最后一个值相加
            next_y = self.y[-1] + y_step    #对于y值也做相同的处理
            self.x.append(next_x)
            self.y.append(next_y)   #获得下一个点的x值和y值后，我们将它们分别附加到列表x和y的末尾。
#绘制随机漫步图
rw = RandomWalk()   #创建了一个RandomWalk实例，并将其存储到rw中
rw.fill_walk()  #调用fill_walk()
plt.scatter(rw.x,rw.y,s=0.1) #将随机漫步包含的x和y值传递给scatter()，并选择了合适的点尺寸
plt.show()

#模拟多次随机漫步
import matplotlib.pyplot as plt
from jcku import RandomWalk
from random import choice
while True:
    rw = RandomWalk()   #创建实例
    rw.fill_walk()  #调用函数模拟获取列表x，y的值
    plt.scatter(rw.x,rw.y,s=1)  #将列表x，y的值放入散点图
    plt.show()
    keep_running = input('y/n: ')
    if keep_running == 'n':
        break

#练习：模拟多次随机漫步
import matplotlib.pyplot as plt
from random import choice
class RW():
    def __init__(self,sum = 10000):
        self.sum = sum
        self.x = [10]
        self.y = [10]
    def walk(self):
        while True:
            xd = choice([-1,1])
            xds = choice([1,2,3,4,0])
            yd = choice([-1,1])
            yds = choice([0,1,2,3,4])
            xs = xd * xds
            ys = yd * yds
            if xs and ys == 0:
                continue
            if len(self.x) >= 10000:
                break
            nx = self.x[-1] + xs
            ny = self.y[-1] + ys
            self.x.append(nx)
            self.y.append(ny)
while True:
    a = input("y/n: ")
    if a == 'n':
        break
    rw = RW()
    rw.walk()
    plt.scatter(rw.x,rw.y,s=1)
    plt.show()

#设置随机漫步图的样式
#给点着色
import matplotlib.pyplot as plt
from random import choice
class RW():
    def __init__(self,sum = 5000):
        self.sum = sum
        self.x = [0]
        self.y = [0]
    def walk(self):
        while len(self.x) < self.sum:
            xd = choice([-1,1])
            yd = choice([-1,1])
            xds = choice([0,1,2,3,4,5])
            yds = choice([0,1,2,3,4,5])
            xs = xd * xds
            ys = yd * yds
            if xs and ys == 0:
                continue
            nx = self.x[-1] + xs
            ny = self.y[-1] + ys
            self.x.append(nx)
            self.y.append(ny)
rw = RW(100000) #增加点数(默认为5000)
rw.walk()
plt.figure(figsize=(10,6))  #调整尺寸以适合屏幕
point_numbers = list(range(rw.sum)) #使用了range()生成了一个数字列表，其中包含的数字个数与漫步包含的点数相同
plt.scatter(rw.x,rw.y,s=5,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none')#将参数c设置为point_numbers，指定使用颜色映射Blues，并传递实参edgecolor=none以删除每个点周围的轮廓。最终的随机漫步图从浅蓝色渐变为深蓝色
plt.scatter(0,0,s=100,c='red')   #重新绘制起点和终点
plt.scatter(rw.x[-1],rw.y[-1],c='red',s=100) #让起点和终点变得更大，并显示为不同的颜色，以突出它们
plt.axes().get_xaxis().set_visible(False)   #隐藏坐标轴
plt.axes().get_yaxis().set_visible(False)   #隐藏坐标轴
plt.show()


#使用Pygal 模拟掷骰子
#Pygal 画廊 http://www.pygal.org/

#模拟掷一个骰子
from random import randint
class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    def roll(self): #方法roll()使用函数randint()来返回一个1和面数之间的随机数
        return randint(1,self.sides)
#掷骰子
d = Die()   #创建实例时，如果没有指定任何实参，面数为默认值
results = []    #创建一个空列表
s = int(input("times: "))
for i in range(s):
    result = d.roll()
    results.append(result)  #掷骰子s次，并将每次的结果都存储在列表results中
print(results)
a = 0 ; b = 0
for i in range(s):
    if results[i] <= 3:
        a += 1
    else:
        b += 1
print(a,b)

#分析结果  计算每个点数出现的次数
from random import randint
class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    def roll(self):
        return randint(1,self.sides)
die = Die()
results = []
for i in range(1000):
    i = die.roll()
    results.append(i)
frequencies = []    #创建空列表frequencies，用于存储每种点数出现的次数
for i in range(1,die.sides+1):
    frequency = results.count(i)    #我们遍历可能的点数，用count()方法计算每种点数在results中出现了多少次
    frequencies.append(frequency)   #将这个值附加到列表frequencies的末尾
print(frequencies)

#将结果可视化
#绘制直方图
from random import randint
class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    def roll(self):
        return randint(1,self.sides)
die = Die()
results = []
for i in range(1000):
    result = die.roll()
    results.append(result)
frequencies = []
for i in range(1,die.sides+1):
    frequency = results.count(i)
    frequencies.append(frequency)
print(frequencies)
import pygal
hist = pygal.Bar()  #为创建条形图，我们创建了一个pygal.Bar()实例，并将其存储在hist中
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6',frequencies)  #使用add()将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值）
hist.render_to_file('die_visual.svg')   #最后，将这个图表渲染为一个SVG文件，这种文件的扩展名必须为.svg。

#同时掷两个骰子
from random import randint
class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    def roll(self):
        return randint(1,self.sides)
die1 = Die()
die2 = Die()
results = []
for i in range(1000):
    result = die1.roll() + die2.roll()  #计算每次的总点数
    results.append(result)
frequencies = []
sum_sides = die1.sides + die2.sides #可能出现的最大点数12为两个骰子的最大可能点数之和，我们将这个值存储在了sum_sides中
for i in range(2,sum_sides+1):  #分析结果时，我们计算2到sum_sides的各种点数出现的次数
    frequency = results.count(i)
    frequencies.append(frequency)
print(frequencies)
import pygal
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = []  #如果列表x_labels比这里所示的长得多，那么编写一个循环来自动生成它将更合适
for i in range(2,sum_sides+1):
    hist.x_labels.append(i)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')

#同时掷两个面数不同的骰子
from random import randint
class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    def roll(self):
        return randint(1,self.sides)
d1 = Die()
d2 = Die(20)
results = []
for i in range(5000000):
    result = d1.roll() + d2.roll()
    results.append(result)
frequencies = []
sum_sides = d1.sides + d2.sides
for i in range(2,sum_sides+1):
    frequency = results.count(i)
    frequencies.append(frequency)
print(frequencies)
import pygal
hist = pygal.Bar()
hist.title = "D6+D20 5000 results"
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.x_labels = []
for i in range(2,sum_sides+1):
    hist.x_labels.append(i)
hist.add('D6+D20',frequencies)
hist.render_to_file('D6+D20.svg')


#分析下载的数据
#分析CSV 文件头          补:csv文件相当于excel表格
import csv
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\sitka_weather_07-2014.csv'#将要使用的文件的名称存储在filename中
with open(filename) as f:   #打开这个文件，并将结果文件对象存储在f中
    reader = csv.reader(f)  #调用csv.reader()，并将前面存储的文件对象作为实参传递给它,从而创建一个与该文件相关联的阅读器（reader）对象将这个阅读器对象存储在reader中
    header_row = next(reader)   #模块csv包含函数next()，调用它并将阅读器对象传递给它时，它将返回文件中的下一行(初始默认为第0行，故第一次调用返回第0行)
    print(header_row)   #返回的值是列表

#打印文件头及其位置(所处列数)
import csv
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index,column_header in enumerate(header_row):   #对列表调用了enumerate()获取每个元素的索引及其值
        print(index,column_header)

#提取并读取数据（读取每一列的数据）
import csv
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    ht = [] #创建一个空列表
    atime = []
    for i in reader:    #让i遍历reader，因为上面header_row = next(reader)已经获取了第0行的数据，故i遍历reader时从第一行开始，每一列存为i列表中的一个元素
        atime.append(i[0])
        ht.append(i[1]) #让空列表ht去储存i中第一列的元素（初始为第0列）
    print(atime)
    print(ht)

#绘制气温图表
import csv
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    hts = []
    for i in reader:
        ht = int(i[1])  #使用int()将这些字符串转换为数字，让matplotlib能够读取它们
        hts.append(ht)
    print(hts)
from matplotlib import pyplot as plt
fig = plt.figure(dpi=128,figsize=(10,6)) #所显示图幅的分辨率及长宽
plt.plot(hts,c='red')   #将最高气温列表传给plot() 来绘制折线图
plt.title("Daily high temperatures,July 2014",fontsize=25)
plt.xlabel('',fontsize=15)
plt.ylabel("Temperature(F)",fontsize=15)
plt.tick_params(axis='both',which='major',labelsize=15)
plt.show()

#模块datetime
from datetime import datetime   #导入了模块datetime中的datetime类
first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')  #调用方法strptime()，并将包含所需日期的字符串作为第一个实参。第二个实参告诉Python如何设置日期的格式
print(first_date)
#补充：模块datetime中设置日期和时间格式的实参
# %A 星期的名称，如Monday
# %B 月份名，如January
# %m 用数字表示的月份（01~12）
# %d 用数字表示月份中的一天（01~31）
# %Y 四位的年份，如2015
# %y 两位的年份，如15
# %H 24小时制的小时数（00~23）
# %I 12小时制的小时数（01~12）
# %p am或pm
# %M 分钟数（00~59）
# %S 秒数（00~61）

#在图表中添加日期
from datetime import datetime
import csv
import matplotlib.pyplot as plt
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    datas =[];hts = []  #创建了两个空列表，用于存储从文件中提取的日期和最高气温
    for i in reader:
        data = datetime.strptime(i[0],"%Y-%m-%d")
        datas.append(data)
        ht = int(i[1])
        hts.append(ht)
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(datas,hts,c='red')
    plt.title("Daily high temperatures,July 2014", fontsize=25)
    plt.xlabel('', fontsize=15)
    fig.autofmt_xdate()     #调用fig.autofmt_xdate()来绘制斜的日期标签，以免它们彼此重叠
    plt.ylabel("Temperature(F)", fontsize=15)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.show()

#     练习
import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    datas = []
    hts = []
    for i in reader:
        data = datetime.strptime(i[0],"%Y-%m-%d")
        ht = int(i[1])
        datas.append(data)
        hts.append(ht)
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(datas,hts,c='orange')
    plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=15)
    fig.autofmt_xdate()  # 调用fig.autofmt_xdate()来绘制斜的日期标签，以免它们彼此重叠
    plt.ylabel("Temperature(F)", fontsize=15)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.show()

#绘制最高最低温对比图
import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,maxs,mins =[],[],[]
    for i in reader:
        d = datetime.strptime(i[0],'%Y-%m-%d')
        dates.append(d)
        max = int(i[1])
        min = int(i[3]) #从每行的第4列（row[3]）提取每天的最低气温，并存储它们
        maxs.append(max)
        mins.append(min)
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,maxs,c='red')
    plt.plot(dates,mins,c='blue')
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=15)
    fig.autofmt_xdate()  # 调用fig.autofmt_xdate()来绘制斜的日期标签，以免它们彼此重叠
    plt.ylabel("Temperature(F)", fontsize=15)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.show()

#给图表区域着色
import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,maxs,mins = [],[],[]
    for i in reader:
        d = datetime.strptime(i[0],"%Y-%m-%d")
        max = int(i[1])
        min = int(i[3])
        dates.append(d)
        maxs.append(max)
        mins.append(min)
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,maxs,c='red',alpha=0.5)  #实参alpha指定颜色的透明度。Alpha值为0表示完全透明，1（默认设置）表示完全不透明
    plt.plot(dates,mins,c='blue',alpha=0.5)
    plt.fill_between(dates,maxs,mins,facecolor='green',alpha=0.9)#向fill_between()传递了一个x值系列：列表dates，还传递了两个y值系列：maxs和mins。实参facecolor指定了填充区域的颜色，
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=15)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=15)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.show()

#错误检查   若某一天的数据缺失，则上面的代码就会报错，则需要错误检查
import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,maxs,mins = [],[],[]
    for i in reader:
        try:        #对于每一行，我们都尝试从中提取日期、最高气温和最低气温
            d = datetime.strptime(i[0], "%Y-%m-%d")
            max = int(i[1])
            min = int(i[3])
        except ValueError:  #只要缺失其中一项数据，Python就会引发ValueError异常，而我们可这样处理：打印一条错误消息，指出缺失数据的日期
            print()
        else:   #打印错误消息后，循环将接着处理下一行。如果获取特定日期的所有数据时没有发生错误，将运行else代码块，并将数据附加到相应列表的末尾
            dates.append(d)
            maxs.append(max)
            mins.append(min)
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,maxs,c='red',alpha=0.5)
    plt.plot(dates,mins,c='blue',alpha=0.5)
    plt.fill_between(dates,maxs,mins,facecolor='green',alpha=0.9)
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=15)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=15)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.show()


#制作世界人口地图：JSON 格式

#提取相关的世界人口数据
import json
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f) #将数据加载到一个列表中
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))  #将字符串转换为数字值
#原始数据的格式常常不统一，因此经常会出现错误。导致上述错误的原因是，Python不能直接将包含小数点的字符串如'1127437398.85751'转换为整数
# 为消除这种错误，我们先将字符串转换为浮点数，再将浮点数转换为整数
#函数float()将字符串转换为小数，而函数int()丢弃小数部分，返回一个整数
        print(country_name + ":" + str(population))  #打印每个国家2010年的人口数量

#获取两个字母的国别码
#制作地图前，还需要解决数据存在的最后一个问题。Pygal中的地图制作工具要求数据为特定的格式：用国别码表示国家，以及用数字表示人口数量
#population_data.json中包含的是三个字母的国别码，但Pygal使用两个字母的国别码。我们需要想办法根据国家名获取两个字母的国别码
#Pygal使用的国别码存储在模块_maps_world.i18n（internationalization的缩写）中。字典COUNTRIES包含的键和值分别为两个字母的国别码和国家名。要查看这些国别码，可从模块_maps_world.i18n中导入这个字典，并打印其键和值
from pygal_maps_world.i18n import COUNTRIES
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
#在上面的for循环中，我们让Python将键按字母顺序排序，然后打印每个国别码及其对应的国家

#创建国别码函数
from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):#get_country_code()接受国家名，并将其存储在形参country_name中
    for code,name in COUNTRIES.items(): #遍历COUNTRIES中的国家名—国别码对
        if name == country_name:    #如果找到指定的国家名
            return code          # 就返回相应的国别码
    return None#没有找到指定的国家名时返回None

#使用国别码函数得到部分（导致显示错误消息的原因有两个。首先，并非所有人口数量对应的都是国家，有些人口数量对应的是地区（阿拉伯世界）和经济类群（所有收入水平）。
#其次，有些统计数据使用了不同的完整国家名（如Yemen, Rep.，而不是Yemen）。）的国别码和人口数据
import json
from jcku import get_country_code
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)   #将国别码存储在code中，如果没有国别码，就在其中存储None
        if code:
            print(code + ": " + str(population))#返回了国别码，就打印国别码和相应国家的人口数量
        else:
            print('ERROR - ' + country_name)#如果没有找到国别码，就显示一条错误消息

#制作世界地图  pygal_maps_world.maps提供了图表类型World，可帮助你制作呈现各国数据的世界地图
import pygal_maps_world.maps
wm = pygal_maps_world.maps.World()
wm.title = 'North,Central,and South America'
wm.add('North America', ['ca', 'mx', 'us'])#方法add()，它接受一个标签和一个列表，其中后者包含我们要突出的国家的国别码
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')#方法render_to_file()创建一个包含该图表的.svg文件

#在世界地图上呈现数字数据
import pygal_maps_world.maps
wm = pygal_maps_world.maps.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
#使用了方法add()，但这次通过第二个实参传递了一个字典而不是列表这个字典将两个字母的Pygal国别码作为键，将人
#口数量作为值。Pygal根据这些数字自动给不同国家着以深浅不一的颜色（人口最少的国家颜色
#最浅，人口最多的国家颜色最深）
wm.render_to_file('na_populations.svg')

#绘制完整的世界人口地图
import json
from jcku import get_country_code
import pygal_maps_world.maps
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
cc_populations = {}#创建了一个空字典，用于以Pygal要求的格式存储国别码和人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:    #如果返回了国别码，就将国别码和人口数量分别作为键和值填充字典cc_populations
            cc_populations[code] = population
wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010',cc_populations)#调用了add()，并向它传递由国别码和人口数量组成的字典
wm.render_to_file('world_population.svg')

#根据人口数量将国家分组  来进行颜色区分
import json
from jcku import get_country_code
import pygal_maps_world.maps
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
cc_pops_1,cc_pops_2,cc_pops_3, = {},{},{}#将国家分组，创建了三个空字典
for cc,pop in cc_populations.items():#遍历cc_populations，检查每个国
    if pop <= 10000000:              #家的人口数量。if-elif-else代码块将每个国别码和人口数量
        cc_pops_1[cc] = pop          #加入到合适的字典（cc_pops_1、cc_pops_2或cc_pops_3）中。
    elif 10000000 < pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))
wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)            #绘制地图时，我们将全部三个分组都添加到Worldmap中
wm.render_to_file('world_population.svg')

#根据人口数量将国家分组  来进行颜色区分
import json
from jcku import get_country_code
import pygal_maps_world.maps
filename = 'E:\PYcharm\PythonLearing\pcc-master\pcc-master\chapter_16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
cc_pops_1,cc_pops_2,cc_pops_3, = {},{},{}
for cc,pop in cc_populations.items():
    if pop <= 10000000:
        cc_pops_1[cc] = pop
    elif 10000000 < pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))
wm = pygal_maps_world.maps.World()
from pygal.style import LightColorizedStyle, RotateStyle #Pygal样式存储在模块style中，我们从这个模块中导入了样式RotateStyle(调色模式),LightColorizedStyle(高亮显示)
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)#Pygal将根据指定的颜色为每组选择颜色。十六进制格式的RGB颜色是一个以井号（#）打头的字符串，后面跟着6个字符，其中前两个字符表示红色分量，接下来的两个表示绿色分量，最后两个表示蓝色分量。每个分量的取值范围为00（没有相应的颜色）~FF（包含最多的相应颜色）
wm = pygal_maps_world.maps.World(style=wm_style)#RotateStyle返回一个样式对象，我们将其存储在wm_style中。为使用这个样式对象，我们在创建Worldmap实例时以关键字实参的方式传递它
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_population.svg')


#使用API

#处理API响应
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'#存储API调用的URL
r = requests.get(url)   #调用get()并将URL传递给它，再将响应对象存储在变量r中
print("Status code:", r.status_code)#响应对象包含一个名为status_code的属性（状态码200表示请求成功）。
response_dict = r.json()#这个API返回JSON格式的信息,使用方法json()将这些信息转换为一个Python字典存储在response_dict中
print(response_dict.keys())

#处理响应字典
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' #GitHub的API返回有关每个仓库的大量信息
r = requests.get(url)
response_dict = r.json()
print("Total repositories: ",response_dict['total_count'])#指出了GitHub总共包含多少个Python仓库
repo_dicts = response_dict['items']
# 与'items'相关联的值是一个列表，其中包含很多字典
# 而每个字典都包含有关一个Python仓库的信息
# 将这个字典列表存储在repo_dicts中
print("Repositories returned: ",len(repo_dicts))#打印repo_dicts的长度，以获悉我们获得了多少个仓库的信息
repo_dict = repo_dicts[0]   #提取了repo_dicts中的第一个字典，并将其存储在repo_dict中
print("\nKeys: ",len(repo_dict))#打印这个字典包含的键数，看看其中有多少信息
for key in sorted((repo_dict.keys())):  #打印这个字典的所有键，看看其中包含哪些信息
    print(key)

# 研究第一个仓库
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()
repo_dicts = response_dict['items']
repo_dict = repo_dicts[0]
print("\nSelected information about first repository:")
print('Name: ',repo_dict['name'])   #打印项目的名称
print('Owner: ',repo_dict['owner']['login'])    #使用键owner来访问表示所有者的字典(repo_dict['owner']是一个字典)，再使用键login来获取所有者的登录名
print('Stars: ',repo_dict['stargazers_count'])#打印项目获得了多少个星的评级
print('Repository:', repo_dict['html_url'])#项目在GitHub仓库的URL
print('Created:', repo_dict['created_at'])#显示项目的创建时间
print('Updated:', repo_dict['updated_at'])#最后一次更新的时间
print('Description:', repo_dict['description'])#打印仓库的描述

# 打印所有仓库
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()
repo_dicts = response_dict['items']
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:#遍历repo_dicts中的所有字典。在这个循环中，我们打印每个项目的名称、所有者、星级、在GitHub上的URL以及描述
    print('Name: ', repo_dict['name'])  # 打印项目的名称
    print('Owner: ', repo_dict['owner']['login'])  # 使用键owner来访问表示所有者的字典(repo_dict['owner']是一个字典)，再使用键login来获取所有者的登录名
    print('Stars: ', repo_dict['stargazers_count'])  # 打印项目获得了多少个星的评级
    print('Repository:', repo_dict['html_url'])  # 项目在GitHub仓库的URL
    print('Created:', repo_dict['created_at'])  # 显示项目的创建时间
    print('Updated:', repo_dict['updated_at'])  # 最后一次更新的时间
    print('Description:', repo_dict['description'])  # 打印仓库的描述

#使用Pygal 可视化仓库
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightStyle as LS
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)   # 执行API调用并存储响应
print("Status code:", r.status_code)
response_dict = r.json()    # 将API响应存储在一个变量中
print("Total repositories:", response_dict['total_count'])
repo_dicts = response_dict['items'] # 研究有关仓库的信息
names,stars = [],[] #创建了两个空列表，用于存储将包含在图表中的信息
for repo_dict in repo_dicts:    #。在循环中，我们将项目的名称和获得的星数附加到这些列表的末尾
    names.append(repo_dict['name']) #将项目的名称放在names中
    stars.append(repo_dict['stargazers_count'])
# 可视化
my_style = LS(base_style=LCS)#设置基本风格
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)#使用Bar()创建一个简单的条形图
#让标签绕x轴旋转45度（x_label_rotation=45）
# 隐藏了图例（show_legend=False）
chart.title = 'Most-Starred Python Projects on GitHub'  #给图表指定了标题
chart.x_labels = names  #将属性x_labels设置为列表names
chart.add('',stars) #由于我们不需要给这个数据系列添加标签，因此在添加数据时，将标签设置成了空字符串
chart.render_to_file('python_repos.svg')

#改进Pygal 图表
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightStyle as LS
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("Status code:", r.status_code)
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
repo_dicts = response_dict['items']
names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
my_style = LS(base_style=LCS)
my_config = pygal.Config()  #创建了一个Pygal类Config的实例，并将其命名为my_config。即将所有的配置属性分多次加入到其中，以免在创建表格设置属性时显得冗长
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 25#设置图表标题字体大小。
my_config.label_font_size = 15#副标签字体大小（在这个图表中，副标签是x轴上的项目名以及y轴上的大部分数字）
my_config.major_label_font_size = 18#主标签字体大小
my_config.truncate_label = 15#使用truncate_label将较长的项目名（x轴）缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名，将显示完整的项目名）
my_config.show_y_guides = False#将show_y_guides设置为False，以隐藏图表中的水平线
my_config.width = 1000  #设置了自定义宽度，让图表更充分地利用浏览器中的可用空间
chart = pygal.Bar(my_config, style=my_style)#在创建Bar实例时，我们将my_config作为第一个实参，从而通过一个实参传递了所有的配置设置
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('',stars)
chart.render_to_file('python_repos.svg')

#进一步优化Pygal 图表  添加自定义工具提示
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightStyle as LS
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("Status code:", r.status_code)
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
repo_dicts = response_dict['items']
names,plot_dicts = [],[]#创建了两个空列表names和plot_dicts。为生成x轴上的标签，我们依然需要列表names
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {                             #对于每个项目，创建字典plot_dict
        'value': repo_dict['stargazers_count'],#用键'value'存储星数
        'label': str(repo_dict['description']),#用键'label'存储项目描述 由于项目描述中可能会出现纯数字，故用str化为字符型
        'xlink': repo_dict['html_url'],#用键'xlink'存储网站的链接
        }
    plot_dicts.append(plot_dict)
my_style = LS(base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 25
my_config.label_font_size = 15
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')





#####网络爬虫#####

#获取WEB代码
import requests
r = requests.get('http://www.santostang.com/')
print(r.text)   #可获取WEB代码

#去除tag标签，只获取文字内容
from bs4 import BeautifulSoup
html_sample = '\
<html>\
<body>\
<h1 id="title">Hellow World!</h1>\
<a href="#" class="link">This is link1</a>\
<a href="###" class="link">This is link2</a>\
</body>\
</html>'
soup = BeautifulSoup(html_sample,'html.parser')
print(soup.text)    #只打印文字内容

#找出含有特定标签的元素    select方法
from bs4 import BeautifulSoup
html_sample = '\
<html>\
<body>\
<h1 id="title">Hellow World!</h1>\
<a href="#" class="link">This is link1</a>\
<a href="###" class="link">This is link2</a>\
</body>\
</html>'
soup = BeautifulSoup(html_sample,'html.parser')
h = soup.select('h1')   #使用 select 找出含有和标签的元素。同理要找出a标签的元素，只需将soup.select()中填入'a'即可
print(h)    #select方法回传的是列表,要获得纯文本，则要先取出h中的元素，即h[0]等，然后再加上.text即可获取纯文本。

from bs4 import BeautifulSoup
html_sample = '\
<html>\
<body>\
<h1 id="title">Hellow World!</h1>\
<a href="#" class="link">This is link1</a>\
<a href="###" class="link">This is link2</a>\
</body>\
</html>'
soup = BeautifulSoup(html_sample,'html.parser')
atag = soup.select('a')
print(atag)
for tag in atag:    #select方法回传的是列表,要获得纯文本，则要先取出h中的元素,然后再加上.text即可获取纯文本
    print(tag)
    print(tag.text)

#取得含有特定CSS属性的元素
from bs4 import BeautifulSoup
html_sample = '\
<html>\
<body>\
<h1 id="htitle">Hellow World!</h1>\
<a href="#" id="atitle" class="link">This is link1</a>\
<a href="###" class="link">This is link2</a>\
</body>\
</html>'
soup = BeautifulSoup(html_sample,'html.parser')
atag = soup.select('#atitle')   #使用selcet找出id为atitle的元素(id前要加#)
print(atag)

from bs4 import BeautifulSoup
html_sample = '\
<html>\
<body>\
<h1 id="htitle">Hellow World!</h1>\
<a href="#" id="atitle" class="link">This is link1</a>\
<a href="###" class="link">This is link2</a>\
</body>\
</html>'
soup = BeautifulSoup(html_sample,'html.parser')
atag = soup.select('.link')     #使用selcet找出class为link的元素(class前要加.)
print(atag)

#取得所有a标签内的链接
from bs4 import BeautifulSoup
html_sample = '\
<html>\
<body>\
<h1 id="htitle">Hellow World!</h1>\
<a href="www.baidu.com" id="atitle" class="link">This is link1</a>\
<a href="www.hao123.com" class="link">This is link2</a>\
</body>\
</html>'
soup = BeautifulSoup(html_sample,'html.parser')
atag = soup.select('a') #使用select找出所有的a标签
for link in atag:
    print(link['href']) #获得a标签中的href链接    

#输入属性名获取属性值   
from bs4 import BeautifulSoup
html_sample = '\
<html>\
<body>\
<h1 id="htitle">Hellow World!</h1>\
<a href="www.baidu.com" id="atitle" class="link">This is link1</a>\
<a href="www.hao123.com" class="link" ss=sedrssssssssssss>This is link2</a>\
</body>\
</html>'
soup = BeautifulSoup(html_sample,'html.parser')#在上面给a标签随便一个属性值
atag = soup.select('a')
print(atag[1]['ss'])    #输入属性名便可以获取属性值

#根据不同的HTML标签取得对应的内容
import requests
from bs4 import BeautifulSoup
url = 'https://news.sina.com.cn/'
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
for i in soup.select('.ct_t_01'):
    print(i.select('h1')[0].text)
    print(i.select('a')[0]['href'])

#练习
import requests
from bs4 import BeautifulSoup
url = 'https://news.sina.com.cn/china/'
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
for i in soup.select('.news-2'):
    for j in range(0, 11):
        print(i.select('li')[j].text)
        print(i.select('a')[j]['href'])

#炸金花
import random
i = 3
while i:
    a = random.randint(1,4)
    b = random.randint(1,13)
    print(str(a) + "," + str(b))
    i -= 1





#####深度学习#####

#1.5.2　生成NumPy 数组  使用np.array()方法
import numpy as np
x = np.array([1.0,2.0,3.0])
print(x)

#1.5.3 NumPy数组的算术运算
import numpy as np
x = np.array([1,2,3])
y = np.array([3,6,9])
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(y / 3)

# #1.5.4　NumPy 的N维数组
# import numpy as np
# # a = np.array([[3,-2,1],[6,-4,2],[9,-6,3]])
# # b = np.array([[2,3,1],[-1,0,2],[-2,1,-3],[1,5,-2]])
# # c = np.dot(a,a)
# # d = np.dot(c,a)
# # print(c)
# # print(d)
# a = np.array([[1,1],[-1,-1]])
# b = np.array([[1,0],[1,2]])
# c = np.dot(a,a)
# print(c)


# Kalman filter example demo in Python
#卡尔曼滤波的一个典型实例是从一组有限的，包含噪声的，通过对物体位置的观察序列（可能有偏差）预测出物体的位置的坐标及速度

import numpy
import pylab

# 这里是假设A=1，H=1的情况

# 参数初始化
n_iter = 50
sz = (n_iter,)  # size of array
x = -0.37727  # truth value (typo in example at top of p. 13 calls this z)真实值
z = numpy.random.normal(x, 0.1, size=sz)  # observations (normal about x, sigma=0.1)观测值

Q = 1e-5  # process variance

# 分配数组空间
xhat = numpy.zeros(sz)  # a posteri estimate of x 滤波估计值
P = numpy.zeros(sz)  # a posteri error estimate滤波估计协方差矩阵
xhatminus = numpy.zeros(sz)  # a priori estimate of x 估计值
Pminus = numpy.zeros(sz)  # a priori error estimate估计协方差矩阵
K = numpy.zeros(sz)  # gain or blending factor卡尔曼增益

R = 0.1 ** 2  # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = 0.0
P[0] = 1.0

for k in range(1, n_iter):
    # 预测
    xhatminus[k] = xhat[k - 1]  # X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0
    Pminus[k] = P[k - 1] + Q  # P(k|k-1) = AP(k-1|k-1)A' + Q(k) ,A=1

    # 更新
    K[k] = Pminus[k] / (Pminus[k] + R)  # Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
    xhat[k] = xhatminus[k] + K[k] * (z[k] - xhatminus[k])  # X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
    P[k] = (1 - K[k]) * Pminus[k]  # P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1

pylab.figure()
pylab.plot(z, 'k+', label='noisy measurements')  # 观测值
pylab.plot(xhat, 'b-', label='a posteri estimate')  # 滤波估计值
pylab.axhline(x, color='g', label='truth value')  # 真实值
pylab.legend()
pylab.xlabel('Iteration')
pylab.ylabel('Voltage')

pylab.figure()
valid_iter = range(1, n_iter)  # Pminus not valid at step 0
pylab.plot(valid_iter, Pminus[valid_iter], label='a priori error estimate')
pylab.xlabel('Iteration')
pylab.ylabel('$(Voltage)^2$')
pylab.setp(pylab.gca(), 'ylim', [0, .01])
pylab.show()



###numpy库基础###
import numpy as np
x1 = np.random.randint(10,size=5)
x2 = np.random.randint(10,size=(5,6))
x3 = np.random.randint(10,size=(3,4,5))
#print(x1,x2,x3)
# print(x3.shape)
# print(x3.ndim)#查看维度
# print(x3.nbytes)#查看占用了多少内存空间
# print(x3[0,2,1])
# print(x3[0][2][1])#index索引

x4 = np.arange(10)#生成一个等差数列
# print(x4)
# #slicing切片
# print(x4[:6])
# print(x4[4:])
# print(x4[4:7])
# print(x4[4:7:2])#间隔（2-1）个再取
# print(x2[:2,:3])
# print(x3[1:,1:,:2])#如何用切片取高维数组

#copy()方法
# x2_1 = x2[:2,:2]
# x2_copy = x2[:2,:2].copy()
# x2[0,0] = 1
# print(x2_1)
# print(x2_copy)

#矩阵的变形
# x2t = x2.reshape(6,5)
# x2tt = x2.reshape(30)
# x2ttt = x2.reshape(2,3,5)
# print(x2)
# print(x2t)
# print(x2tt)
# print(x2ttt)
# x2tt1 = x2tt.reshape(1,30)
# print(x2tt1)
# print(x2tt.shape,x2tt1.shape)

#数组的拼接concatenate（）方法
x = np.array([[1,2,3],[6,5,4]])
y = np.array([[4,5,6],[7,8,9]])
# print(np.concatenate([x,y],axis=1))#二维数组，axis最大为1，1时横着拼，0时纵着拼

#纵拼接vstack（）方法
# print(np.vstack([x,y]))
#横拼接方法hstack()方法
# print(np.hstack([x,y]))

#用numpy实现结构体
# name = ['a','b','c','d']
# age = [12,23,34,45]
# weight = [34,45,56,67]
#
# x = np.zeros(4,dtype=int)#i-->int  f-->float   U-->Unicode   10是长度  4，8是字节数
# data = np.zeros(4,dtype={'names':('name','age','weight'),'formats':('U10','i4','f8')})
# data['name'] = name
# print(data['name'])
# data['age'] = age
# print(data['age'])
# data['weight'] = weight
# print(data['weight'])
# print(data[data['age']<30])#打印年龄小于30的人的全部数据
# print(data[data['age']<30]['name'])#只打印年龄小于30岁的人的名字



###matplotlib库基础###
import matplotlib.pyplot as plt
import numpy as np
#给定x，y得出线性图像
# x = [1,2,3]
# y = [3,6,9]
# plt.plot(x,y)
# plt.show()
#非线性图像
# x = np.linspace(-3,4,10)#从-3—4生成10个点
# y = x**3
# plt.plot(x,y,color = 'red' )
# plt.show()
# x = np.linspace(-5,5,30)
# y = x**2
# plt.xlabel('x axis')#命名x轴
# plt.ylabel('y axis')#命名y轴
# plt.title('y = x**2')#命名图相标题
# plt.plot(x,y)
# plt.show()

#在同一张图中投影多个曲线
# x = np.linspace(-4,4,30)
# y1 = x**2
# y2 = x**3
# y3 = -x**3
# plt.plot(x,y1,label='y=x**2')
# plt.plot(x,y2,label='y=x**3')
# plt.plot(x,y3,label='y=-x**3')
# plt.legend()#给出图列
# plt.show()

#在同一个图中展示多个图
#例
# plt.figure(figsize=(10,8))
# x = np.linspace(-3*np.pi,3*np.pi,100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = y2 + y1
# plt.subplot(3,1,1)
# plt.title('trig function')
# plt.plot(x,y1,'go-')
# plt.ylabel('y = sinx')
# plt.subplot(3,1,2)
# plt.plot(x,y2,'r.-')
# plt.ylabel('y = cosx')
# plt.subplot(3,1,3)
# plt.plot(x,y3,'m*:')
# plt.ylabel('y = sinx + cosx')
# plt.xlabel('x')
# plt.show()
#练
# plt.figure(figsize=(10,10))
# x = np.linspace(-5,5,100)
# y1 = x
# y2 = x**2
# y3 = x**3
# y4 = x**4
# plt.subplot(2,2,1)
# plt.plot(x,y1,'go-')
# plt.subplot(2,2,2)
# plt.plot(x,y2,'r.-')
# plt.subplot(2,2,3)
# plt.plot(x,y3,'m*:')
# plt.subplot(2,2,4)
# plt.plot(x,y4,'k--')
# plt.show()

#用for循环做出2*3个图
# plt.figure(figsize=(10, 10))
# for i in range(1,7):
#     plt.subplot(2,3,i)
#     plt.text(0.5,0.5,str((2,3,i)),
#              fontsize=18 , ha='center')
# plt.show()

#1000个标准正态分布随机数
# from pylab import *
# y = randn(1000)
# plot(y)
# plt.autoscale(tight='x')
# plt.tight_layout()#自动调整视宽
# plt.show()

#errorbar误差图
from sympy import *
# plt.style.use('seaborn-whitegrid')
# x = np.linspace(0,10,50)
# dy = 0.8
# y = np.sin(x) + dy * np.random.randn(50)
# plt.errorbar(x,y,yerr = dy , fmt = 'o' , color = 'blue' , #yerr设置误差大小,fmt设置点的格式,color设置点的颜色
#              ecolor = 'red' , elinewidth = 3 , capsize = 5)#ecolor设置误差棒的颜色，elinewidth设置误差棒的宽，capsiize设置顶线的长度
# plt.show()

#等值线图(绘制z=f(x,y)图像)
# def f(x,y):
#     return np.sin(x)**5 + np.cos(10 + y * x) * np.cos(x)
# x = np.linspace(0,5,50)
# y = np.linspace(0,5,40)
# X , Y = np.meshgrid(x , y)#从坐标向量中返回坐标矩阵,相当于一个y配对50个x，或一个x配对40个y
# Z = f(X , Y)
# plt.contour(X,Y,Z,colors = 'red')#加上等值颜色，但不给区域上色
# plt.contourf(X,Y,Z,20,cmap='RdGy')#加上等值颜色，并给区域上色
# plt.colorbar()#将颜色的图例显示出来
# contours = plt.contour(X, Y, Z, 3, colors='black')
# plt.clabel(contours, inline=True, fontsize=8)
# plt.imshow(Z, extent=[0,5,0,5], origin='lower', cmap='RdGy', alpha=0.9)
# plt.colorbar()
# plt.show()

# plt.style.use('classic')#经典matlab风格
# rng = np.random.RandomState(0)
# x = np.linspace(0,10,500)
# y = np.cumsum(rng.randn(500,6),0)
# plt.plot(x , y)
# plt.legend('ABCDEF', ncol=2 , loc='upper left')
# plt.show()

import seaborn as sns
# sns.set()
# rng = np.random.RandomState(0)
# x = np.linspace(0,10,500)
# y = np.cumsum(rng.randn(500,6),0)
# plt.plot(x , y)
# plt.legend('ABCDEF', ncol=2 , loc='upper left')
# plt.show()


#多元正态分布(多元间有相互的关系，用协方差来表示)
import pandas as pd
# data = np.random.multivariate_normal([0,0],[[5,2],[2,2]],size = 2000)#均值都是[0,0]，[[5,2],[2,2]]xy的协方差矩阵
# data = pd.DataFrame(data , columns = ['x','y'])
# # for col in 'xy':
# #     plt.hist(data[col],normed = True , alpha = 0.5)
# for col  in 'xy':
#     sns.kdeplot(data[col],sahde = True)#也可以用和密度函数来投影
# plt.show()

# iris = sns.load_dataset('iris')#导入外部数据
# iris.head()
# sns.pairplot(iris , hue = 'species',size = 2.5)#用pairplot来绘制出被导入数据的head间的相互特征关系
# plt.show()

#饼状图
# data = [0.2,0.5,0.3,0.05,0.214]
# namelist = ['1','2','3','4','5']
# labels = namelist
# plt.pie(data , labels = labels , shadow = True)
# plt.show()


###基本数据结构###

##  栈  ##
#后进先出 LIFO#
# class Stack():
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def peek(self):
#         return self.items[-1]
#     def size(self):
#         return len(self.items)
# stack = Stack()
# print(stack.isEmpty())
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.peek())
# print(stack.pop())
# print(stack.peek())
# print(stack.items)

###队列###
#先进先出  FIFO
# class Queue():
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def enqueue(self,item):
#         self.items.insert(0,item)
#     def dequeue(self):
#         return self.items.pop()
#     def peek(self):
#         return self.items[-1]
#     def size(self):
#         return len(self.items)
# qq = Queue()
# print(qq.isEmpty())
# qq.enqueue(1)
# qq.enqueue('two')
# print(qq.peek())
# qq.enqueue(33)
# print(qq.size())
# print(qq.isEmpty())
# qq.dequeue()
# print(qq.peek())

###单链表###
# class Node(object):
#     def __init__(self,value):
#         self.value = value
#         self.nextnode = None
# a = Node(1)
# b = Node(3)
# D = Node(2)
# a.nextnode = D
# D.nextnode = b
# print(a.nextnode.nextnode.value)

###双链表###
# class Dnode(object):
#     def __init__(self,value):
#         self.value = value
#         self.nextnode = None
#         self.prevnode = None
# a = Dnode(1)
# b = Dnode(2)
# c = Dnode(3)
# a.nextnode = b
# b.prevnode = a
# b.nextnode = c
# c.prevnode = b
# print(c.prevnode.prevnode.value)

###双端队列###
# class Deque:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def addRear(self,item):#标准入队
#         self.items.insert(0,item)
#     def addFront(self,item):
#         self.items.append(item)
#     def removeRear(self):#标准出队
#         self.items.pop(0)
#     def removeFront(self):
#         self.items.pop()
#     def size(self):
#         return len(self.items)
# d = Deque()
# print(d.isEmpty())
# d.addFront(1)
# d.addFront('two')
# d.addFront(33)
# print(d.size())
# print(d.items)
# d.addRear('4')
# print(d.items)
# d.addFront('0')
# print(d.items)
# d.removeFront()
# print(d.items)
# d.removeRear()
# print(d.items)

###二叉树--list###
# def BinaryTree(r):#创建二叉树
#     return [r,[],[]]
# def insertLeft(root,newBranch):#插入左子树
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1,[newBranch,t,[]])
#     else:
#         root.insert(1,[newBranch,[],[]])
#     return root
# def insertRight(root,newBranch):#插入右子树
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2,[newBranch,[],t])
#     else:
#         root.insert(2,[newBranch,[],[]])
#     return root
# def getRootVal(root):#获取根节点
#     return root[0]
# def setRootVal(root,newVal):#修改根节点
#     root[0] = newVal
# def getLeftChild(root):#获取左子树
#     return root[1]
# def getRightChild(root):#获取右子树
#     return root[2]
# tree = BinaryTree(1)
# print(tree)
# insertLeft(tree,2)
# print(tree)
# insertRight(tree,3)
# print(tree)
# insertLeft(tree[1],4)
# print(tree)
# insertRight(tree,5)
# setRootVal(tree,-1)
# print(tree)

###二叉树--class###
# class BinaryTree(object):
#     def __init__(self,rootObj):
#         self.key = rootObj
#         self.leftChild = None
#         self.rightChild = None
#     def insertLeft(self,newNode):
#         if self.leftChild == None:
#             self.leftChild = BinaryTree(newNode)
#         else:
#             t = BinaryTree(newNode)
#             t.leftChild = self.leftChild
#             self.leftChild = t
#     def insertRight(self,newNode):
#         if self.rightChild == None:
#             self.rightChild = BinaryTree(newNode)
#         else:
#             t = BinaryTree(newNode)
#             t.rightChild = self.rightChild
#             self.rightChild = t
#     def getLeftChild(self):
#         return self.leftChild
#     def getRightChild(self):
#         return self.rightChild
#     def setRootVal(self,value):
#         self.key = value
#     def getRootVal(self):
#         return self.key
# r = BinaryTree('a')
# print(r.getRootVal())
# r.insertRight(11)
# r.insertLeft(22)
# print(r.getLeftChild().getRootVal())
# r.insertLeft(33)
# print(r.getLeftChild().getRootVal())
# print(r.getLeftChild().getLeftChild().getRootVal())

###图###
#G = (V,E)  V--vertex/node ; E--edge(两个节点的连接)
# from collections import OrderedDict
# class Node():
#     def __init__(self,num):
#         self.num = num
#         self.adjacent = OrderedDict()
#
# class Graph:
#     def __init__(self):
#         self.nodes = OrderedDict()
#     def add_node(self,num):
#         self.node  = Node(num)
#         self.nodes[num] = self.node
#         return self.node
#     def add_edge(self,source,dest,weight = 0):#source起始节点 dest末节点
#         if source not in self.nodes:
#             self.add_node(source)
#         if dest not in self.nodes:
#             self.add_node(dest)
#         self.nodes[source].adjacent[self.nodes[dest]] = weight
# g = Graph()
# g.add_edge(0,1,10)
# g.add_edge(1,0,5)
# print(g.nodes)
# print(g.nodes[0].adjacent)
# print(g.nodes[1].adjacent)


###Pandas库基础###
#Series 序列 时间序列 带标号的数组
#dataframe 若干个序列的组合 并且赋予每一个序列一个列名
import pandas as pd
import numpy as np
# s = pd.Series([1,2,np.nan,4,5])
# print(s)
# ss = pd.Series([1,2,np.nan,4,5],['a','b','c','d','e'])#改变行名
# print(ss)
# new_index = pd.date_range('2019-01-01',periods = 5,freq = 'D')#给定一个时间范围
# print(new_index)
# s.index = new_index#把新的索引列名赋给s
# print(s)

#通过Series生成Dataframe
# df1 = {'names' : pd.Series(['John','Mike','Lily'],['1','2','3']),
#        'age' : pd.Series(['18','17','19'],['1','2','3']),
#        'height' : pd.Series(['180','175','168'],['1','2','3'])
#        }#生成一个字典文件
# print(df1)
# df1 = pd.DataFrame(df1)#用dataframe将字典数据转化成表格
# print(df1)
# df1.rename(columns = {'age':'Age','names':'Names'},inplace = True)#修改列名，必须加inplace=True，否则无法显示
# print(df1)
# df1.columns = ['NAMES','AGE','HEIGHT']#一次性修改所有列名
# print(df1)
# df1.index = ['a','b','c']#修改所有行名
# print(df1)

#通过二维数组生成Dataframe
# df2 = pd.DataFrame(np.random.randn(5,4),['1','2','3','4','5'],['a','b','c','d'])#随机生成5行4列的矩阵，先输行名再输列名
# print(df2)

#通过excel导入生成Dataframe（后面再讲）

#数据选择,切片
# df3 = pd.DataFrame({'Company':['Google','Boost','Xiaomi','Twitter'],
#                    'Person':['Sam','Jack','Amy','Carl'],
#                    'Sale':[200,300,150,250]
#                    })
# print(df3)
# print(df3.iloc[2:])#进行一个其切片选择数据
# df3['New Sale'] = 2 * df3['Sale']#在原有的列的基础上创建新的列
# print(df3)
# df3.drop('New Sale' , axis = 1 , inplace = True)#列的删除
# print(df3)
# df3.drop(0 , inplace = True)#默认的axis=0
# print(df3)
#数据的筛选
# df4 = pd.DataFrame(np.random.randn(6,5),['1','2','3','4','5','6'],['a','b','c','d','e'])
# print(df4)
# print(df4[(df4['a']>0) & (df4['d']<0)])
#数据的统计
# df5 = pd.DataFrame({'Company':['Google','Xiaomi','Xiaomi','Twitter','Google','Twitter'],
#                    'Person':['Sam','Jack','Amy','Carl','Alan','Jackson'],
#                    'Sale':[200,300,150,250,500,200]
#                    })
# print(df5.groupby('Company').sum())#同组别求和
# print(df5.groupby('Company').mean())#求平均值






#####机器学习#####


###决策树算法###

# DictVectorizer:数据类型转换
from sklearn.feature_extraction import DictVectorizer

# csv:原始数据放在csv文件中，该package为python自带，不需要安装
import csv

# 引入数据预处理包、决策树包、读写字符串包
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

# 从csv文件中读取数据，并保存到allElectronicsData变量中
allElectronicsData = open(r'E:\BaiduNetdiskDownload\Dtree-master\Dtree-master\AllElectronics.csv', 'r')
# csv的reader方法按行读取数据
reader = csv.reader(allElectronicsData)
# next方法读取到csv文件的第一行数据
headers = next(reader)
# 打印第一行数据
print(headers)

# 建两个list，featureList装特征值，labelList装类别标签
featureList = []
labelList = []

# 遍历csv文件的每一行
for row in reader:
    # 将类别标签加入到labelList中
    labelList.append(row[len(row) - 1])
    # 下面这几步的目的是为了让特征值转化成一种字典的形式，就可以调用sk-learn里面的DictVectorizer，直接将特征的类别值转化成0,1值
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
print(featureList)

# 实例化
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print("dummyX:" + str(dummyX))
print(vec.get_feature_names())

# label的转化，直接用preprocessing的LabelBinarizer方法
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:" + str(dummyY))
print("labelList:" + str(labelList))

# criterion是选择决策树节点的标准，这里是按照“熵”为标准，即ID3算法；默认标准是gini index，即CART算法。
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf:" + str(clf))

# 生成dot文件
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

# 测试代码，取第1个实例数据，将001->100，即age：youth->middle_aged
oneRowX = dummyX[0, :]
print("oneRowX:" + str(oneRowX))
newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print("newRowX:" + str(newRowX))


###KNN算法###
#一个简单的例子
from sklearn import neighbors
from sklearn import datasets
knn = neighbors.KNeighborsClassifier()
iris = datasets.load_iris()
knn.fit(iris.data , iris.target)
predicedlabel = knn.predict([[100,0.1,0.2,50]])
print(predicedlabel)

#底层实现KNN
import math
import numpy as np
from numpy import genfromtxt
def loadData(file):
    data = genfromtxt(file,delimiter=',')
    Y = data[:,-1]
    Y_test_len = len(Y)
    X_test = data[:Y_test_len,:-1]
    Y_test = data[:Y_test_len,-1]
    y_number = len(set(Y_test))
    return X_test , Y_test , y_number
def getDistance(X_test  , Y_test , X_predict):
    distances = []
    x_number = len(X_test[1])
    for j in range(len(Y_test)):
        distance = 0
        distance2 = 0
        for i in range(x_number):
            distance2 += (X_test[j][i] - X_predict[0][i])**2
        distance += math.sqrt(distance2)
        distances.append(distance)
    return distances
def getNearstNeighbor(distances , k=3):
    distances_sort = sorted(distances)
    min_k = []
    index = []
    for i in range(k):
        min_k.append(distances_sort[i])
    for i in range(k):
        index.append(distances.index(min_k[i]))
    return index
def predict(index):
    Y_class =[]
    for i in range(len(index)):
        Y_class.append(Y_test[index[i]])
    return np.argmax(np.bincount(Y_class))
file = "E:\BaiduNetdiskDownload\教程\机器学习\csv\SVM-movies.csv"
X_test , Y_test , y_number = loadData(file)
X_predict = [[1000,500000]]
a = predict(getNearstNeighbor(getDistance(X_test  , Y_test , X_predict)))
print(a)


###SVM支持向量机###
#一个简单的例子
from sklearn import svm
x = [[1,1],[10,0],[2,6],[3,8]]
y = [0,0,1,1]
clf = svm.SVC(kernel='linear')
clf.fit(x,y)
print(clf)
print(clf.support_vectors_)
print(clf.predict([[3,0],[100,121]]))
#另一个简单的例子
from sklearn import svm
from numpy import genfromtxt
datapath = 'E:\BaiduNetdiskDownload\教程\机器学习\csv\SVM-movies.csv'
data = genfromtxt(datapath , delimiter=',')
x = data[:,:-1]
y = data[:,-1]
clf = svm.SVC(kernel='linear')
clf.fit(x,y)
print(clf)
print(clf.support_vectors_)
print(clf.predict([[55,2],[15,80]]))

#利用正态分布随即点做出SVM图像
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
np.random.seed(0)
X = np.r_[np.random.rand(100 , 2) - [2 , 2] , np.random.rand(100 , 2) + [2 , 2]]
Y = [0] * 100 + [1] * 100
clf = svm.SVC(kernel='linear')
clf.fit(X,Y)
w = clf.coef_
w0 = w[0,0]
w1 = w[0,1]
bias = clf.intercept_
a = -w0 / w1
b = -bias[0] / w1
x = np.linspace(-5,5)
y = a * x + b
plt.plot(x,y,'k-')
plt.scatter(X[0:100,0],X[0:100,1],s=4)
plt.scatter(X[101:200,0],X[101:200,1],s=4)
SV = clf.support_vectors_
b0 = SV[0][1] - a * SV[0][0]
b1 = SV[1][1] - a * SV[1][0]
y0 = a * x + b0
y1 = a * x + b1
plt.plot(x,y0,'k--')
plt.plot(x,y1,'k--')
plt.show()


###神经网络###
# 
# import numpy as np
# 
# #定义所需函数及其导数
# def tanh(x):
#     return np.tanh(x)
# def tanh_deriv(x):
#     return 1.0 - tanh(x)*tanh(x)
# def logistic(x):
#     return 1 / (1 + np.exp(-x))
# def logistic_deriv(x):
#     return logistic(x) * (1 - logistic(x))
# #创建神经网络类
# class NeuralNetwork:
#     def __init__(self,layers,activation = 'tanh'):
#         # 定义类中所将要用到的函数及导数
#         if activation == 'logistic':
#             self.activation = logistic
#             self.activation_deriv = logistic_deriv
#         else:
#             self.activation = tanh
#             self.activation_deriv = tanh_deriv
#         #随机初始化权重
#         self.weights = []
#         for i in range(1,len(layers) - 1):
#             self.weights.append(2 * np.random.random((layers[i - 1] + 1 , layers[i] + 1)) - 1)
#             self.weights.append(2 * np.random.random((layers[i] + 1 , layers[i + 1])) - 1)
#     #开始定义训练器
#     def fit(self,X,y,learning_rate = 0.2,epochs = 10000):
#         X = np.atleast_2d(X)#更改X的数据类型，确认X的维度至少为2维
#         temp = np.ones([X.shape[0] , X.shape[1] + 1])#初始化一个全是1的矩阵，若X为2d（行数=X的行，列数=X的列数加1，因为要对bias初始化）
#         temp[: , 0 : -1] = X#把X的值赋给temp
#         X = temp#再将temp赋给X，则此时，X便多了一列
#         y = np.array(y)#更改y的数据类型
#         #开始训练
#         for k in range(epochs):#一共循环epochs次
#             i = np.random.randint(X.shape[0])#随机取一行
#             a = [X[i]]#把行中的值赋给a，即a中目前储存的是输入层的值
#             #正向更新
#             for l in range(len(self.weights)):
#                 a.append(self.activation(np.dot(a[l] , self.weights[l])))
#             error = y[i] - a[-1]
#             deltas = [error * self.activation_deriv(a[-1])]
#             #BP算法反向更新
#             for l in range(len(a) - 2,0,-1):#从最后一层到第0层，每次退1
#                 deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_deriv(a[l]))
#             deltas.reverse()
#             for i in range(len(self.weights)):
#                 layer = np.atleast_2d(a[i])
#                 delta = np.atleast_2d(deltas[i])
#                 self.weights[i] += learning_rate * layer.T.dot(delta)#layer.T.dot(delta)是指将layer转置后再点乘delta
#     #进行预测验证
#     def predict(self,x):
#         x = np.array(x)
#         temp = np.ones(x.shape[0] + 1)
#         temp[0:-1] = x
#         a = temp
#         for l in range(0,len(self.weights)):
#             a = self.activation(np.dot(a,self.weights[l]))
#         return a
#简单的神经网络应用
#异或判断
# nn = NeuralNetwork([2,2,1],'tanh')
# x = np.array([[0,0],[0,1],[1,0],[1,1]])
# y = np.array([0,1,1,0])
# nn.fit(x,y)
# for i in [[0,0],[0,1],[1,0],[1,1]]:
#     ip = nn.predict(i)
#     print(i,ip)
#手写数字识别
# from sklearn.datasets import load_digits
# from sklearn.metrics import confusion_matrix , classification_report
# from sklearn.preprocessing import LabelBinarizer
# from sklearn.model_selection import  train_test_split
# digits = load_digits()
# X = digits.data
# y = digits.target
# X -= X.min()
# X /= X.max()
# nn = NeuralNetwork([64,100,10],'logistic')
# X_train , X_test , y_train , y_test = train_test_split(X , y)
# labels_train = LabelBinarizer().fit_transform(y_train)
# labels_test = LabelBinarizer().fit_transform(y_test)
# nn.fit(X_train , labels_train , epochs = 3000)
# predictions = []
# for i in range(X_test.shape[0]):
#     o = nn.predict(X_test[i])
#     predictions.append(np.argmax(o))
# print(confusion_matrix(y_test , predictions))
# print(classification_report(y_test , predictions))


###简单线性回归###
# import numpy as np
# def fit(x,y):
#     n = len(x)
#     numerator = 0
#     denominator = 0
#     for i in range(0,n):
#         numerator += (x[i] - np.mean(x)) * (y[i] - np.mean(y))
#         denominator += (x[i] - np.mean(x))**2
#         b1 = numerator / float(denominator)
#         b0 = np.mean(y) - b1 * np.mean(x)
#     return b0 , b1
# def predict(x,b0,b1):
#     y = b0 + b1 * x
#     return y
# X = [1,3,2,1,3]
# Y = [14,24,28,17,27]
# b0 , b1 = fit(X , Y)
# print(predict(6,b0,b1))


###多元线性回归###
##无分类型变量
# from numpy import genfromtxt
# import numpy as np
# from sklearn import datasets , linear_model
# dataPath = "E:\BaiduNetdiskDownload\教程\机器学习\csv\mutiply-regression.csv"#导入数据路径
# deliveryData = genfromtxt(dataPath,delimiter=',')#获取数据的文本，转化为numpy array的类型，delimiter是指以什么为分隔符获取数据
# X = deliveryData[:,:-1]#取所有行，取从第一列到倒数1第二列
# Y = deliveryData[:,-1]#取所有行，取最后一列
# regression = linear_model.LinearRegression()#调用线性回归模型
# regression.fit(X,Y)#输入数据，建立模型
# print(regression.coef_)#.coef_获取b1,b2,...,bn
# print(regression.intercept_)#.intercept_获取b0
# xPred = [[102,6]]#因为X为2d所以这里的xPred也必须为2d
# yPred = regression.predict(xPred)
# print(yPred)
##有分类型变量
#将分类型的数据转化为0,1型数据，如分为三类1,2,3；则若为1，则可表示为1 0 0；若为3，则可表示为0 0 1
# from numpy import genfromtxt
# from sklearn import linear_model
# data = "E:\BaiduNetdiskDownload\教程\机器学习\csv\mutiply-regression1.csv"
# datadelivery = genfromtxt(data,delimiter=',')
# X = datadelivery[:,:-1]
# Y = datadelivery[:,-1]
# regression = linear_model.LinearRegression()
# regression.fit(X,Y)
# print(regression.coef_)
# print(regression.intercept_)
# x = [[100,5,0,1,0]]
# print(regression.predict(x))


###非线性回归###
import numpy as np
import random
def gradientDescent(x , y , theta , alphe , m , numIterations):
    xTrans = x.transpose()
    for i in range(0 , numIterations):
        hypothesis = np.dot(x , theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * m)
        print("Iteration: %d | Cost: %f" % (i , cost))
        gradient = np.dot(xTrans , loss) / m
        theta = theta - alphe * gradient
    return theta
def genData(numPoints , bias ,  variance):#numPoints是点的个数，相当于行数；bias给一个偏差，让数据更“乱” variance是方差，类似于给定一个正态分布的范围
    x = np.zeros(shape=(numPoints , 2))
    y = np.zeros(shape=numPoints)#相当于numPoints行，一列
    for i in range(0 , numPoints):
        x[i][0] = 1
        x[i][1] = i
        y[i] = (i + bias) + random.uniform(0 , 1) * variance
    return x , y
x , y = genData(100,25,10)
m , n = np.shape(x)
numIterations = 100000
alphe = 0.0005
theta = np.ones(n)
theta = gradientDescent(x , y , theta , alphe , m , numIterations)
print(theta)



###xgboost算法###
import xgboost
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 载入数据集
dataset = loadtxt('E:\BaiduNetdiskDownload\教程\机器学习\csv\SVM-movies.csv', delimiter=",")
# split data into X and y
X = dataset[:, :-1]
Y = dataset[:, -1]

# 把数据集拆分成训练集和测试集
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# 拟合XGBoost模型
model = XGBClassifier()
model.fit(X_train, y_train)

# 对测试集做预测
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

# 评估预测结果
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
'''
# ##python经典算法的实现##
# #哈希表(未完成)
# class HashTable(object):
#     def __init__(self , size):
#         self.size = size
#         self.slots = [None] * self.size
#         self.data = [None] * self.size
#     def put(self,key,data):
#         hashValue = self.hashfunction(key , len(self.size))
#         if self.slots[hashValue] == None:
#             self.slots[hashValue] = key
#             self.data[hashValue] = data
#         else:
#             if self.slots[hashValue] == key:
#                 self.data[hashValue] = data
#             else:
#                 nextslot = self.rehash(hashValue , len(self.size))
#                 while self.slots[nextslot] != None and self.slots[nextslot] != key:
#                     nextslot = self.rehash(nextslot , len(self.size))
#                 if self.slots[nextslot] == None:
#                     self.slots[nextslot] = key
#                     self.data[nextslot] = data
#                 else:
#                     self.data[nextslot] = data
#     def hashfunction(self , key , size):
#         return key % size
#     def rehash(self , oldhash , size):
#         return (oldhash + 1) % size
#     def get(self , key

































# 图的demo
# from collections import OrderedDict
# class Node():
#     def __init__(self,num):
#         self.num = num
#         self.adjacent = OrderedDict()
# class Graph:
#     def __init__(self):
#         self.nodes = OrderedDict()
#     def add_node(self,num):
#         self.node  = Node(num)
#         self.nodes[num] = self.node
#         return self.node
#     def add_edge(self,source,dest,weight = 0):#source起始节点 dest末节点
#         if source not in self.nodes:
#             self.add_node(source)
#         if dest not in self.nodes:
#             self.add_node(dest)
#         self.nodes[source].adjacent[self.nodes[dest]] = weight
# g = Graph()
# g.add_edge(0,1,10)
# g.add_edge(1,0,5)
# print(g.nodes)
# print(g.nodes[0].adjacent)
# print(g.nodes[1].adjacent)


# from itertools import combinations
# import networkx as nx
# import matplotlib.pyplot as plt
#
# data = [
#     ['dahuo', 'dingxiang', 'haitang', 'blou'],
#     ['haitang', 'alou', 'zuyuan'],
#     ['dingxiang', 'nancao', 'xiaomen']
# ]
#
# data.append(['nancao', 'daka', 'dahuo'])
# del data[2]
# edges = []
# for i in data:
#     combs = combinations(i, 2)
#     edges += list(combs)
# G = nx.Graph()
# G.add_edges_from(edges)
# nx.draw(G, with_labels=True)
# plt.show()


# #网格表示
# import matplotlib.pyplot as plt
# all_nodes = [[1.5,4],[1.5,5],[1.5,10],[3,2],[3,6],[3,9],[4,5]]
# plt.figure()
# for i in all_nodes:
#     plt.scatter(i[0],i[1],color='blue')
# # for x in range(20):
# #     for y in range(20):
# #         all_nodes.append([x,y])
# #         plt.scatter(x,y,color='red')
# def neighbors(node):
#     dirs = [[1,0],[0,1],[-1,0],[0,-1]]
#     result = []
#     for i in dirs:
#         result.append([node[0] + i[0] , node[1] + i[1]])
#         plt.scatter(node[0] + i[0] , node[1] + i[1], color='red')
#     return result
# # newnode = [25,20]
# # print(neighbors(newnode))
# plt.show()


###Networkx库的基本操作###
# import networkx as nx
# import matplotlib.pyplot as plt

# #无向图
# G = nx.Graph()                 #建立一个空的无向图G
# G.add_node(1)                  #添加一个节点1
# G.add_edge(2,3)                #添加一条边2-3（隐含着添加了两个节点2、3）
# G.add_edge(3,2)                #对于无向图，边3-2与边2-3被认为是一条边
# print ("nodes:", G.nodes())      #输出全部的节点： [1, 2, 3]
# print ("edges:", G.edges())      #输出全部的边：[(2, 3)]
# print ("number of edges:", G.number_of_edges())   #输出边的数量：1
# nx.draw(G)
# plt.show()

# #多点无向图
# g = nx.Graph()
# g.add_node(1)
# g.add_node(2)
# g.add_nodes_from([3,4,5,6])#点集，一次添加多个点
# g.add_cycle([1,2,3,4])#成环
# g.add_edge(1,3)
# g.add_edges_from([(3,5),(3,6),(3,7)])#加边集
# nx.draw(g)
# plt.show()

# #有向图
# g = nx.DiGraph()
# g.add_node(1)
# g.add_node(2)
# g.add_nodes_from([3,4,5,6,7])
# g.add_cycle([1,2,3,4])
# g.add_edge(1,3)
# g.add_edges_from([(3,5),(3,7),(4,6)])
# #g = g.to_undirected()#有向图转化成无向图
# nx.draw(g)
# plt.show()

# #加权图
# g = nx.Graph()
# g.add_edge(1,2)#添加一条边2-3（隐含着添加了两个节点2、3）
# g.add_weighted_edges_from([(1,3,5),(2,4,10)])#添加边1，3并赋予5个权重（隐含着添加了点3）
# nx.draw(g)
# print(g.get_edge_data(1,3))#获取边的权重
# plt.show()

# #求无向图的任意两点间的最短路径
# g = nx.Graph()
# g.add_edges_from([(1,2),(1,3),(1,4),(1,5),(4,5),(4,6),(5,6)])
# path = nx.all_pairs_shortest_path(g)
# print(list(path)[1])
# nx.draw(g)
# plt.show()

# #找图中两个点的最短路径
# g = nx.Graph()
# g.add_nodes_from([1,2,3,4,5,6,7,8,9])
# g.add_edges_from([(1,2),(1,5),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(1,3),(1,5),(2,3),(4,5),(5,7),(7,9)])
# try:
#     n = nx.shortest_path(g,1,9)
#     print(n)
# except nx.NetworkXNoPath:
#     print('No Path')
# nx.draw(g)
# plt.show()

# #有向图+最短路径函数
# import networkx as nx
# import pylab
# import numpy as np
# #自定义网络
# row=np.array([0,0,0,1,2,3,6])
# col=np.array([1,2,3,4,5,6,7])
# G=nx.DiGraph()#生成一个空的有向图
# for i in range(0,np.size(col)+1):#为这个网络添加节点
#     G.add_node(i)
# for i in range(np.size(row)):#在网络中添加边
#     G.add_edges_from([(row[i],col[i])])
# G.add_edge(5,7)
# pos=nx.shell_layout(G)#给网路设置布局
# #画出网络图像
# nx.draw(G,pos,with_labels=True, node_color='white', edge_color='red', node_size=400, alpha=0.5 )
# pylab.title('Self_Define Net',fontsize=15)
# #使用最短距离函数
# p=nx.shortest_path(G,source=0,target=7)
# print('源节点为0，终点为7：', p)
# distance=nx.shortest_path_length(G,source=0,target=7)
# print('源节点为0，终点为7,最短距离：', distance)
# pylab.show()
#
# g = nx.Graph()
# g.add_nodes_from('abcd')
# g.add_edges_from([('a','bcd')])
# nx.draw(g)
# plt.show()





# import cv2
#
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#
# smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
# # 调用摄像头摄像头
# cap = cv2.VideoCapture(0)
#
# while (True):
#     # 获取摄像头拍摄到的画面
#     ret, frame = cap.read()
#     faces = face_cascade.detectMultiScale(frame, 1.3, 2)
#     img = frame
#     for (x, y, w, h) in faces:
#         # 画出人脸框，蓝色，画笔宽度微
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (25, 89, 0), 2)
#         # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
#         face_area = img[y:y + h, x:x + w]
#
#         ## 人眼检测
#         # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
#         eyes = eye_cascade.detectMultiScale(face_area, 1.3, 10)
#         for (ex, ey, ew, eh) in eyes:
#             # 画出人眼框，绿色，画笔宽度为1
#             cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)
#
#         ## 微笑检测
#         # 用微笑级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
#         smiles = smile_cascade.detectMultiScale(face_area, scaleFactor=1.16, minNeighbors=65, minSize=(25, 25),
#                                                 flags=cv2.CASCADE_SCALE_IMAGE)
#         for (ex, ey, ew, eh) in smiles:
#             # 画出微笑框，红色（BGR色彩体系），画笔宽度为1
#             cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)
#             cv2.putText(img, 'Smile', (x, y - 7), 3, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
#
#             # 实时展示效果画面
#     cv2.imshow('frame2', img)
#     # 每5毫秒监听一次键盘动作
#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break
#
# # 最后，关闭所有窗口
# cap.release()
# cv2.destroyAllWindows()




#
# import sys
# import random
# from PySide2 import QtCore, QtWidgets, QtGui
#
# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#
#         self.button = QtWidgets.QPushButton("Click me!")
#         self.text = QtWidgets.QLabel("Hello World")
#         self.text.setAlignment(QtCore.Qt.AlignCenter)
#
#         self.layout = QtWidgets.QVBoxLayout()
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)
#         self.setLayout(self.layout)
#
#         self.button.clicked.connect(self.magic)
#
#
#     def magic(self):
#         self.text.setText(random.choice(self.hello))
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#
#     widget = MyWidget()
#     widget.resize(800, 600)
#     widget.show()
#
#     sys.exit(app.exec_())

























# #A star
# import sys
# import numpy as np
# import time
# from pylab import *
# from matplotlib.patches import Rectangle       #用于绘制小矩形
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.cost = 1     #该点的代价
# ##设置点的属性Point(x,y)
#
# class RandomMap():
#     def __init__(self, size):
#         self.size = size
#         self.obstacle = size // 8
#         self.GenerateObstacle()         #自动运行生成障碍的函数
#     def GenerateObstacle(self):
#         self.obstacle_point = []
#         self.obstacle_point.append(Point(self.size//2, self.size//2))
#         self.obstacle_point.append(Point(self.size//2, self.size//2-1))
#         for i in range(self.size // 2 - 4, self.size // 2):
#             self.obstacle_point.append(Point(i, self.size - i))
#             self.obstacle_point.append(Point(i, self.size - i - 1))
#             self.obstacle_point.append(Point(self.size - i, i))
#             self.obstacle_point.append(Point(self.size - i, i - 1))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 8, self.size // 2 - 4 - 1 -1))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 7, self.size // 2 - 4 - 1 - 1))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 6, self.size // 2 - 4 - 1 - 1))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 7, self.size // 2 - 4 - 1 - 2))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 6, self.size // 2 - 4 - 1 - 2))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 6, self.size // 2 - 4 - 1 - 3))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 5, self.size // 2 - 4 - 1 - 2))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 5, self.size // 2 - 4 - 1 - 3))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 4, self.size // 2 - 4 - 1 - 3))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 5, self.size // 2 - 4 - 1 - 4))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 4 + 4, self.size // 2 - 4 - 1 - 4))
#
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 5, self.size // 2 + 3))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 6, self.size // 2 + 3))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 5, self.size // 2 + 2))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 6, self.size // 2 + 2))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 7, self.size // 2 + 2))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 6, self.size // 2 + 1))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 7, self.size // 2 + 1))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 8, self.size // 2 + 1))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 8, self.size // 2 + 0))
#         self.obstacle_point.append(Point(self.size - self.size // 2 - 7, self.size // 2 + 0))
#
#         for i in range(self.obstacle-1):            #控制障碍物的数目
#             x = np.random.randint(0, self.size)     #在0～self.size中随机出现一个数
#             y = np.random.randint(0, self.size)
#             self.obstacle_point.append(Point(x, y))
#             if (np.random.rand() > 0.5):            #在0～1中随机出现一个小数
#                 for l in range(self.size // 4):
#                     self.obstacle_point.append(Point(x, y + l))
#                     pass
#             else:
#                 for l in range(self.size // 4):
#                     self.obstacle_point.append(Point(x + l, y))
#                     pass
#     def Obstacle(self):
#         for p in self.obstacle_point:
#             p.cost = sys.maxsize
#     def IsObstacle(self, i, j):         #判断某点是否为障碍点
#         for p in self.obstacle_point:
#             if i == p.x and j == p.y:
#                 return True
#         return False
# ##生成带有随机障碍物地图RandomMap(x)
#
# class AStar:
#     def __init__(self, map):
#         self.map=map
#         self.open_set = []          #定义好open表与close表
#         self.close_set = []
#
#     def BaseCost(self, p):
#         x_dis = p.x
#         y_dis = p.y
#         return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)
#     # 曼哈顿对角距离表示g(n)
#
#     def HeuristicCost(self, p):
#         x_dis = self.map.size - 1 - p.x
#         y_dis = self.map.size - 1 - p.y
#         return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)
#     #曼哈顿对角距离表示h(n)
#
#     def TotalCost(self, p):
#         return self.BaseCost(p) + self.HeuristicCost(p)
#     # 总距离
#
#     def IsValidPoint(self, x, y):
#         if x < 0 or y < 0:
#             return False
#         if x >= self.map.size or y >= self.map.size:
#             return False
#         return not self.map.IsObstacle(x, y)
#     # 判断点是否为有效点(地图内部且不在障碍物上)
#
#     def IsInPointList(self, p, point_list):
#         for point in point_list:
#             if point.x == p.x and point.y == p.y:
#                 return True
#         return False
#     #判断p是否在point_list中
#
#     def IsInOpenList(self, p):
#         return self.IsInPointList(p, self.open_set)
#     #判断该点在不在open表中
#
#     def IsInCloseList(self, p):
#         return self.IsInPointList(p, self.close_set)
#     #判断该点在不在close表中
#
#     def IsStartPoint(self, p):
#         return p.x == 0 and p.y == 0
#     # 判断点是否为起点
#
#     def IsEndPoint(self, p):
#         return p.x == self.map.size - 1 and p.y == self.map.size - 1
#     # 判断点是否为终点
#
#     def SaveImage(self):
#         time_number = int(round(time.time() * 1000)) #round()四舍五入函数
#         name = str(time_number) + '.png'
#         savefig(name)
#     ##以时间为名保存图像为png格式
#
#     def ProcessPoint(self, x, y, parent):
#         if not self.IsValidPoint(x, y):         #对无效点不作处理
#             return
#         point = Point(x, y)
#         if self.IsInCloseList(point):           #对已经访问过的点不坐处理,已经经过的点会被放进close表
#             return
#         #print('过程点（', point.x, ',', point.y, '）', '的代价为：', self.TotalCost(point))
#         if not self.IsInOpenList(point):        #如果不在open表，把新点放进open表
#             point.parent = parent               #给该点一个父子节，便于得到最终路径
#             point.cost = self.TotalCost(point)  #该点的h(n)+g(n)为该点代价
#             self.open_set.append(point)
#     ##对每个节点进行判断与处于
#
#     def SelectPointInOpenList(self):
#         index = 0
#         selected_index = -1         #索引地址
#         min_cost = sys.maxsize
#         for p in self.open_set:
#             cost = self.TotalCost(p)
#             if cost < min_cost:
#                 min_cost = cost
#                 selected_index = index
#             index += 1
#         return selected_index       #返回最小代价对应的索引地址
#     ##找到最小代价的点的索引地址(open表)
#
#     def BuildPath(self,p,ax,start_time):
#         path = []
#         while True:
#             path.insert(0, p)           #不断在前面插入父节点
#             if self.IsStartPoint(p):    #判断节点是不是初始点
#                 break
#             else:
#                 p = p.parent            #若不是初始点，追踪该点的父节点
#         for p in path:
#             rec = Rectangle((p.x, p.y), 1, 1, color='g')    #1,1应该指得是宽,高
#                                                             #print(rec)会显示"Rectangle(xy=(*, *), width=1, height=1, angle=0)"
#             ax.add_patch(rec)           #将上面的rec矩阵画出来(实心)
#             draw()                      #show()包含draw()，但是draw()更适合多次保存的程序
#             self.SaveImage()            #保存图片
#         draw()
#         self.SaveImage()   #########################################################
#         end_time = time.time()          #记录结束时间
#         print('算法运算时间为：', int(end_time-start_time), '秒')
#     ##用实心矩阵绘制最终路径
#
#     def RunAndSaveImage(self,ax):
#         start_time = time.time()
#         start_point = Point(0, 0)
#         start_point.cost = 0
#         self.open_set.append(start_point)
#         while True:
#             index = self.SelectPointInOpenList()    #不断得到新的索引地址
#             if index < 0:                           #索引失败时会返回-1
#                 print('无路可走！计算失败！')
#                 return
#             p = self.open_set[index]
#
#             rec = Rectangle((p.x, p.y), 1, 1, color='c')
#             ax.add_patch(rec)                       #用实心矩阵绘制索引的节点
#             self.SaveImage()                        #实时保存图片
#
#             if self.IsEndPoint(p):                  #绘制最终路径
#                 self.SaveImage()   ###########################################
#                 return self.BuildPath(p,ax,start_time)
#
#             del self.open_set[index]                #把已经走完的节点从open表中删除
#             self.close_set.append(p)                #把已经走完的节点加入到close表中
#
#             x = p.x
#             y = p.y
#             self.ProcessPoint(x-1, y+1, p)          #对周围对点进行排查，寻找新的节点，并加入到open表中
#             self.ProcessPoint(x-1, y, p)
#             self.ProcessPoint(x-1, y-1, p)
#             self.ProcessPoint(x, y-1, p)
#             self.ProcessPoint(x+1, y-1, p)
#             self.ProcessPoint(x+1, y, p)
#             self.ProcessPoint(x+1, y+1, p)
#             self.ProcessPoint(x, y+1, p)
#     ##寻找最优路径并且绘制出来
# ##A*算法，对点属性的判断及距离判断
#
# figure(figsize=(5, 5))      #图幅
#
# map = RandomMap(50)          #生成随机地图
#
# ax = gca()                  #当前子图,gcf()为图表
#
# ax.set_xlim([0, map.size])  #确定图片大小
# ax.set_ylim([0, map.size])
#
# for i in range(map.size):
#     for j in range(map.size):
#         if map.IsObstacle(i,j):
#             rec = Rectangle((i, j), width=1, height=1, color='gray')
#             ax.add_patch(rec)
#         else:
#             rec = Rectangle((i, j), width=1, height=1, facecolor='w') #edgecolor边框颜色,facecolor实心颜色
#             ax.add_patch(rec)
# #用实心矩形绘制地图(纯灰色为障碍物)
#
# rec = Rectangle((0, 0), width = 1, height = 1, facecolor='b')
# ax.add_patch(rec)           #起点为蓝色小矩形
#
# rec = Rectangle((map.size-1, map.size-1), width = 1, height = 1, facecolor='r')
# ax.add_patch(rec)           #终点为红色小矩形
#
# axis('equal')               #把坐标系和表格分离
# axis('off')                 #删除坐标系
#
# tight_layout()              #调整图像外部边缘距离(可忽略)
#
# #show()
#
# a_star = AStar(map)
#
# a_star.RunAndSaveImage(ax)




















































# layers1 = [2,1,1,1,1,1]
# weights1 = []
# for i in range(1, len(layers1) - 1):
#     weights1.append((2 * np.random.random((layers1[i - 1] + 1, layers1[i] + 1)) - 1) * 0.25)
#     weights1.append((2 * np.random.random((layers1[i] + 1, layers1[i + 1])) - 1) * 0.25)
# print(weights1)
# layers = [2,1,1,1,1,1]
# weights = []
# for i in range(1,len(layers) - 1):
#     weights.append(2 * np.random.random((layers[i - 1] , layers[i])) - 1)
#     weights.append((2 * np.random.random((layers[i] , layers[i + 1])) - 1))
# print(weights)


###sklearn库的基本操作###
##数据集和模型
# from sklearn import datasets#导入数据集
# from sklearn.linear_model import LinearRegression#导入模型
# a = datasets.load_boston()#赋予数据集
#
# x = a.data#赋予特征向量
# y = a.target#赋予标记
#
# c = LinearRegression()#赋予模型
# c.fit(x,y)#导入数据训练模型
# print(x.shape)#特征向量的维度
# print(y.shape)#标记的维度
# print(c.predict(x[:4,:]))#预测
# print(y[:4])
# print(c.coef_)#得到权重（W）
# print(c.intercept_)#得到偏置（bias）
# print(c.score(x,y))#得到训练的正确率
##标准化数据
# from sklearn import preprocessing
# a = [100,25,425,30,2417,-21,-3258,-20,27,10000]
# print(a)
# print(preprocessing.minmax_scale(a,feature_range=(-1,1)))


###pytorch库基础###
# import torch
# import numpy as np

# x = torch.empty(5,3)#构造一个未初始化的5x3矩阵
# print(x)
# x1 = torch.rand(5,3)#构造一个随机初始化的矩阵
# print(x1)
# x2 = torch.zeros(5,3,dtype=torch.long)#构造一个填充的零矩阵类型是长整形
# print(x2)
# x3 = torch.tensor([5.5,3])#直接从数据构造张量
# print(x3)
# x4 = torch.ones(5,3)#构造一个5x3的单位矩阵
# print(x4)
# x5 = torch.rand_like(x4)#_like指构造和所输入矩阵维度一样的矩阵
# print(x5)
# print(x5.size())#得到它的大小

# 加法
# x = torch.rand(4,4)
# y = torch.rand_like(x)
# print(x + y)
# print(torch.add(x , y))
# print(y.add_(x))

# 调整张量的大小/形状
# x = torch.randn(4,4)
# print(x)
# y = x.view(16)
# print(y[2].item())#将元素张量转化为数字类型（一次不可转多个）
# z = x.view(2,2,4)
# print(z)

# 将torch张量转化为numpy数组
# a = torch.ones(5,5)
# print(a)
# b = a.numpy()#numpy化
# print(b)
# a.add_(1)#a在变化的同时b也会变
# print(a)
# print(b)

# 将NumPy阵列转换为torch张量
# a = np.ones(5)
# b = torch.from_numpy(a)
# np.add(a,1)
# print(a)
# print(b)

# torch.Tensor是包的中心类。如果您设置了它的属性.requires_grad如True，它开始跟踪它上的所有操作。
# 当你完成你的计算，你可以调用.backward()并自动计算所有梯度。这个张量的梯度将累积到.grad属性。
# x = torch.ones(2,2,requires_grad=True)
# print(x)
# y = x + 2
# print(y)
# z = y * y * 3
# print(z)
# out = z.mean()
# print(out)
# out.backward()
# print(x.grad)

# x = torch.randn(3,requires_grad=True)
# y = x * 2
# while y.data.norm() < 1000:
#     y = y * 2
# print(y)
# z = torch.tensor([5,10,15],dtype=torch.float)
# y.backward(z)
# print(x.grad)




##数值分析-习题一-16##
# def f1(x):
#     return 2*x**3+5
# def f2(x1,x2):
#     return (f1(x1) - f1(x2))/(x1 - x2)
# def f3(x1,x2,x3):
#     return (f2(x1,x3) - f2(x1,x2))/(x3 - x2)
# def f4(x1,x2,x3,x4):
#     return (f3(x1,x2,x4) - f3(x1,x2,x3))/(x4 - x3)
# def f5(x1,x2,x3,x4,x5):
#     return (f4(x1,x2,x3,x5) - f4(x1,x2,x3,x4))/(x5 - x4)


# 如何可视化三维函数
# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
#
# figure = plt.figure()
# axes = Axes3D(figure)
#
# X = np.arange(-10,10,0.25)
# Y = np.arange(-10,10,0.25)
# X , Y = np.meshgrid(X,Y)
#
# Z1 = X**2
# Z2 = Y**2
#
# axes.plot_surface(X , Y , Z1 , cmap='Accent')
# axes.plot_surface(X , Y , Z2 , cmap='Blues')
# plt.show()

# #多项式拟合
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1])
# y = np.array([-0.2209,0.3295,0.8826,1.4392,2.0003,2.5645,3.1334,3.7061,4.2836])
# z1 = np.polyfit(x, y, 3)#用3次多项式拟合
# p1 = np.poly1d(z1)
# print(p1) #在屏幕上打印拟合多项式
# yvals=p1(x)#也可以使用yvals=np.polyval(z1,x)
# plot1=plt.plot(x, y, '*',label='original values')
# plot2=plt.plot(x, yvals, 'r',label='polyfit values')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
# plt.title('polyfitting')
# plt.show()

# #数值计算迭代
# def f(x):
#     return (20 / (x*x + 2*x + 10))
# print(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))


# import numpy as np
# A = np.array([0.7,0.1,0.3],[0.2,0.8,0.3],[0.1,0.1,0.34])
# B = np.array([0.55],[0.4],[0.05])
# C = np.dot(A,B)
# print(np.dot(A,B))
# print(np.dot(C,B))



