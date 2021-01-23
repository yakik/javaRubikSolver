from production.cube.cube import Cube
from production.solver.solver import Solver
from production.utils.face import Face
from production.utils.direction import Direction
from production.cube.rubik_file_reader import Rubik_file_reader
from production.solver.rotation_tree import Rotation_tree
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


            readFirstFloor = Rubik_file_reader("c:\\Users\\yk700h\\dev\\rubikCubeSolver\\python\\Resources\\FirstFloor.txt")
            readSecondFloor = Rubik_file_reader("c:\\Users\\yk700h\\dev\\rubikCubeSolver\\python\\Resources\\SecondFloor.txt")
            readThirdFloor = Rubik_file_reader("c:\\Users\\yk700h\\dev\\rubikCubeSolver\\python\\Resources\\ThirdFloor.txt")

        
            firstFloorTree = Rotation_tree.getRotationTreeFromFile(readFirstFloor)
            readFirstFloor.close()
            secondFloorTree = Rotation_tree.getRotationTreeFromFile(readSecondFloor)
            readSecondFloor.close()
            thirdFloorTree = Rotation_tree.getRotationTreeFromFile(readThirdFloor)
            readThirdFloor.close()
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

        


    
