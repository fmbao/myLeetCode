
# @before-stub-for-debug-begin
from python3problem215 import *
from typing import *
# @before-stub-for-debug-end



#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## 不是最高效的方法
        # nums.sort()
        # return nums[-k]
        ## 采用快排实现的算法思路(准确来说不是快排，一般叫做快速选择算法)
        def partition(nums:List[int], low:int, high:int):
            ## 快排的核心函数
            ## 根本目的是找出一个数使得这个数字左边的所有数值都比这个数值小
            ## 右边这个数值都比这个数值大
            if low == high:
                return low
            res = nums[low]
            i = low
            j = high + 1
            while True:
                i +=1
                while nums[i] < res:
                    if i == high:
                        break
                    i += 1

                j -= 1
                while nums[j] > res:
                    if j == low:
                        break
                    j -= 1

                if i >= j:
                    break
                swap(nums,i,j)
            swap(nums, j, low)
            return j

        def swap(nums:List[int], i:int, j:int):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp



        low = 0
        high = len(nums) -1
        k = len(nums) - k
        while low <= high:
            p = partition(nums, low, high)
            if p< k:
                low = p+1
            elif p>k:
                high = p-1
            else:
                return nums[p]

        return -1

        ##还有一种最小堆的解法
        # import heapq as h
        # heap = []
        # for num in nums:
        #     if len(heap) < k:
        #         h.heappush(heap, num)
        #     else:
        #         if num > heap[0]:
        #             h.heappop(heap)
        #             h.heappush(heap, num)
        #     return h.heappop(heap)



# @lc code=end

