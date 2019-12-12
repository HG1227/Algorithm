#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 387. 字符串中的第一个唯一字符.py
# @time: 2019/12/12

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


