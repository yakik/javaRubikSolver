from production.utils.position import Position

import unittest
class PositionTest(unittest.TestCase):
        
        def getString(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            self.assertEqual("U, F", myPosition.getString())
        

        
        def rotateCW_U(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CW))
            self.assertEqual(Face.LEFT, myPosition.getFace(Face.TOP))
        

        
        def rotateCW_D(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CW))
            self.assertEqual(Face.RIGHT, myPosition.getFace(Face.BOTTOM))
        

        
        def rotateCCW(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CCW))
            self.assertEqual(Face.RIGHT, myPosition.getFace(Face.TOP))
        

        
        def rotateCCW_D(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.FRONT, Direction.CCW))
            self.assertEqual(Face.LEFT, myPosition.getFace(Face.BOTTOM))
        

        
        def moreRotationTests(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.LEFT, Direction.CW))
            self.assertEqual(True, myPosition.equals(Position(Face.BACK, Face.TOP)))
            myPosition.rotate(Rotation(Face.BOTTOM, Direction.CW))
            self.assertEqual(True, myPosition.equals(Position(Face.BACK, Face.LEFT)))
            myPosition.rotate(Rotation(Face.BOTTOM, Direction.CCW))
            self.assertEqual(True, myPosition.equals(Position(Face.BACK, Face.TOP)))
        

        
        def rotateCCW_DD(self):
            myPosition = Position(Face.TOP, Face.FRONT)
            myPosition.rotate(Rotation(Face.BOTTOM, Direction.CCW))
            self.assertEqual(Face.BOTTOM, myPosition.getFace(Face.BOTTOM))
        
     