#!/usr/bin/env python
'''
    备份程序
    1. 需要支持完全和增量备份
    2. 周一执行完全备份
    3. 其他时间执行增量备份
    4. 备份文件需要打包为 tar 文件并使用 gzip 格式压缩
'''
import time
import tarfile
import hashlib
import pickle
import os

def check_md5(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as fobj:
        while True:
            data = fobj.read(4096)          #每次读取4K的数据
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def full_back(src,dst,md5file):
    #组装完整备份文件名（绝对路径）
    fname = os.path.basename(src)
    date = time.strftime('%Y_%m_%d')
    fname = '%s_full_%s.tar.gz' % (fname,date)   # c_full_xxxx_xx_xx.tar.gz
    fname = os.path.join(dst,fname)         #/backup/c_full_xxxx_xx_xx.tar.gz

    #执行完整备份操作
    tar = tarfile.open(fname,'w:gz')
    tar.add(src)
    tar.close()

    #md5校验变量{filename: md5value}
    md5_values = {}
    for path,floders,files in os.walk(src):
        for file in files:
            key = os.path.join(path,file)
            md5_values[key] = check_md5(key)

    #将源目录下所有文件的md5校验值字典写入本地文件
    with open(md5file,'wb') as fobj:
        pickle.dump(md5_values,fobj)


def incr_back(src,dst,md5file):
    #组装增量备份文件名（绝对路径）
    fname = os.path.basename(src)
    date = time.strftime('%Y_%m_%d')
    fname = '%s_incr_%s.tar.gz' % (fname,date)  # c_incr_xxxx_xx_xx.tar.gz
    fname = os.path.join(dst,fname)     #/backup/c_incr_xxxx_xx_xx.tar.gz

    #读取上次一备份md5file的内容
    with open(md5file,'rb') as fobj:
        old_md5_values = pickle.load(fobj)      #获取前一天的所有文件md5值，格式是字典

    #获取当前时间源目录下所有文件的md5值
    md5_dic = {}
    for path,floders,files in os.walk(src):
        for file in files:
            key = os.path.join(path,file)
            md5_dic[key] = check_md5(key)

    #查找发生变化（md5值不一致）的文件，将其放入增量备份的tar包
    tar = tarfile.open(fname, 'w:gz')
    for key in md5_dic:
        if md5_dic[key] != old_md5_values[key]:
            tar.add(key)
    tar.close()

    #更新本日md5file的值，覆盖旧的md5file
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5_dic)



if __name__ == '__main__':
    src = '/tmp/demo'
    dst = '/tmp/backup'
    md5file = '/tmp/backup/md5file'
    if time.localtime()[6] == 0:
        full_back()
    else:
        incr_back()