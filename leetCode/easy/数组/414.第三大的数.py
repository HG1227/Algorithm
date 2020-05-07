# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 414.第三大的数.py
@time : 2020/5/7 
"""
"""
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:

输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans=sorted(list(set(nums)))
        return ans[-3] if len(ans)>2 else ans[-1]

"""
如果n个数是随机的，可以在若干次后，很快得到比较大的三个数。
此时后面的数应该先和第三个数比较，因为数学期望上，
它比第三个数小的可能性大于0.5，所以就被挡在门外。
这样的话大部分的情况下，只需要一次比较。这个有点像闯关比赛，
第三个数是第一关，第二个数是第二关，第一个数是最后一关。
如果这些数是正态分布的话，那么每一关闯不过的可能性大于闯过。
"""

class Solution2:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num > third:  # 通过第3关
                if num < second:
                    third = num
                elif num > second:  # 通过第2关
                    if num < first:
                        third = second
                        second = num
                    elif num > first:  # 通过第1关
                        third = second
                        second = first
                        first = num
        if third == float('-inf'):
            return first
        else:
            return third


if __name__ == '__main__':
    pass