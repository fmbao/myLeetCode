'''
Author: your name
Date: 2022-01-09 14:25:35
LastEditTime: 2022-01-15 17:32:16
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode/18.四数之和.py
'''
#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
""".vscode/
使用 四个指针(a<b<c<d) ,固定最小的a 和 b 在左边 c = b+1 d = size-1 移动两个指针包夹求解
保存使得nums[a]+nums[b]+nums[c]+nums[d] ==  target 的解，偏大时 d左移 偏小时c右移动
c 和 d相遇的时候，表示以当前a和b为最小值的解已经全部求得，b++ 进入下一步 b循环，当b循环结束之后
a++ 进入下一步a循环，也就是a在最外面循环，里面嵌套b 循环，再嵌套双指针c和d进行包夹求解



"""

"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        def Search(i, target, oneSolution):

            if target == 0 and len(oneSolution) == 4:  # 出口，找到正确的解了
                output.append(oneSolution)
                return
            elif len(oneSolution) > 4 or i >= len(nums):  # 剪枝，超范围了
                return

            if target - nums[i] - (3 - len(oneSolution)) * nums[-1] > 0:  # 当前这个数太小了
                Search(i + 1, target, oneSolution)
            elif target - (4 - len(oneSolution)) * nums[i] < 0:  # 当前组数的和太大了
                return
            else:  # 当前组数似乎没毛病
                Search(i + 1, target, oneSolution)  # 不选这个数
                Search(i + 1, target - nums[i], oneSolution + [nums[i]])  # 选这个数

        Search(0, target, [])

        output1 = []
        output2 = []
        for t in output:
            if set(t) not in output1:
                output1.append(set(t))
                output2.append(t)

        return output2

作者：flying_du
链接：https://leetcode-cn.com/problems/4sum/solution/python-wo-jiu-bu-yong-zhi-zhen-fa-zha-di-quan-guo-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        class Solution:
      def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplet = list()
        if not nums or len(nums) < 4:
            return quadruplet
        nums.sort()
        length = len(nums)
        ## 定义4个指针 i，j，left，right  i从0开始遍历，j从i+1开始遍历，留下 left和right作为双指针
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]: #当i 的值和前面的值相等 就忽略
                continue
            # 获取当前最小值 如果最小值比目标值大 就说明后面越来远大的值根本没戏
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3]> target:
                break
            # 获取当前最大值 如果最大值比目标值小 说明后面越来越小 根本没戏 忽略
            if nums[i] + nums[length -3 ] + nums[length - 2] + nums[length -1] < target:
                continue # 这里使用continue 继续进行下一次的循环  因为下一次循环会有更大的数字
            # 第二层循环 j 初始值 指向i+1
            for j in range(i+1,length - 2):
                if j > i + 1 and nums[j] == nums[j-1]: # 当j的值和前面的值相等就忽略
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] >target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] <target:
                    continue
                left ,right = j+1, length -1
                # 双指针遍历 如果等于目标值 left++ 并去重 right-- 并去重 当当前 和大于 目标值时right--
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplet.append([nums[i] ,nums[j] ,nums[left] , nums[right]])
                        left +=1 # left先+1然后和他之前的left-1 进行比较 如果之后+1 就和后面的left进行+1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        right -=1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return quadruplet









# @lc code=end

