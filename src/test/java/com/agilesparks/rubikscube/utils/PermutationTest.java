package com.agilesparks.rubikscube.utils;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.cube.CubeCubicle;
import com.agilesparks.rubikscube.cube.Rubik;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Permutation;
import com.agilesparks.rubikscube.utils.Position;
import com.agilesparks.rubikscube.utils.Rotation;

public class PermutationTest {

    @Test
    public void getValue() {
        Rubik myRubik = new Rubik();
        myRubik.rotateFace(new Rotation(Face.F, Direction.CW));
        Permutation myPermutation = myRubik.getPermutation();
        assertEquals("first floor",10, myPermutation.getValue(1) );
        assertEquals("second floor", 14, myPermutation.getValue(2) );
        assertEquals("third floor",24, myPermutation.getValue(3) );

    }

    @Test
    public void testEqualsEqual() {
        Permutation Apermutation = new Permutation();
        Permutation Bpermutation = new Permutation();

        for (int i=0;i<20;i++){
            Apermutation.addCubicleData(new CubeCubicle(new Location(Face.D, Face.R)
                    , new Location(Face.D, Face.R), new Position(Face.U, Face.F)));
            Bpermutation.addCubicleData(new CubeCubicle(new Location(Face.D, Face.R)
                    , new Location(Face.D, Face.R), new Position(Face.U, Face.F)));
        }

        assertEquals(true, Apermutation.equals(Bpermutation));

    }
    @Test
    public void testEqualsFirstFloor() {
        Permutation Apermutation = new Permutation();
        Permutation Bpermutation = new Permutation();

        for (int i=0;i<19;i++){
            Apermutation.addCubicleData(new CubeCubicle(new Location(Face.D, Face.R)
                    , new Location(Face.D, Face.R), new Position(Face.U, Face.F)));
            Bpermutation.addCubicleData(new CubeCubicle(new Location(Face.D, Face.R)
                    , new Location(Face.D, Face.R), new Position(Face.U, Face.F)));
        }
        Apermutation.addCubicleData(new CubeCubicle(new Location(Face.U, Face.R)
                , new Location(Face.U, Face.R), new Position(Face.U, Face.F)));
        Bpermutation.addCubicleData(new CubeCubicle(new Location(Face.U, Face.R)
                , new Location(Face.U, Face.L), new Position(Face.U, Face.F)));

        assertEquals("first floor",false, Apermutation.equals(Bpermutation));
        assertEquals("third floor",false, Apermutation.equals(Bpermutation));

    }
}