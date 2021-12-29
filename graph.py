class Node:

    def __init__(self ,id , data=0):
        self.id = id
        self.data = data
        self.connectedTo = dict()

    def addNeighbour(self ,neibour ,weight=0):
        if neibour not in self.connectedTo:
            self.connectedTo[neibour.id] = weight

    def setData(self,newdata):
        self.data = newdata

    def getConnection(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getData(self):
        return self.data

    def getWeight(self ,neibour):
        return self.connectedTo[neibour.id]

    def __str__(self):
        return str(self.data)+" conected to "+str([node.data for node in self.connectedTo])

class Graph:
    total_node = 0
    def __init__(self):
        self.allNodes = dict()

    def addNode(self ,id ,data = 0):
        if id not in self.allNodes:
            node = Node(id ,data)
            self.allNodes[id] = node
            self.total_node += 1

    def addNodeData(self ,id ,data):
        if id in self.allNodes:
            node = self.allNodes[id]
            node.setData(data)
        else:
            print("this id doesnt associeted to any node ")

    def addEdge(self ,id_first ,id_second ,weight = 0 ):
        if (id_first in self.allNodes) and (id_second in self.allNodes):
            first_node = self.allNodes[id_first]
            second_node = self.allNodes[id_second]
            first_node.addNeighbour(second_node ,weight)
            second_node.addNeighbour(first_node, weight)
        else:
            print(" one of the id doesnt associeted to any node")

    def isNeighbour(self ,v ,u ):
        if u>=1 and u<=81 and v>=1 and v<=81:
            if (v in self.allNodes[u].getConnection()) or (u in self.allNodes[v].getConnection()) :
                return True
        return False

    def printEdge(self):
        combin = []
        for id in self.allNodes:
            node = self.allNodes[id]
            for con in node.getConnection():
                if [id,con] not in combin:
                    print(id,f'<-- {node.getWeight(self.getNode(con))} -->',con)
                    combin.append([id,con])
                    combin.append([con, id])

    def getNode(self ,id):
        if id in self.allNodes:
            return self.allNodes[id]
        return None

    def getAllNodeIds(self):
        return self.allNodes.keys()



