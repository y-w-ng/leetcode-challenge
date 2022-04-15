class Solution:
    """https://leetcode.com/problems/all-paths-from-source-to-target/"""
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        if len(graph) <= 1:
            return graph
        edges = {}
        for i, nodes in enumerate(graph):
            edges[i] = nodes
            
        stack = [(0, [0])]
        result = []
        while len(stack) > 0:
            node, paths = stack.pop(0)
            
            if node == len(graph) -1:
                result.append(paths)
            
            next_nodes = edges[node]
            for n in next_nodes:
                stack.append((n, paths + [n]))
            
        return result
    # TODO: recursive
