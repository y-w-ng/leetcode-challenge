class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0 or len(prerequisites) == 0:
            return list(range(numCourses))
        
        graph = {}
        for f, t in prerequisites:
            if f in graph:
                graph[f] += [t]
            else:
                graph[f] = [t]
                
        stack = []
        # visited = set()
        visited = [0] * numCourses
        def _traverse(i):
            # i: course index
            # if i not in visited:
            
            if visited[i] == 0:
                # visited.add(i)
                visited[i] = 1
                if i not in graph:
                    
                    stack.append(i)
                    visited[i] = -1
                    return visited[i]
                for c in graph[i]:
                    
                    state = _traverse(c)
                    if state > 0:
                        return visited[i]
                
                # if all([c in stack for c in graph[i]]):
                #     stack.append(i)
                stack.append(i)
                visited[i] = -1
            return  visited[i]


        
        for i in range(numCourses):
            if visited[i] == 0:
                _traverse(i)

        if len(stack) == numCourses:
            return stack
        else:
            return []
        