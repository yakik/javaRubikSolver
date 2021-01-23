import unittest
from production.utils.face import Face
from production.utils.face_handler import Face_handler
class FaceTest(unittest.TestCase):
    
        
   def test_FaceGetIntGetChar(self):
      myFace = Face.BOTTOM
      self.assertEqual(1,myFace)
      self.assertEqual('D', Face_handler.getCharValue(myFace))
      myFace = Face.FRONT
      self.assertEqual(4, myFace)
      self.assertEqual('F', Face_handler.getCharValue(myFace))
      myFace = Face.RIGHT
      self.assertEqual(2, myFace)
      self.assertEqual('R', Face_handler.getCharValue(myFace))
      myFace = Face.TOP
      self.assertEqual(0, myFace)
      self.assertEqual('U', Face_handler.getCharValue(myFace))
      myFace = Face.BACK
      self.assertEqual(5, myFace)
      self.assertEqual('B', Face_handler.getCharValue(myFace))
      myFace = Face.LEFT
      self.assertEqual(3, myFace)
      self.assertEqual('L', Face_handler.getCharValue(myFace))
        

        
   def test_FaceEquals(self):
      myFace = Face.BOTTOM
      self.assertEqual(Face.BOTTOM, myFace)
      self.assertEqual(True, myFace == Face.BOTTOM)
        

        
   def test_FaceGetOpposite(self):
      myFace = Face.BOTTOM
      self.assertEqual(Face.TOP, Face_handler.getOpposite(myFace))
      myFace = Face.FRONT
      self.assertEqual(Face.BACK, Face_handler.getOpposite(myFace))
      myFace = Face.RIGHT
      self.assertEqual(Face.LEFT, Face_handler.getOpposite(myFace))
      myFace = Face.TOP
      self.assertEqual(Face.BOTTOM, Face_handler.getOpposite(myFace))
      myFace = Face.BACK
      self.assertEqual(Face.FRONT, Face_handler.getOpposite(myFace))
      myFace = Face.LEFT
      self.assertEqual(Face.RIGHT, Face_handler.getOpposite(myFace))
   

    
