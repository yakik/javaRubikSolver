import unittest
from production.solver.rotation_sequence import Rotation_sequence
from production.utils.rotation import Rotation
from production.utils.face import Face

class RotationLinkedListTest(unittest.TestCase):
   def test_is_redundantCW(self):
      myList = Rotation_sequence()
      myList.add_rotation(Rotation("FRONT", "CW"))
      self.assertEqual(True, myList.is_redundant(Rotation("FRONT", "CW")))

   def test_is_redundantCCW(self):
      myList = Rotation_sequence()
      myList.add_rotation(Rotation("FRONT", "CCW"))
      myList.add_rotation(Rotation("FRONT", "CCW"))
      self.assertEqual(True, myList.is_redundant(Rotation("FRONT", "CCW")))


