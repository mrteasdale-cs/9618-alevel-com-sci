class Node:
    pass

class TreeClass:
    global Tree # TYPE NODE

    def __init__(self, Tree, FirstNode, NumberNodes):
        self.__Tree = []
        self.__FirstNode = -1
        self.__NumberNodes = 0
        for i in range(20):
            self.__Tree[i] = Node(-1)

    def insertNode(self, NewNode):
        if self.__NumberNodes == -1:
            Tree[0] = NewNode
            self.__FirstNode = 0
            self.__NumberNodes += 1
        else:
            getcurrentnode = self.__FirstNode
            while (self.__FirstNode != -1):
                previousnode = getcurrentnode
                if NewNode.GetData() < self.__Tree[getcurrentnode].GetData():
                    #get the left node using GetLeft()
                    pass
                elif NewNode.GetData() < self.__Tree[getcurrentnode].GetData():
                    pass# to the right using self.__Tree[accessNode].GetRight()

            #append the nodes
            
            self.__NumberNodes += 1