# Python 学习笔记

## 1. 数据类型和变量

- r ' ' 表示 ' ' 内部的字符默认不转义。
- '''...''' 表示多行内容，如：
``` Python
>>> print('''line1
... line2
... line3''')
line1
line2
line3
```
写成程序就是：
``` Python
print('''line1
line2
line3''')
```
- 布尔值为```True```和```False```，逻辑运算用```and```，```or```，```not```。
- ```None``` 是 Python 里一个特殊的空值。
- Python 中变量的类型不固定：

``` Python
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
```

- Python 中有两种除法，一种是```/```，表示浮点除法；一种是```//```，表示地板除法，同 MATLAB 中的 floor() :

``` Python
>>> print("10/3 =",10/3)
10/3 = 3.3333333333333335
>>> print("10//3 =",10//3)
10//3 = 3
```

- ```**``` :乘方
## 2. 字符串和编码 

- 在最新的 Python 3 版本中字符串用 Unicode 编码。ord() 函数获取字符的整数表示， chr() 函数可以把编码转换为对应的字符：

``` Python
>>> ord('A')
65
>>> chr(65)
'A'
>>> ord('中')
20013
>>> chr(20013)
'中'
```

- 如果要在网络上传输字符串或者把字符串保存到磁盘上，就需要把```str```变成以字节为单位的```bytes```。 Python 对```bytes```类型的数据用带b前缀的单引号或双引号表示：

``` Python
x = b'ABC'
```

- 以 Unicode 表示的```str```通过```encode()```方法可以编码为指定的```bytes```，例如：

``` Python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: 
ordinal not in range(128)
```

纯英文的```str```可以用 ASCII 编码为```bytes```，内容是一样的，含有中文的```str```可以用 UTF-8 编码为```bytes```。含有中文的```str```无法用 ASCII 编码，因为中文编码的范围超过了 ASCII 编码的范围， Python 会报错。

- 如果从网络或者磁盘上读取了字节流，那么读到的数据是```bytes```。要把```bytes```变成```str```，需要用```decode()```方法：

``` Python
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

- 计算字符串的长度用```len()```函数：

``` Python
>>> len('ABC')
3
>>> len('中文')
2
>>> len(b'ABC')
3
>>> len('中文'.encode('utf-8'))
6
```

上述代码表明，```len()```函数对于```str```字符串计算的是字符数，对于```bytes```字符串计算的是字节数。

- Python 源文件也是一个文本文件，所以当源代码有中文时，需要在保存的时候将源代码保存为 UTF-8 编码。当 Python 解释器读取源代码时，为了让它按照 UTF-8 读取，需要在文件开头写上：

``` Python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

第一行是用于告诉 Linux/macOS 这是一个 Python 执行文件，第二行是为了告诉解释器按照 UTF-8 编码格式读取源代码。

- Python中格式化输出字符串的方式和C语言相同，用```%```实现：

``` Python
>>> "Hello, %s" % "world"
'Hello, world'
>>> 'Hello %s, you owe me %d dollars' % ('zengsihan',100000)
'Hello zengsihan, you owe me 100000 dollars
```

有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用```%%```来表示一个```%```：

``` Python
>>> 'This mission is %d%% completed.'% 59
'This mission is 59% completed.'
```

## 3. list 和 tuple
- list 是 Python 内置的一种数据类型，是一种**有序**的可更改的集合，可以随时添加和删除其中的元素，声明方式同 MATLAB 的行向量（空列表的声明方式和空向量也一样）。用 len() 函数可以获得 list 元素中的个数。用数组的索引方式可以访问 list 中的每一个位置的元素。如：
``` Python
>>> classmates=['michael','bob','tracy']
>>> classmates
['michael', 'bob', 'tracy']
>>> len(classmates)
3
>>> L=[]
>>> len(L)
0
>>> classmates[0]
'michael'
>>> classmates[1]
'bob'
```

如果想要获取最后一个元素，除了计算索引位置之外，还可以用```-1```做索引，直接获取最后一个元素。一次类推可以得到倒数第二个/第三个。如：

``` Python
>>> classmates[-1]
'tracy'
>>> classmates[-2]
'bob'
>>> classmates[-3]
'michael'
```

- 由于 list 是一个可变的有序集合，所以可以在 list 的末尾追加元素，用 append(*item_name*) 函数；也可以用 insert(*item_location*,*item_name*) 函数把元素插入到指定的位置；也可以用 pop() 函数删除 list 末尾的元素；也可以用 pop(*item_location*) 删除指定位置的元素。要把某个元素替换成别的元素，可以直接给对应索引位置的元素赋值。如：

