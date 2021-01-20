import unittest
class RotationLinkedListTest(unittest.TestCase):
    

        
        def isRedundantCW(self):
           myList = RotationSequence()
            myList.addRotation(Rotation(Face.FRONT, Direction.CW))
            Assert.AreEqual(True, myList.isRedundant(Rotation(Face.FRONT, Direction.CW)))
        

        
        def isRedundantCCW(self):
           myList = RotationSequence()
            myList.addRotation(Rotation(Face.FRONT, Direction.CCW))
            myList.addRotation(Rotation(Face.FRONT, Direction.CCW))
            Assert.AreEqual(True, myList.isRedundant(Rotation(Face.FRONT, Direction.CCW)))
        
    
