# @before-stub-for-debug-begin
from python3problem57 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for idx,inter in enumerate(intervals):
            if inter[1] < newInterval[0]:
               ans.append(inter)
            elif newInterval[1] < inter[0]:
                ans.append(newInterval)
                ans.extend(intervals[idx:]) # 关键，不然会导致多加一层的问题
                break
            else:
                if inter[0]< newInterval[0]:
                    newInterval[0] = inter[0]
                if inter[1]> newInterval[1]:
                    newInterval[1] = inter[1]
        else:
            ans.append(newInterval)
        return ans




# @lc code=end

