class SolutionManager:
    


        def __init__(self):
            self.c_solutionList = list()
            for i in (0,41):
                self.c_solutionList.append(List<SolutionNode>())
        

        def addSolution(self,p_rotationLinkedList,p_permutation,p_prevSolution,
                         p_value, p_floor):

            if  len(self.c_solutionList[p_value]) < 40:
            
                self.c_solutionList[p_value].append(SolutionNode(Solution(p_rotationLinkedList.getCopy(), p_permutation.getCopy(), p_prevSolution)))

                #         Console.Write("AddedValue=%d, Index=%d\n", p_value, p_value)
            



        


        def getBestUndeveloped(self):
            i = 40
           l_bestSolution = null
            while i >= 0 and l_bestSolution == null)
            
                if len(self.c_solutionList[i]) > 0:
                    j = 0
                    while j < len(self.c_solutionList[i]) and l_bestSolution == null:
                    
                        SolutionNode l_node = self.c_solutionList[i][j+=1]
                        if !l_node.isDeveloped():
                        
                            l_bestSolution = l_node.getSolution()
                            l_node.setDeveloped()
                        
                    
                
                i--
            
            return l_bestSolution
        

        def getBest(self):
            i = 40
           l_returnValue = null
            while i >= 0 and l_returnValue == null:
            
                if len(self.c_solutionList[i]) > 0:
                    l_returnValue = self.c_solutionList[i][0].getSolution()
                i--
            
            return l_returnValue
        

        def getBestValue(self):
            i = 40
            l_returnValue = 0
            while i >= 0 and l_returnValue == 0)
            
                if len(self.c_solutionList[i]) > 0:
                    l_returnValue = i
                i--
            
            return l_returnValue
        

        class SolutionNode
        
           c_solution
            Boolean c_isDeveloped

            def SolutionNode(self,p_solution)
            
                c_isDeveloped = False
                c_solution = p_solution
            

            def getSolution(self)
            
                return c_solution
            


            def isDeveloped(self)
            
                return c_isDeveloped
            

            def setDeveloped(self)
            
                c_isDeveloped = True
            


        
    