``` Python
>>> classmates.append('chenyubo')
>>> classmates.insert(4,'toby')
>>> classmates
['michael', 'bob', 'tracy', 'chenyubo', 'toby']
>>> classmates.pop()
'toby'
>>> classmates.pop(2)
'tracy'
>>> classmates
['michael', 'bob', 'chenyubo']
>>> classmates[1]='Bob'
>>> classmates
['michael', 'Bob', 'chenyubo']
```

-  list 里面的元素的数据类型可以不同，list 元素也可以是另一个 list 。如果 list 内部还有 list 则可以把外层的 list 看做一个二维数组（很少用到）。如：

``` Python
>>> L=['Apple',1,2,True]
>>> L
['Apple', 1, 2, True]
>>> s=['Python','MATLAB',['C','C++'],'Java']
>>> len(s)
4
>>> s[2][1]
'C++'
```

- 寻找 list 中的某一个元素（首次出现）的位置用```index(item)```函数。

- tuple 是 Python 中内置的另一种**有序**列表，用小括号将所有元素括起来。它和 list 非常相似，但是 tuple 一旦初始化就不能修改，也就是说它没有 append(), insert(), pop() 之类的方法。其他获取元素的方法和 list 相同，只是不能赋值。如：

``` Python
'C++'
>>> classmates=('micheal','bob','chenyubo')
>>> classmates.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'pop'
```

- 为了防止定义单元素的 tuple 的小括号和数学运算的小括号冲突，在定义只有一个元素的 tuple 时必须加一个逗号来消除歧义。另外需要注意的是，如果 tuple 中的元素中包含 list ，那么这个 list 中的元素是可以改变的，因为 tuple 中的不可改变是指 tuple 中元素的指向永远不改变，如果指向一个 list ，就不能改成指向其他对象，但是指向的 list 本身可变。如：

``` Python
>>> classmate=('michael',)
>>> classmate
('michael',)
>>> t=('a','b',['x','y'])
>>> t
('a', 'b', ['x', 'y'])
>>> t[2][0]='a'
>>> t[2][1]='b'
>>> t
('a', 'b', ['a', 'b'])
```

## 4. 条件判断

- Python 的条件判断和 C 语言几乎一样，格式如下：

``` Python
# do-if.py
age=3
if age>=18:
    print('adult')
elif age>=6:
    print('teenager')
else:
    print('kid')
```

需要注意的是，```if```可以简写：

```Python
if x:
    print('True')
```

只要```x```是非零数值、非空字符串、非空 list 等，就判断为```True```。

- 另外需要注意的是， Python 中 input() 函数返回的数据类型是```str```，不能直接和指数比较，所以在如下情况中必须先用 int() 函数把```str```转换成整数，再用```if```比较大小。

``` Python
# test_int.py
birth=input('please input your birth : ')
birth=int(birth)
if birth>2000:
    print('00后')
else:
    print('00前')
```

## 5. 循环

- Python 中的 for 循环的格式是：```for …… in ……:```，可以依次把 list 或 tuple 中的每个元素迭代出来。如：

``` Python
# test_cycle.py
classmates=['Michael','Bob','Tracy']
for name in classmates:
    print('Hello',name)
number=0
numberlist=[1,2,3,4,5,6,7,8,9,10]
for x in numberlist:
    number=number+x
print('Sum of 1 to 10 equals ',number)
```

输出结果为：

```
Hello Michael
Hello Bob
Hello Tracy
Sum of 1 to 10 equals  55
```

- 如果要计算 1-100 的整数和，从 1 写到 100 很难。 Python 提供一个 range(*number*)函数，可以生成一个小于 *number* 的整数序列，再通过 list() 函数转换为 list ，如：

``` Python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- Python 中的 while 循环格式为

``` 
while *循环执行条件*:
    *your codes*
```

如求解100以内的所有奇数的和：

``` Python
# test_cycle.py
number=0
maxnumber=100
n=maxnumber-1
while n>0:
    number=number+n
    n=n-2
