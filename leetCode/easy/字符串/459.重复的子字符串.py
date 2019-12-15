#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 459.重的子字符串.py
# @time: 2019/12/13

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1: -1].find(s) != -1


class Solution2(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                leng = len(s) // i
                if s[:i] * leng == s:
                    return True
        return False
