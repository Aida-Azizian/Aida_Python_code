
import sys
from collections import deque, namedtuple
class WeightedDigraph:
    def __init__(self, vertices, edges):
        self.vertices=vertices
        self.dict = {}#create a dictionary for the graph with vertices and edges
        for v in vertices:
            self.dict[v] = {}
        for e in edges:
            self.dict[e[0]][e[2]] = e[1]
    def cheapest_path(self,start,goal):
        shortest_distance = {}
        predecessor = {}
        unseenNodes=[]
        for v in self.vertices:# at first all vertices are in a set of unvisited vertices
            unseenNodes.append(v)
        path = []
        for node in unseenNodes:# distance value, is a very large number for all other vertices
            shortest_distance[node] = sys.maxsize
        shortest_distance[start] = 0 # distance value, zero for S
 
        while unseenNodes:# to update the distance of all states
            minNode = None
            for node in unseenNodes:# For each node and it's neighbours,
                if minNode is None: #compare the newly calculated distance to the previous distance value and update it if the new value is the smaller one.
                    minNode = node
                elif shortest_distance[node] < shortest_distance[minNode]:
                    minNode = node
            for neighbor in self.dict[minNode]:  
                updated_distance = shortest_distance[minNode] + self.dict[minNode][neighbor]
                if updated_distance < shortest_distance[neighbor]:
                    shortest_distance[neighbor] = updated_distance #updated the distance value 
                    predecessor[neighbor]=minNode
            unseenNodes.remove(minNode)# remove the node from unseen nodes
        currentNode = goal
        while currentNode != start:
            try:
                path.insert(0,currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print('None','None')
                break
        path.insert(0,start)
        if shortest_distance[goal]<1000 and path:
            print(str(path),str(shortest_distance[goal]))
 
 
        

