package com.agilesparks.rubikscube.cube;

import java.lang.reflect.Array;

import com.agilesparks.rubikscube.utils.Color;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.LocationInFace;

public class NewCube {

	private Color colors[][] = new Color[6][8];

	public void setColor(Face face, LocationInFace locationInFace, Color color) {
		colors[face.getInt()][locationInFace.getInt()] = color;
	}

	public Color getColor(Face face, LocationInFace locationInFace) {
		return colors[face.getInt()][locationInFace.getInt()];
	}

	public NewCube() {

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.FRONT, locationInFace, Color.FRONTCOLOR);

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.BACK, locationInFace, Color.BACKCOLOR);

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.RIGHT, locationInFace, Color.RIGHTCOLOR);

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.LEFT, locationInFace, Color.LEFTCOLOR);

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.TOP, locationInFace, Color.TOPCOLOR);

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.BOTTOM, locationInFace, Color.BOTTOMCOLOR);

	}
	
	public NewCube(NewCube source) {
		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.FRONT, locationInFace, source.getColor(Face.FRONT, locationInFace));

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.BACK, locationInFace,source.getColor(Face.BACK, locationInFace));

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.RIGHT, locationInFace, source.getColor(Face.RIGHT, locationInFace));

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.LEFT, locationInFace, source.getColor(Face.LEFT, locationInFace));

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.TOP, locationInFace, source.getColor(Face.TOP, locationInFace));

		for (LocationInFace locationInFace : LocationInFace.values())
			setColor(Face.BOTTOM, locationInFace, source.getColor(Face.BOTTOM, locationInFace));
	}

	public void rotateFace(Face face, Direction direction) {
		switch (face) {
		case FRONT:
			rotateFrontFace(direction);
			break;
		case RIGHT:
			rotateRightFace(direction);
			break;
		case LEFT:
			rotateLeftFace(direction);
			break;
		case BACK:
			rotateBackFace(direction);
			break;
		case TOP:
			rotateTopFace(direction);
			break;
		case BOTTOM:
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
					Face.BOTTOM,LocationInFace.LEFT,
					Face.BACK, LocationInFace.RIGHT);
			rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMLEFT,
					Face.FRONT, LocationInFace.BOTTOMLEFT,
					Face.BOTTOM,LocationInFace.BOTTOMLEFT,
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
					Face.BOTTOM,LocationInFace.RIGHT,
					Face.FRONT, LocationInFace.RIGHT);
			rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMRIGHT,
					Face.BACK, LocationInFace.TOPLEFT,
					Face.BOTTOM,LocationInFace.BOTTOMRIGHT,
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
//                 TL T TR
//                 L TOP R 
//                 BL B BR

// TL T TR TL T TR TL T TR TL T TR
// LBACK R LLEFT R LFRONTR LRIGHTR 
// BL B BR BL B BR BL B BR BL B BR

//                 TL T TR
//                 LBOTTOMR 
//                 BL B BR

	private void rotateLeftToRight(Face firstFace, LocationInFace firstLocationInFace, Face secondFace,
			LocationInFace secondLocationInFace, Face thirdFace, LocationInFace thirdLocationInFace, Face fourthFace,
			LocationInFace fourthLocationInFace) {
		Color temp = getColor(fourthFace, fourthLocationInFace);
		setColor(fourthFace, fourthLocationInFace, getColor(thirdFace, thirdLocationInFace));
		setColor(thirdFace, thirdLocationInFace, getColor(secondFace, secondLocationInFace));
		setColor(secondFace, secondLocationInFace, getColor(firstFace, firstLocationInFace));
		setColor(firstFace, firstLocationInFace, temp);

	}
	
	public int countDifferenceSecondFloor(NewCube myRubik2) {
		int counter = 0;
		if (colorInFaceNotEqual(myRubik2, Face.FRONT, LocationInFace.LEFT) ||
				colorInFaceNotEqual(myRubik2, Face.LEFT, LocationInFace.RIGHT))
			counter++;
		if (colorInFaceNotEqual(myRubik2, Face.LEFT, LocationInFace.LEFT) ||
				colorInFaceNotEqual(myRubik2, Face.BACK, LocationInFace.RIGHT))
			counter++;
		if (colorInFaceNotEqual(myRubik2, Face.BACK, LocationInFace.LEFT) ||
				colorInFaceNotEqual(myRubik2, Face.RIGHT, LocationInFace.RIGHT))
			counter++;
		if (colorInFaceNotEqual(myRubik2, Face.RIGHT, LocationInFace.LEFT) ||
				colorInFaceNotEqual(myRubik2, Face.FRONT, LocationInFace.RIGHT))
			counter++;

		return counter;

	}


	public int countDifferenceFirstFloor(NewCube cube) {
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
	
	public int countDifferenceThirdFloor(NewCube myRubik2) {
		int counter = 0;
		if (colorInFaceNotEqual(myRubik2, Face.FRONT, LocationInFace.TOP) ||
				colorInFaceNotEqual(myRubik2, Face.TOP, LocationInFace.BOTTOM))
			counter++;
		if (colorInFaceNotEqual(myRubik2, Face.LEFT, LocationInFace.TOP) ||
				colorInFaceNotEqual(myRubik2, Face.TOP, LocationInFace.LEFT))
			counter++;
		if (colorInFaceNotEqual(myRubik2, Face.BACK, LocationInFace.TOP) ||
				colorInFaceNotEqual(myRubik2, Face.TOP, LocationInFace.TOP))
			counter++;
		if (colorInFaceNotEqual(myRubik2, Face.RIGHT, LocationInFace.TOP) ||
				colorInFaceNotEqual(myRubik2, Face.TOP, LocationInFace.RIGHT))
			counter++;
		
		
		if (colorInFaceNotEqual(myRubik2, Face.FRONT, LocationInFace.TOPLEFT) ||
				colorInFaceNotEqual(myRubik2, Face.TOP, LocationInFace.BOTTOMLEFT) ||
				colorInFaceNotEqual(myRubik2, Face.LEFT, LocationInFace.TOPRIGHT))
			counter++;
		if (colorInFaceNotEqual(myRubik2, Face.FRONT, LocationInFace.TOPRIGHT) ||
				colorInFaceNotEqual(myRubik2, Face.TOP, LocationInFace.BOTTOMRIGHT) ||
				colorInFaceNotEqual(myRubik2, Face.RIGHT, LocationInFace.TOPLEFT))
			counter++;
		if (colorInFaceNotEqual(myRubik2, Face.BACK, LocationInFace.TOPRIGHT) ||
				colorInFaceNotEqual(myRubik2, Face.TOP, LocationInFace.TOPLEFT) ||
				colorInFaceNotEqual(myRubik2, Face.LEFT, LocationInFace.TOPLEFT))
			counter++;
		if (colorInFaceNotEqual(myRubik2, Face.BACK, LocationInFace.TOPLEFT) ||
				colorInFaceNotEqual(myRubik2, Face.TOP, LocationInFace.TOPRIGHT) ||
				colorInFaceNotEqual(myRubik2, Face.RIGHT, LocationInFace.TOPRIGHT))
			counter++;

		return counter;

	}


	private boolean colorInFaceNotEqual(NewCube comparedCube, Face face, LocationInFace locationInFace) {
		return getColor(face, locationInFace) != comparedCube.getColor(face, LocationInFace.BOTTOM);
	}

	public int countAllDifferences(NewCube comparedCube) {
		return countDifferenceThirdFloor(comparedCube)+
				countDifferenceFirstFloor(comparedCube) +
				countDifferenceSecondFloor(comparedCube);
	}

}
