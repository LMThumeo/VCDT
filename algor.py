import math
import sys

class Node:
    x = 0
    y = 0
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]

    def show(self):
        print("x is", self.x )
        print("y is", self.y )
  
    def distance(self, node):
    # Convert to natural number        
        return math.sqrt((node.x - self.x)**2 + (node.y - self.y)**2)
  
    def is_self(self, node):
        return node.x == self.x and node.y == self.y


class Graph:
    nodes = []
    edges = {}

    def __init__(self, nodes):
        self.nodes = nodes
        self.initialize_edges()

    def initialize_edges(self):
        for i, nodeI in enumerate(self.nodes):
            self.edges[i] = []
            for j, nodeJ in enumerate(self.nodes):
                if nodeJ.is_self(nodeI):
                    continue
                if nodeJ.x == nodeI.x + 1 or nodeJ.x == nodeI.x - 1 or (nodeJ.x == nodeI.x and nodeJ.y != nodeI.y):
                    self.edges[i].append([j, nodeJ.distance(nodeI)])

    def minDistance (self, distance, sptSet):
        min = sys.maxsize
        for index, node in enumerate(self.nodes):
            if distance[index] <= min  and sptSet[index] == False:
                min = distance[index]
                minIndex = index
        return minIndex            
  
    def shortest_path(self, nodeA: Node):

        distance = [sys.maxsize] * len(self.nodes)
        distance[0] = 0 #nodeA
        
        pre = ["NA"] * len(self.nodes)
        pre[0] = -1
        
        # for i, node in enumerate(self.nodes):
        #     if not node.is_self(nodeA):
        #         distance[i] = sys.maxsize

        sptSet = [False] * len(self.nodes)

        for node in enumerate(self.nodes):
            u = self.minDistance(distance, sptSet)
            sptSet[u] = True
            for v, nodeV in enumerate(self.nodes):
                if sptSet[v] == False:
                    distUV = sys.maxsize
                    for adj in self.edges[v]:
                        if adj[0] == u:
                            distUV = adj[1]
                            break
                    if distance[v] > distance[u] + distUV:
                        distance[v] = distance[u] + distUV
                        pre[v] = u
        #trace path to find next step
        trace = []              
        u = 1
        while(u != -1):
            trace.append(u)
            u = pre[u]
        # print (trace)   
        return trace[len(trace)-2]

def findNext(permannentPoint, pointList):

    des = permannentPoint[0]
    prePoint = permannentPoint[len(permannentPoint)-1]

    if des == prePoint:
        return permannentPoint, pointList

    pointList =[prePoint, des, *pointList]
    nodeList = []
    for p in pointList:
        node = Node(p)
        nodeList.append(node)
    g = Graph(nodeList)
    index = g.shortest_path(Node(prePoint))
    nextPoint = pointList[index]
    permannentPoint = [*permannentPoint, nextPoint]
    pointList.remove(nextPoint)
    return permannentPoint, pointList[2:]    


# per = [[5, 3], [1, 7]]
# point = [[2, 7], [2, 3], [3, 2], [4, 3], [2, 6]]
# a, b = findNext(per, point)
# print (a)
# print(b)
#[ [1, 7], [5, 3], [2, 7], [2, 3], [3, 2], [4, 3], [2, 6]]
#  0         1       2       3       4       5       6

# permannentPoint = [[5,7], [2,6], [1, 1]]
# pointList = [[1,2],  [3, 6], [4, 10], [2, 5], [1, 10],[1,5], [2, 7], [1,3], [2,4]]
# a, b = findNext(permannentPoint, pointList)
# print (a)
# print(b)

# [[1, 1], [5, 7], [1,2],  [3, 6], [4, 10], [2, 5], [1, 10], [1, 5], [2, 7], [1,3], [2,4]]
#  0       1        2       3       4       5           6       7       8     9       10
