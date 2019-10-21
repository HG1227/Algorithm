#!/usr/bin/python
#coding:utf-8

"""
@software: PyCharm
@file: 67_二进制求和.py
"""

'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''
 
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a, b):
        if a==b=="0":
            return "0"
        num1=num2=0
        for i,x in enumerate(a):
            num1+=int(x)*(2**(len(a)-i-1))
        for i,x in enumerate(b):
            num2+=int(x)*(2**(len(b)-i-1))
        num=num1+num2

        return bin(num)[2:]

        # numss=""
        # while num>1:
        #     nums=num%2
        #     numss+=str(nums)
        #     num=num//2
        # numss+="1"
        # return numss[::-1]