using cube;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using utils;

namespace CSharpRubikSolverUTests
{

	public class CubeTest {
		[TestMethod]
	public void overallTest() {
			Cube myRubik = new Cube(), myRubik2 = new Cube();
			myRubik.rotateFace(Face.FRONT, Direction.CW);
			Assert.AreEqual(8, myRubik.countAllDifferences(myRubik2));
			myRubik.rotateFace(Face.TOP, Direction.CW);
			Assert.AreEqual(13, myRubik.countAllDifferences(myRubik2));
		}

		[TestMethod]
	public void compareFirstFloor() {
			Cube myRubik = new Cube(), myRubik2 = new Cube();
			myRubik.setColor(Face.FRONT, LocationInFace.BOTTOMLEFT, Color.BACKCOLOR);
			myRubik.setColor(Face.BACK, LocationInFace.BOTTOM, Color.FRONTCOLOR);
			myRubik.setColor(Face.FRONT, LocationInFace.TOPLEFT, Color.BACKCOLOR);
			Assert.AreEqual(2, myRubik.countDifferenceFirstFloor(myRubik2));
			myRubik.setColor(Face.LEFT, LocationInFace.BOTTOMLEFT, Color.BACKCOLOR);
			Assert.AreEqual(3, myRubik.countDifferenceFirstFloor(myRubik2));


		}
		[TestMethod]
		public void rotateFrontClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.FRONT, Direction.CW);
			Assert.AreEqual(Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOM));
			Assert.AreEqual(Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual(Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual(Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.FRONT, Direction.CW);
			myRubik.rotateFace(Face.FRONT, Direction.CW);
			myRubik.rotateFace(Face.FRONT, Direction.CW);
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual(Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateLeftClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.LEFT, Direction.CW);
			Assert.AreEqual(Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT));
			Assert.AreEqual(Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual(Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
			Assert.AreEqual(Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.LEFT, Direction.CW);
			myRubik.rotateFace(Face.LEFT, Direction.CW);
			myRubik.rotateFace(Face.LEFT, Direction.CW);
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT));
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
			Assert.AreEqual(Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateRightClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.RIGHT, Direction.CW);
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT));
			Assert.AreEqual(Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual(Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
			Assert.AreEqual(Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.RIGHT, Direction.CW);
			myRubik.rotateFace(Face.RIGHT, Direction.CW);
			myRubik.rotateFace(Face.RIGHT, Direction.CW);
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateBackClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.BACK, Direction.CW);
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP));
			Assert.AreEqual(Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
			Assert.AreEqual(Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
			Assert.AreEqual(Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.BACK, Direction.CW);
			myRubik.rotateFace(Face.BACK, Direction.CW);
			myRubik.rotateFace(Face.BACK, Direction.CW);
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP));
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
			Assert.AreEqual(Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
			Assert.AreEqual(Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateTopClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.TOP, Direction.CW);
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP));
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT));
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.TOP, Direction.CW);
			myRubik.rotateFace(Face.TOP, Direction.CW);
			myRubik.rotateFace(Face.TOP, Direction.CW);
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateBottomClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.BOTTOM, Direction.CW);
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM));
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual( Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.BOTTOM, Direction.CW);
			myRubik.rotateFace(Face.BOTTOM, Direction.CW);
			myRubik.rotateFace(Face.BOTTOM, Direction.CW);
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual( Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT));

		}


		[TestMethod]
		public void rotateFrontCounterClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.FRONT, Direction.CCW);
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOM));
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.FRONT, Direction.CCW);
			myRubik.rotateFace(Face.FRONT, Direction.CCW);
			myRubik.rotateFace(Face.FRONT, Direction.CCW);
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateLeftCounterClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.LEFT, Direction.CCW);
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.LEFT, Direction.CCW);
			myRubik.rotateFace(Face.LEFT, Direction.CCW);
			myRubik.rotateFace(Face.LEFT, Direction.CCW);
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateRightCounterClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.RIGHT, Direction.CCW);
			Assert.AreEqual( Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT));
			Assert.AreEqual( Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual( Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.RIGHT, Direction.CCW);
			myRubik.rotateFace(Face.RIGHT, Direction.CCW);
			myRubik.rotateFace(Face.RIGHT, Direction.CCW);
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateBackCounterClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.BACK, Direction.CCW);
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP));
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
			Assert.AreEqual( Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.BACK, Direction.CCW);
			myRubik.rotateFace(Face.BACK, Direction.CCW);
			myRubik.rotateFace(Face.BACK, Direction.CCW);
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
			Assert.AreEqual( Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateTopCounterClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.TOP, Direction.CCW);
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP));
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT));
			Assert.AreEqual( Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.TOP, Direction.CCW);
			myRubik.rotateFace(Face.TOP, Direction.CCW);
			myRubik.rotateFace(Face.TOP, Direction.CCW);
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT));
			Assert.AreEqual( Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
		public void rotateBottomCounterClockwise() {
			//Colors for : Front, Back, Right, Left, Top and Bottom  faces
			Cube myRubik = new Cube();
			myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM));
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual( Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual( Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT));
			myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
			myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
			myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT));
			Assert.AreEqual( Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
			Assert.AreEqual( Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT));

		}

		[TestMethod]
	public void simpleRotations() {
			Cube myRubik = new Cube();
			for (int i = 0; i < 20; i++) {
				myRubik.rotateFace(Face.TOP, Direction.CW);
				myRubik.rotateFace(Face.RIGHT, Direction.CW);
				myRubik.rotateFace(Face.LEFT, Direction.CW);
				myRubik.rotateFace(Face.BOTTOM, Direction.CW);
				myRubik.rotateFace(Face.RIGHT, Direction.CW);
				myRubik.rotateFace(Face.TOP, Direction.CW);
				myRubik.rotateFace(Face.RIGHT, Direction.CW);
				myRubik.rotateFace(Face.BACK, Direction.CW);
				myRubik.rotateFace(Face.LEFT, Direction.CW);
				myRubik.rotateFace(Face.FRONT, Direction.CW);
			}
			for (int i = 0; i < 20; i++) {
				myRubik.rotateFace(Face.FRONT, Direction.CCW);
				myRubik.rotateFace(Face.LEFT, Direction.CCW);
				myRubik.rotateFace(Face.BACK, Direction.CCW);
				myRubik.rotateFace(Face.RIGHT, Direction.CCW);
				myRubik.rotateFace(Face.TOP, Direction.CCW);
				myRubik.rotateFace(Face.RIGHT, Direction.CCW);
				myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
				myRubik.rotateFace(Face.LEFT, Direction.CCW);
				myRubik.rotateFace(Face.RIGHT, Direction.CCW);
				myRubik.rotateFace(Face.TOP, Direction.CCW);
			}
			myRubik.rotateFace(Face.FRONT, Direction.CW);
			myRubik.rotateFace(Face.FRONT, Direction.CCW);
		Assert.IsTrue(myRubik.equals(new Cube()));

		}

	}
}
