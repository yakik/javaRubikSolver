package com.agilesparks.rubikscube;

import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Face;

public class PositionTest {

    @Test
    public void getString() {
        Position myPosition = new Position(Face.U,Face.F);
        assertEquals("U, F",myPosition.getString());
    }

    @Test
    public void rotateCW_U() {
        Position myPosition = new Position(Face.U, Face.F);
        myPosition.rotate(new Rotation(Face.F, Direction.CW));
        assertEquals(Face.L,myPosition.getFace(Face.U));
    }

    @Test
    public void rotateCW_D() {
        Position myPosition = new Position(Face.U, Face.F);
        myPosition.rotate(new Rotation(Face.F, Direction.CW));
        assertEquals(Face.R,myPosition.getFace(Face.D));
    }

    @Test
    public void  rotateCCW() {
        Position myPosition = new Position(Face.U, Face.F);
        myPosition.rotate(new Rotation(Face.F, Direction.CCW));
        assertEquals(Face.R,myPosition.getFace(Face.U));
    }

    @Test
    public void rotateCCW_D() {
        Position myPosition = new Position(Face.U, Face.F);
        myPosition.rotate(new Rotation(Face.F, Direction.CCW));
        assertEquals(Face.L,myPosition.getFace(Face.D));
    }

    @Test
    public void moreRotationTests() {
        Position myPosition = new Position(Face.U, Face.F);
        myPosition.rotate(new Rotation(Face.L, Direction.CW));
        assertEquals(true,myPosition.equals(new Position(Face.B,Face.U)));
        myPosition.rotate(new Rotation(Face.D, Direction.CW));
        assertEquals(true,myPosition.equals(new Position(Face.B,Face.L)));
        myPosition.rotate(new Rotation(Face.D, Direction.CCW));
        assertEquals(true,myPosition.equals(new Position(Face.B,Face.U)));
    }

    @Test
    public void rotateCCW_DD() {
        Position myPosition = new Position(Face.U, Face.F);
        myPosition.rotate(new Rotation(Face.D, Direction.CCW));
        assertEquals(Face.D,myPosition.getFace(Face.D));
    }
   
}