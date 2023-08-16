import math
class Graph():
    def __init__(self, nodes = None, edges = None, neighbors = None, location = None, name = None):
        self.nodes = {}
        self.edges = {}
        self.neighbors = []
        self.location = None
        self.name = None
    def add_edge(self, vertex, weight):
        return
    def add_neighbors(Self, neighbors):
        return
    def add_location(self, location):
        return 
    def add_name(self, name):
        return
    def add_nodes(self, vertex):
        return
    
class Heap():
    def __init__(self, spot = None, distance = None, name = None, length = None, heap = None):
        self.heap = []
        self.spot = ()
        self.distance = None
        self.name = None
        self.length = 0

    def add_spot(self, spot):
        self.length += 1
        self.heap.append(spot)
        self.heapify_up(self.length - 1)

    def pop_min(self):
        pspot = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.heap = self.heap[:-1]
        self.length -= 1
        self.heapify_down(0)
        return pspot
    
    def Parent(self, x):
        return math.floor((x-1)/2)

    def left_Child(self,x):
        return (2*x)+1
    def right_Child(self,x):
        return (2*x)+2
     

    def heapify_up(self,i):
        while (i > 0) and (int(self.heap[i][4:]) < int(self.heap[self.Parent(i)][4:])):
            self.heap[i], self.heap[self.Parent(i)] = self.heap[self.Parent(i)], self.heap[i]
            i = self.Parent(i)

    def heapify_down(self, i):
        n = self.length -1
        while (self.left_Child(i) <= n) and (int(self.heap[i][4:]) > int(self.heap[self.left_Child(i)][4:])) or \
            (self.right_Child(i) <= n) and (int(self.heap[i][4:]) > int(self.heap[self.right_Child(i)][4:])):
            if (self.right_Child(i) > n) or (int(self.heap[self.left_Child(i)][4:]) < int(self.heap[self.right_Child(i)][4:])):
                j = self.left_Child(i)
            else:
                j = self.right_Child(i)
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i=j
        
    
    def __str__(self):
        return self.heap


    