
#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        for single_data in intervals[1:]:
            if single_data[0] > end:
                 result.append([start,end])
                 start = single_data[0]
            end = max(end,single_data[1])  # 关键
        result.append([start,end])   # 关键
        return result



# @lc code=end

