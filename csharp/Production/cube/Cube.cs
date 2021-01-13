using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using utils;

namespace cube
{

	public class Cube {


		public static Cube getPermutationFromCube(Cube cube) {


			return cube.getCopy();
		}

		public static int getValue(Cube l_permutation, int p_highestFloor) {
			int l_value = 0;
			Cube fixedCube = new Cube();
			l_value = 2 * (8 - l_permutation.countDifferenceFirstFloor(fixedCube));
			if (p_highestFloor > 1)
				l_value += 2 * (4 - l_permutation.countDifferenceSecondFloor(fixedCube));
			if (p_highestFloor > 2)
				l_value += 2 * (8 - l_permutation.countDifferenceThirdFloor(fixedCube));

			return l_value;
		}




		private Color[,] colors = new Color[6,8];
	
	 public Boolean equals(Cube comparedCube) {
			if (countDifferenceFirstFloor(comparedCube) +
					countDifferenceSecondFloor(comparedCube) +
					countDifferenceThirdFloor(comparedCube) == 0)
				return true;
			else
				return false;
		}

		public void setColor(Face face, LocationInFace locationInFace, Color color) {
			colors[(int)face,(int)locationInFace] = color;
		}

		public Color getColor(Face face, LocationInFace locationInFace) {
			return colors[(int)face,(int)locationInFace];
		}

		public Cube() {

			foreach (LocationInFace locationInFace in Enum.GetValues(typeof(LocationInFace))) {
				setColor(Face.FRONT, locationInFace, Color.FRONTCOLOR);
				setColor(Face.BACK, locationInFace, Color.BACKCOLOR);
				setColor(Face.RIGHT, locationInFace, Color.RIGHTCOLOR);
				setColor(Face.LEFT, locationInFace, Color.LEFTCOLOR);
				setColor(Face.TOP, locationInFace, Color.TOPCOLOR);
				setColor(Face.BOTTOM, locationInFace, Color.BOTTOMCOLOR);
			}

		}

		public Cube(Cube source) {
			foreach (LocationInFace locationInFace in Enum.GetValues(typeof(LocationInFace)))
			{
				setColor(Face.FRONT, locationInFace, source.getColor(Face.FRONT, locationInFace));
				setColor(Face.BACK, locationInFace, source.getColor(Face.BACK, locationInFace));
				setColor(Face.RIGHT, locationInFace, source.getColor(Face.RIGHT, locationInFace));
				setColor(Face.LEFT, locationInFace, source.getColor(Face.LEFT, locationInFace));
				setColor(Face.TOP, locationInFace, source.getColor(Face.TOP, locationInFace));
				setColor(Face.BOTTOM, locationInFace, source.getColor(Face.BOTTOM, locationInFace));
			}
		}

		public void rotateFace(Face face, Direction direction) {
			switch (face) {
				case Face.FRONT:
					rotateFrontFace(direction);
					break;
				case Face.RIGHT:
					rotateRightFace(direction);
					break;
				case Face.LEFT:
					rotateLeftFace(direction);
					break;
				case Face.BACK:
					rotateBackFace(direction);
					break;
				case Face.TOP:
					rotateTopFace(direction);
					break;
				case Face.BOTTOM:
					rotateBottomFace(direction);
					break;
				default:
					break;
			}

		}

		private void rotateBottomFace(Direction direction) {
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.BOTTOM);

