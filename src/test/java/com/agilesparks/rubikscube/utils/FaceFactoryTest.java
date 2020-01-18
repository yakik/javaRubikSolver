package com.agilesparks.rubikscube.utils;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.FaceFactory;

public class FaceFactoryTest {

    @Test
    public void getFaceByInt() {
        FaceFactory myFactory = new FaceFactory();
        assertEquals(Face.LEFT, FaceFactory.getFaceByInt(3));
        assertEquals(Face.RIGHT, FaceFactory.getFaceByInt(2));
        assertEquals(Face.TOP, FaceFactory.getFaceByInt(0));
        assertEquals(Face.BOTTOM, FaceFactory.getFaceByInt(1));
        assertEquals(Face.FRONT, FaceFactory.getFaceByInt(4));
        assertEquals(Face.BACK, FaceFactory.getFaceByInt(5));


    }
}

