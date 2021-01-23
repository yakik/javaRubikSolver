from production.solver.rotation_sequence import Rotation_sequence

class Rotation_tree:
    def __init__(self):
        self.c_array = list()

    def add_rotation_linked_list(self, p_list):
        #Console.Write("FFFFF")
        self.c_array.append(p_list.get_copy())

    def get_size(self):
        return len(self.c_array)

    def get_rotationSequence(self, p_index):
        return self.c_array[p_index]

    @staticmethod
    def get_rotation_tree_from_file(p_File):
        myTree = Rotation_tree()
        l_rotationLinkedList = Rotation_sequence()
        while l_rotationLinkedList.read_from_file(p_File):
            myTree.add_rotation_linked_list(l_rotationLinkedList)
        return myTree
