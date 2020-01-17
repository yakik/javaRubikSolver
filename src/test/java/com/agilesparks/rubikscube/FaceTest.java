package com.agilesparks.rubikscube;


import static org.junit.Assert.*;

import org.junit.Test;

public class FaceTest {
    @Test
    public void testFaceGetIntGetChar() {
        Face myFace = Face.D;
        assertEquals(1, myFace.getInt());
        assertEquals('D', myFace.getIntOfChar());
        myFace = Face.F;
        assertEquals(4, myFace.getInt());
        assertEquals('F', myFace.getIntOfChar());
        myFace = Face.R;
        assertEquals(2, myFace.getInt());
        assertEquals('R', myFace.getIntOfChar());
        myFace = Face.U;
        assertEquals(0, myFace.getInt());
        assertEquals('U', myFace.getIntOfChar());
        myFace = Face.B;
        assertEquals(5, myFace.getInt());
        assertEquals('B', myFace.getIntOfChar());
        myFace = Face.L;
        assertEquals(3, myFace.getInt());
        assertEquals('L', myFace.getIntOfChar());
    };

    @Test
    public void testFaceEquals() {
        Face myFace = Face.D;
        assertEquals(Face.D, myFace);
        assertEquals(true, myFace==Face.D);
    }

    @Test
    public void testFaceGetOpposite() {
        Face myFace = Face.D;
        assertEquals(Face.U, myFace.getOpposite());
        myFace = Face.F;
        assertEquals(Face.B, myFace.getOpposite());
        myFace = Face.R;
        assertEquals(Face.L, myFace.getOpposite());
        myFace = Face.U;
        assertEquals(Face.D, myFace.getOpposite());
        myFace = Face.B;
        assertEquals(Face.F, myFace.getOpposite());
        myFace = Face.L;
        assertEquals(Face.R, myFace.getOpposite());
    }

}