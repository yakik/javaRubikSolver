class RotationTree:

       def __init__():
            self.c_array = list()

        def addRotationLinkedList(self, p_list):
            #Console.Write("FFFFF")
            self.c_array.append(p_list.getCopy())

        def getSize(self):
            return len(self.c_array)

        def getRotationSequence(self, p_index):
            return self.c_array[p_index]

        @staticmethod
        def getRotationTreeFromFile(p_File):
           myTree = RotationTree()
           l_rotationLinkedList = RotationSequence()
           while l_rotationLinkedList.readFromFile(p_File):
                myTree.addRotationLinkedList(l_rotationLinkedList)
            return myTree
