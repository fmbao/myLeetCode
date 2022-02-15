
#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        final_result = []
        data_len = len(candidates)
        def dfs(idx, res, t):
            if t == 0:
                final_result.append(res[:])
                return
            if t <0:
                return
            for i in range(idx, data_len):
                res.append(candidates[i])
                dfs(i, res, t- candidates[i])
                res.pop()
        dfs(0, [], target)  # 如果为 dfs(0, final_result, target) 将导致错误
        return final_result


# @lc code=end

