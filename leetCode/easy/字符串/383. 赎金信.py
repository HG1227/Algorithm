#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 383. 赎金信.py
# @time: 2019/12/11

import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

class Solution2(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        # 哈希表存储magazine字符及个数
        for c in magazine:
            if c in magazine_dict:
                magazine_dict[c] += 1
            else:
                magazine_dict[c] = 1

        for c in ransomNote:
            if c in magazine_dict and magazine_dict[c] > 0:
                magazine_dict[c] -= 1
            else:
                return False

        return True