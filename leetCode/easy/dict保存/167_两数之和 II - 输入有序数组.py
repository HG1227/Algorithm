#!/usr/bin/python
# coding:utf-8

"""
@software: PyCharm
@file: 167_两数之和 II - 输入有序数组.py
"""

'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

'''

"""字典"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = dict()
        for i in range(0, len(numbers)):
            sub = target - numbers[i]
            if sub in res.keys():
                return [res[sub] + 1, i + 1]
            else:
                res[numbers[i]] = i
        return []


class Solution2(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                right = right - 1

        return []

class Solution3(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = dict()
        for index ,value in enumerate(numbers):
            sub = target - value
            if sub in res.keys():
                return [res[sub] + 1, index + 1]
            else:
                res[value] = index
        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 18
    c = Solution3()
    re = c.twoSum(nums, target)
    print(re)
