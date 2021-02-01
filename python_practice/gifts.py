# -*- coding=utf-8 -*-
# author:lg62850

'''
送礼物
1、定义初始值
2、定义一个送礼物的方法
3、定义一个展示礼物的方法
4、调用方法
'''

have_gift=False

def send():
    print('送礼物啦！')
    global have_gift
    have_gift=True

def show():
    if have_gift==True:
        print('收到了，我很喜欢！')
    else:
        print('我没有收到礼物！')

if __name__=='__main__':
    send()
    show()