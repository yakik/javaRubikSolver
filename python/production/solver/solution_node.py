class Solution_node:
            
    def __init__(self,p_solution):
        self.c_is_developed = False
        self.c_solution = p_solution

    def get_solution(self):
        return self.c_solution

    def is_developed(self):
        return self.c_is_developed

    def set_developed(self):
        self.c_is_developed = True