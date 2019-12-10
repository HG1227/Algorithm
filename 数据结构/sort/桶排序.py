#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 桶排序.py
# @time: 2019/12/10


def insert_sort(nums, order=1):
    # 第一个数不动，从第二个数开始比较
    for i in range(1, len(nums)):
        j = i - 1
        tmp = nums[i]  # 记录本次待比较的词语
        while j >= 0:
            if tmp < nums[j]:
                nums[j + 1] = nums[j]
                nums[j] = tmp
                j = j - 1
            else:
                break
    if order == 1:
        return nums
    else:
        return nums[::-1]


def bucket_sort(nums, n, order=1):
    max_num = max(nums)
    min_num = min(nums)
    step = (max_num + 0.1 - min_num) / int(n)
    # print(step)
    tong = [[] for _ in range(n)]
    for i in range(len(nums)):
        # int((nums[i] - min_num) / step)  第几个桶
        tong[int((nums[i] - min_num) / step)].append(nums[i])
    result = []
    print(tong)
    for k in range(n):
        tong[k] = insert_sort(tong[k])
        result = result + tong[k]
    if order == 1:
        return result
    else:
        return result[::-1]


nums = [50, 100, 10, 8, 9, 5, 6, 7, 18, 13, 6.5, 10.1, 10.2, 100.3]
print(bucket_sort(nums, 5))
print(bucket_sort(nums, 5, 0))
