#!/usr/bin/python
# coding:utf-8

"""
@software: PyCharm
@file: 231._2的幂.py
"""
'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false
'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        判断一个数是否是2的此方数，只需判断是否只有1位二进制位是1即可，用之前提到的方法，n与n-1的按位与可以把最右边一位1变为0。
        
        解题思路：
        若 n = 2^x,且 x为自然数（即 n为2的幂），则一定满足以下条件：
           1. 恒有 n & (n - 1) == 0，
              这是因为：
                n二进制最高位为1，其余所有位为0；
                n - 1二进制最高位为0，其余所有位为1；
           2.一定满足 n > 0。

        """
        return n > 0 and not (n & n - 1)



