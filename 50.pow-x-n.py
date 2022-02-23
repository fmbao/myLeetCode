
#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 采用递归的方式进行求解
        # 需要注意的是两点： 1. n = 0 2. n< 0
        def powCore(N):
            if N == 0 :
                return 1.0
            y = powCore(N//2)
            return y*y if N %2 ==0 else y*y *x # 核心要点
        return powCore(n) if n >=0 else 1.0/powCore(-n) # 核心要点





# @lc code=end

