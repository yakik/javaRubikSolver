import unittest
from production.solver.rotation_sequence import Rotation_sequence
from production.utils.rotation import Rotation
from production.utils.face import Face
from production.utils.direction import Direction

class RotationLinkedListTest(unittest.TestCase):
   def test_is_redundantCW(self):
      myList = Rotation_sequence()
      myList.add_rotation(Rotation(Face.FRONT, Direction.CW))
      self.assertEqual(True, myList.is_redundant(Rotation(Face.FRONT, Direction.CW)))

   def test_is_redundantCCW(self):
      myList = Rotation_sequence()
      myList.add_rotation(Rotation(Face.FRONT, Direction.CCW))
      myList.add_rotation(Rotation(Face.FRONT, Direction.CCW))
      self.assertEqual(True, myList.is_redundant(Rotation(Face.FRONT, Direction.CCW)))


