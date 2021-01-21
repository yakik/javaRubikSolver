from production.utils.color import Color
from production.utils.face import Face
from production.utils.location import Location
from production.utils.rotation import Rotation
from production.utils.locationInFace import LocationInFace
from production.utils.direction import Direction
from production.cube.cube import Cube
from production.solver.solutionManager import SolutionManager
from production.solver.rotationSequence import RotationSequence

class Solver:

        def solve(self, p_rubik, p_firstTree, p_secondTree, p_thirdTree):
            l_permutation = Cube(p_rubik)
            l_solutionManager = SolutionManager()
            l_rotationLinkedList = RotationSequence()
            l_floor = self.getTargetFloorPerm(l_permutation)
            l_numberOfCubicleInPlace = Cube.getValue(l_permutation, l_floor)
            l_solutionManager.addSolution(l_rotationLinkedList, l_permutation, None, l_numberOfCubicleInPlace, l_floor)
            l_solutionToDev = l_solutionManager.getBestUndeveloped()
            while (l_solutionToDev != None and l_solutionManager.getBestValue() < 40):
                targetFloor = self.getTargetFloor(l_solutionToDev.getPermutation())
                Console.Write("Searching %d", Cube.getValue(l_solutionToDev.getPermutation(), targetFloor))
                if l_solutionManager.getBestValue() > Cube.getValue(l_solutionToDev.getPermutation(), targetFloor) + 14:
                    Console.WriteLine("Couldn't Find a Solution")
                    return l_solutionManager.getBest()
                
                if targetFloor == 1:
                    self.findBetterSolution(l_solutionToDev, p_firstTree, l_solutionManager, targetFloor)
                if targetFloor == 2:
                    self.findBetterSolution(l_solutionToDev, p_secondTree, l_solutionManager, targetFloor)
                if targetFloor == 3:
                    self.findBetterSolution(l_solutionToDev, p_thirdTree, l_solutionManager, targetFloor)

                l_floor = self.getTargetFloorValue(l_solutionManager.getBestValue())

                Console.Write("Floor=0, Best yet:1, bestUnDeveloped=2\n", l_floor, l_solutionManager.getBestValue(), l_solutionManager.getBestUndeveloped() != None)
                l_solutionToDev = l_solutionManager.getBestUndeveloped()
            return l_solutionManager.getBest()

        def getTargetFloorPerm(self,p_permutation):
            if Cube.getValue(p_permutation, 1) >= 16:
                if Cube.getValue(p_permutation, 2) < 24:
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

        def findBetterSolution(self,p_solution,p_tree,p_solutionManager,
                                        p_floor):
            l_rubik = Cube()
            l_permutation = p_solution.getPermutation().getCopy()
            l_minimumValue = Cube.getValue(l_permutation, p_floor)
            l_rubik = Cube(l_permutation)
            searchTree(l_minimumValue - 4, p_tree, l_rubik, p_solutionManager,
                    p_solution, p_floor, 0)

        def searchTree(self, minimumValueToReach,searchTree,
                              cubeToSolve,solutionManager,
                              previousSolution, targetFloorToSortInCube, depth):
            if minimumValueToReach < 2:
                minimumValueToReach = 2
            for rotationSequenceIndex in range(0,searchTree.getSize()):
                rotationSequence = searchTree.getRotationSequence(rotationSequenceIndex)
                if rotationSequence != None:
                    cubeAfterRotationSequence = getCubeAfterApplyingSequence(Cube(cubeToSolve), rotationSequence)
                    addSequenceToSolutionIfHigherValue(minimumValueToReach, solutionManager, previousSolution,
                            targetFloorToSortInCube, rotationSequence, cubeAfterRotationSequence)
                    if targetFloorToSortInCube == 3 and depth == 0:
                        self.searchTree(minimumValueToReach, searchTree, cubeAfterRotationSequence, solutionManager,
                                Solution(rotationSequence, cubeAfterRotationSequence, previousSolution), targetFloorToSortInCube, 1)

        def addSequenceToSolutionIfHigherValue(self, minimumValueToReach,solutionManager,
               previousSolution, targetFloorToSortInCube,rotationSequence,
               cubeAfterRotationSequence):
            if Cube.getValue(cubeAfterRotationSequence, targetFloorToSortInCube) >= minimumValueToReach:
                solutionManager.addSolution(rotationSequence, cubeAfterRotationSequence, previousSolution,
                        Cube.getValue(cubeAfterRotationSequence, targetFloorToSortInCube), targetFloorToSortInCube)

        def getCubeAfterApplyingSequence(self,cubeForExperimentation,rotationSequence):
            for rotationIndex in range(0, rotationSequence.size()):
                cubeForExperimentation.rotateFace(rotationSequence.getRotation(rotationIndex).getFace(),
                        rotationSequence.getRotation(rotationIndex).getDirection())
            cubeAfterRotationSequence = Cube.getPermutationFromCube(cubeForExperimentation).getCopy()
            return cubeAfterRotationSequence