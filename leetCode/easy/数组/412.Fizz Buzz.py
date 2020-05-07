# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 412.Fizz Buzz.py
@time : 2020/5/7 
"""
"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                res.append("FizzBuzz")
            elif i%3==0:
                res.append("Fizz")
            elif i%5==0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res

class Solution2(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or str(i) for i in range(1, n + 1)]

if __name__ == '__main__':
    pass