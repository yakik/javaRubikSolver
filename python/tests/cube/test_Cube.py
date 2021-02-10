from production.cube.cube import Cube
from production.utils.face import Face
from production.utils.location_in_face import Location_in_face

import unittest

class CubeTest(unittest.TestCase):
		
	def test_overallTest(self):
		myRubik = Cube()
		myRubik2 = Cube()
		myRubik.rotate_face(Face.FRONT, "CW")
		self.assertEqual(8, myRubik.count_all_differences(myRubik2))
		myRubik.rotate_face(Face.TOP, "CW")
		self.assertEqual(13, myRubik.count_all_differences(myRubik2))
		
	def test_compareFirstFloor(self):
		myRubik = Cube()
		myRubik2 = Cube()
		myRubik.set_color(Face.FRONT, Location_in_face.BOTTOMLEFT, "BACKCOLOR")
		myRubik.set_color(Face.BACK, Location_in_face.BOTTOM, "FRONTCOLOR")
		myRubik.set_color(Face.FRONT, Location_in_face.TOPLEFT, "BACKCOLOR")
		self.assertEqual(2, myRubik.count_difference_first_floor(myRubik2))
		myRubik.set_color(Face.LEFT, Location_in_face.BOTTOMLEFT, "BACKCOLOR")
		self.assertEqual(3, myRubik.count_difference_first_floor(myRubik2))
		
	def test_rotateFrontClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.FRONT, "CW")
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOM))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.FRONT, "CW")
		myRubik.rotate_face(Face.FRONT, "CW")
		myRubik.rotate_face(Face.FRONT, "CW")
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
	
	def test_rotateLeftClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.LEFT, "CW")
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.TOP, Location_in_face.LEFT))
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.LEFT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.LEFT, "CW")
		myRubik.rotate_face(Face.LEFT, "CW")
		myRubik.rotate_face(Face.LEFT, "CW")
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.LEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.LEFT, Location_in_face.BOTTOMLEFT))

	def test_rotateRightClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.RIGHT, "CW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.RIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.RIGHT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.RIGHT, "CW")
		myRubik.rotate_face(Face.RIGHT, "CW")
		myRubik.rotate_face(Face.RIGHT, "CW")
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.RIGHT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.RIGHT, Location_in_face.BOTTOMLEFT))
	
	def test_rotateBackClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.BACK, "CW")
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOP))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.BACK, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.BACK, "CW")
		myRubik.rotate_face(Face.BACK, "CW")
		myRubik.rotate_face(Face.BACK, "CW")
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOP))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.BACK, Location_in_face.BOTTOMLEFT))
	
	def test_rotateTopClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.TOP, "CW")
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOP))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOPRIGHT))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOPLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.TOP, "CW")
		myRubik.rotate_face(Face.TOP, "CW")
		myRubik.rotate_face(Face.TOP, "CW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOP))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOPRIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOPLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
	
	def test_rotateBottomClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.BOTTOM, "CW")
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOM))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		self.assertEqual("BOTTOMCOLOR", myRubik.get_color(Face.BOTTOM, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.BOTTOM, "CW")
		myRubik.rotate_face(Face.BOTTOM, "CW")
		myRubik.rotate_face(Face.BOTTOM, "CW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOM))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		self.assertEqual("BOTTOMCOLOR", myRubik.get_color(Face.BOTTOM, Location_in_face.BOTTOMLEFT))

	def test_rotateFrontCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.FRONT, "CCW")
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOM))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.FRONT, "CCW")
		myRubik.rotate_face(Face.FRONT, "CCW")
		myRubik.rotate_face(Face.FRONT, "CCW")
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))

	def test_rotateLeftCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.LEFT, "CCW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.LEFT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.LEFT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.LEFT, "CCW")
		myRubik.rotate_face(Face.LEFT, "CCW")
		myRubik.rotate_face(Face.LEFT, "CCW")
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.LEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.LEFT, Location_in_face.BOTTOMLEFT))
	
	def test_rotateRightCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.RIGHT, "CCW")
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.TOP, Location_in_face.RIGHT))
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.RIGHT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.RIGHT, "CCW")
		myRubik.rotate_face(Face.RIGHT, "CCW")
		myRubik.rotate_face(Face.RIGHT, "CCW")
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.RIGHT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.RIGHT, Location_in_face.BOTTOMLEFT))
	
	def test_rotateBackCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.BACK, "CCW")
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOP))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.BACK, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.BACK, "CCW")
		myRubik.rotate_face(Face.BACK, "CCW")
		myRubik.rotate_face(Face.BACK, "CCW")
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOP))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual("BACKCOLOR", myRubik.get_color(Face.BACK, Location_in_face.BOTTOMLEFT))
	
	def test_rotateTopCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.TOP, "CCW")
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOP))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOPRIGHT))
		self.assertEqual("LEFTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOPLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.TOP, "CCW")
		myRubik.rotate_face(Face.TOP, "CCW")
		myRubik.rotate_face(Face.TOP, "CCW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOP))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOPRIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.TOPLEFT))
		self.assertEqual("TOPCOLOR", myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
	
	def test_rotateBottomCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.BOTTOM, "CCW")
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOM))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		self.assertEqual("BOTTOMCOLOR", myRubik.get_color(Face.BOTTOM, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.BOTTOM, "CCW")
		myRubik.rotate_face(Face.BOTTOM, "CCW")
		myRubik.rotate_face(Face.BOTTOM, "CCW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOM))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMRIGHT))
		self.assertEqual("FRONTCOLOR", myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		self.assertEqual("BOTTOMCOLOR", myRubik.get_color(Face.BOTTOM, Location_in_face.BOTTOMLEFT))
	
	def test_simpleRotations(self):
			myRubik = Cube()
			for i in range(0,20):
				myRubik.rotate_face(Face.TOP, "CW")
				myRubik.rotate_face(Face.RIGHT, "CW")
				myRubik.rotate_face(Face.LEFT, "CW")
				myRubik.rotate_face(Face.BOTTOM, "CW")
				myRubik.rotate_face(Face.RIGHT, "CW")
				myRubik.rotate_face(Face.TOP, "CW")
				myRubik.rotate_face(Face.RIGHT, "CW")
				myRubik.rotate_face(Face.BACK, "CW")
				myRubik.rotate_face(Face.LEFT, "CW")
				myRubik.rotate_face(Face.FRONT, "CW")
			
			for i in range(0,20):
				myRubik.rotate_face(Face.FRONT, "CCW")
				myRubik.rotate_face(Face.LEFT, "CCW")
				myRubik.rotate_face(Face.BACK, "CCW")
				myRubik.rotate_face(Face.RIGHT, "CCW")
				myRubik.rotate_face(Face.TOP, "CCW")
				myRubik.rotate_face(Face.RIGHT, "CCW")
				myRubik.rotate_face(Face.BOTTOM, "CCW")
				myRubik.rotate_face(Face.LEFT, "CCW")
				myRubik.rotate_face(Face.RIGHT, "CCW")
				myRubik.rotate_face(Face.TOP, "CCW")
			
			myRubik.rotate_face(Face.FRONT, "CW")
			myRubik.rotate_face(Face.FRONT, "CCW")
			self.assertTrue(myRubik.equals(Cube()))