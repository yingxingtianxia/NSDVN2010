#!/usr/bin/env python
# 9x9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%s x %s = %s\t' % (j,i,j*i),end="")
    print()