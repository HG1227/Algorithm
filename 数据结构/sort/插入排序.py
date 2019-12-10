#!/usr/bin/python
# coding:utf-8

"""
@software: PyCharm
@file: 插入排序.py
@time: 2019/11/28
"""

'''
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，
找到相应位置并插入。插入排序在实现上，在从后向前扫描过程中，
需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
最坏时间复杂度：O(n^2)
稳定性：稳定
'''


def insertionSort(alist):
    for key, item in enumerate(alist):
        index = key
        while index > 0 and alist[index - 1] > item:
            alist[index] = alist[index - 1]
            index -= 1
        alist[index] = item
    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(insertionSort(alist))


def insertionSort2(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentvalue

    return alist


print(insertionSort2(alist))
