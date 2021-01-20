class Solution:



        def __init__(self, RotationSequence p_rotationLinkedList, Cube p_permutation, Solution p_prevSolution):
            self.c_rotationLinkedList = p_rotationLinkedList.getCopy()
            self.c_permutation = p_permutation.getCopy()
            self.c_prevSolution = p_prevSolution
        

        def getPermutation(self):
            return self.c_permutation
        

        def getRotationLinkedList(self):
            return self.c_rotationLinkedList
        

        def getPrevSolution(self):
            return self.c_prevSolution
        

        def equals(self, Solution p_solution)

        
            return (self.c_permutation == (p_solution.getPermutation()))
        

        def print(self):
            if self.c_prevSolution != null)
                self.c_prevSolution.print()
            self.c_rotationLinkedList.print()
            Console.Write("\n")
        

        def applyToRubik(self, Cube p_rubik):
            if self.c_prevSolution != null)
                self.c_prevSolution.applyToRubik(p_rubik)
            self.c_rotationLinkedList.applyToRubik(p_rubik)

        
    

