package com.agilesparks.rubikscube.utils;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Face;

public class FaceTest {
    @Test
    public void testFaceGetIntGetChar() {
        Face myFace = Face.BOTTOM;
        assertEquals(1, myFace.getInt());
        assertEquals('D', myFace.getIntOfChar());
        myFace = Face.FRONT;
        assertEquals(4, myFace.getInt());
        assertEquals('F', myFace.getIntOfChar());
        myFace = Face.RIGHT;
        assertEquals(2, myFace.getInt());
        assertEquals('R', myFace.getIntOfChar());
        myFace = Face.TOP;
        assertEquals(0, myFace.getInt());
        assertEquals('U', myFace.getIntOfChar());
        myFace = Face.BACK;
        assertEquals(5, myFace.getInt());
        assertEquals('B', myFace.getIntOfChar());
        myFace = Face.LEFT;
        assertEquals(3, myFace.getInt());
        assertEquals('L', myFace.getIntOfChar());
    };

    @Test
    public void testFaceEquals() {
        Face myFace = Face.BOTTOM;
        assertEquals(Face.BOTTOM, myFace);
        assertEquals(true, myFace==Face.BOTTOM);
    }

    @Test
    public void testFaceGetOpposite() {
        Face myFace = Face.BOTTOM;
        assertEquals(Face.TOP, myFace.getOpposite());
        myFace = Face.FRONT;
        assertEquals(Face.BACK, myFace.getOpposite());
        myFace = Face.RIGHT;
        assertEquals(Face.LEFT, myFace.getOpposite());
        myFace = Face.TOP;
        assertEquals(Face.BOTTOM, myFace.getOpposite());
        myFace = Face.BACK;
        assertEquals(Face.FRONT, myFace.getOpposite());
        myFace = Face.LEFT;
        assertEquals(Face.RIGHT, myFace.getOpposite());
    }

}