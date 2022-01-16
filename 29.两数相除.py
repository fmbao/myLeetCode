'''
Author: baochenchen
Date: 2022-01-16 01:00:07
LastEditTime: 2022-01-16 09:45:40
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode/29.两数相除.py
'''
#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        FLAG = 1
        if dividend < 0 : FLAG, dividend = -FLAG , -dividend
        if divisor < 0 : FLAG, divisor = -FLAG , -divisor

        def div(dividend, divisor):
            if dividend < divisor :return 0
            currentNum = divisor
            multiple = 1
            while currentNum + currentNum < dividend :
                currentNum += currentNum
                multiple += multiple
            return multiple + div(dividend - currentNum, divisor)

        res = div(dividend, divisor)
        res = res if FLAG > 0 else -res
        if res < INT_MIN :return INT_MIN
        elif INT_MIN <= res <= INT_MAX :return res
        else:return INT_MAX





















# @lc code=end

