# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        single_path = []
        ss = []
        used = [False for _ in range(len(nums))]
        # 采用回溯的方式 进行解决
        def permute_core():
            if len(single_path) == len(nums):

                result.append(single_path[:]) # single_path[:] 和single_path 差异巨大 因为a[:]是深拷贝
                print("single_path[] ",single_path)
                print("single_path[:] ",single_path[:])
                print("result: ", result)
            for i in range(len(nums)):
                if used[i] == True :
                    continue
                single_path.append(nums[i])
                used[i] = True
                permute_core()
                single_path.pop()
                used[i] = False
        permute_core()
        print("final result ",result)
        return result


# @lc code=end

