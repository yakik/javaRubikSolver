import unittest
class DirectionTest(unittest.TestCase):
    
        
        def testDirectionGetIntGetChar(self):
           myDirection = Direction.CW
            self.assertEqual(0, (int)myDirection)
            self.assertEqual("CW", myDirection.getString())
            myDirection = Direction.CCW
            self.assertEqual(1,(int) myDirection)
            self.assertEqual("CCW", myDirection.getString())
        

        
        def testDirectionEquals(self):
           myDirection = Direction.CW
            self.assertEqual(Direction.CW, myDirection)
            self.assertEqual(True, myDirection == Direction.CW)
        
        
        def DirectionOpposite(self):
           myDirection = Direction.CW
            self.assertEqual(Direction.CCW, DirectionHandler.getOpposite(myDirection))
            myDirection = Direction.CCW
            self.assertEqual(Direction.CW, DirectionHandler.getOpposite(myDirection))
        

    
