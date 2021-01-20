using cube

    class Solution 


        Cube c_permutation
        RotationSequence c_rotationLinkedList
        Solution c_prevSolution


        Solution(RotationSequence p_rotationLinkedList, Cube p_permutation, Solution p_prevSolution):
            c_rotationLinkedList = p_rotationLinkedList.getCopy()
            c_permutation = p_permutation.getCopy()
            c_prevSolution = p_prevSolution
        

        Cube getPermutation():
            return c_permutation
        

        RotationSequence getRotationLinkedList():
            return c_rotationLinkedList
        

        Solution getPrevSolution():
            return c_prevSolution
        

        Boolean equals(Solution p_solution)

        
            return (c_permutation == (p_solution.getPermutation()))
        

        print():
            if c_prevSolution != null)
                c_prevSolution.print()
            c_rotationLinkedList.print()
            Console.Write("\n")
        

        applyToRubik(Cube p_rubik):
            if c_prevSolution != null)
                c_prevSolution.applyToRubik(p_rubik)
            c_rotationLinkedList.applyToRubik(p_rubik)

        
    

