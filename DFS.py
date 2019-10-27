class Node:
        def __init__(self,name):
            self.name = name
            self.adj = []
            self.visited = False
class Dfs:
    def dfs(self,node):
        node.visited =True
        print("%s" %node.name)
        for n in node.adj:
            if not n.visited:
                self.dfs(n)

Node1 = Node("A")
Node2 = Node("B")
Node3 = Node("C")

Node1.adj.append(Node2)
Node2.adj.append(Node3)
dfs = Dfs()
dfs.dfs(Node1)
