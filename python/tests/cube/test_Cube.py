from production.cube.cube import Cube
from production.utils.location_in_face_handler import Location_in_face_handler

import unittest

class CubeTest(unittest.TestCase):
		
	def test_overallTest(self):
		myRubik = Cube()
		myRubik2 = Cube()
		myRubik.rotate_face("FRONT", "CW")
		self.assertEqual(8, myRubik.count_all_differences(myRubik2))
		myRubik.rotate_face("TOP", "CW")
		self.assertEqual(13, myRubik.count_all_differences(myRubik2))
		
	def test_compareFirstFloor(self):
		myRubik = Cube()
		myRubik2 = Cube()
		myRubik.set_color("FRONT", "LIF_BOTTOMLEFT", "BACKCOLOR")
		myRubik.set_color("BACK", "LIF_BOTTOM", "FRONTCOLOR")
		myRubik.set_color("FRONT", "LIF_TOPLEFT", "BACKCOLOR")
		self.assertEqual(2, myRubik.count_difference_first_floor(myRubik2))
		myRubik.set_color("LEFT", "LIF_BOTTOMLEFT", "BACKCOLOR")
		self.assertEqual(3, myRubik.count_difference_first_floor(myRubik2))
		
	def test_rotateFrontClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("FRONT", "CW")
		self.assertEqual("LEFTCOLOR", myRubik.get_color("TOP", "LIF_BOTTOM"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMRIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("FRONT", "CW")
		myRubik.rotate_face("FRONT", "CW")
		myRubik.rotate_face("FRONT", "CW")
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMRIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMLEFT"))
	
	def test_rotateLeftClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("LEFT", "CW")
		self.assertEqual("BACKCOLOR", myRubik.get_color("TOP", "LIF_LEFT"))
		self.assertEqual("BACKCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("BACKCOLOR", myRubik.get_color("TOP", "LIF_TOPLEFT"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("LEFT", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("LEFT", "CW")
		myRubik.rotate_face("LEFT", "CW")
		myRubik.rotate_face("LEFT", "CW")
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_LEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOPLEFT"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("LEFT", "LIF_BOTTOMLEFT"))

	def test_rotateRightClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("RIGHT", "CW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color("TOP", "LIF_RIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMRIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("TOP", "LIF_TOPRIGHT"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("RIGHT", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("RIGHT", "CW")
		myRubik.rotate_face("RIGHT", "CW")
		myRubik.rotate_face("RIGHT", "CW")
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_RIGHT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMRIGHT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOPRIGHT"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("RIGHT", "LIF_BOTTOMLEFT"))
	
	def test_rotateBackClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("BACK", "CW")
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("TOP", "LIF_TOP"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("TOP", "LIF_TOPRIGHT"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("TOP", "LIF_TOPLEFT"))
		self.assertEqual("BACKCOLOR", myRubik.get_color("BACK", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("BACK", "CW")
		myRubik.rotate_face("BACK", "CW")
		myRubik.rotate_face("BACK", "CW")
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOP"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOPRIGHT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOPLEFT"))
		self.assertEqual("BACKCOLOR", myRubik.get_color("BACK", "LIF_BOTTOMLEFT"))
	
	def test_rotateTopClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("TOP", "CW")
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("FRONT", "LIF_TOP"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("FRONT", "LIF_TOPRIGHT"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("FRONT", "LIF_TOPLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("TOP", "CW")
		myRubik.rotate_face("TOP", "CW")
		myRubik.rotate_face("TOP", "CW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_TOP"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_TOPRIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_TOPLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
	
	def test_rotateBottomClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("BOTTOM", "CW")
		self.assertEqual("LEFTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOM"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMRIGHT"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMLEFT"))
		self.assertEqual("BOTTOMCOLOR", myRubik.get_color("BOTTOM", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("BOTTOM", "CW")
		myRubik.rotate_face("BOTTOM", "CW")
		myRubik.rotate_face("BOTTOM", "CW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOM"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMRIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMLEFT"))
		self.assertEqual("BOTTOMCOLOR", myRubik.get_color("BOTTOM", "LIF_BOTTOMLEFT"))

	def test_rotateFrontCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("FRONT", "CCW")
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("TOP", "LIF_BOTTOM"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMRIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("FRONT", "CCW")
		myRubik.rotate_face("FRONT", "CCW")
		myRubik.rotate_face("FRONT", "CCW")
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMRIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMLEFT"))

	def test_rotateLeftCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("LEFT", "CCW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color("TOP", "LIF_LEFT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("TOP", "LIF_TOPLEFT"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("LEFT", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("LEFT", "CCW")
		myRubik.rotate_face("LEFT", "CCW")
		myRubik.rotate_face("LEFT", "CCW")
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_LEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOPLEFT"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("LEFT", "LIF_BOTTOMLEFT"))
	
	def test_rotateRightCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("RIGHT", "CCW")
		self.assertEqual("BACKCOLOR", myRubik.get_color("TOP", "LIF_RIGHT"))
		self.assertEqual("BACKCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMRIGHT"))
		self.assertEqual("BACKCOLOR", myRubik.get_color("TOP", "LIF_TOPRIGHT"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("RIGHT", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("RIGHT", "CCW")
		myRubik.rotate_face("RIGHT", "CCW")
		myRubik.rotate_face("RIGHT", "CCW")
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_RIGHT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMRIGHT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOPRIGHT"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("RIGHT", "LIF_BOTTOMLEFT"))
	
	def test_rotateBackCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("BACK", "CCW")
		self.assertEqual("LEFTCOLOR", myRubik.get_color("TOP", "LIF_TOP"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("TOP", "LIF_TOPRIGHT"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("TOP", "LIF_TOPLEFT"))
		self.assertEqual("BACKCOLOR", myRubik.get_color("BACK", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("BACK", "CCW")
		myRubik.rotate_face("BACK", "CCW")
		myRubik.rotate_face("BACK", "CCW")
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOP"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOPRIGHT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_TOPLEFT"))
		self.assertEqual("BACKCOLOR", myRubik.get_color("BACK", "LIF_BOTTOMLEFT"))
	
	def test_rotateTopCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("TOP", "CCW")
		self.assertEqual("LEFTCOLOR", myRubik.get_color("FRONT", "LIF_TOP"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("FRONT", "LIF_TOPRIGHT"))
		self.assertEqual("LEFTCOLOR", myRubik.get_color("FRONT", "LIF_TOPLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("TOP", "CCW")
		myRubik.rotate_face("TOP", "CCW")
		myRubik.rotate_face("TOP", "CCW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_TOP"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_TOPRIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_TOPLEFT"))
		self.assertEqual("TOPCOLOR", myRubik.get_color("TOP", "LIF_BOTTOMLEFT"))
	
	def test_rotateBottomCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face("BOTTOM", "CCW")
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOM"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMRIGHT"))
		self.assertEqual("RIGHTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMLEFT"))
		self.assertEqual("BOTTOMCOLOR", myRubik.get_color("BOTTOM", "LIF_BOTTOMLEFT"))
		myRubik.rotate_face("BOTTOM", "CCW")
		myRubik.rotate_face("BOTTOM", "CCW")
		myRubik.rotate_face("BOTTOM", "CCW")
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOM"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMRIGHT"))
		self.assertEqual("FRONTCOLOR", myRubik.get_color("FRONT", "LIF_BOTTOMLEFT"))
		self.assertEqual("BOTTOMCOLOR", myRubik.get_color("BOTTOM", "LIF_BOTTOMLEFT"))
	
	def test_simpleRotations(self):
			myRubik = Cube()
			for i in range(0,20):
				myRubik.rotate_face("TOP", "CW")
				myRubik.rotate_face("RIGHT", "CW")
				myRubik.rotate_face("LEFT", "CW")
				myRubik.rotate_face("BOTTOM", "CW")
				myRubik.rotate_face("RIGHT", "CW")
				myRubik.rotate_face("TOP", "CW")
				myRubik.rotate_face("RIGHT", "CW")
				myRubik.rotate_face("BACK", "CW")
				myRubik.rotate_face("LEFT", "CW")
				myRubik.rotate_face("FRONT", "CW")
			
			for i in range(0,20):
				myRubik.rotate_face("FRONT", "CCW")
				myRubik.rotate_face("LEFT", "CCW")
				myRubik.rotate_face("BACK", "CCW")
				myRubik.rotate_face("RIGHT", "CCW")
				myRubik.rotate_face("TOP", "CCW")
				myRubik.rotate_face("RIGHT", "CCW")
				myRubik.rotate_face("BOTTOM", "CCW")
				myRubik.rotate_face("LEFT", "CCW")
				myRubik.rotate_face("RIGHT", "CCW")
				myRubik.rotate_face("TOP", "CCW")
			
			myRubik.rotate_face("FRONT", "CW")
			myRubik.rotate_face("FRONT", "CCW")
			self.assertTrue(myRubik.equals(Cube()))