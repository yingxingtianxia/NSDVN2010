#!/usr/bin/env python
'''
创建文件
1. 编写一个程序，要求用户输入文件名
2. 如果文件已存在，要求用户重新输入
3. 提示用户输入数据，每行数据先写到列表中
4. 将列表数据写入到用户输入的文件名中
'''
import os


def get_fname():
    while True:
        fname = input('请输入文件名：')
        if os.path.exists(fname):
            print('文件已存在')
            continue
        else:
            return fname


def get_content():
    content = []
    while True:
        cont = input('请输入内容(end结束)：')
        if cont == 'end':
            break
        content.append('%s\n' % cont)
    return content


def wfile(fname, content):
    with open(fname, 'a+') as fobj:
        fobj.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
