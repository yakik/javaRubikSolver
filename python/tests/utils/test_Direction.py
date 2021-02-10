import unittest
from production.utils.direction_handler import Direction_handler
class DirectionTest(unittest.TestCase):
   
   def test_DirectionGetIntGetChar(self):
      myDirection = "CW"
      self.assertEqual("CW", myDirection)
      self.assertEqual("CW", Direction_handler.getString(myDirection))
      myDirection = "CCW"
      self.assertEqual("CCW", myDirection)
      self.assertEqual("CCW", Direction_handler.getString(myDirection))
   
   def test_DirectionEquals(self):
      myDirection = "CW"
      self.assertEqual("CW", myDirection)
      self.assertEqual(True, myDirection == "CW")
   
   def test_DirectionOpposite(self):
      myDirection = "CW"
      self.assertEqual("CCW", Direction_handler.getOpposite(myDirection))
      myDirection = "CCW"
      self.assertEqual("CW", Direction_handler.getOpposite(myDirection))
        

    
