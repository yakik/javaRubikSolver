import unittest
from production.utils.face import Face
from production.utils.face_handler import Face_handler
class FaceTest(unittest.TestCase):
    
        
   def test_FaceGetIntGetChar(self):
      myFace = "BOTTOM"

      self.assertEqual('D', Face_handler.getCharValue(myFace))
      myFace = "FRONT"
      self.assertEqual('F', Face_handler.getCharValue(myFace))
      myFace = "RIGHT"
      self.assertEqual('R', Face_handler.getCharValue(myFace))
      myFace = "TOP"
      self.assertEqual('U', Face_handler.getCharValue(myFace))
      myFace = "BACK"
      self.assertEqual('B', Face_handler.getCharValue(myFace))
      myFace = "LEFT"
      self.assertEqual('L', Face_handler.getCharValue(myFace))
        

        
   def test_FaceEquals(self):
      myFace = "BOTTOM"
      self.assertEqual("BOTTOM", myFace)
      self.assertEqual(True, myFace == "BOTTOM")
        

        
   def test_FaceGetOpposite(self):
      myFace = "BOTTOM"
      self.assertEqual("TOP", Face_handler.getOpposite(myFace))
      myFace = "FRONT"
      self.assertEqual("BACK", Face_handler.getOpposite(myFace))
      myFace = "RIGHT"
      self.assertEqual("LEFT", Face_handler.getOpposite(myFace))
      myFace = "TOP"
      self.assertEqual("BOTTOM", Face_handler.getOpposite(myFace))
      myFace = "BACK"
      self.assertEqual("FRONT", Face_handler.getOpposite(myFace))
      myFace = "LEFT"
      self.assertEqual("RIGHT", Face_handler.getOpposite(myFace))
   

    
