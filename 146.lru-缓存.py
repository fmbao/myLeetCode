
#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start

class DlinkNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        # self.capacity = capacity
        self.head = DlinkNode(0,0)
        self.tail = DlinkNode(0,0)

        ## 出错的地方
        self.head.next = self.tail
        self.tail.prev = self.head
        ## 出错的地方 需要明确size和 capacity 不一样的地方
        self.size = 0
        self.capacity = capacity



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        ## 如果 想要获取的节点在 cache中 就将这个节点放置到最前面
        node = self.cache[key]
        self.moveToHead(node)
        ## 出错的地方，需要明确的是 node 和value不一样的地方
        return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DlinkNode(key,value)
            self.cache[key] = node
            ## 出错的地方 如果新加入一个新的节点就放置在整个链表的最前面
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                ## 出错地方  如果size大于 capacity 需要将尾部的节点去掉 同时将其从cache中去掉
                removed = self.removeTail()
                ## 删除cache对应的节点
                self.cache.pop(removed.key)
                self.size -=1
        else:
            ## 如果key 存在 就先通过哈希表定位 在修改 value 并移动到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)


    def removeNode(self,node:DlinkNode):
        node.prev.next = node.next

        node.next.prev = node.prev

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def addToHead(self, node: DlinkNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


    def moveToHead(self,node: DlinkNode):
        self.removeNode(node)
        self.addToHead(node)





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

