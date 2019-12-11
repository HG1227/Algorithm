#!/usr/bin/python
# coding:utf-8

"""
@software: PyCharm
@file: 242_有效的字母异位词.py
"""

'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

'''
"""
用两个字典保存字母出现的次数，最后判断两个字典是否相同
"""


class Solution():
    def isAnagram(self, s, t):
        '''

        :param s:   str
        :param t:   str
        :return:    bool
        '''
        dict1 = {}
        dict2 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
            print(dict1[i])
        print('***')
        for i in t:
            dict2[i] = dict2.get(i, 0) + 1
            print(dict2[i])

        return dict1 == dict2

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def isAnagram3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            # 结果字典
            dic = {}
            # 先遍历s，数每个字符出现的次数，存在字典dic中，key是字符，value是出现次数
            for i in s:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
            # 遍历t，遇见相同字符，就在dic中减一；遇见不同字符，直接返回false
            for i in t:
                if i in dic:
                    dic[i] -= 1
                else:
                    return False
            # 遍历结果字典，是否每个value都为0
            for i in dic:
                if dic[i] != 0:
                    return False
        return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    c = Solution()
    re = c.isAnagram(s, t)
    print(re)
