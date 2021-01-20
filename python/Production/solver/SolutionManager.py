using cube


using solver


    class SolutionManager
    

        List<List<SolutionNode>> c_solutionList = new List<List<SolutionNode>>()


        SolutionManager():
            i
            if i = 0 i < 41 i++)
                c_solutionList.Add(new List<SolutionNode>())
        

        addSolution(RotationSequence p_rotationLinkedList, Cube p_permutation, Solution p_prevSolution,
                         p_value, p_floor):

            if /*(p_value>=32 and getBestValue()>=36) or*/ c_solutionList[p_value].Count < 40)
            
                c_solutionList[p_value].Add(new SolutionNode(new Solution(p_rotationLinkedList.getCopy(), p_permutation.getCopy(), p_prevSolution)))

                //         Console.Write("Added Solution Value=%d, Index=%d\n", p_value, p_value)
            



        


        Solution getBestUndeveloped():
            i = 40
            Solution l_bestSolution = null
            while i >= 0 and l_bestSolution == null)
            
                if c_solutionList[i].Count > 0):
                    j = 0
                    while j < c_solutionList[i].Count and l_bestSolution == null)
                    
                        SolutionNode l_node = c_solutionList[i][j++]
                        if !l_node.isDeveloped())
                        
                            l_bestSolution = l_node.getSolution()
                            l_node.setDeveloped()
                        
                    
                
                i--
            
            return l_bestSolution
        

        Solution getBest():
            i = 40
            Solution l_returnValue = null
            while i >= 0 and l_returnValue == null)
            
                if c_solutionList[i].Count > 0)
                    l_returnValue = c_solutionList[i][0].getSolution()
                i--
            
            return l_returnValue
        

        getBestValue():
            i = 40
            l_returnValue = 0
            while i >= 0 and l_returnValue == 0)
            
                if c_solutionList[i].Count > 0)
                    l_returnValue = i
                i--
            
            return l_returnValue
        

        class SolutionNode
        
            Solution c_solution
            Boolean c_isDeveloped

            SolutionNode(Solution p_solution)
            
                c_isDeveloped = false
                c_solution = p_solution
            

            Solution getSolution()
            
                return c_solution
            


            Boolean isDeveloped()
            
                return c_isDeveloped
            

            setDeveloped()
            
                c_isDeveloped = true
            


        
    
