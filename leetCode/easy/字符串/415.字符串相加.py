#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 415.字符串相加.py
# @time: 2019/12/12


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = " "
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            temp = n1 + n2 + carry
            carry = temp // 10
            res = str(temp % 10) + res
            i, j = i - 1, j - 1
        return '1' + res if carry else res
