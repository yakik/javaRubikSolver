from production.solver.rotation_sequence import Rotation_sequence

class Rotation_tree:
    def __init__(self):
        self.c_array = list()

    def add_rotationLinkedList(self, p_list):
        #Console.Write("FFFFF")
        self.c_array.append(p_list.get_copy())

    def getSize(self):
        return len(self.c_array)

    def get_rotationSequence(self, p_index):
        return self.c_array[p_index]

    @staticmethod
    def get_rotationTreeFromFile(p_File):
        myTree = Rotation_tree()
        l_rotationLinkedList = Rotation_sequence()
        while l_rotationLinkedList.readFromFile(p_File):
            myTree.add_rotationLinkedList(l_rotationLinkedList)
        return myTree
