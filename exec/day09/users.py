#!/usr/bin/env python
'''
1. 支持新用户注册，新用户名和密码注册到字典中
2. 支持老用户登陆，用户名和密码正确提示登陆成功
3. 主程序通过循环询问，进行何种操作，根据用户的选择，执行注册或是登陆操作
'''
users = {}

def register():
    print('reg')

def login():
    print('login')

def main():
    prompt = '''####操作清单####
0--->注册
1--->登录
2--->退出
请选择:'''
    cmds = {'0': register,'1': login}
    while True:
        choice = input(prompt)
        choice = choice.strip(' ')
        if choice == '':                #用户直接拍了回车
            continue
        if choice not in '012':
            print('非法选项，请重新输入')
        if choice == '2':
            break
        # elif int(choice) == 0:
        #     register()
        # elif int(choice) == 1:
        #     login()
        cmds[choice]()

if __name__ == '__main__':
    main()