#!/usr/bin/python
#coding:utf-8

"""
@software: PyCharm
@file: 205_同构字符串.py
"""

"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。
"""

"""
用一个字典保存
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return  False

        res=dict()
        for i in range(0,len(s)):
            if s[i] in res.keys():
                if res[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in res.values():
                    return  False
                else:
                    res[s[i]] =t[i]

        return  True

    def isIsomorphic2(self, s, t):
        return list(map(s.find, s)) == list(map(t.find, t))

    def isIsomorphic3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # 使用哈希映射记录每个字母的转换方法，键：s的字母，值：t的字母
        hash_map = {}

        # 由于s和t具有相同的长度，所以使用zip遍历
        for c1, c2 in zip(s, t):

            # 如果c1已在键中，且c2与键c1的值不对应，说明出现了s=aa，t=ab这种情况
            if c1 in hash_map and c2 != hash_map[c1]:
                return False

            # 如果c1不在键中，但c2出现在字典的值中，说明出现了s=ab，t=aa这种情况
            if c1 not in hash_map and c2 in hash_map.values():
                return False

            # 仅有以上两种情况需要输出False，如果不满足以上两种情况，则添加键值对
            hash_map[c1] = c2

        # 循环走完说明s和t中每个字母都有唯一的对应关系，可以输出True
        return True

if __name__=="__main__":
    s='egg'
    t='edd'
    c=Solution()
    re=c.isIsomorphic2(s,t)
    print(re)

    print(list(map(s.find, s)))
    #[0, 1, 0, 1]