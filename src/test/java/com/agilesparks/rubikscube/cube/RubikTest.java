package com.agilesparks.rubikscube.cube;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.cube.CubeCubicle;
import com.agilesparks.rubikscube.cube.Rubik;
import com.agilesparks.rubikscube.solver.AssistAssertRubik;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Permutation;
import com.agilesparks.rubikscube.utils.Position;
import com.agilesparks.rubikscube.utils.Rotation;

public class RubikTest {

    @Test
    public  void setPermutationTest() {
        Permutation myPermutation = new Permutation();
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.U), new Location(Face.F, Face.U), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.R), new Location(Face.F, Face.R), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.L), new Location(Face.F, Face.L), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.D), new Location(Face.F, Face.D), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.U), new Location(Face.B, Face.U), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.R), new Location(Face.B, Face.R), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.L), new Location(Face.B, Face.L), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.D), new Location(Face.B, Face.D), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.U, Face.R), new Location(Face.U, Face.R), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.U, Face.L), new Location(Face.U, Face.L), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.D, Face.R), new Location(Face.D, Face.R), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.D, Face.L), new Location(Face.D, Face.L), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.U, Face.R), new Location(Face.F, Face.U, Face.R), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.U, Face.L), new Location(Face.F, Face.U, Face.L), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.D, Face.R), new Location(Face.F, Face.D, Face.R), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.D, Face.L), new Location(Face.F, Face.D, Face.L), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.U, Face.R), new Location(Face.B, Face.U, Face.R), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.U, Face.L), new Location(Face.B, Face.U, Face.L), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.D, Face.R), new Location(Face.B, Face.D, Face.R), new Position(Face.U, Face.F)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.D, Face.L), new Location(Face.B, Face.D, Face.L), new Position(Face.U, Face.F)));

        Rubik myRubik = new Rubik();



