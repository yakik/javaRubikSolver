package com.agilesparks.rubikscube.cube;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.cube.Permutation;
import com.agilesparks.rubikscube.cube.Cube;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Position;
import com.agilesparks.rubikscube.utils.Rotation;

public class PermutationTest {

    @Test
    public void getValue() {
        Cube myRubik = new Cube();
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        Permutation myPermutation = Permutation.getPermutationFromCube(myRubik);
        assertEquals("first floor",10, Cube.getValue(myPermutation.newCube, 1) );
        assertEquals("second floor", 14, Cube.getValue(myPermutation.newCube, 2) );
        assertEquals("third floor",24, Cube.getValue(myPermutation.newCube, 3) );

    }
    @Test
    public void getValueFull() {
        Cube myRubik = new Cube();
        Permutation myPermutation = Permutation.getPermutationFromCube(myRubik);
        assertEquals("Full",40, Cube.getValue(myPermutation.newCube, 3) );

    }

   
   
}