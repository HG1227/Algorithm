#!/usr/bin/python
#coding:utf-8

"""
@software: PyCharm
@file: 476_数字的补数.py
"""

'''
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

注意:

给定的整数保证在32位带符号整数的范围内。
你可以假定二进制数不包含前导零位。
示例 1:

输入: 5
输出: 2
解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。
示例 2:

输入: 1
输出: 0
解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
'''


"""
更巧妙的方法，要得到对位取反，
其实就是用全1的数字进行按位异或，但是要位数刚刚好
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=1
        while i<=num:
            i = i << 1
        return (i-1) ^ num
