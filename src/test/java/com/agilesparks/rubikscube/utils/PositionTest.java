package com.agilesparks.rubikscube.utils;

import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Position;
import com.agilesparks.rubikscube.utils.Rotation;

public class PositionTest {

    @Test
    public void getString() {
        Position myPosition = new Position(Face.TOP,Face.FRONT);
        assertEquals("U, F",myPosition.getString());
    }

    @Test
    public void rotateCW_U() {
        Position myPosition = new Position(Face.TOP, Face.FRONT);
        myPosition.rotate(new Rotation(Face.FRONT, Direction.CW));
        assertEquals(Face.LEFT,myPosition.getFace(Face.TOP));
    }

    @Test
    public void rotateCW_D() {
        Position myPosition = new Position(Face.TOP, Face.FRONT);
        myPosition.rotate(new Rotation(Face.FRONT, Direction.CW));
        assertEquals(Face.RIGHT,myPosition.getFace(Face.BOTTOM));
    }

    @Test
    public void  rotateCCW() {
        Position myPosition = new Position(Face.TOP, Face.FRONT);
        myPosition.rotate(new Rotation(Face.FRONT, Direction.CCW));
        assertEquals(Face.RIGHT,myPosition.getFace(Face.TOP));
    }

    @Test
    public void rotateCCW_D() {
        Position myPosition = new Position(Face.TOP, Face.FRONT);
        myPosition.rotate(new Rotation(Face.FRONT, Direction.CCW));
        assertEquals(Face.LEFT,myPosition.getFace(Face.BOTTOM));
    }

    @Test
    public void moreRotationTests() {
        Position myPosition = new Position(Face.TOP, Face.FRONT);
        myPosition.rotate(new Rotation(Face.LEFT, Direction.CW));
        assertEquals(true,myPosition.equals(new Position(Face.BACK,Face.TOP)));
        myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CW));
        assertEquals(true,myPosition.equals(new Position(Face.BACK,Face.LEFT)));
        myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CCW));
        assertEquals(true,myPosition.equals(new Position(Face.BACK,Face.TOP)));
    }

    @Test
    public void rotateCCW_DD() {
        Position myPosition = new Position(Face.TOP, Face.FRONT);
        myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CCW));
        assertEquals(Face.BOTTOM,myPosition.getFace(Face.BOTTOM));
    }
   
}