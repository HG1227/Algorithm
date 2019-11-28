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


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0;
        j = 0;
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
