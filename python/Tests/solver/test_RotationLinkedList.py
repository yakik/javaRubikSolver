import unittest
from production.solver.rotationSequence import RotationSequence
from production.utils.rotation import Rotation
from production.utils.face import Face
from production.utils.direction import Direction

class RotationLinkedListTest(unittest.TestCase):
    

        
   def test_isRedundantCW(self):
      myList = RotationSequence()
      myList.addRotation(Rotation(Face.FRONT, Direction.CW))
      self.assertEqual(True, myList.isRedundant(Rotation(Face.FRONT, Direction.CW)))



   def test_isRedundantCCW(self):
      myList = RotationSequence()
      myList.addRotation(Rotation(Face.FRONT, Direction.CCW))
      myList.addRotation(Rotation(Face.FRONT, Direction.CCW))
      self.assertEqual(True, myList.isRedundant(Rotation(Face.FRONT, Direction.CCW)))


