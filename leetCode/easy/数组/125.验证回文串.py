# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 125.验证回文串.py
@time : 2020/5/5 
"""

'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false


'''

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # p=''.join(re.findall(r'[\w\d]+',s))
        p = ''.join(re.findall(r'[a-zA-Z0-9]+', s))
        p = p.lower()
        return True if p == p[::-1] else False


if __name__ == '__main__':
    pass
