
#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:
    """前缀树 遍历
    时间复杂度 初始化为 O(1) 其余操作为O(s) 其中S是每次插入或者插叙的字符串的长度
    空间复杂度是O（T）
    """


    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, word):
        node = self
        for w in word:
            ch = ord(w) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node



    def insert(self, word: str) -> None:
        node = self
        for w in word:
            ch = ord(w) - ord("a")
            if node.children[ch] is None:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

