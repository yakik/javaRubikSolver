class Solution:

    def __init__(self, p_rotationLinkedList, p_permutation, p_prevSolution):
        self.c_rotationLinkedList = p_rotationLinkedList.get_copy()
        self.c_permutation = p_permutation.get_copy()
        self.c_prevSolution = p_prevSolution

    def getPermutation(self):
        return self.c_permutation

    def get_rotationLinkedList(self):
        return self.c_rotationLinkedList

    def getPrevSolution(self):
        return self.c_prevSolution

    def equals(self, p_solution):

        return (self.c_permutation == (p_solution.getPermutation()))

    def print(self):
        if self.c_prevSolution != None:
            self.c_prevSolution.print()
        self.c_rotationLinkedList.print()
        print("\n")

    def apply_to_rubik(self, p_rubik):
        if self.c_prevSolution != None:
            self.c_prevSolution.apply_to_rubik(p_rubik)
        self.c_rotationLinkedList.apply_to_rubik(p_rubik)
