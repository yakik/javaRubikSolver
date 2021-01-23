import unittest
from production.utils.direction import Direction
from production.utils.direction_handler import Direction_handler
class DirectionTest(unittest.TestCase):
   
   def test_DirectionGetIntGetChar(self):
      myDirection = Direction.CW
      self.assertEqual(Direction.CW, myDirection)
      self.assertEqual("CW", Direction_handler.getString(myDirection))
      myDirection = Direction.CCW
      self.assertEqual(Direction.CCW, myDirection)
      self.assertEqual("CCW", Direction_handler.getString(myDirection))
   
   def test_DirectionEquals(self):
      myDirection = Direction.CW
      self.assertEqual(Direction.CW, myDirection)
      self.assertEqual(True, myDirection == Direction.CW)
   
   def test_DirectionOpposite(self):
      myDirection = Direction.CW
      self.assertEqual(Direction.CCW, Direction_handler.getOpposite(myDirection))
      myDirection = Direction.CCW
      self.assertEqual(Direction.CW, Direction_handler.getOpposite(myDirection))
        

    
