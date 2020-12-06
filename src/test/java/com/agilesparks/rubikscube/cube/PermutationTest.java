package com.agilesparks.rubikscube.cube;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;

public class PermutationTest {

    @Test
    public void getValue() {
        Cube myRubik = new Cube();
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        Cube myPermutation = new Cube(myRubik);
        assertEquals("first floor",10, Cube.getValue(myPermutation, 1) );
        assertEquals("second floor", 14, Cube.getValue(myPermutation, 2) );
        assertEquals("third floor",24, Cube.getValue(myPermutation, 3) );

    }
    @Test
    public void getValueFull() {
        Cube myRubik = new Cube();
        Cube myPermutation = new Cube(myRubik);
        assertEquals("Full",40, Cube.getValue(myPermutation, 3) );

    }

   
   
}