from production.cube.cube import Cube
from production.solver.solver import Solver
from production.utils.face import Face
from production.utils.direction import Direction
from production.cube.rubikFileReader import RubikFileReader
from production.solver.rotationTree import RotationTree
import unittest
class SolverTest(unittest.TestCase):

        #@Ignore
        
        def test_complexSolver(self):
            #long beginningTime = System.nanoTime()
            myRubik = Cube()
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            mySolver = Solver()


            readFirstFloor = RubikFileReader("..\\..\\..\\Resources\\FirstFloor.txt")
            readSecondFloor = RubikFileReader("..\\..\\..\\Resources\\SecondFloor.txt")
            readThirdFloor = RubikFileReader("..\\..\\..\\Resources\\ThirdFloor.txt")

        
            firstFloorTree = RotationTree.getRotationTreeFromFile(readFirstFloor)
            secondFloorTree = RotationTree.getRotationTreeFromFile(readSecondFloor)
            thirdFloorTree = RotationTree.getRotationTreeFromFile(readThirdFloor)
            #System.out.format("****************")
            mySolution = mySolver.solve(myRubik, firstFloorTree, secondFloorTree, thirdFloorTree)
            #System.out.format("****************")
            mySolution.applyToRubik(myRubik)
            mySolution.print()
            # long endTime = System.n nanoTime()
            #Console.WriteLine("Elapsed Time=%d seconds", ((endTime - beginningTime) / 1000000000))
            #27-12-2017: started 11:39 PM, Failed
            #myRubik.print()
            self.assertTrue(myRubik.equals(Cube()))

        


    
