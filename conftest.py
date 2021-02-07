# -*- coding=utf-8 -*-
# author:lg62850
import pytest

# 执行用例前打印'开始计算'，执行用例后打印'计算结束'
@pytest.fixture(scope='module')
def before_cases():
    print('开始计算')
    yield
    print('计算结束')