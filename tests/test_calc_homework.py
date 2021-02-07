# -*- coding=utf-8 -*-
# author:lg62850
import pytest
import yaml
from python_code.calc import Calculator

# 读取calc.yaml文件中的数据
with open('./tests/datas/calc.yaml') as f:
    calc_datas=yaml.safe_load(f)['add']
    data=calc_datas['datas']
    myid=calc_datas['myids']

@pytest.mark.usefixtures()
class TestCals:
    # 实例化计算器
    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.run(order=1)
    # 参数化测试案例数据
    @pytest.mark.parametrize("a,b,c", data, ids=myid)
    def test_add(self,a,b,c,before_cases):
        result=self.calc.addition(a,b)

        # 如果结果是浮点数，则保留两位小数
        if isinstance(result,float):
            result=round(result,2)

        # 添加断言
        assert result==c

    # 除法测试用例
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,c',[(1,1,1),(0.1,0.1,1),(-1,-0.1,10),(1,0,0)])
    def test_division(self,a,b,c,before_cases):
        # 异常处理
        try:
            result=self.calc.division(a,b)

            # 添加断言
            assert result == c
        except ZeroDivisionError:
            print('被除数不能为零')

    # 减法测试用例
    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures('before_cases')
    @pytest.mark.parametrize('a,b,c',[(1,1,0),(0.1,0.1,0),(-1,-0.1,-0.9)])
    def test_subtraction(self,a,b,c):
        result=self.calc.subtraction(a,b)

        # 添加断言
        assert result == c

    # 乘法测试用例
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,c',[(1,1,1),(0.1,0.1,0.01),(-1,-0.1,0.1),(1,0,0)])
    def test_multiplication(self,a,b,c,before_cases):
        result=self.calc.multiplication(a,b)

        if isinstance(result,float):
            result=round(result,2)

        # 添加断言
        assert result == c