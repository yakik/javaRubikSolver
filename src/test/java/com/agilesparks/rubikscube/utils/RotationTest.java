package com.agilesparks.rubikscube.utils;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.solver.forTestRubikFileReader;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Rotation;


public class RotationTest {

	public void rotationReadTest(String stringToRead, Face expectedFace, Direction expectedDirection){
        Rotation testRotation = new Rotation();
        forTestRubikFileReader myTestReader = new forTestRubikFileReader(stringToRead);
        testRotation.readFromFile(myTestReader);

        assertEquals(expectedFace, testRotation.getFace());
        assertEquals(expectedDirection, testRotation.getDirection());

    }


    @Test
    public void testRotationEquals() {
        Rotation myRotation = new Rotation(Face.FRONT, Direction.CW);
        assertEquals(true, myRotation.equals((new Rotation(Face.FRONT, Direction.CW))));
    }
    @Test
    public void rotationRead_B_CCW() {
        rotationReadTest (" (5,1) ", Face.BACK,Direction.CCW);
    }

    @Test
    public  void rotationRead_D_CW() {
        rotationReadTest (" (1,0) ", Face.BOTTOM,Direction.CW);

    }
}