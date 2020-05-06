# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 217.存在重复元素.py
@time : 2020/5/5 
"""
'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

 

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        for i in range(len(nums)):
            if (nums[i] not in hash):
                hash[nums[i]] = i
            else:
                if (i - hash[nums[i]] <= k):
                    return True
                else:
                    hash[nums[i]] = i
        return False


if __name__ == '__main__':
    pass
