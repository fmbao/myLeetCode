
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
        Meslo LG M for Powerline,JetBrains Mono,monospace
        "leetcode"
        ["leet","code"]
        """
        res = list()
        path = list()
        def traceBack(path,start):
            if start == len(s):
                res.append("".join(path))
            for word in wordDict:
                if s[start:start + len(word)] != word:
                    continue
                path.append(word)
                traceBack(path,start+len(word))
                path.pop()
        traceBack(path,0)
        return s in res
# @lc code=end

