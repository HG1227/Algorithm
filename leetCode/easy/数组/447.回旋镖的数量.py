# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 447.回旋镖的数量.py
@time : 2020/5/7 
"""
"""
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
"""


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                dis = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                cmap[dis] = cmap.get(dis, 0) + 1
            for key in cmap:
                res += (cmap[key]) * (cmap[key] - 1)
        return res


import collections
"""
先说一下这道题的意思，每次找三个点，第一个点和第二个点的欧氏距离等于第
一个点和第三个点的欧氏距离，说明是回旋镖。
思路如下：
每次固定一个点，使用哈希表存储其他点到这个点的距离，如果存在记录次数，
回旋镖的数量应为次数*（次数-1）


著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution2:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in points:
            dis = []
            for j in points:
                dis.append((j[1] - i[1]) ** 2 + (j[0] - i[0]) ** 2)
            for j, k in collections.Counter(dis).items():
                if j != 0 and k >= 2: ans += k * (k - 1)
        return ans


if __name__ == '__main__':
    pass
