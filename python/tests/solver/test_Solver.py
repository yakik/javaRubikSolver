from production.cube.cube import Cube
from production.solver.solver import Solver
from production.utils.face import Face
from production.utils.direction import Direction
from production.cube.rubik_file_reader import Rubik_file_reader
from production.solver.rotation_tree import Rotation_tree
import unittest
class SolverTest(unittest.TestCase):

        @unittest.skip("too long")
        def test_complexSolver(self):
            myRubik = Cube()
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.LEFT, Direction.CW)
            myRubik.rotate_face(Face.FRONT, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.LEFT, Direction.CW)
            myRubik.rotate_face(Face.FRONT, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.LEFT, Direction.CW)
            myRubik.rotate_face(Face.FRONT, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.LEFT, Direction.CW)
            myRubik.rotate_face(Face.FRONT, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.LEFT, Direction.CW)
            myRubik.rotate_face(Face.FRONT, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.LEFT, Direction.CW)
            myRubik.rotate_face(Face.FRONT, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.LEFT, Direction.CW)
            myRubik.rotate_face(Face.FRONT, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            myRubik.rotate_face(Face.BACK, Direction.CW)
            myRubik.rotate_face(Face.LEFT, Direction.CW)
            myRubik.rotate_face(Face.FRONT, Direction.CW)
            myRubik.rotate_face(Face.RIGHT, Direction.CW)
            mySolver = Solver()


            readFirstFloor = Rubik_file_reader("c:\\Users\\yk700h\\dev\\rubikCubeSolver\\python\\Resources\\FirstFloor.txt")
            readSecondFloor = Rubik_file_reader("c:\\Users\\yk700h\\dev\\rubikCubeSolver\\python\\Resources\\SecondFloor.txt")
            readThirdFloor = Rubik_file_reader("c:\\Users\\yk700h\\dev\\rubikCubeSolver\\python\\Resources\\ThirdFloor.txt")

        
            firstFloorTree = Rotation_tree.get_rotation_tree_from_file(readFirstFloor)
            readFirstFloor.close()
            secondFloorTree = Rotation_tree.get_rotation_tree_from_file(readSecondFloor)
            readSecondFloor.close()
            thirdFloorTree = Rotation_tree.get_rotation_tree_from_file(readThirdFloor)
            readThirdFloor.close()
            #System.out.format("****************")
            mySolution = mySolver.solve(myRubik, firstFloorTree, secondFloorTree, thirdFloorTree)
            #System.out.format("****************")
            mySolution.apply_to_rubik(myRubik)
            mySolution.print()
            # long endTime = System.n nanoTime()
            #Console.WriteLine("Elapsed Time=%d seconds", ((endTime - beginningTime) / 1000000000))
            #27-12-2017: started 11:39 PM, Failed
            #myRubik.print()
            self.assertTrue(myRubik.equals(Cube()))

        


    
