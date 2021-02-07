# -*- coding=utf-8 -*-
# author:lg62850
import money
import send_money
import select_money

if __name__=='__main__':
    send_money.send_money(2000)
    print(select_money.select_money())