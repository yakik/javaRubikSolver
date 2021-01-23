class Solution_node:
            
    def __init__(self,p_solution):
        self.c_isDeveloped = False
        self.c_solution = p_solution

    def getSolution(self):
        return self.c_solution

    def isDeveloped(self):
        return self.c_isDeveloped

    def setDeveloped(self):
        self.c_isDeveloped = True