myRubik.rotateFace(new Rotation(Face.R, Direction.CW));
        myRubik.rotateFace(new Rotation(Face.B, Direction.CW));
        myRubik.rotateFace(new Rotation(Face.R, Direction.CW));
        myRubik.rotateFace(new Rotation(Face.B, Direction.CW));
        myRubik.rotateFace(new Rotation(Face.L, Direction.CW));
        myRubik.rotateFace(new Rotation(Face.F, Direction.CW));
        myRubik.rotateFace(new Rotation(Face.R, Direction.CW));
        myRubik.rotateFace(new Rotation(Face.B, Direction.CW));
        myRubik.rotateFace(new Rotation(Face.R, Direction.CW));

        myRubik.setPermutation(myPermutation);
        AssistAssertRubik.checkEntireCube(myRubik);


    }
    @Test
    public void testChangesOnlyInThirdFloor_partII(){
        Permutation myPermutation = new Permutation();
        Rubik myCube = new Rubik();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.U)
                , new Location(Face.F, Face.R), new Position(Face.U, Face.B)));
        assertEquals("one",true, myCube.changesOnlyInThirdFloor(myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.D)
                , new Location(Face.F, Face.L), new Position(Face.U, Face.B)));
        assertEquals("two",false, myCube.changesOnlyInThirdFloor(myPermutation));
    }


    @Test
    public void testChangesOnlyInThirdFloor_partI(){
        Permutation myPermutation = new Permutation();
        Rubik myCube = new Rubik();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.U)
                , new Location(Face.F, Face.R), new Position(Face.U, Face.B)));
        assertEquals("one",true, myCube.changesOnlyInThirdFloor(myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.L)
                , new Location(Face.F, Face.L), new Position(Face.U, Face.B)));
        assertEquals("two",false, myCube.changesOnlyInThirdFloor(myPermutation));
        }

    @Test
    public void testIsDifferentItemsOnlyInSecondFloorLessThanThree_partI(){
        Permutation myPermutation = new Permutation();
        Rubik myCube = new Rubik();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.R)
                , new Location(Face.F, Face.R), new Position(Face.U, Face.B)));
        assertEquals("one",true, myCube.isDifferentItemsOnlyInSecondFloorLessThanThree(myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.L)
                , new Location(Face.F, Face.L), new Position(Face.U, Face.B)));
        assertEquals("two",true, myCube.isDifferentItemsOnlyInSecondFloorLessThanThree(myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.L)
                , new Location(Face.B, Face.R), new Position(Face.U, Face.F)));
        assertEquals("three",false, myCube.isDifferentItemsOnlyInSecondFloorLessThanThree(myPermutation));

            }

    @Test
    public void testIsDifferentItemsOnlyInSecondFloorLessThanThree_partII(){
        Permutation myPermutation = new Permutation();
        Rubik myCube = new Rubik();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.R)
                , new Location(Face.F, Face.R), new Position(Face.U, Face.B)));
        assertEquals("one",true, myCube.isDifferentItemsOnlyInSecondFloorLessThanThree(myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.L)
                , new Location(Face.F, Face.L), new Position(Face.U, Face.B)));
        assertEquals("two",true, myCube.isDifferentItemsOnlyInSecondFloorLessThanThree(myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.D)
                , new Location(Face.B, Face.R), new Position(Face.U, Face.F)));
        assertEquals("three",false, myCube.isDifferentItemsOnlyInSecondFloorLessThanThree(myPermutation));

    }


    @Test
    public void testIsDifferentItemsInFirstFloorLessThanThree(){
        Permutation myPermutation = new Permutation();
        Rubik myCube = new Rubik();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.D)
                , new Location(Face.F, Face.U), new Position(Face.U, Face.F)));
        assertEquals("one",true, myCube.isDifferentItemsInFirstFloorLessThanThree(myPermutation));
                             
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.D, Face.R)
                , new         Location(Face.F, Face.D, Face.R), new Position(Face.U, Face.B)));
        assertEquals("two",true, myCube.isDifferentItemsInFirstFloorLessThanThree(myPermutation));
                             
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.F, Face.D, Face.L)
                , new         Location(Face.F, Face.D, Face.L), new Position(Face.U, Face.F)));
        assertEquals("three",true, myCube.isDifferentItemsInFirstFloorLessThanThree(myPermutation));
                             
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.B, Face.D, Face.L)
                , new         Location(Face.B, Face.D, Face.L), new Position(Face.U, Face.B)));
        assertEquals("four",false, myCube.isDifferentItemsInFirstFloorLessThanThree(myPermutation));
    }


    @Test
    public void constuctorTest() {
        Rubik myRubik = new Rubik();
        int numberOfAssertions = 0;
        for (Face firstFaceDimension : Face.values()) {
            for (Face secondFaceDimension : Face.values()) {
                if (firstFaceDimension != secondFaceDimension
                        && firstFaceDimension.getOpposite() != secondFaceDimension
//                        && firstFaceDimension != Face.NOTDEFINED
//                        && secondFaceDimension != Face.NOTDEFINED
                        ) {
                    assertEquals(true,
                            (new Location(firstFaceDimension, secondFaceDimension))
                                    .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(firstFaceDimension, secondFaceDimension))));
                    numberOfAssertions++;
                }
            }
        }
        assertEquals(24, numberOfAssertions);

    }


    @Test
    public void positionTest() {
        Rubik myRubik = new Rubik();
        myRubik.rotateFace(new Rotation(Face.U, Direction.CW));
        assertEquals("1",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.F))
                .equals(new Position(Face.U, Face.F)));

        myRubik.rotateFace(new Rotation(Face.R, Direction.CW));
        assertEquals("2",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.F))
                .equals(new Position(Face.U, Face.F)));

        myRubik.rotateFace(new Rotation(Face.L, Direction.CW));
        assertEquals("3",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.F))
                .equals(new Position(Face.U, Face.F)));

        Position yaki = myRubik.getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.L));

        myRubik.rotateFace(new Rotation(Face.D, Direction.CW));
        yaki = myRubik.getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.F));
        assertEquals("4",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.F))
                .equals(new Position(Face.B, Face.L)));


    }

    @Test
    public  void positionTest2() {
        Rubik myRubik = new Rubik();


        myRubik.rotateFace(new Rotation(Face.L, Direction.CW));
        assertEquals("1",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.F))
                .equals(new Position(Face.U, Face.F)));

        assertEquals("3",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.L))
                .equals(new Position(Face.B, Face.U)));

        myRubik.rotateFace(new Rotation(Face.D, Direction.CW));
        Position yaki = myRubik.getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.F));
        assertEquals("4",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.D, Face.F))
                .equals(new Position(Face.B, Face.L)));


    }


    @Test
    public  void rotateTest1() {
        Rubik myRubik = new Rubik();
        myRubik.rotateFace(new Rotation(Face.F, Direction.CW));
        assertEquals(true, (new Location(Face.F, Face.D))
                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.F, Face.L))));

    }

    @Test
    public void rotateTest2() {
        Rubik myRubik = new Rubik();
        myRubik.rotateFace(new Rotation(Face.D, Direction.CCW));
        assertEquals(true, (new Location(Face.D, Face.R))
                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.D, Face.F))));
    }

    @Test
    public void rotateTest3() {
    	Rubik myRubik = new Rubik();
        myRubik.rotateFace(new Rotation(Face.D, Direction.CCW));
        assertEquals(true, (new Location(Face.D, Face.R, Face.B))
                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.D, Face.R, Face.F))));
    }

    @Test
    public void TestgetOriginalLocationOfCurrentCubicleInLocation() {
        Rubik myRubik = new Rubik();
        myRubik.rotateFace(new Rotation(Face.F, Direction.CW));
        Location yaki = myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.D, Face.F));
        assertEquals(true, (new Location(Face.F, Face.R))
                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.D, Face.F))));
    }


}