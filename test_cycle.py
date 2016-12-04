#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates=['Michael','Bob','Tracy']
for name in classmates:
	print('Hello',name)
number=0
numberlist=[1,2,3,4,5,6,7,8,9,10]
for x in numberlist:
	number=number+x
print('Sum of 1 to 10 equals ',number)
number=0
maxnumber=100
n=maxnumber-1
while n>0:
	number=number+n
	n=n-2
print('Sum of odd numbers from 1 to 100 equals',number)