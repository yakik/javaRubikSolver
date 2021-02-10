from production.utils.position import Position
from production.utils.face import Face
from production.utils.rotation import Rotation


import unittest
class PositionTest(unittest.TestCase):
        
        def test_getString(self):
            myPosition = Position("TOP", "FRONT")
            self.assertEqual("U, F", myPosition.getString())
        
        def test_rotateCW_U(self):
            myPosition = Position("TOP", "FRONT")
            myPosition.rotate(Rotation("FRONT", "CW"))
            self.assertEqual("LEFT", myPosition.getFace("TOP"))
        
        def test_rotateCW_D(self):
            myPosition = Position("TOP", "FRONT")
            myPosition.rotate(Rotation("FRONT", "CW"))
            self.assertEqual("RIGHT", myPosition.getFace("BOTTOM"))
        
        def test_rotateCCW(self):
            myPosition = Position("TOP", "FRONT")
            myPosition.rotate(Rotation("FRONT", "CCW"))
            self.assertEqual("RIGHT", myPosition.getFace("TOP"))
        
        def test_rotateCCW_D(self):
            myPosition = Position("TOP", "FRONT")
            myPosition.rotate(Rotation("FRONT", "CCW"))
            self.assertEqual("LEFT", myPosition.getFace("BOTTOM"))
        
        def test_moreRotationTests(self):
            myPosition = Position("TOP", "FRONT")
            myPosition.rotate(Rotation("LEFT", "CW"))
            self.assertEqual(True, myPosition.equals(Position("BACK", "TOP")))
            myPosition.rotate(Rotation("BOTTOM", "CW"))
            self.assertEqual(True, myPosition.equals(Position("BACK", "LEFT")))
            myPosition.rotate(Rotation("BOTTOM", "CCW"))
            self.assertEqual(True, myPosition.equals(Position("BACK", "TOP")))
        
        def test_rotateCCW_DD(self):
            myPosition = Position("TOP", "FRONT")
            myPosition.rotate(Rotation("BOTTOM", "CCW"))
            self.assertEqual("BOTTOM", myPosition.getFace("BOTTOM"))