				rotateLeftToRight(Face.BACK, LocationInFace.BOTTOM, Face.LEFT, LocationInFace.BOTTOM, Face.FRONT,
						LocationInFace.BOTTOM, Face.RIGHT, LocationInFace.BOTTOM);
				rotateLeftToRight(Face.BACK, LocationInFace.BOTTOMLEFT, Face.LEFT, LocationInFace.BOTTOMLEFT, Face.FRONT,
						LocationInFace.BOTTOMLEFT, Face.RIGHT, LocationInFace.BOTTOMLEFT);
				rotateLeftToRight(Face.BACK, LocationInFace.BOTTOMRIGHT, Face.LEFT, LocationInFace.BOTTOMRIGHT, Face.FRONT,
						LocationInFace.BOTTOMRIGHT, Face.RIGHT, LocationInFace.BOTTOMRIGHT);
			} else {
				for (int i = 0; i < 3; i++)
					rotateBottomFace(Direction.CW);
			}
		}

		private void rotateTopFace(Direction direction) {
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.TOP);

				rotateLeftToRight(Face.BACK, LocationInFace.TOP, Face.RIGHT, LocationInFace.TOP, Face.FRONT,
						LocationInFace.TOP, Face.LEFT, LocationInFace.TOP);
				rotateLeftToRight(Face.BACK, LocationInFace.TOPLEFT, Face.RIGHT, LocationInFace.TOPLEFT, Face.FRONT,
						LocationInFace.TOPLEFT, Face.LEFT, LocationInFace.TOPLEFT);
				rotateLeftToRight(Face.BACK, LocationInFace.TOPRIGHT, Face.RIGHT, LocationInFace.TOPRIGHT, Face.FRONT,
						LocationInFace.TOPRIGHT, Face.LEFT, LocationInFace.TOPRIGHT);
			} else {
				for (int i = 0; i < 3; i++)
					rotateTopFace(Direction.CW);
			}
		}

		private void rotateBackFace(Direction direction) {
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.BACK);

				rotateLeftToRight(Face.TOP, LocationInFace.TOP, Face.LEFT, LocationInFace.LEFT, Face.BOTTOM,
						LocationInFace.BOTTOM, Face.RIGHT, LocationInFace.RIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.TOPLEFT, Face.LEFT, LocationInFace.BOTTOMLEFT, Face.BOTTOM,
						LocationInFace.BOTTOMRIGHT, Face.RIGHT, LocationInFace.TOPRIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.TOPRIGHT, Face.LEFT, LocationInFace.TOPLEFT, Face.BOTTOM,
						LocationInFace.BOTTOMLEFT, Face.RIGHT, LocationInFace.BOTTOMRIGHT);
			} else {
				for (int i = 0; i < 3; i++)
					rotateBackFace(Direction.CW);
			}
		}

		private void rotateLeftFace(Direction direction) {
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.LEFT);

				rotateLeftToRight(Face.TOP, LocationInFace.LEFT,
						Face.FRONT, LocationInFace.LEFT,
						Face.BOTTOM, LocationInFace.LEFT,
						Face.BACK, LocationInFace.RIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMLEFT,
						Face.FRONT, LocationInFace.BOTTOMLEFT,
						Face.BOTTOM, LocationInFace.BOTTOMLEFT,
						Face.BACK, LocationInFace.TOPRIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.TOPLEFT,
						Face.FRONT, LocationInFace.TOPLEFT,
						Face.BOTTOM, LocationInFace.TOPLEFT,
						Face.BACK, LocationInFace.BOTTOMRIGHT);
			} else {
				for (int i = 0; i < 3; i++)
					rotateLeftFace(Direction.CW);
			}
		}

		private void rotateRightFace(Direction direction) {
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.RIGHT);

				rotateLeftToRight(Face.TOP, LocationInFace.RIGHT,
						Face.BACK, LocationInFace.LEFT,
						Face.BOTTOM, LocationInFace.RIGHT,
						Face.FRONT, LocationInFace.RIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMRIGHT,
						Face.BACK, LocationInFace.TOPLEFT,
						Face.BOTTOM, LocationInFace.BOTTOMRIGHT,
						Face.FRONT, LocationInFace.BOTTOMRIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.TOPRIGHT,
						Face.BACK, LocationInFace.BOTTOMLEFT,
						Face.BOTTOM, LocationInFace.TOPRIGHT,
						Face.FRONT, LocationInFace.TOPRIGHT);
			} else {
				for (int i = 0; i < 3; i++)
					rotateRightFace(Direction.CW);
			}
		}

		private void rotateFrontFace(Direction direction) {
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.FRONT);

				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOM, Face.RIGHT, LocationInFace.LEFT, Face.BOTTOM,
						LocationInFace.TOP, Face.LEFT, LocationInFace.RIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMLEFT, Face.RIGHT, LocationInFace.TOPLEFT, Face.BOTTOM,
						LocationInFace.TOPRIGHT, Face.LEFT, LocationInFace.BOTTOMRIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMRIGHT, Face.RIGHT, LocationInFace.BOTTOMLEFT, Face.BOTTOM,
						LocationInFace.TOPLEFT, Face.LEFT, LocationInFace.TOPRIGHT);
			} else {
				for (int i = 0; i < 3; i++)
					rotateFrontFace(Direction.CW);
			}
		}

		private void rotateLeftToRightFaceOnly(Face face) {
			rotateLeftToRight(face, LocationInFace.TOP, face, LocationInFace.RIGHT, face, LocationInFace.BOTTOM, face,
					LocationInFace.LEFT);
			rotateLeftToRight(face, LocationInFace.BOTTOMLEFT, face, LocationInFace.TOPLEFT, face, LocationInFace.TOPRIGHT,
					face, LocationInFace.BOTTOMRIGHT);
		}

		public void print() {
			printFace(Face.TOP);
			printFace(Face.BOTTOM);
			printFace(Face.FRONT);
			printFace(Face.BACK);
			printFace(Face.LEFT);
			printFace(Face.RIGHT);

		}

		private void printFace(Face face) {
			Console.Write("\n%S\n\n", FaceHandler.getCharValue(face));
			Console.Write("%11s %11s %11s\n", getColor(face, LocationInFace.TOPLEFT),
					getColor(face, LocationInFace.TOP), getColor(face, LocationInFace.TOPRIGHT));
			Console.Write("%11s             %11s\n", getColor(face, LocationInFace.LEFT),
					getColor(face, LocationInFace.RIGHT));
			Console.Write("%11s %11s %11s\n", getColor(face, LocationInFace.BOTTOMLEFT),
					getColor(face, LocationInFace.BOTTOM), getColor(face, LocationInFace.BOTTOMRIGHT));
		}
		//                TL T TR
		//                L TOP R 
		//                BL B BR

		//TL T TR TL T TR TL T TR TL T TR
		//LBACK R LLEFT R LFRONTR LRIGHTR 
		//BL B BR BL B BR BL B BR BL B BR

		//                TL T TR
		//                LBOTTOMR 
		//                BL B BR

		private void rotateLeftToRight(Face firstFace, LocationInFace firstLocationInFace, Face secondFace,
				LocationInFace secondLocationInFace, Face thirdFace, LocationInFace thirdLocationInFace, Face fourthFace,
				LocationInFace fourthLocationInFace) {
			Color temp = getColor(fourthFace, fourthLocationInFace);
			setColor(fourthFace, fourthLocationInFace, getColor(thirdFace, thirdLocationInFace));
			setColor(thirdFace, thirdLocationInFace, getColor(secondFace, secondLocationInFace));
			setColor(secondFace, secondLocationInFace, getColor(firstFace, firstLocationInFace));
			setColor(firstFace, firstLocationInFace, temp);

		}

		public int countDifferenceSecondFloor(Cube cube) {
			int counter = 0;
			if (colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.LEFT) ||
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.RIGHT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.LEFT) ||
					colorInFaceNotEqual(cube, Face.BACK, LocationInFace.RIGHT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.BACK, LocationInFace.LEFT) ||
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.RIGHT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.LEFT) ||
					colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.RIGHT))
				counter++;

			return counter;

		}


		public int countDifferenceFirstFloor(Cube cube) {
			int counter = 0;
			if (colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.BOTTOM) ||
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.TOP))
				counter++;
			if (colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.BOTTOM) ||
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.LEFT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.BACK, LocationInFace.BOTTOM) ||
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.BOTTOM))
				counter++;
			if (colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.BOTTOM) ||
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.RIGHT))
				counter++;


			if (colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.BOTTOMLEFT) ||
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.TOPLEFT) ||
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.BOTTOMRIGHT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.BOTTOMRIGHT) ||
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.TOPRIGHT) ||
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.BOTTOMLEFT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.BACK, LocationInFace.BOTTOMRIGHT) ||
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.BOTTOMLEFT) ||
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.BOTTOMLEFT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.BACK, LocationInFace.BOTTOMLEFT) ||
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.BOTTOMRIGHT) ||
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.BOTTOMRIGHT))
				counter++;

			return counter;

		}

		public int countDifferenceThirdFloor(Cube cube) {
			int counter = 0;
			if (colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.TOP) ||
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.BOTTOM))
				counter++;
			if (colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.TOP) ||
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.LEFT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.BACK, LocationInFace.TOP) ||
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.TOP))
				counter++;
			if (colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.TOP) ||
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.RIGHT))
				counter++;


			if (colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.TOPLEFT) ||
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.BOTTOMLEFT) ||
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.TOPRIGHT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.TOPRIGHT) ||
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.BOTTOMRIGHT) ||
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.TOPLEFT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.BACK, LocationInFace.TOPRIGHT) ||
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.TOPLEFT) ||
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.TOPLEFT))
				counter++;
			if (colorInFaceNotEqual(cube, Face.BACK, LocationInFace.TOPLEFT) ||
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.TOPRIGHT) ||
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.TOPRIGHT))
				counter++;

			return counter;

		}


		private Boolean colorInFaceNotEqual(Cube comparedCube, Face face, LocationInFace locationInFace) {
			return getColor(face, locationInFace) != comparedCube.getColor(face, LocationInFace.BOTTOM);
		}

		public int countAllDifferences(Cube comparedCube) {
			return countDifferenceThirdFloor(comparedCube) +
					countDifferenceFirstFloor(comparedCube) +
					countDifferenceSecondFloor(comparedCube);
		}

		public Cube getCopy() {
			return new Cube(this);
		}



	}

}



