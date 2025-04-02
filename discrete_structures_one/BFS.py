"""
Discrete Strcutures 1

Author: Mark Ryan Hilario | bluery0206    
Date: April 2, 2025

Not an activity but I did anyways

Just tryna practice by doing some old activities

Implementing Depth First Search

It is a graph traversal algorithm that explores the graph in a deathwards motion using a
stack. It follows these rules:
    visit unvisited adjacent vertex/node
    mark as visited
    display
    and push in the stack
    if no adjacent vertex. pop vertex from stack
    repeat    
"""

class Node:
    """ Class for nodes """

    def __init__(self, name:str|int) -> None: 
        self.name:str = name
        self.neighbors:list = []

    def add_neighbor(self, neighbor:object) -> None:
        """ Method to add neighbor """
        self.neighbors.append(neighbor)

    def __str__(self) -> str:
        """ get called when, eg var = Node(); print(var) """
        return f"{self.name}({self.neighbors=})"

    def __repr__(self) -> str:
        """
            get called when, eg var = Node(); print(var)
            but unlike __str__, 
        """
        return str(self.name)

    def __gt__(self, node:object) -> bool:
        """ gets called when we node > node """
        return self.name > node.name
    

class BFS:
    def __init__(self, nodes: list[Node]) -> None:
        self.nodes: list[Node] = nodes

    def traverse(self, starting_node_idx: Node, end_node: Node | None = None) -> list[Node]:
        print("Initializing traverse session...")

        if starting_node_idx > len(self.nodes):
            print(f"Invalid starting node index (Number of nodes in the list: {len(self.nodes)}).")

        unvisited = self.nodes.copy()
        node = self.nodes[starting_node_idx] # Current node
        stack = []
        visited = []

        print("Traversing...")
        while unvisited:
            print(f"Exploring node {node}...")
            node.neighbors.sort() # To organize from the first alphabet to the last or small to large number

            if node not in stack:
                print(f"{node} added to the stack.")
                stack.append(node)
            
            if node not in visited:
                print(f"{node} added to the visited nodes list.")
                visited.append(node)

            if node in unvisited:
                print(f"{node} removed from the unvisited nodes list.")
                unvisited.remove(node)

            print(f"{node=}, {node.neighbors=}, {stack=}, {unvisited=}, {visited=}")

            print(f"Checking {node.name} neighbors...")
            for neighbor in node.neighbors:
                if neighbor in unvisited:
                    print(f"Neighbor {neighbor.name} IS available. Switching...")
                    node = neighbor
                    break
                elif neighbor in visited and neighbor == node.neighbors[-1]:
                    print(f"All neighbors of Node {node.name} are visited.")
                    print(f"Removing node {node.name} from the stack...")
                    stack.pop()
                    print(f"Switching to node {stack[-1].name}")
                    node = stack[-1]
                    break
                else:
                    print(f"Neighbor {neighbor.name} IS NOT available. Skipping...")

        print(f"Exploration done. Starting Node: {self.nodes[starting_node_idx].name}, path: {visited}")

        return visited


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.add_neighbor(b)
a.add_neighbor(g)
a.add_neighbor(d)

b.add_neighbor(e)
b.add_neighbor(a)
b.add_neighbor(f)

c.add_neighbor(h)
c.add_neighbor(f)

d.add_neighbor(a)
d.add_neighbor(f)

e.add_neighbor(b)
e.add_neighbor(g)

f.add_neighbor(d)
f.add_neighbor(c)
f.add_neighbor(b)

g.add_neighbor(a)
g.add_neighbor(e)

h.add_neighbor(c)

bfs = BFS([a, b, c, d, e, f, g, h])
bfs.traverse(starting_node_idx=0)
print(bfs.nodes)