print('Sum of odd numbers from 1 to 100 equals',number)
```

注：不要忘了两种循环语句的最后都有一个冒号。

## 6. dict 和 set

- dict 是 Python 中内置的类似 map 的数据格式，使用 key-value 方式存储，查找速度极快。一个 key 只能对应一个 value ，所以多次赋值的话后来的值会把原来的值冲掉。可以通过 key 把数据放入 dict 。如：

``` Python
>>> score={'Michael':95,'Bob':75,'chenyubo':100}
>>> score['Michael']
95
>>> score['chenyubo']
100
>>> score['Bob']=85
>>> score['Bob']
85
>>> score['Adam']=59
>>> score['Adam']
59
```

如果 key 不存在， dict 就会报错。要避免 key 不存在的错误，有两种办法：一是通过```in```判断 key 是否存在，二是通过 dict 提供的 get 方法，如果 key 不存在，可以返回```None```(在命令行中返回```None```时不显示结果)或者返回自己制定的value。要删除一个 key ，可以使用 pop(*key*) 方法。如：

``` Python
>>> score['zengsihan']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'zengsihan'
>>> 'Adam'in score
True
>>> 'zegnsihan' in score
False
>>> score.get('Adam')
59
>>> score.get('zengsihan')
>>> score.get('zengsihan',-1)
-1
>>> score.pop('Adam')
59
>>> score
{'chenyubo': 100, 'Bob': 85, 'Michael': 95}
```

需要注意的是， dict 是用空间换取时间的一种方法。 dict 内部存放的顺序和 key 存放的顺序无关。 **dict 的 key 必须是不可变对象**（字符串、整数等，不包括 list ），因为通过 key 计算位置使用的是哈希算法，如果 key 可变的话 dict 内部就混乱了。  

- set 和 dict 类似，也是一组 key 的集合，但不存储 value 。由于 key 不能重复，所以在 set 中没有重复的元素。要创建一个 set ，需要提供一个 list 作为输入。重复元素在 set 中自动被过滤。如：

``` Python
>>> s=set([1,2,3])
>>> s
{1, 2, 3}
>>> ss=set([1,1,2,2,3,3,3])
>>> ss
{1, 2, 3}
```

- 通过```add(key)```方法可以把元素添加到 set 中。可以重复添加但是没有效果。通过```remove(key)```方法可以删除 set 中的元素。set 可以看成数学意义上的**无序**和**无重复**元素的集合，所以两个 set 可以做交、并等运算。如：

``` Python
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.remove(1)
>>> s
{2, 3, 4}
>>> s & ss
{2, 3}
>>> s|ss
{1, 2, 3, 4}
```

set 的原理和 dict 是一样的，所以不能把 list 放入 set。

## 7. 类型转换与函数

- 类型转换的用法同 MATLAB ，直接用类型名做函数名：

``` Python
>>> int(12.34)
12
>>> int('2')
2
>>> float('12.34')
12.34
>>> str(2)
'2'
```

- 进制转换的函数为```hex()```,```bin()```。返回值是一个字符串.
- Python 中可以把函数名赋值给变量，用变量名调用函数，如：

``` Python
>>> a=abs
>>> a(-2)
2
```

- 定义函数的格式如下：

``` Python
def function_name(function_parameter_list):
    ...
    function codes
    ...
    return return_value
```

如果没有 return 语句则自动返回 ```None``` 。
- 如果已经把函数定义在```file_name.py```文件中，那么可以在该文件的目录下启动 Python 解释器，用```from file_name import function_name```来导入函数。注意函数名不包含```.py```扩展名。
- Python 中可以定义空函数，用```pass```语句：

``` Python
def nop():
    pass
```

注：```pass```语句什么都不干，实际上多用于做占位符，等想好了怎么写再替换掉```pass```。

- 对输入类型做检查可以用内置函数```isinstance()```实现：

``` Python
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
```

- Python 中函数可以返回“多个值”，实际上返回的是一个有多个值的 tuple 。在语法上，返回一个 tuple 可以省略括号，而多个变量可以同时接收一个 tuple ，按位置赋给对应的值。
- ```import  import_name```导入函数包。
- 默认参数的使用方法与C语言完全相同，有几点要注意：一是必选参数在前，默认参数在后；二是把变化大的参数放在前面，变化小的参数放在后面，这样变化小的参数就可以作为默认参数。
- 默认参数必须指向**不变对象**（也就是不能为list），否则会出现以下情况：

``` Python
def add_end(L=[]):
    L.append('end')
    return L

>>> add_end([1,2,3])
[1,2,3,'end']
>>> add_end()
['end']
>>> add_end()
['end','end']
```

最后一次调用的返回结果出了问题，因为默认参数L也是一个变量，指向对象[]，如果改变了L的内容，下次调用的时候，默认参数的内容就改变了。为了避免这种情况，默认参数可以用```None```实现：

``` Python
def add_end(L=[]):
    if L is None:
        L=[]
    L.append('end')
    return L
```

- Python 中的函数可以使用可变参数，定义方式是在参数前面加一个```*```。如：

``` Python 
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
```

可变参数既可以直接传入：```func(1,2,3)```，也可以先组装 list 或者 tuple ，再通过在变量名前面加一个```*```传入：```func(*[1,2,3])```。这种方式很有用，也很常见。

- 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收```city```和```job```作为关键字参数。这种方式定义的函数如下：

``` Python
def person(name,age,*,city,job):
  print(name,age,city,job)
```

- 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。调用方式如下：

``` Python
>>> person('Jack',24,city='Beijing',job='teacher')
Jack 24 Beijing Engineer
```

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了：

``` Python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```

命名关键字参数必须传入参数名，这和位置参数不同。命名关键字参数可以有缺省值，从而简化调用：

``` Python
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
```

