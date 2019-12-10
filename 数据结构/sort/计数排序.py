#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 计数排序.py
# @time: 2019/12/10


def countSort(nums, order=1):
    max_num = max(nums)
    min_num = min(nums)
    extra = [0] * (max_num - min_num + 1)  # 创建桶
    for n in nums:
        extra[n - min_num] += 1

    result = []
    for i in range(len(extra)):
        if extra[i] != 0:
            result = result + ([min_num + i] * extra[i])

    if order == 1:
        return result
    else:
        return result[::-1]


test = [-2, 4, 6, 9, 0, 76, 21, 87, 65, 43, 32]
print(countSort(test))
print(countSort(test, 2))

# https://blog.csdn.net/weixin_43216017/article/details/90299151
# https://blog.csdn.net/wardseptember/article/details/81434641
