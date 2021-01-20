import unittest
class PositionTest(unittest.TestCase):
    

        
        def getString(self):
            Position myPosition = Position(Face.TOP, Face.FRONT)
            Assert.AreEqual("U, F", myPosition.getString())
        

        
        def rotateCW_U(self):
            Position myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CW))
            Assert.AreEqual(Face.LEFT, myPosition.getFace(Face.TOP))
        

        
        def rotateCW_D(self):
            Position myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CW))
            Assert.AreEqual(Face.RIGHT, myPosition.getFace(Face.BOTTOM))
        

        
        def rotateCCW(self):
            Position myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CCW))
            Assert.AreEqual(Face.RIGHT, myPosition.getFace(Face.TOP))
        

        
        def rotateCCW_D(self):
            Position myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CCW))
            Assert.AreEqual(Face.LEFT, myPosition.getFace(Face.BOTTOM))
        

        
        def moreRotationTests(self):
            Position myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.LEFT, Direction.CW))
            Assert.AreEqual(True, myPosition.equals(Position(Face.BACK, Face.TOP)))
            myPosition.rotate(Rotation(Face.BOTTOM, Direction.CW))
            Assert.AreEqual(True, myPosition.equals(Position(Face.BACK, Face.LEFT)))
            myPosition.rotate(Rotation(Face.BOTTOM, Direction.CCW))
            Assert.AreEqual(True, myPosition.equals(Position(Face.BACK, Face.TOP)))
        

        
        def rotateCCW_DD(self):
            Position myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.BOTTOM, Direction.CCW))
            Assert.AreEqual(Face.BOTTOM, myPosition.getFace(Face.BOTTOM))
        
     