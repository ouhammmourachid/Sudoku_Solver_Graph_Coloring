from graph import Graph
import numpy as np

class SodokuConnections:

    def __init__(self ,rows =9,cols =9):
        self.graph = Graph()
        self.cols = cols
        self.rows = rows
        self.total_size = rows*cols
        self.__generateGraph()
        self.__conectEdges()

    def __generateGraph(self):
        for id in range(1 ,self.total_size+1):
            self.graph.addNode(id)
    def __conectEdges(self):
        matrix = np.arange(1,82).reshape((9,9))
        for i in range(self.cols):
            self.__connectThose(matrix[i])
        for j in range(self.rows):
            self.__connectThose(matrix[:,j])
        for i in range(3):
            for j in range(3):
                lis = matrix[j*3:(j+1)*3,i*3:(i+1)*3]
                self.__connectThose(np.reshape(lis ,(len(lis)**2,)))

    def __connectThose(self ,lis):
        lis = list(lis)
        cpy_list = lis.copy()
        for id in cpy_list:
            first_id = id
            del lis[0]
            for second_id in lis:
                self.graph.addEdge(first_id ,second_id)


sodoku = SodokuConnections()
sodoku.graph.printEdge()
print(sodoku.graph.isNeighbour(1,28))