import unittest


class PermutationTest(unittest.TestCase):

       def getValue(self):
           myRubik = Cube()
           myRubik.rotateFace(Face.FRONT, Direction.CW)
           myPermutation = Cube(myRubik)
            self.assertEqual(10, Cube.getValue(myPermutation, 1), "first floor")
            self.assertEqual(14, Cube.getValue(
                myPermutation, 2), "second floor")
            self.assertEqual(24, Cube.getValue(myPermutation, 3), "third floor")


        def getValueFull(self):
           myRubik = Cube()
           myPermutation = Cube(myRubik)
            self.assertEqual(40, Cube.getValue(myPermutation, 3))
