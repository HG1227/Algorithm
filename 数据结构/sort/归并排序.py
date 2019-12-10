#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 归并排序.py
# @time: 2019/11/28


'''
归并排序是采用分治法的一个非常典型的应用。
归并排序的思想就是先递归分解数组，再合并数组。
将数组分解最小之后，然后合并两个有序数组，
基本思路是比较两个数组的最前面的数，谁小就先取谁，
取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，
最后把另一个数组的剩余部分复制过来即可。
'''


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        righ_thalf = alist[mid:]

        merge_sort(left_half)
        merge_sort(righ_thalf)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(righ_thalf):
            if left_half[i] < righ_thalf[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = righ_thalf[j]
                j += 1
            k += 1

        # 如果左半边或者右半边有一个先到末尾，上面的循环就退出了
        # 那么就把没有到末尾那半边的最后的元素添加到新的序列中，以免数值少算
        while i < len(left_half):
            alist[k] = righ_thalf[i]
            i += 1
            k += 1

        while j < len(left_half):
            alist[k] = righ_thalf[j]
            j += 1
            k += 1


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)
