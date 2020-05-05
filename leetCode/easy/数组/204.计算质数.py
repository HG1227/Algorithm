# -*- encoding: utf-8 -*-
"""
@software: PyCharm
@file : 204.计算质数.py
@time : 2020/5/5 
"""
'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''
# 要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数
class Solution:
    def countPrimes(self, n: int) -> int:
        # 最小的质数是 2
        if n < 2: return 0

        is_primes = [1] * n
        is_primes[0] = is_primes[1] = 0 # 0和1不是质数，先排除掉
        for i in range(2,int(n**0.5)+1):
            if is_primes[i]:
                is_primes[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(is_primes)

if __name__ == '__main__':
    pass