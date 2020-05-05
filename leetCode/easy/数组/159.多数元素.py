# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 159.多数元素.py
@time : 2020/5/5 
"""
'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''
# 使用一个字典
class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = dict()
        for i in nums:
            if i in res.keys():
                res[i] = res[i] + 1
            else:
                res[i] = 1

            if res[i] > len(nums) / 2:
                return i


import collections
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [k for k, v in collections.Counter(nums).items() if v>len(nums)//2][0]
if __name__ == '__main__':
    pass