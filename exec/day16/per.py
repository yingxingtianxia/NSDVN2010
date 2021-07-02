#!/usr/bin/env python
'''
魔法方法：用了容易让人魔怔的方法
'''
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    #魔法方法
    def __repr__(self):
        return '我是__repr__方法'
    def __str__(self):
        return '我是__str__方法'

    #实例方法
    def eat(self,time,food):
        return '%s今天%s吃了%s' % (self.name,time,food)
    def drink(self,drink):
        return '%s今天吃顶了，喝了%s促进消化' % (self.name,drink)
    def run(self,distance):
        return '%s还是撑得慌，去跑了%s公里' % (self.name,distance)


if __name__ == '__main__':
    p1 = Person('王宝宝',22,'男')
    print(p1)
    print(p1.eat('早上','豆汁'))
    print(p1.eat('中午','卤煮'))
    print(p1.eat('晚上','炖吊子'))