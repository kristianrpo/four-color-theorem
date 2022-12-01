from collections import deque
class Vertex:
    def __init__ (self,i):
        self.data = i
        self.color = None
        self.level = -1
        self.neighbour = []
        self.visited = False 
        self.dad = None
    def add_neigh (self, vertexx):
        if vertexx not in self.neighbour:
            self.neighbour.append(vertexx)

class Graph:
    def __init__ (self):
        self.dictionary = {}
    def add_vertex(self,v):
        if v not in self.dictionary:
            self.dictionary[v] = Vertex(v)
    def add_edge(self,a,b):
        if a in self.dictionary and b in self.dictionary:
            self.dictionary[a].add_neigh(b)
            self.dictionary[b].add_neigh(a)
    def print_graph(self):
        keys = list(self.dictionary.keys())
        for i in range(len(keys)):
            print(keys[i],str("->"),self.dictionary[keys[i]].neighbour)
    
    def print_graph_with_colors(self):
        keys = list(self.dictionary.keys())
        for i in range(len(keys)):
            print(keys[i],str("->"),self.dictionary[keys[i]].color)


    def paint_graph_countries(self,vertices,colores):
        for vertex in vertices:
            neigh_act = self.dictionary[vertex].neighbour
            colors_use = []
            for neighbours in neigh_act:
                if self.dictionary[neighbours].color == None:
                    continue
                else:
                    colors_use.append(self.dictionary[neighbours].color)
            for color in colores:
                if color in colors_use:
                    continue
                else:
                    self.dictionary[vertex].color = color
                    break


def metodo_de_prueba():
    g = Graph()
    list_of_vertexs = ["BRASIL","ARGENTINA","COLOMBIA","PERÚ","CHILE","ECUADOR","VENEZUELA","URUGUAY","BOLIVIA","PARAGUAY","GUAYANA","SURINAME","GUYANA FRANCESA"]
    list_of_relations = ["COLOMBIA","BRASIL","COLOMBIA","VENEZUELA","COLOMBIA","ECUADOR","COLOMBIA","PERÚ","ECUADOR","PERÚ","PERÚ","BRASIL","PERÚ","BOLIVIA","PERÚ","CHILE","CHILE","BOLIVIA","CHILE","ARGENTINA","ARGENTINA","BOLIVIA","ARGENTINA","PARAGUAY","ARGENTINA","URUGUAY","URUGUAY","BRASIL","PARAGUAY","BOLIVIA","PARAGUAY","BRASIL","BOLIVIA","BRASIL","VENEZUELA","BRASIL","GUAYANA","VENEZUELA","GUAYANA","BRASIL","GUAYANA","SURINAME","SURINAME","BRASIL","SURINAME","GUYANA FRANCESA","GUYANA FRANCESA","BRASIL","ARGENTINA","BRASIL"]
    colors = ["AMARILLO","AZUL","ROJO","VERDE"]
    for v in range(len(list_of_vertexs)):
        g.add_vertex(list_of_vertexs[v])
    for v in range(0,len(list_of_relations)-1,2):
        g.add_edge(list_of_relations[v],list_of_relations[v+1])
    g.print_graph()
    print()
    print("and his colors is:")
    print()
    g.paint_graph_countries(list_of_vertexs,colors)
    g.print_graph_with_colors()

if __name__ == '__main__':
    metodo_de_prueba()
