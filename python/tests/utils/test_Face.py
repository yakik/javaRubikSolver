import unittest
from production.utils.face import Face
from production.utils.face_handler import FaceHandler
class FaceTest(unittest.TestCase):
    
        
   def test_FaceGetIntGetChar(self):
      myFace = Face.BOTTOM
      self.assertEqual(1,myFace)
      self.assertEqual('D', FaceHandler.getCharValue(myFace))
      myFace = Face.FRONT
      self.assertEqual(4, myFace)
      self.assertEqual('F', FaceHandler.getCharValue(myFace))
      myFace = Face.RIGHT
      self.assertEqual(2, myFace)
      self.assertEqual('R', FaceHandler.getCharValue(myFace))
      myFace = Face.TOP
      self.assertEqual(0, myFace)
      self.assertEqual('U', FaceHandler.getCharValue(myFace))
      myFace = Face.BACK
      self.assertEqual(5, myFace)
      self.assertEqual('B', FaceHandler.getCharValue(myFace))
      myFace = Face.LEFT
      self.assertEqual(3, myFace)
      self.assertEqual('L', FaceHandler.getCharValue(myFace))
        

        
   def test_FaceEquals(self):
      myFace = Face.BOTTOM
      self.assertEqual(Face.BOTTOM, myFace)
      self.assertEqual(True, myFace == Face.BOTTOM)
        

        
   def test_FaceGetOpposite(self):
      myFace = Face.BOTTOM
      self.assertEqual(Face.TOP, FaceHandler.getOpposite(myFace))
      myFace = Face.FRONT
      self.assertEqual(Face.BACK, FaceHandler.getOpposite(myFace))
      myFace = Face.RIGHT
      self.assertEqual(Face.LEFT, FaceHandler.getOpposite(myFace))
      myFace = Face.TOP
      self.assertEqual(Face.BOTTOM, FaceHandler.getOpposite(myFace))
      myFace = Face.BACK
      self.assertEqual(Face.FRONT, FaceHandler.getOpposite(myFace))
      myFace = Face.LEFT
      self.assertEqual(Face.RIGHT, FaceHandler.getOpposite(myFace))
   

    
