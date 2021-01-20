import unittest
class RotationLinkedListTest(unittest.TestCase):
    

        
        def isRedundantCW(self):
           myList = RotationSequence()
            myList.addRotation(Rotation(Face.FRONT, Direction.CW))
            self.assertEqual(True, myList.isRedundant(Rotation(Face.FRONT, Direction.CW)))
        

        
        def isRedundantCCW(self):
           myList = RotationSequence()
            myList.addRotation(Rotation(Face.FRONT, Direction.CCW))
            myList.addRotation(Rotation(Face.FRONT, Direction.CCW))
            self.assertEqual(True, myList.isRedundant(Rotation(Face.FRONT, Direction.CCW)))
        
    
