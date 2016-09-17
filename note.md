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

