package com.agilesparks.rubikscube.cube;

import java.lang.reflect.Array;

import com.agilesparks.rubikscube.utils.Color;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.LocationInFace;

public class NewCube {

	private Color colors[][] = new Color[6][8];

	private void setColor(Face face, LocationInFace locationInFace, Color color) {
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

	public void rotateFace(Face face, Direction direction) {
		switch (face) {
		case FRONT:
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.FRONT);

				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOM,
						Face.RIGHT, LocationInFace.LEFT,
						Face.BOTTOM, LocationInFace.TOP,
						Face.LEFT, LocationInFace.RIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMLEFT,
						Face.RIGHT, LocationInFace.TOPLEFT,
						Face.BOTTOM,LocationInFace.TOPRIGHT,
						Face.LEFT, LocationInFace.BOTTOMRIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMRIGHT,
						Face.RIGHT, LocationInFace.BOTTOMLEFT,
						Face.BOTTOM, LocationInFace.TOPLEFT,
						Face.LEFT, LocationInFace.TOPRIGHT);
			}
			break;
		case RIGHT:
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.RIGHT);
				
				rotateLeftToRight(Face.TOP, LocationInFace.RIGHT, 
						Face.BACK, LocationInFace.LEFT,
						Face.BOTTOM, LocationInFace.RIGHT,
						Face.FRONT, LocationInFace.RIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMRIGHT,
						Face.BACK, LocationInFace.TOPLEFT,
						Face.BOTTOM, LocationInFace.BOTTOMRIGHT,
						Face.FRONT,	LocationInFace.BOTTOMRIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.TOPRIGHT,
						Face.BACK, LocationInFace.BOTTOMLEFT,
						Face.BOTTOM, LocationInFace.TOPRIGHT,
						Face.FRONT, LocationInFace.TOPRIGHT);
			}
			break;
		case LEFT:
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.LEFT);
				
				rotateLeftToRight(Face.TOP, LocationInFace.LEFT, 
						Face.FRONT, LocationInFace.LEFT,
						Face.BOTTOM, LocationInFace.RIGHT,
						Face.BACK, LocationInFace.LEFT);
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMLEFT,
						Face.FRONT, LocationInFace.TOPLEFT,
						Face.BOTTOM, LocationInFace.BOTTOMRIGHT,
						Face.BACK,	LocationInFace.BOTTOMLEFT);
				rotateLeftToRight(Face.TOP, LocationInFace.TOPLEFT,
						Face.FRONT, LocationInFace.BOTTOMLEFT,
						Face.BOTTOM, LocationInFace.TOPRIGHT,
						Face.BACK, LocationInFace.TOPLEFT);
			}
			break;
		case BACK:
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.BACK);

				rotateLeftToRight(Face.TOP, LocationInFace.TOP,
						Face.LEFT, LocationInFace.LEFT,
						Face.BOTTOM, LocationInFace.BOTTOM,
						Face.RIGHT, LocationInFace.RIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.TOPLEFT,
						Face.LEFT, LocationInFace.BOTTOMLEFT,
						Face.BOTTOM,LocationInFace.BOTTOMRIGHT,
						Face.RIGHT, LocationInFace.TOPRIGHT);
				rotateLeftToRight(Face.TOP, LocationInFace.TOPRIGHT,
						Face.LEFT, LocationInFace.TOPLEFT,
						Face.BOTTOM, LocationInFace.BOTTOMLEFT,
						Face.RIGHT, LocationInFace.TOPLEFT);
			}
			break;
		case TOP:
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.TOP);

				rotateLeftToRight(Face.BACK, LocationInFace.TOP,
						Face.RIGHT, LocationInFace.TOP,
						Face.FRONT, LocationInFace.TOP,
						Face.LEFT, LocationInFace.TOP);
				rotateLeftToRight(Face.BACK, LocationInFace.TOPLEFT,
						Face.RIGHT, LocationInFace.TOPLEFT,
						Face.FRONT,LocationInFace.TOPLEFT,
						Face.LEFT, LocationInFace.TOPLEFT);
				rotateLeftToRight(Face.BACK, LocationInFace.TOPRIGHT,
						Face.RIGHT, LocationInFace.TOPRIGHT,
						Face.FRONT, LocationInFace.TOPRIGHT,
						Face.LEFT, LocationInFace.TOPRIGHT);
			}
			break;
		case BOTTOM:
			if (direction == Direction.CW) {
				rotateLeftToRightFaceOnly(Face.BOTTOM);

				rotateLeftToRight(Face.BACK, LocationInFace.BOTTOM,
						Face.LEFT, LocationInFace.BOTTOM,
						Face.FRONT, LocationInFace.BOTTOM,
						Face.RIGHT, LocationInFace.BOTTOM);
				rotateLeftToRight(Face.BACK, LocationInFace.BOTTOMLEFT,
						Face.LEFT, LocationInFace.BOTTOMLEFT,
						Face.FRONT,LocationInFace.BOTTOMLEFT,
						Face.RIGHT, LocationInFace.BOTTOMLEFT);
				rotateLeftToRight(Face.BACK, LocationInFace.BOTTOMRIGHT,
						Face.LEFT, LocationInFace.BOTTOMRIGHT,
						Face.FRONT, LocationInFace.BOTTOMRIGHT,
						Face.RIGHT, LocationInFace.BOTTOMRIGHT);
			}
			break;
		default:
			break;
		}

	}


	private void rotateLeftToRightFaceOnly(Face face) {
		rotateLeftToRight(face, LocationInFace.TOP, face, LocationInFace.RIGHT, face,
				LocationInFace.BOTTOM, face, LocationInFace.LEFT);
		rotateLeftToRight(face, LocationInFace.BOTTOMLEFT, face, LocationInFace.TOPLEFT, face,
				LocationInFace.TOPRIGHT, face, LocationInFace.BOTTOMRIGHT);
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

}
