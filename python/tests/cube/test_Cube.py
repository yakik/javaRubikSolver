from production.cube.cube import Cube
from production.solver.solver import Solver
from production.utils.face import Face
from production.utils.direction import Direction
from production.utils.location_in_face import Location_in_face
from production.utils.color import Color

import unittest

class CubeTest(unittest.TestCase):
		
	def test_overallTest(self):
		myRubik = Cube()
		myRubik2 = Cube()
		myRubik.rotate_face(Face.FRONT, Direction.CW)
		self.assertEqual(8, myRubik.count_all_differences(myRubik2))
		myRubik.rotate_face(Face.TOP, Direction.CW)
		self.assertEqual(13, myRubik.count_all_differences(myRubik2))
		
	def test_compareFirstFloor(self):
		myRubik = Cube()
		myRubik2 = Cube()
		myRubik.set_color(Face.FRONT, Location_in_face.BOTTOMLEFT, Color.BACKCOLOR)
		myRubik.set_color(Face.BACK, Location_in_face.BOTTOM, Color.FRONTCOLOR)
		myRubik.set_color(Face.FRONT, Location_in_face.TOPLEFT, Color.BACKCOLOR)
		self.assertEqual(2, myRubik.count_difference_first_floor(myRubik2))
		myRubik.set_color(Face.LEFT, Location_in_face.BOTTOMLEFT, Color.BACKCOLOR)
		self.assertEqual(3, myRubik.count_difference_first_floor(myRubik2))
		
	def test_rotateFrontClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.FRONT, Direction.CW)
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOM))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.FRONT, Direction.CW)
		myRubik.rotate_face(Face.FRONT, Direction.CW)
		myRubik.rotate_face(Face.FRONT, Direction.CW)
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
	
	def test_rotateLeftClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.LEFT, Direction.CW)
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.TOP, Location_in_face.LEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.LEFT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.LEFT, Direction.CW)
		myRubik.rotate_face(Face.LEFT, Direction.CW)
		myRubik.rotate_face(Face.LEFT, Direction.CW)
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.LEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.LEFT, Location_in_face.BOTTOMLEFT))

	def test_rotateRightClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.RIGHT, Direction.CW)
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.RIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.RIGHT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.RIGHT, Direction.CW)
		myRubik.rotate_face(Face.RIGHT, Direction.CW)
		myRubik.rotate_face(Face.RIGHT, Direction.CW)
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.RIGHT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.RIGHT, Location_in_face.BOTTOMLEFT))
	
	def test_rotateBackClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.BACK, Direction.CW)
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOP))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.BACK, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.BACK, Direction.CW)
		myRubik.rotate_face(Face.BACK, Direction.CW)
		myRubik.rotate_face(Face.BACK, Direction.CW)
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOP))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.BACK, Location_in_face.BOTTOMLEFT))
	
	def test_rotateTopClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.TOP, Direction.CW)
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOP))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOPLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.TOP, Direction.CW)
		myRubik.rotate_face(Face.TOP, Direction.CW)
		myRubik.rotate_face(Face.TOP, Direction.CW)
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOP))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOPLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
	
	def test_rotateBottomClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.BOTTOM, Direction.CW)
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOM))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.BOTTOMCOLOR, myRubik.get_color(Face.BOTTOM, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.BOTTOM, Direction.CW)
		myRubik.rotate_face(Face.BOTTOM, Direction.CW)
		myRubik.rotate_face(Face.BOTTOM, Direction.CW)
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOM))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.BOTTOMCOLOR, myRubik.get_color(Face.BOTTOM, Location_in_face.BOTTOMLEFT))

	def test_rotateFrontCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.FRONT, Direction.CCW)
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOM))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.FRONT, Direction.CCW)
		myRubik.rotate_face(Face.FRONT, Direction.CCW)
		myRubik.rotate_face(Face.FRONT, Direction.CCW)
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))

	def test_rotateLeftCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.LEFT, Direction.CCW)
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.LEFT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.LEFT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.LEFT, Direction.CCW)
		myRubik.rotate_face(Face.LEFT, Direction.CCW)
		myRubik.rotate_face(Face.LEFT, Direction.CCW)
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.LEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.LEFT, Location_in_face.BOTTOMLEFT))
	
	def test_rotateRightCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.RIGHT, Direction.CCW)
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.TOP, Location_in_face.RIGHT))
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.RIGHT, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.RIGHT, Direction.CCW)
		myRubik.rotate_face(Face.RIGHT, Direction.CCW)
		myRubik.rotate_face(Face.RIGHT, Direction.CCW)
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.RIGHT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.RIGHT, Location_in_face.BOTTOMLEFT))
	
	def test_rotateBackCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.BACK, Direction.CCW)
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOP))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.BACK, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.BACK, Direction.CCW)
		myRubik.rotate_face(Face.BACK, Direction.CCW)
		myRubik.rotate_face(Face.BACK, Direction.CCW)
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOP))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.TOPLEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.get_color(Face.BACK, Location_in_face.BOTTOMLEFT))
	
	def test_rotateTopCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.TOP, Direction.CCW)
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOP))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOPLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.TOP, Direction.CCW)
		myRubik.rotate_face(Face.TOP, Direction.CCW)
		myRubik.rotate_face(Face.TOP, Direction.CCW)
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOP))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOPRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.TOPLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.get_color(Face.TOP, Location_in_face.BOTTOMLEFT))
	
	def test_rotateBottomCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotate_face(Face.BOTTOM, Direction.CCW)
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOM))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.BOTTOMCOLOR, myRubik.get_color(Face.BOTTOM, Location_in_face.BOTTOMLEFT))
		myRubik.rotate_face(Face.BOTTOM, Direction.CCW)
		myRubik.rotate_face(Face.BOTTOM, Direction.CCW)
		myRubik.rotate_face(Face.BOTTOM, Direction.CCW)
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOM))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.get_color(Face.FRONT, Location_in_face.BOTTOMLEFT))
		self.assertEqual(Color.BOTTOMCOLOR, myRubik.get_color(Face.BOTTOM, Location_in_face.BOTTOMLEFT))
	
	def test_simpleRotations(self):
			myRubik = Cube()
			for i in range(0,20):
				myRubik.rotate_face(Face.TOP, Direction.CW)
				myRubik.rotate_face(Face.RIGHT, Direction.CW)
				myRubik.rotate_face(Face.LEFT, Direction.CW)
				myRubik.rotate_face(Face.BOTTOM, Direction.CW)
				myRubik.rotate_face(Face.RIGHT, Direction.CW)
				myRubik.rotate_face(Face.TOP, Direction.CW)
				myRubik.rotate_face(Face.RIGHT, Direction.CW)
				myRubik.rotate_face(Face.BACK, Direction.CW)
				myRubik.rotate_face(Face.LEFT, Direction.CW)
				myRubik.rotate_face(Face.FRONT, Direction.CW)
			
			for i in range(0,20):
				myRubik.rotate_face(Face.FRONT, Direction.CCW)
				myRubik.rotate_face(Face.LEFT, Direction.CCW)
				myRubik.rotate_face(Face.BACK, Direction.CCW)
				myRubik.rotate_face(Face.RIGHT, Direction.CCW)
				myRubik.rotate_face(Face.TOP, Direction.CCW)
				myRubik.rotate_face(Face.RIGHT, Direction.CCW)
				myRubik.rotate_face(Face.BOTTOM, Direction.CCW)
				myRubik.rotate_face(Face.LEFT, Direction.CCW)
				myRubik.rotate_face(Face.RIGHT, Direction.CCW)
				myRubik.rotate_face(Face.TOP, Direction.CCW)
			
			myRubik.rotate_face(Face.FRONT, Direction.CW)
			myRubik.rotate_face(Face.FRONT, Direction.CCW)
			self.assertTrue(myRubik.equals(Cube()))