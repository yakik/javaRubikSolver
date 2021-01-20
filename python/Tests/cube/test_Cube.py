from production.cube.cube import Cube
from production.solver.solver import Solver
from production.utils.face import Face
from production.utils.direction import Direction
from production.utils.locationInFace import LocationInFace
from production.utils.color import Color



import unittest

class CubeTest(unittest.TestCase):
		
	def test_overallTest(self):
		myRubik = Cube()
		myRubik2 = Cube()
		myRubik.rotateFace(Face.FRONT, Direction.CW)
		self.assertEqual(8, myRubik.countAllDifferences(myRubik2))
		myRubik.rotateFace(Face.TOP, Direction.CW)
		self.assertEqual(13, myRubik.countAllDifferences(myRubik2))
		

		
	def test_compareFirstFloor(self):
		myRubik = Cube()
		myRubik2 = Cube()
		myRubik.setColor(Face.FRONT, LocationInFace.BOTTOMLEFT, Color.BACKCOLOR)
		myRubik.setColor(Face.BACK, LocationInFace.BOTTOM, Color.FRONTCOLOR)
		myRubik.setColor(Face.FRONT, LocationInFace.TOPLEFT, Color.BACKCOLOR)
		self.assertEqual(2, myRubik.countDifferenceFirstFloor(myRubik2))
		myRubik.setColor(Face.LEFT, LocationInFace.BOTTOMLEFT, Color.BACKCOLOR)
		self.assertEqual(3, myRubik.countDifferenceFirstFloor(myRubik2))


		
		
	def test_rotateFrontClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.FRONT, Direction.CW)
		self.assertEqual(Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOM))
		self.assertEqual(Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.FRONT, Direction.CW)
		myRubik.rotateFace(Face.FRONT, Direction.CW)
		myRubik.rotateFace(Face.FRONT, Direction.CW)
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateLeftClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.LEFT, Direction.CW)
		self.assertEqual(Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.LEFT, Direction.CW)
		myRubik.rotateFace(Face.LEFT, Direction.CW)
		myRubik.rotateFace(Face.LEFT, Direction.CW)
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT))
		self.assertEqual(Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateRightClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.RIGHT, Direction.CW)
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT))
		self.assertEqual(Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.RIGHT, Direction.CW)
		myRubik.rotateFace(Face.RIGHT, Direction.CW)
		myRubik.rotateFace(Face.RIGHT, Direction.CW)
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT))
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT))
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateBackClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.BACK, Direction.CW)
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT))
		self.assertEqual(Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.BACK, Direction.CW)
		myRubik.rotateFace(Face.BACK, Direction.CW)
		myRubik.rotateFace(Face.BACK, Direction.CW)
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP))
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT))
		self.assertEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT))
		self.assertEqual(Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateTopClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.TOP, Direction.CW)
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP))
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT))
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.TOP, Direction.CW)
		myRubik.rotateFace(Face.TOP, Direction.CW)
		myRubik.rotateFace(Face.TOP, Direction.CW)
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateBottomClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.BOTTOM, Direction.CW)
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM))
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT))
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT))
		self.assertEqual( Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.BOTTOM, Direction.CW)
		myRubik.rotateFace(Face.BOTTOM, Direction.CW)
		myRubik.rotateFace(Face.BOTTOM, Direction.CW)
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT))
		self.assertEqual( Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT))

	


	
	def test_rotateFrontCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.FRONT, Direction.CCW)
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOM))
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.FRONT, Direction.CCW)
		myRubik.rotateFace(Face.FRONT, Direction.CCW)
		myRubik.rotateFace(Face.FRONT, Direction.CCW)
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateLeftCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.LEFT, Direction.CCW)
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT))
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.LEFT, Direction.CCW)
		myRubik.rotateFace(Face.LEFT, Direction.CCW)
		myRubik.rotateFace(Face.LEFT, Direction.CCW)
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT))
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateRightCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.RIGHT, Direction.CCW)
		self.assertEqual( Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT))
		self.assertEqual( Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT))
		self.assertEqual( Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT))
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.RIGHT, Direction.CCW)
		myRubik.rotateFace(Face.RIGHT, Direction.CCW)
		myRubik.rotateFace(Face.RIGHT, Direction.CCW)
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT))
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateBackCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.BACK, Direction.CCW)
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP))
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT))
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT))
		self.assertEqual( Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.BACK, Direction.CCW)
		myRubik.rotateFace(Face.BACK, Direction.CCW)
		myRubik.rotateFace(Face.BACK, Direction.CCW)
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT))
		self.assertEqual( Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateTopCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.TOP, Direction.CCW)
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP))
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT))
		self.assertEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.TOP, Direction.CCW)
		myRubik.rotateFace(Face.TOP, Direction.CCW)
		myRubik.rotateFace(Face.TOP, Direction.CCW)
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT))
		self.assertEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT))

	

	
	def test_rotateBottomCounterClockwise(self):
		#Colors for : Front, Back, Right, Left, Top and Bottom  faces
		myRubik = Cube()
		myRubik.rotateFace(Face.BOTTOM, Direction.CCW)
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM))
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT))
		self.assertEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT))
		self.assertEqual( Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT))
		myRubik.rotateFace(Face.BOTTOM, Direction.CCW)
		myRubik.rotateFace(Face.BOTTOM, Direction.CCW)
		myRubik.rotateFace(Face.BOTTOM, Direction.CCW)
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT))
		self.assertEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT))
		self.assertEqual( Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT))

	

	
	def test_simpleRotations(self):
			myRubik = Cube()
			for i in range(0,20):
				myRubik.rotateFace(Face.TOP, Direction.CW)
				myRubik.rotateFace(Face.RIGHT, Direction.CW)
				myRubik.rotateFace(Face.LEFT, Direction.CW)
				myRubik.rotateFace(Face.BOTTOM, Direction.CW)
				myRubik.rotateFace(Face.RIGHT, Direction.CW)
				myRubik.rotateFace(Face.TOP, Direction.CW)
				myRubik.rotateFace(Face.RIGHT, Direction.CW)
				myRubik.rotateFace(Face.BACK, Direction.CW)
				myRubik.rotateFace(Face.LEFT, Direction.CW)
				myRubik.rotateFace(Face.FRONT, Direction.CW)
			
			for i in range(0,20):
				myRubik.rotateFace(Face.FRONT, Direction.CCW)
				myRubik.rotateFace(Face.LEFT, Direction.CCW)
				myRubik.rotateFace(Face.BACK, Direction.CCW)
				myRubik.rotateFace(Face.RIGHT, Direction.CCW)
				myRubik.rotateFace(Face.TOP, Direction.CCW)
				myRubik.rotateFace(Face.RIGHT, Direction.CCW)
				myRubik.rotateFace(Face.BOTTOM, Direction.CCW)
				myRubik.rotateFace(Face.LEFT, Direction.CCW)
				myRubik.rotateFace(Face.RIGHT, Direction.CCW)
				myRubik.rotateFace(Face.TOP, Direction.CCW)
			
			myRubik.rotateFace(Face.FRONT, Direction.CW)
			myRubik.rotateFace(Face.FRONT, Direction.CCW)
			Assert.IsTrue(myRubik.equals(Cube()))