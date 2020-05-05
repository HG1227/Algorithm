# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 119.杨辉三角2.py
@time : 2020/5/5 
"""

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
示例:

输入: 3
输出: [1,3,3,1]

"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


if __name__ == '__main__':
    pass