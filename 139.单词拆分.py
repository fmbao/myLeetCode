# @before-stub-for-debug-begin
from python3problem139 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        "leetcode"
        ["leet","code"]
        """
        from itertools import permutation
        idx_range = list(range(len(wordDict)))
        all_index =list(permutation(idx_range))

        for index in all_index:
            new_wordDict = sorted(wordDict, key=)
            for singleWord in wordDict:
                if singleWord in s:
                    s = ''.join(s.split(singleWord))
        if s is '':
            return True
        else:
            return False
# @lc code=end

