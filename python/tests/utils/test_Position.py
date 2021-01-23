from production.utils.position import Position
from production.utils.face import Face
from production.utils.rotation import Rotation
from production.utils.direction import Direction
from production.utils.face_handler import FaceHandler

import unittest
class PositionTest(unittest.TestCase):
        
        def test_getString(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            self.assertEqual("U, F", myPosition.getString())
        
        def test_rotateCW_U(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CW))
            self.assertEqual(Face.LEFT, myPosition.getFace(Face.TOP))
        
        def test_rotateCW_D(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CW))
            self.assertEqual(Face.RIGHT, myPosition.getFace(Face.BOTTOM))
        
        def test_rotateCCW(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CCW))
            self.assertEqual(Face.RIGHT, myPosition.getFace(Face.TOP))
        
        def test_rotateCCW_D(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CCW))
            self.assertEqual(Face.LEFT, myPosition.getFace(Face.BOTTOM))
        
        def test_moreRotationTests(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.LEFT, Direction.CW))
            self.assertEqual(True, myPosition.equals(Position(Face.BACK, Face.TOP)))
            myPosition.rotate(Rotation(Face.BOTTOM, Direction.CW))
            self.assertEqual(True, myPosition.equals(Position(Face.BACK, Face.LEFT)))
            myPosition.rotate(Rotation(Face.BOTTOM, Direction.CCW))
            self.assertEqual(True, myPosition.equals(Position(Face.BACK, Face.TOP)))
        
        def test_rotateCCW_DD(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.BOTTOM, Direction.CCW))
            self.assertEqual(Face.BOTTOM, myPosition.getFace(Face.BOTTOM))