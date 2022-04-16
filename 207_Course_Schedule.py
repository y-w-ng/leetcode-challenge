class Solution:
    """https://leetcode.com/problems/course-schedule/"""
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0 or len(prerequisites) == 0:
            return True
        
        edges = {}
        for t, f in prerequisites:
            if f in edges:
                edges[f] += [t]
            else:
                edges[f] = [t]
        
        visited = [0] * numCourses
        stack = []
        def _traverse(n):
            if visited[n] == 0:
                visited[n] = 1
                
                if n not in edges:
                    stack.append(n)
                    return
                
                for c in edges[n]:
                    if visited[c] == 0:
                        _traverse(c)
                if all([c in stack for c in edges[n]]):
                    stack.append(n)
            return
        
        while sum(visited) < numCourses:
            
            for i in range(numCourses):
                if visited[i] == 0:
                    _traverse(i)
        
        return len(stack) == numCourses
