#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 选择排序.py
# @time: 2019/11/29


'''
选择排序（Selection sort）是一种简单直观的排序算法。
它的工作原理如下。首先在未排序序列中找到最小（大）元素，
存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

选择排序的主要优点与数据移动有关。
如果某个元素位于正确的最终位置上，则它不会被移动。
选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上，
因此对n个元素的表进行排序总共进行至多n-1次交换。
在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。

原文链接：https://blog.csdn.net/u014745194/article/details/72783174
'''


def selection_sort(alist):
    for i in range(len(alist) - 1):
        min = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min]:
                min = j
        alist[i], alist[min] = alist[min], alist[i]
    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(selection_sort(alist))
