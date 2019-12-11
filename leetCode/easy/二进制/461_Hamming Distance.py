#!/usr/bin/python
#coding:utf-8

"""
@software: PyCharm
@file: 461_Hamming Distance.py
"""
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.
Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""


"""
二进制解法，异或之后计算1的个数
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #得到的t为整型的
        t=x^y
        count=0
        while t!=0:
            count=count+1
            t=t&(t-1)  #(t-1)相当于把二进制右移一位

        return  count

        # count2 = 0
        # while n:
        #     count2 += n & 1
        #     n >>= 1
        # return count2


print(3^4)
