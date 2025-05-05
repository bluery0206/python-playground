"""
Discrete Strcutures 1

Author: Mark Ryan Hilario | bluery0206    
Date: April 2, 2025

Not an activity but I did anyways

Just tryna practice by doing some old activities

Implementing Minimum Spanning Tree

"""

class Node:
    """ Class for nodes """

    def __init__(self, name:str|int) -> None: 
        self.name:str = name
        self.neighbors: list = []

    def __gt__(self, node:object) -> bool:
        """ gets called when we node > node """
        return self.name > node.name
    
    def __repr__(self):
        return f"{self.name}"


class Edge:
    """ Edge"""

    def __init__(self, nodes: Node, weight: int) -> None:
        self.nodes = nodes
        self.weight: int = weight

    def __str__(self):
        return f"Edge{self.nodes}, weight:{self.weight}"

    def __lt__(self, node:Node) -> bool:
        return self.weight < node.weight


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

edges = [
    [(a, b), 1],
    [(a, f), 5],
    [(b, a), 1],
    [(b, c), 8],
    [(b, d), 4],
    [(b, f), 5],
    [(c, b), 8],
    [(c, d), 2],
    [(c, f), 3],
    [(d, b), 4],
    [(d, c), 2],
    [(d, e), 10],
    [(d, f), 1],
    [(e, d), 10],
    [(e, f), 4],
    [(f, a), 5],
    [(f, b), 5],
    [(f, c), 3],
    [(f, d), 1],
    [(f, e), 4],
]

# Create them instance of edge
for idx, edge in enumerate(edges):
    edges[idx] = Edge(*edge)

print()
edges.sort()


for edge in edges:
    print(edge)

sorted_list = edges.copy()
connected_edges = []

print()

for idk in sorted_list:
    node_a, node_b = idk.nodes

    

# class DFS:
#     def __init__(self, nodes: list[Node]) -> None:
#         self.nodes: list[Node] = nodes

#     def traverse(self, starting_node_idx: Node, end_node: Node | None = None) -> list[Node]:
#         print("Initializing traverse session...")

#         if starting_node_idx > len(self.nodes):
#             print(f"Invalid starting node index (Number of nodes in the list: {len(self.nodes)}).")

#         unvisited = self.nodes.copy()
#         node = self.nodes[starting_node_idx] # Current node
#         stack = []
#         visited = []

#         print("Traversing...")
#         while unvisited:
#             print(f"Exploring node {node}...")
#             node.neighbors.sort() # To organize from the first alphabet to the last or small to large number

#             if node not in stack:
#                 print(f"{node} added to the stack.")
#                 stack.append(node)
            
#             if node not in visited:
#                 print(f"{node} added to the visited nodes list.")
#                 visited.append(node)

#             if node in unvisited:
#                 print(f"{node} removed from the unvisited nodes list.")
#                 unvisited.remove(node)

#             print(f"{node=}, {node.neighbors=}, {stack=}, {unvisited=}, {visited=}")

#             print(f"Checking {node.name} neighbors...")
#             for neighbor in node.neighbors:
#                 if neighbor in unvisited:
#                     print(f"Neighbor {neighbor.name} IS available. Switching...")
#                     node = neighbor
#                     break
#                 elif neighbor in visited and neighbor == node.neighbors[-1]:
#                     print(f"All neighbors of Node {node.name} are visited.")
#                     print(f"Removing node {node.name} from the stack...")
#                     stack.pop()
#                     print(f"Switching to node {stack[-1].name}")
#                     node = stack[-1]
#                     break
#                 else:
#                     print(f"Neighbor {neighbor.name} IS NOT available. Skipping...")

#         print(f"Exploration done. Starting Node: {self.nodes[starting_node_idx].name}, path: {visited}")

#         return visited


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")

# a.add_neighbor(b)
# a.add_neighbor(g)
# a.add_neighbor(d)

# b.add_neighbor(e)
# b.add_neighbor(a)
# b.add_neighbor(f)

# c.add_neighbor(h)
# c.add_neighbor(f)

# d.add_neighbor(a)
# d.add_neighbor(f)

# e.add_neighbor(b)
# e.add_neighbor(g)

# f.add_neighbor(d)
# f.add_neighbor(c)
# f.add_neighbor(b)

# g.add_neighbor(a)
# g.add_neighbor(e)

# h.add_neighbor(c)

# dfs = DFS([a, b, c, d, e, f, g, h])
# dfs.traverse(starting_node_idx=0)
# print(dfs.nodes)