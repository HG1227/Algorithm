#!/usr/bin/python
# coding:utf-8

"""
@software: PyCharm
@file: 371_两整数之和.py
"""

'''
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        # 超时
        while b != 0:
            add = a & b     # 记录a+b的进位，直到进位为0是退出
            a = a ^ b   #结果相加
            b = add<< 1
        return  a   #循环


    '''
    二进制的加法无外乎就以下几种情况，

    1+1 = 0 （有进位）
    1+0 = 1 （无进位）
    0+0 = 0 （无进位）
    0+1 = 1 （无进位）
    可以把加法分成无进位的异或结果a^b 与保存的进位相加，
    循环直到没有进位为止，就可以得到结果了。
    再分析二进制加法中进位怎么能保存，因为只有 1+1的时候会产生进位，这不就是与操作嘛，a&b 但是进位需要在更高的一位，所以我们就左移一位嘛就搞定了，
    所以，进位就可以这样保存
    c = (a&b)<<1;
    这样就可以用 a = (a^b) ^ c 得到一轮结果 ，但是有可能还会有进位，
    所以需要将这个放在循环里面就可以了。

    '''


def getSum( a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """

    # 超时
    while b != 0:
        add = (a & b) << 1
        a = a ^ b
        b = add
    return a

print(getSum(50,20))