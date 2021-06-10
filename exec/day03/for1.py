#!/usr/bin/env python
astr = 'abcdefg'
for i in astr:
    print(i)
alist = [1, 2, 3, 'a', 'b']
for i in alist:
    print(i)
atu = (1, 2, 3, 'a', 'b')
for i in atu:
    print(i)

aset = set([1, 2, 3])
for i in aset:
    print(i)

adic = {"a": 1, "b": 2, "c": 3}
for item in adic:
    print(item)
for item in adic.items():
    print(item)
for i in adic:
    print(i, adic[i])


#range()函数    range(start,end,step)

for i in range(10):
    print(i)

print(list(range(10)))

for i in range(10,15):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(10,1,-3):
    print(i)            #1不会被打印

#Python3相对于Python2做了优化
#python  -->   range(100000000000000000)
#python3 -->   range(100000000000000000)