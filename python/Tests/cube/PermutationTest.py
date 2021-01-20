import unittest
class PermutationTest(unittest.TestCase):
    

        
        def getValue(self):
           myRubik = new Cube()
            myRubik.rotateFace(Face.FRONT, Direction.CW)
           myPermutation = new Cube(myRubik)
            Assert.AreEqual( 10, Cube.getValue(myPermutation, 1), "first floor")
            Assert.AreEqual( 14, Cube.getValue(myPermutation, 2), "second floor")
            Assert.AreEqual(24, Cube.getValue(myPermutation, 3), "third floor")

        
        
        def getValueFull(self):
           myRubik = new Cube()
           myPermutation = new Cube(myRubik)
            Assert.AreEqual( 40, Cube.getValue(myPermutation, 3))

        



    
