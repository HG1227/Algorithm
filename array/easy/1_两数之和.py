#!/usr/bin/python
#coding:utf-8

"""
@software: PyCharm
@file: 1_两数之和.py
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in num_dict.keys():
                return [num_dict[sub], index]
            else:
                num_dict[value] = index

        return []

if __name__=="__main__":
    nums = [2, 7, 11, 15]
    target = 9
    c=Solution()
    re=c.twoSum(nums,target)
    print(re)


 
