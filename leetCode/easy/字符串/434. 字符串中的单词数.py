#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 434. 字符串中的单词数.py
# @time: 2019/12/13


class Solution:
    def countSegments(self, s: str) -> int:
        slen = len(s)
        nw = 0
        for i in range(slen):
            if (i == 0 and s[i] != ' ') or (s[i] != " " and s[i - 1] == " "):
                nw += 1

        return nw


class Solution2:
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count

