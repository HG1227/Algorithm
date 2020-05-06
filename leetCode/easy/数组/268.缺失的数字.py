# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 268.缺失的数字.py
@time : 2020/5/6 
"""

"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8

"""

# 根据等差数列求和公式即可
# 差值即为缺失的数字
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return int(n * (n + 1) / 2 - sum(nums))


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)


if __name__ == '__main__':
    pass