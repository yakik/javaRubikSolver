import unittest
using utils




    
    class DirectionTest(unittest.TestCase):
    
        
        def testDirectionGetIntGetChar(self):
            Direction myDirection = Direction.CW
            Assert.AreEqual(0, (int)myDirection)
            Assert.AreEqual("CW", myDirection.getString())
            myDirection = Direction.CCW
            Assert.AreEqual(1,(int) myDirection)
            Assert.AreEqual("CCW", myDirection.getString())
        

        
        def testDirectionEquals(self):
            Direction myDirection = Direction.CW
            Assert.AreEqual(Direction.CW, myDirection)
            Assert.AreEqual(true, myDirection == Direction.CW)
        
        
        def DirectionOpposite(self):
            Direction myDirection = Direction.CW
            Assert.AreEqual(Direction.CCW, DirectionHandler.getOpposite(myDirection))
            myDirection = Direction.CCW
            Assert.AreEqual(Direction.CW, DirectionHandler.getOpposite(myDirection))
        

    
