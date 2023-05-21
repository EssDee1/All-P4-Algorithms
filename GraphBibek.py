graph = {

}

def addVertex(vertex):
    if vertex not in graph:
        graph[vertex] = []

def addEdge(vertex, edge, weightedVal):
    if vertex in graph:
        val = len(graph[vertex])
        if val != 0:
            for i in graph[vertex]:
                if i[0] == edge:
                    print(f'Edge {edge} already exists.')
        graph[vertex].append([edge, weightedVal])

        

addVertex('A')
addVertex('B')
addVertex('C')
addVertex('D')
addEdge('A', "B", 5)
addEdge('A', "C", 5)
addEdge('B', "C", 3)
addEdge('B', "A", 3)
addEdge('C', "A", 3)
addEdge('C', "D", 3)
print(graph)

def findPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if (start not in graph) or (end not in graph):
        print(f"Vertex {start} does not exist.")
        return None
    for i in graph[start]:
        if i[0] == end:
            path = path + [end]
            return path
        for k in graph[i[0]]:
            print(k)
            if k[0] == end:
                path = path + [i[0]] + [end]
                return path
            
print(findPath(graph, "B", "A"))
