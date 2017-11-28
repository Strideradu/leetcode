# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        clones = {}
        queue = collections.deque([])
        if node is None:
            return None
        clone = UndirectedGraphNode(node.label)
        clones[node.label] = clone
        queue.append(node)
        visited = set()
        while(queue):
            cur = queue.popleft()
            if not cur.label in visited:
                cur_clone = clones[cur.label]
                visited.add(cur.label)
                for neighbor in cur.neighbors:
                    if clones.get(neighbor.label, False) is False:
                        new_node = UndirectedGraphNode(neighbor.label)
                        clones[neighbor.label] = new_node
                    queue.append(neighbor)
                    cur_clone.neighbors.append(clones[neighbor.label])

        return clone
