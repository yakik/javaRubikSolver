package com.agilesparks.rubikscube.utils;

public class Position {

    private Face g_faceOrder[][] = {
            {Face.FRONT, Face.LEFT, Face.BACK, Face.RIGHT}, {Face.RIGHT, Face.BACK, Face.LEFT, Face.FRONT
    }, {Face.TOP, Face.BACK, Face.BOTTOM, Face.FRONT
    }, {Face.TOP, Face.FRONT, Face.BOTTOM, Face.BACK
    }, {Face.TOP, Face.RIGHT, Face.BOTTOM, Face.LEFT
    }, {Face.TOP, Face.LEFT, Face.BOTTOM, Face.RIGHT
    }
    };
    private Face c_currentUp;
    private Face c_currentFront;

    public Position(Face p_Up, Face p_Front) {
        c_currentUp = p_Up;
        c_currentFront = p_Front;
    }

    Position() {
        c_currentUp = Face.TOP;
        c_currentFront = Face.FRONT;
    }

    public String getString() {
        return String.format("%c, %c", c_currentUp.getIntOfChar(), c_currentFront.getIntOfChar());
    }

    public void rotate(Rotation p_rotation) {
        Face l_temp;
        Face l_face = p_rotation.getFace();
        Direction l_direction = p_rotation.getDirection();
        if (l_face == Face.TOP)
            if (l_direction == Direction.CW)
                c_currentFront = getFace(Face.RIGHT);
            else
                c_currentFront = getFace(Face.LEFT);
        else if (l_face == Face.RIGHT)
            if (l_direction == Direction.CW) {
                l_temp = c_currentFront;
                c_currentFront = getFace(Face.BOTTOM);
                c_currentUp = l_temp;
            } else {
                l_temp = getFace(Face.BACK);
                c_currentFront = c_currentUp;
                c_currentUp = l_temp;
            }
        else if (l_face == Face.FRONT)
            if (l_direction == Direction.CW)
                c_currentUp = getFace(Face.LEFT);
            else
                c_currentUp = getFace(Face.RIGHT);
        else
            rotate(new Rotation(l_face.getOpposite(), l_direction.getOpposite()));

    }

public Position getCopy(){
        return new Position(c_currentUp,c_currentFront);
}
    public Face getFace(Face p_viewpoint) {
        if (p_viewpoint == Face.TOP)
            return c_currentUp;
        else if (p_viewpoint == Face.BOTTOM)
            return c_currentUp.getOpposite();
        else
            return getHorizonalFacebyVirtual(p_viewpoint);
    }


    Face getHorizonalFacebyVirtual(Face p_viewpoint) {
        int i = 0;

        while (g_faceOrder[c_currentUp.getInt()][i] != c_currentFront && i < 4)
            i++;
        switch (p_viewpoint) {
            case FRONT:
                return g_faceOrder[c_currentUp.getInt()][i];

            case LEFT:
                return g_faceOrder[c_currentUp.getInt()][(i + 1) % 4];

            case BACK:
                return g_faceOrder[c_currentUp.getInt()][(i + 2) % 4];

            case RIGHT:
                return g_faceOrder[c_currentUp.getInt()][(i + 3) % 4];

            default:
                return Face.TOP;

        }
    }

    public boolean equals(Position p_position) {
        return ((c_currentUp == p_position.c_currentUp) &&
                (c_currentFront == p_position.c_currentFront));
    }

//	int operator !=(
//	Position p_position)
//
//	{
//		return !(equals(p_position));
//	}

}