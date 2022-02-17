
#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, path, leftTarget):
            if leftTarget ==0:
                final_res.append(path[:])
                return

            for i in range(index, len(candidates)):
                if leftTarget - candidates[i] < 0:
                    break
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])  # 这个地方比较容易出错，核心的也就是下面三段代码，主要是path中元素的更新
                dfs(i+1, path , leftTarget - candidates[i])
                path.pop()

        candidates.sort()
        final_res = []
        dfs(0, [], target)
        return final_res

# @lc code=end

