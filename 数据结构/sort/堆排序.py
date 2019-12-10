#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 堆排序.py
# @time: 2019/12/9


def heap_sort(alist):
    if alist == None or len(alist) == 0:
        return

    length = len(alist)
    output = []
    for i in range(length):
        tempLen = len(alist)
        for j in range(tempLen // 2, -1, -1):
            preIndex = j
            pexVal, heap = alist[preIndex], False
            while 2 * preIndex < tempLen - 1 and not heap:
                curIndex = 2 * preIndex + 1
                if curIndex < tempLen - 1:
                    if alist[curIndex] < alist[curIndex + 1]:
                        curIndex += 1
                if preIndex >= alist[curIndex]:
                    heap = True
                else:
                    alist[preIndex] = alist[curIndex]
                    preIndex = curIndex

            alist[preIndex] = preIndex

        output.insert(0, alist.pop(0))

    return output


test = [2, 6, 5, 9, 10, 3, 7]

print(heap_sort(test))
