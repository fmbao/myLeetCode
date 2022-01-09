'''
Author: your name
Date: 2022-01-09 12:52:53
LastEditTime: 2022-01-09 13:36:40
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode/16.最接近的三数之和.py
'''
#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

""".vscode/
1. 先对数组进行排序，时间复杂度是O(nlogn)
2.  在数组nums中，进行遍历，每次遍历一个值利用其下标i，形成一个固定值nums[i]
3. 再次使用前指针指向start=i+1 处，后指针指向end = nums.length - 1处，也就是结尾处
4. 根据sum = nums[i] + nums[L] + nums[R]的结果，判断sum的结果和 目标的结果的距离，如果距离更近就更新最终的结果ans
5. 同时判断sum和目标的大小关系，因为数组有序，如果sum > target 就 R-- 如果sum < target 就 L++。如果sum==target 就说明距离是0 就直接返回结果
6. 整个遍历的过程： 固定值为n次，双指针为n次 时间复杂度为O(n2)
7. 总的时间复杂度 O(nlogn) + O(n2) = O(n2)

"""

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        if nums == None or n < 3:
            return nums.sum()
        ans = nums[0]+nums[1]+nums[2]

        for i in range(n):
            L = i+1
            R=n-1
            while L < R:
                sum = nums[L] + nums[i] + nums[R]
                if abs((sum - target)) < abs((target - ans)):
                    ans = sum
                if sum > target:
                    R -=1
                elif sum < target:
                    L +=1
                else:
                    return ans
        return ans

# @lc code=end

