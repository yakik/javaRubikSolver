from production.solver.solution import Solution
from production.solver.solution_node import Solution_node

class Solution_manager:

        def __init__(self):
            self.c_solutionList = list()
            for _ in range(0, 41):
                self.c_solutionList.append(list())

        def add_solution(self, p_rotationLinkedList, p_permutation, p_prevSolution,
                         p_value, p_floor):
            if len(self.c_solutionList[p_value]) < 40:
                self.c_solutionList[p_value].append(Solution_node(Solution(
                    p_rotationLinkedList.get_copy(), p_permutation.get_copy(), p_prevSolution)))

        def get_best_undeveloped(self):
            i = 40
            l_bestSolution = None
            while (i >= 0 and l_bestSolution == None):

                if len(self.c_solutionList[i]) > 0:
                    j = 0
                    while (j < len(self.c_solutionList[i]) and l_bestSolution == None):
                        l_node = self.c_solutionList[i][j]
                        j+=1
                        if not l_node.is_developed():
                            l_bestSolution = l_node.get_solution()
                            l_node.set_developed()
                i-=1
            return l_bestSolution

        def get_best(self):
            i = 40
            l_returnValue = None
            while (i >= 0 and l_returnValue == None):
                if len(self.c_solutionList[i]) > 0:
                    l_returnValue = self.c_solutionList[i][0].get_solution()
                i-=1
            return l_returnValue
        

        def get_best_value(self):
            i = 40
            l_returnValue = 0
            while (i >= 0 and l_returnValue == 0):
                if len(self.c_solutionList[i]) > 0:
                    l_returnValue = i
                i-=1
            return l_returnValue