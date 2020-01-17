package com.agilesparks.rubikscube;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Face;

public class FaceFactoryTest {

    @Test
    public void getFaceByInt() {
        FaceFactory myFactory = new FaceFactory();
        assertEquals(Face.L, FaceFactory.getFaceByInt(3));
        assertEquals(Face.R, FaceFactory.getFaceByInt(2));
        assertEquals(Face.U, FaceFactory.getFaceByInt(0));
        assertEquals(Face.D, FaceFactory.getFaceByInt(1));
        assertEquals(Face.F, FaceFactory.getFaceByInt(4));
        assertEquals(Face.B, FaceFactory.getFaceByInt(5));


    }
}

