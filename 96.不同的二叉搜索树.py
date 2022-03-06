
#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        memory = [[0]* (n+1) for _ in range(n+1)]

        def count(low,high):
            if low > high:
                return 1
            if memory[low][high] != 0:
                return memory[low][high]
            res = 0
            for i in range(low,high+1):
                left = count(low, i-1)
                right = count(i+1, high)
                res += left * right
            memory[low][high] = res
            return res
        return count(1,n)
# @lc code=end

