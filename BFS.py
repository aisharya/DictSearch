class Node:
    def __init__(self,name):
        self.name = name
        self.adjacent = []
        self.visited = False
        self.pred = None
class Bfs:
    def bfs(self,startNode):
        queque = []
        queque.append(startNode)
        startNode.visited = True
        while queque:
            actualNode = queque.pop(0)
            print("%s" %actualNode.name)
            for n in actualNode.adjacent:                        
                if not n.visited:                                     
                    n.visited = True
                    queque.append(n)
                
                
Node1 = Node("A")
Node2 = Node("B")
Node3 = Node("C")
Node4 = Node("D")
Node5 = Node("E")

Node1.adjacent.append(Node2)
Node2.adjacent.append(Node3)
Node3.adjacent.append(Node4)
Node4.adjacent.append(Node5)

bfs = Bfs()
bfs.bfs(Node1)
