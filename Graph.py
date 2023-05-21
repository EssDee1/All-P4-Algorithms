class Graph:
    def __init__(self):
        self.GraphList = {}

    def AddVertex(self, v):
        if v in self.GraphList:
            print("Vertex Already Exists")

        else:
            self.GraphList[v] = {}
            print("Added")

    def AddEdge(self, v1, v2, weight):
        if v1 in self.GraphList and v2 in self.GraphList[v1]:
                print("Edge Already Exists")

        else:
            self.GraphList[v1][v2] = weight
            self.GraphList[v2][v1] = weight

    def Display(self):
        print(self.GraphList)
  

ThisGraph = Graph()
ThisGraph.AddVertex('A')
ThisGraph.AddVertex('B')
ThisGraph.AddVertex('C')
ThisGraph.AddVertex('D')

ThisGraph.Display()

ThisGraph.AddEdge('A','B', 2)
ThisGraph.AddEdge('A','B', 2)
ThisGraph.AddEdge('B','C', 4)
ThisGraph.AddEdge('C', 'D', 3)

ThisGraph.Display()
