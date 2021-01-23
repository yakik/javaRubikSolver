import unittest
from production.cube.cube import Cube
from production.utils.face import Face
from production.utils.direction import Direction


class PermutationTest(unittest.TestCase):

    def test_getValue(self):
        myRubik = Cube()
        myRubik.rotate_face(Face.FRONT, Direction.CW)
        myPermutation = Cube(myRubik)
        self.assertEqual(10, Cube.get_value(myPermutation, 1), "first floor")
        self.assertEqual(14, Cube.get_value(
            myPermutation, 2), "second floor")
        self.assertEqual(24, Cube.get_value(myPermutation, 3), "third floor")

    def test_getValueFull(self):
        myRubik = Cube()
        myPermutation = Cube(myRubik)
        self.assertEqual(40, Cube.get_value(myPermutation, 3))
