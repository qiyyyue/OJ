
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        use_dict = {}

        def make_clone_graph(org_node):
            if not org_node:
                return

            new_node = Node(org_node.val, [])
            use_dict[org_node] = new_node
            for node in org_node.neighbors:
                if node not in use_dict:
                    new_node.neighbors.append(make_clone_graph(node))
                else:
                    new_node.neighbors.append(use_dict[node])
            return new_node

        return make_clone_graph(node)