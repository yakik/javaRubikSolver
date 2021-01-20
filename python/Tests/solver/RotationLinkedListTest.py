import unittest
using cube

using solver
using utils


    
    class RotationLinkedListTest(unittest.TestCase):
    

        
        def isRedundantCW(self):
            RotationSequence myList = new RotationSequence()
            myList.addRotation(new Rotation(Face.FRONT, Direction.CW))
            Assert.AreEqual(true, myList.isRedundant(new Rotation(Face.FRONT, Direction.CW)))
        

        
        def isRedundantCCW(self):
            RotationSequence myList = new RotationSequence()
            myList.addRotation(new Rotation(Face.FRONT, Direction.CCW))
            myList.addRotation(new Rotation(Face.FRONT, Direction.CCW))
            Assert.AreEqual(true, myList.isRedundant(new Rotation(Face.FRONT, Direction.CCW)))
        
    
