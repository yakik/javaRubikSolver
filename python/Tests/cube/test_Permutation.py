import unittest
from production.cube.cube import Cube
from production.utils.face import Face
from production.utils.direction import Direction


class PermutationTest(unittest.TestCase):

    def test_getValue(self):
        myRubik = Cube()
        myRubik.rotateFace(Face.FRONT, Direction.CW)
        myPermutation = Cube(myRubik)
        self.assertEqual(10, Cube.getValue(myPermutation, 1), "first floor")
        self.assertEqual(14, Cube.getValue(
            myPermutation, 2), "second floor")
        self.assertEqual(24, Cube.getValue(myPermutation, 3), "third floor")

    def test_getValueFull(self):
        myRubik = Cube()
        myPermutation = Cube(myRubik)
        self.assertEqual(40, Cube.getValue(myPermutation, 3))
