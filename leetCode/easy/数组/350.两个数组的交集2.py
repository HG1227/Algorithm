# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 350.两个数组的交集2.py
@time : 2020/5/7 
"""
"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

"""
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1,c2 = collections.Counter(nums1),collections.Counter(nums2)
        return [i for i in c1.keys() for j in range(min([c1[i], c2[i]]))]
if __name__ == '__main__':
    pass