class Solver:

      

        def solve(self, Cube p_rubik, RotationTree p_firstTree, RotationTree p_secondTree, RotationTree p_thirdTree):

            l_numberOfCubicleInPlace
            Cube l_permutation = new Cube(p_rubik)
            SolutionManager l_solutionManager = new SolutionManager()
            Solution l_solutionToDev

            RotationSequence l_rotationLinkedList = new RotationSequence()

            l_floor = getTargetFloor(l_permutation)
            l_numberOfCubicleInPlace = Cube.getValue(l_permutation, l_floor)

            l_solutionManager.addSolution(l_rotationLinkedList, l_permutation, null, l_numberOfCubicleInPlace, l_floor)
            while (l_solutionToDev = l_solutionManager.getBestUndeveloped()) != null and
                    l_solutionManager.getBestValue() < 40):
                targetFloor = getTargetFloor(l_solutionToDev.getPermutation())
                Console.Write("Searching %d", Cube.getValue(l_solutionToDev.getPermutation(), targetFloor))
                if l_solutionManager.getBestValue() > Cube.getValue(l_solutionToDev.getPermutation(), targetFloor) + 14):
                    Console.WriteLine("Couldn't Find a Solution")
                    return l_solutionManager.getBest()
                
                if targetFloor == 1)
                    findBetterSolution(l_solutionToDev, p_firstTree, l_solutionManager, targetFloor)
                if targetFloor == 2)
                    findBetterSolution(l_solutionToDev, p_secondTree, l_solutionManager, targetFloor)
                if targetFloor == 3)
                    findBetterSolution(l_solutionToDev, p_thirdTree, l_solutionManager, targetFloor)

                l_floor = getTargetFloor(l_solutionManager.getBestValue())

                Console.Write("Floor=0, Best yet:1, bestUnDeveloped=2\n", l_floor, l_solutionManager.getBestValue(), l_solutionManager.getBestUndeveloped() != null)
            

            return l_solutionManager.getBest()
        

        def getTargetFloor(self, Cube p_permutation):
            if Cube.getValue(p_permutation, 1) >= 16):
                if Cube.getValue(p_permutation, 2) < 24):
                    return 2
                 else:
                    return 3
                
             else:
                return 1
            
        

        def getTargetFloor(self, p_value):
            if p_value >= 16):
                if p_value < 24):
                    return 2
                 else:
                    return 3
                
             else:
                return 1
            
        




        def findBetterSolution(self, Solution p_solution, RotationTree p_tree, SolutionManager p_solutionManager,
                                        p_floor):
            Cube l_rubik = new Cube()
            Cube l_permutation = p_solution.getPermutation().getCopy()
            l_minimumValue = Cube.getValue(l_permutation, p_floor)

            l_rubik = new Cube(l_permutation)
            searchTree(l_minimumValue - 4, p_tree, l_rubik, p_solutionManager,
                    p_solution, p_floor, 0)
        


        def searchTree(self, minimumValueToReach, RotationTree searchTree,
                               Cube cubeToSolve, SolutionManager solutionManager,
                               Solution previousSolution, targetFloorToSortInCube, depth):
            if minimumValueToReach < 2) minimumValueToReach = 2
            if rotationSequenceIndex = 0 rotationSequenceIndex < searchTree.getSize() rotationSequenceIndex++):
                RotationSequence rotationSequence = searchTree.getRotationSequence(rotationSequenceIndex)
                if rotationSequence != null):
                    Cube cubeAfterRotationSequence = getCubeAfterApplyingSequence(new Cube(cubeToSolve), rotationSequence)

                    addSequenceToSolutionIfHigherValue(minimumValueToReach, solutionManager, previousSolution,
                            targetFloorToSortInCube, rotationSequence, cubeAfterRotationSequence)
                    if targetFloorToSortInCube == 3 and depth == 0):
                        this.searchTree(minimumValueToReach, searchTree, cubeAfterRotationSequence, solutionManager,
                                new Solution(rotationSequence, cubeAfterRotationSequence, previousSolution), targetFloorToSortInCube, 1)

                    
                
            
        

        def addSequenceToSolutionIfHigherValue(self, minimumValueToReach, SolutionManager solutionManager,
                Solution previousSolution, targetFloorToSortInCube, RotationSequence rotationSequence,
                Cube cubeAfterRotationSequence):
            if Cube.getValue(cubeAfterRotationSequence, targetFloorToSortInCube) >= minimumValueToReach):
                solutionManager.addSolution(rotationSequence, cubeAfterRotationSequence, previousSolution,
                        Cube.getValue(cubeAfterRotationSequence, targetFloorToSortInCube), targetFloorToSortInCube)
            
        

        def getCubeAfterApplyingSequence(self, Cube cubeForExperimentation, RotationSequence rotationSequence):
            if rotationIndex = 0 rotationIndex < rotationSequence.size() rotationIndex++)
                cubeForExperimentation.rotateFace(rotationSequence.getRotation(rotationIndex).getFace(),
                        rotationSequence.getRotation(rotationIndex).getDirection())
            Cube cubeAfterRotationSequence = Cube.getPermutationFromCube(cubeForExperimentation).getCopy()
            return cubeAfterRotationSequence
        



    

