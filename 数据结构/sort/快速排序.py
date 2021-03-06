#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 快速排序.py
# @time: 2019/11/29


"""
快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），
通过一趟排序将要排序的数据分割成独立的两部分，
其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，
以此达到整个数据变成有序序列。
————————————————
原文链接：https://blog.csdn.net/u014745194/article/details/72783479

分析步骤：
步骤为：
1、从数列中挑出一个元素，称为”基准”（pivot）。

2、重新排序数列，所有元素比基准值小的摆放在基准前面，
    所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
    在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。

3、递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。
虽然一直递归下去，但是这个算法总会结束，因为在每次的迭代（iteration）中，
它至少会把一个元素摆到它最后的位置去。
"""


def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:
        return

    # 基准
    mid = alist[start]

    # 左边的游标
    left = start
    # 右边游标
    right = end

    while left < right:
        while left < right and alist[right] >= mid:
            # 右边的游标移动，左边的游标不动
            right -= 1

        alist[left] = alist[right]

        while left < right and alist[left] < mid:
            # 左边的游标移动，右边的游标不动
            left += 1

        alist[right] = alist[left]

    # 退出循环后，left 与 right 重合，即相等
    alist[left] = mid
    # 递归的方式，排左边的序列
    quick_sort(alist, start, left - 1)
    # 递归方式排右边的序列
    quick_sort(alist, left + 1, end)


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(f"原列表为：{alist}")
    quick_sort(alist, 0, len(alist) - 1)
    print(f"新列表为：{alist}")
