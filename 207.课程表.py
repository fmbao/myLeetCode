# @before-stub-for-debug-begin
from python3problem207 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hasCycle = False
        visited = [False for _ in range(numCourses)]
        onPath = [False for _ in range(numCourses)]

        def buildGraph(numCourses, prerequisites):
            graph = defaultdict(list)
            for prerequisite in prerequisites:
                graph[prerequisite[1]].append(prerequisite[0])
            return graph
        def traverse(graph,startIdx):
            nonlocal hasCycle
            if onPath[startIdx]:
                hasCycle = True
            if visited[startIdx] or hasCycle:
                return
            visited[startIdx] = True
            onPath[startIdx] = True
            for i in graph[startIdx]:
                traverse(graph,i)
            onPath[startIdx]=False


        graph = buildGraph(numCourses, prerequisites)
        for i in range(numCourses):
            traverse(graph, i)
        return not hasCycle









# @lc code=end

