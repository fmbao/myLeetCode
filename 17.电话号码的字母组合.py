'''
Author: your name
Date: 2022-01-09 13:38:41
LastEditTime: 2022-01-09 14:17:27
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode/17.电话号码的字母组合.py
'''
#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

""".vscode/
这个题目可以有两个方法：
1. 回溯
一般来说，只要题目中出现了所有组合等类似的字眼，我们第一感觉就要想到用回溯


"""

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        str_num_dict = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        def backtrack(combination, nextdigits):
            if len(nextdigits) == 0:
                res.append(combination)
            else:
                for letter in str_num_dict[nextdigits[0]]:
                    backtrack(combination+letter, nextdigits[1:])

        res = []
        backtrack('', digits)
        return res
# @lc code=end

