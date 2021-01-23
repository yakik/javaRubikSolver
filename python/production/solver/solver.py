from production.utils.color import Color
from production.utils.face import Face
from production.utils.location import Location
from production.utils.rotation import Rotation
from production.utils.location_in_face import Location_in_face
from production.utils.direction import Direction
from production.cube.cube import Cube
from production.solver.solution_manager import Solution_manager
from production.solver.solution import Solution
from production.solver.rotation_sequence import Rotation_sequence

class Solver:

        def solve(self, p_rubik, p_firstTree, p_secondTree, p_thirdTree):
            l_permutation = Cube(p_rubik)
            l_solutionManager = Solution_manager()
            l_rotationLinkedList = Rotation_sequence()
            l_floor = self.getTargetFloorPerm(l_permutation)
            l_numberOfCubicleInPlace = Cube.get_value(l_permutation, l_floor)
            l_solutionManager.add_solution(l_rotationLinkedList, l_permutation, None, l_numberOfCubicleInPlace, l_floor)
            l_solutionToDev = l_solutionManager.get_best_undeveloped()
            while (l_solutionToDev != None and l_solutionManager.get_best_value() < 40):
                targetFloor = self.getTargetFloorPerm(l_solutionToDev.getPermutation())
                print("Searching " + str(Cube.get_value(l_solutionToDev.getPermutation(), targetFloor)) + "\n")
                if l_solutionManager.get_best_value() > (Cube.get_value(l_solutionToDev.getPermutation(), targetFloor) + 14):
                    print("Couldn't Find a Solution\n")
                    return l_solutionManager.get_best()
                
                if targetFloor == 1:
                    self.findBetterSolution(l_solutionToDev, p_firstTree, l_solutionManager, targetFloor)
                if targetFloor == 2:
                    self.findBetterSolution(l_solutionToDev, p_secondTree, l_solutionManager, targetFloor)
                if targetFloor == 3:
                    self.findBetterSolution(l_solutionToDev, p_thirdTree, l_solutionManager, targetFloor)

                l_floor = self.getTargetFloorValue(l_solutionManager.get_best_value())

                print("Floor="+str(l_floor)+" Best yet:"+str(l_solutionManager.get_best_value())+", best_undeveloped="+str(l_solutionManager.get_best_undeveloped() != None)+"\n")
                l_solutionToDev = l_solutionManager.get_best_undeveloped()
            return l_solutionManager.get_best()

        def getTargetFloorPerm(self,p_permutation):
            if Cube.get_value(p_permutation, 1) >= 16:
                if Cube.get_value(p_permutation, 2) < 24:
                    return 2
                else:
                    return 3
            else:
                return 1

        def getTargetFloorValue(self, p_value):
            if p_value >= 16:
                if p_value < 24:
                    return 2
                else:
                    return 3
            else:
                return 1

        def findBetterSolution(self,p_solution,p_tree,p_solutionManager, p_floor):
            l_rubik = Cube()
            l_permutation = p_solution.getPermutation().get_copy()
            l_minimumValue = Cube.get_value(l_permutation, p_floor)
            l_rubik = Cube(l_permutation)
            self.searchTree(l_minimumValue - 4, p_tree, l_rubik, p_solutionManager, p_solution, p_floor, 0)

        def searchTree(self, minimumValueToReach,searchTree,
                              cubeToSolve,solutionManager,
                              previousSolution, targetFloorToSortInCube, depth):
            if minimumValueToReach < 2:
                minimumValueToReach = 2
            for rotationSequenceIndex in range(0,searchTree.get_size()):
                rotationSequence = searchTree.get_rotationSequence(rotationSequenceIndex)
                if rotationSequence != None:
                    cubeAfterRotationSequence = self.getCubeAfterApplyingSequence(Cube(cubeToSolve), rotationSequence)
                    self.addSequenceToSolutionIfHigherValue(minimumValueToReach, solutionManager, previousSolution,
                            targetFloorToSortInCube, rotationSequence, cubeAfterRotationSequence)
                    if targetFloorToSortInCube == 3 and depth == 0:
                        self.searchTree(minimumValueToReach, searchTree, cubeAfterRotationSequence, solutionManager,
                                Solution(rotationSequence, cubeAfterRotationSequence, previousSolution), targetFloorToSortInCube, 1)

        def addSequenceToSolutionIfHigherValue(self, minimumValueToReach,solutionManager,
               previousSolution, targetFloorToSortInCube,rotationSequence,
               cubeAfterRotationSequence):
            if Cube.get_value(cubeAfterRotationSequence, targetFloorToSortInCube) >= minimumValueToReach:
                solutionManager.add_solution(rotationSequence, cubeAfterRotationSequence, previousSolution,
                                            Cube.get_value(cubeAfterRotationSequence, targetFloorToSortInCube), targetFloorToSortInCube)

        def getCubeAfterApplyingSequence(self,cubeForExperimentation,rotationSequence):
            for rotationIndex in range(0, rotationSequence.size()):
                cubeForExperimentation.rotate_face(rotationSequence.get_rotation(rotationIndex).getFace(),
                                                   rotationSequence.get_rotation(rotationIndex).getDirection())
            cubeAfterRotationSequence = Cube.get_permutation_from_cube(cubeForExperimentation).get_copy()
            return cubeAfterRotationSequence