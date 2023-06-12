class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        if self.adj_list == {}:
            return False
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
        print('')
        return True

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def avoidDuplicateAppend(self, listTarget, value):
        if value not in listTarget:
            listTarget.append(value)
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def isInGraph(self, vertex):
        if vertex in self.adj_list.keys():
            return True
        return False

    def printAllConnected(self, vertex):
        if self.adj_list == {}:
            return False
        print(f'Data in {vertex} Vertex ==>', end='')
        for data in self.adj_list[vertex]:
            print(data, end=', ' if data != self.adj_list[vertex][-1] else '')
        print('')
        return True

if __name__ =='__main__':
    print('\n============ FINAL RESULT============') 
    my_grap = Graph()
    listVertex = [21, 76, 44, 18, 52, 27, 82]
    listVertex = [str(data) for data in listVertex]
    for vertex in listVertex: my_grap.add_vertex(vertex)

    #21
    my_grap.add_edge(listVertex[0], listVertex[1])
    my_grap.add_edge(listVertex[0], listVertex[2])
    my_grap.add_edge(listVertex[0], listVertex[3])
    
    76
    my_grap.add_edge(listVertex[1], listVertex[0])
    my_grap.add_edge(listVertex[1], listVertex[2])
    
    #44
    my_grap.add_edge(listVertex[2], listVertex[1])
    my_grap.add_edge(listVertex[2], listVertex[0])
    my_grap.add_edge(listVertex[2], listVertex[3])
    
    #18
    my_grap.add_edge(listVertex[3], listVertex[0])
    my_grap.add_edge(listVertex[3], listVertex[2])
    my_grap.add_edge(listVertex[3], listVertex[4])
    
    #52
    my_grap.add_edge(listVertex[4], listVertex[3])
    my_grap.add_edge(listVertex[4], listVertex[5])
    
    #27
    my_grap.add_edge(listVertex[5], listVertex[4])
    my_grap.add_edge(listVertex[5], listVertex[6])
    
    #82
    my_grap.add_edge(listVertex[6], listVertex[5])
    my_grap.print_graph

    my_grap.print_graph()

    my_grap.printAllConnected(listVertex[0])

    print(f'{listVertex[1]} is contains' if my_grap.isInGraph (listVertex[1]) else f'{listVertex[1]} is not contains')
    print('=================================\n')
    
    my_grap.add_vertex('A')
    my_grap.add_vertex('B')
    my_grap.add_vertex('C')
    my_grap.add_vertex('D')

    my_grap.add_edge('A','B')
    my_grap.add_edge('A','C')
    my_grap.add_edge('A','D')
    my_grap.add_edge('B','D')
    my_grap.add_edge('C','D')

# ================== Default ===============
# my_graph = Graph()
# my_graph.print_graph()
# ================== Add Vertex ===============
# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.print_graph()
# ================== Add Edge ===============
# my_graph = Graph()
# my_graph.add_vertex(1)
# my_graph.add_vertex(2)
# my_graph.add_edge(1,2)
# my_graph.print_graph()
# ================== Remove Edge ===============
# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_edge('A', 'B')
# my_graph.add_edge('B', 'C')
# my_graph.add_edge('C', 'A')
# print('Graph before remove_edge():')
# my_graph.print_graph()

# my_graph.remove_edge('A','C')

# print('\nGraph after remove_edge():')
# my_graph.print_graph()
# ================== Remove Vertex ===============
# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')

# my_graph.add_edge('A', 'B')
# my_graph.add_edge('A', 'C')
# my_graph.add_edge('A', 'D')
# my_graph.add_edge('B', 'D')
# my_graph.add_edge('C', 'D')

# print('Graph before remove_vertex():')
# my_graph.print_graph()

# my_graph.remove_vertex('D')

# print('\nGraph after remove_vertex():')
# my_graph.print_graph()
