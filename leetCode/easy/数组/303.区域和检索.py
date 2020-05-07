# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 303.区域和检索.py
@time : 2020/5/6 
"""

'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

'''
# 数组存储前n项的累加和，这里要判断i是否为0
class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = nums
        for i in range(1,len(nums)):
            self.dp[i] += self.dp[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - (self.dp[i-1] if i > 0 else 0)
if __name__ == '__main__':
    pass