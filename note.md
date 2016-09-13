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

