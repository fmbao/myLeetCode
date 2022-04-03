# @before-stub-for-debug-begin
from python3problem394 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        ### 采用先进先出的 队列形式进行处理
        """102.二叉树的层序遍历.py
        输入：s = "3[a]2[bc]"
        输出："aaabcbc"
        之前自己实现 的代码总是有点问题 现在看别人的代码实现一下
        """
        stack =[]
        res =""
        num = 0
        for c in s:
            if c.isdigit():
                num = num*10+int(c)
            elif c=='[':
                stack.append((res,num))
                res,num='',0
            elif c==']':
                top = stack.pop()
                res = top[0] + top[1]*res
            else:
                res += c
        return res



        # def convert_alphabet(single_str):
        #     res = None
        #     flag = 0
        #     if 0 <= ord(single_str) - ord('0') <= 10:
        #         res = ord(single_str) - ord('0')
        #         flag = 0
        #     elif 0 <= ord(single_str) - ord('a') <= 26 or single_str == '[' or single_str == ']':
        #         res = single_str
        #         flag = 1
        #     else:
        #         print("invalid ele {}".format(single_str))
        #     return res,flag
        # import collections
        # num_queue = collections.deque()
        # alphabet_queue = collections.deque()
        # for i in range(len(s)):
        #     single_ele,flag = convert_alphabet(s[i])
        #     if flag == 0: # num_queue
        #         num_queue.append(single_ele)
        #     elif flag == 1: # alphabet
        #         alphabet_queue.append(single_ele)
        #     else: # []
        #         continue
        # res = ''

        # while len(alphabet_queue)>0:
        #     full_alphabet = ''
        #     alphabet  = alphabet_queue.pop()

        #     # while alphabet != '[' or alphabet != ']':
        #     if alphabet == ']':
        #         # alphabet  = alphabet_queue.pop()
        #         # if alphabet == ']':
        #         continue
        #         # else:
        #     while alphabet != '[':
        #         full_alphabet += alphabet
        #         alphabet  = alphabet_queue.pop()
        #     # full_alphabet[::-1]
        #     repeat_num = num_queue.pop()
        #     for i in range(repeat_num):
        #         res += full_alphabet
        #     # print("ss")
        #     # res += full_alphabet
        # return res[::-1]


# @lc code=end

