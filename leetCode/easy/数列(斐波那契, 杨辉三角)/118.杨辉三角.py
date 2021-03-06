# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 118.杨辉三角.py
@time : 2020/5/5 
"""

'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


下一行 = 上一行错位相加
[1,3,3,1],
  [1,3,3,1],
[1,4,6,4,1]
'''

class Solution:
    def generate(self, numRows: int): #-> List[List[int]]
        if numRows == 0 : return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a, b in zip([0] + res[-1], res[-1]+[0])]
            res.append(newRow)
        return res

if __name__ == '__main__':
    pass
