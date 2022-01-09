'''
Author: your name
Date: 2022-01-09 11:52:58
LastEditTime: 2022-01-09 12:51:58
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode/15.三数之和.py
'''
#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start

""".vscode/
1. 特殊的情况判断，长度小于3 或者 数组为null，直接返回[]
2. 对数组进行排序
3. 遍历排序之后的数组
    3.1 如果num[i]>0 因为已经排序好了，所以后面不可能三个数相加等于0，直接返回结果
    3.2 对于重复元素，跳过，避免重复解
    3.3 对于左边的指针L=i+1,右边的指针，L=n-1 ,当L<R时，执行循环判断
        3.3.1 当nums[i]+nums[L]+nums[R]==0 执行循环，判断左边界和右边界是否和下一位置重复
        去除重复解，并将L，R移动到下一个位置，寻找新的解
        3.3.2 如果和大于0， 说明nums[R]太大，R左移动
        3.3.3 如果和小于0 说明nums[L]太小，L右移动


"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        if n<3 or nums==None:
            return []
        nums.sort()
        for i in range(n):
            if nums[i]>0:
                return res
            if i>0 and nums[i-1]==nums[i]:
                continue
            L = i+1
            R = n-1
            while L < R:
                if nums[i] + nums[L] + nums[R] ==0:
                    res.append([nums[i],nums[L],nums[R]])
                    while L< R and nums[L] ==nums[L+1]:
                        L = L+1
                    while L< R and nums[R] ==nums[R-1]:
                        R = R - 1

                    L = L + 1
                    R = R - 1

                elif nums[i]+nums[L]+nums[R] > 0:
                    R = R - 1
                else:
                    L = L + 1
        return res








# @lc code=end

