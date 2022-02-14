# @before-stub-for-debug-begin
from python3problem38 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        pre = '1'
        for i in range(n-1):
            cur = ""
            pos = 0
            start = 0
            while pos < len(pre):
                while pos < len(pre) and pre[pos] == pre[start]:
                    pos = pos + 1
                cur += str(pos - start) + pre[start]
                start = pos
            pre = cur
        return pre



# @lc code=end

