# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 448.找到所有数组中消失的数字.py
@time : 2020/5/7 
"""
"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

"""
import numpy as np
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return np.setdiff1d([i for i in range(1, len(nums) + 1)], nums)

class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]
# 利用集合，位运算的特点

class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a=set(nums)
        b=set(range(1,len(nums)+1))
        return list(a^b)


if __name__ == '__main__':
    pass
