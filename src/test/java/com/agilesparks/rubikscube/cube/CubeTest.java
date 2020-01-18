package com.agilesparks.rubikscube.cube;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.cube.CubeCubicle;
import com.agilesparks.rubikscube.cube.Cube;
import com.agilesparks.rubikscube.solver.AssistAssertRubik;
import com.agilesparks.rubikscube.solver.CubeStatus;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Permutation;
import com.agilesparks.rubikscube.utils.Position;
import com.agilesparks.rubikscube.utils.Rotation;

public class CubeTest {

    @Test
    public  void setPermutationTest() {
        Permutation myPermutation = new Permutation();
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.TOP), new Location(Face.FRONT, Face.TOP), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.RIGHT), new Location(Face.FRONT, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.LEFT), new Location(Face.FRONT, Face.LEFT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM), new Location(Face.FRONT, Face.BOTTOM), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.TOP), new Location(Face.BACK, Face.TOP), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.RIGHT), new Location(Face.BACK, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.LEFT), new Location(Face.BACK, Face.LEFT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.BOTTOM), new Location(Face.BACK, Face.BOTTOM), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.TOP, Face.RIGHT), new Location(Face.TOP, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.TOP, Face.LEFT), new Location(Face.TOP, Face.LEFT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BOTTOM, Face.RIGHT), new Location(Face.BOTTOM, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BOTTOM, Face.LEFT), new Location(Face.BOTTOM, Face.LEFT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.TOP, Face.RIGHT), new Location(Face.FRONT, Face.TOP, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.TOP, Face.LEFT), new Location(Face.FRONT, Face.TOP, Face.LEFT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM, Face.RIGHT), new Location(Face.FRONT, Face.BOTTOM, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM, Face.LEFT), new Location(Face.FRONT, Face.BOTTOM, Face.LEFT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.TOP, Face.RIGHT), new Location(Face.BACK, Face.TOP, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.TOP, Face.LEFT), new Location(Face.BACK, Face.TOP, Face.LEFT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.BOTTOM, Face.RIGHT), new Location(Face.BACK, Face.BOTTOM, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.BOTTOM, Face.LEFT), new Location(Face.BACK, Face.BOTTOM, Face.LEFT), new Position(Face.TOP, Face.FRONT)));

        Cube myRubik = new Cube();



        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);

        myRubik.setPermutation(myPermutation);
        AssistAssertRubik.checkEntireCube(myRubik);


    }
    @Test
    public void testChangesOnlyInThirdFloor_partII(){
        Permutation myPermutation = new Permutation();
        Cube myCube = new Cube();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.TOP)
                , new Location(Face.FRONT, Face.RIGHT), new Position(Face.TOP, Face.BACK)));
        assertEquals("one",true, CubeStatus.changesOnlyInThirdFloor(myCube, myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM)
                , new Location(Face.FRONT, Face.LEFT), new Position(Face.TOP, Face.BACK)));
        assertEquals("two",false, CubeStatus.changesOnlyInThirdFloor(myCube, myPermutation));
    }


    @Test
    public void testChangesOnlyInThirdFloor_partI(){
        Permutation myPermutation = new Permutation();
        Cube myCube = new Cube();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.TOP)
                , new Location(Face.FRONT, Face.RIGHT), new Position(Face.TOP, Face.BACK)));
        assertEquals("one",true, CubeStatus.changesOnlyInThirdFloor(myCube, myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.LEFT)
                , new Location(Face.FRONT, Face.LEFT), new Position(Face.TOP, Face.BACK)));
        assertEquals("two",false, CubeStatus.changesOnlyInThirdFloor(myCube, myPermutation));
        }

    @Test
    public void testIsDifferentItemsOnlyInSecondFloorLessThanThree_partI(){
        Permutation myPermutation = new Permutation();
        Cube myCube = new Cube();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.RIGHT)
                , new Location(Face.FRONT, Face.RIGHT), new Position(Face.TOP, Face.BACK)));
        assertEquals("one",true, CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(myCube, myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.LEFT)
                , new Location(Face.FRONT, Face.LEFT), new Position(Face.TOP, Face.BACK)));
        assertEquals("two",true, CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(myCube, myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.LEFT)
                , new Location(Face.BACK, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        assertEquals("three",false, CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(myCube, myPermutation));

            }

    @Test
    public void testIsDifferentItemsOnlyInSecondFloorLessThanThree_partII(){
        Permutation myPermutation = new Permutation();
        Cube myCube = new Cube();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.RIGHT)
                , new Location(Face.FRONT, Face.RIGHT), new Position(Face.TOP, Face.BACK)));
        assertEquals("one",true, CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(myCube, myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.LEFT)
                , new Location(Face.FRONT, Face.LEFT), new Position(Face.TOP, Face.BACK)));
        assertEquals("two",true, CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(myCube, myPermutation));

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.BOTTOM)
                , new Location(Face.BACK, Face.RIGHT), new Position(Face.TOP, Face.FRONT)));
        assertEquals("three",false, CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(myCube, myPermutation));

    }


    @Test
    public void testIsDifferentItemsInFirstFloorLessThanThree(){
        Permutation myPermutation = new Permutation();
        Cube myCube = new Cube();

        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM)
                , new Location(Face.FRONT, Face.TOP), new Position(Face.TOP, Face.FRONT)));
        assertEquals("one",true, CubeStatus.isDifferentItemsInFirstFloorLessThanThree(myCube, myPermutation));
                             
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM, Face.RIGHT)
                , new         Location(Face.FRONT, Face.BOTTOM, Face.RIGHT), new Position(Face.TOP, Face.BACK)));
        assertEquals("two",true, CubeStatus.isDifferentItemsInFirstFloorLessThanThree(myCube, myPermutation));
                             
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM, Face.LEFT)
                , new         Location(Face.FRONT, Face.BOTTOM, Face.LEFT), new Position(Face.TOP, Face.FRONT)));
        assertEquals("three",true, CubeStatus.isDifferentItemsInFirstFloorLessThanThree(myCube, myPermutation));
                             
        myPermutation.addCubicleData(new CubeCubicle(new Location(Face.BACK, Face.BOTTOM, Face.LEFT)
                , new         Location(Face.BACK, Face.BOTTOM, Face.LEFT), new Position(Face.TOP, Face.BACK)));
        assertEquals("four",false, CubeStatus.isDifferentItemsInFirstFloorLessThanThree(myCube, myPermutation));
    }


    @Test
    public void constuctorTest() {
        Cube myRubik = new Cube();
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
        Cube myRubik = new Cube();
        myRubik.rotateFace(Face.TOP, Direction.CW);
        assertEquals("1",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.FRONT))
                .equals(new Position(Face.TOP, Face.FRONT)));

        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        assertEquals("2",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.FRONT))
                .equals(new Position(Face.TOP, Face.FRONT)));

        myRubik.rotateFace(Face.LEFT, Direction.CW);
        assertEquals("3",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.FRONT))
                .equals(new Position(Face.TOP, Face.FRONT)));

        Position yaki = myRubik.getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.LEFT));

        myRubik.rotateFace(Face.BOTTOM, Direction.CW);
        yaki = myRubik.getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.FRONT));
        assertEquals("4",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.FRONT))
                .equals(new Position(Face.BACK, Face.LEFT)));


    }

    @Test
    public  void positionTest2() {
        Cube myRubik = new Cube();


        myRubik.rotateFace(Face.LEFT, Direction.CW);
        assertEquals("1",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.FRONT))
                .equals(new Position(Face.TOP, Face.FRONT)));

        assertEquals("3",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.LEFT))
                .equals(new Position(Face.BACK, Face.TOP)));

        myRubik.rotateFace(Face.BOTTOM, Direction.CW);
        Position yaki = myRubik.getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.FRONT));
        assertEquals("4",true, myRubik
                .getPositionOfCubicleOfCubiclePlace(new Location(Face.BOTTOM, Face.FRONT))
                .equals(new Position(Face.BACK, Face.LEFT)));


    }


    @Test
    public  void rotateTest1() {
        Cube myRubik = new Cube();
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        assertEquals(true, (new Location(Face.FRONT, Face.BOTTOM))
                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.FRONT, Face.LEFT))));

    }

    @Test
    public void rotateTest2() {
        Cube myRubik = new Cube();
        myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
        assertEquals(true, (new Location(Face.BOTTOM, Face.RIGHT))
                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.BOTTOM, Face.FRONT))));
    }

    @Test
    public void rotateTest3() {
    	Cube myRubik = new Cube();
        myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
        assertEquals(true, (new Location(Face.BOTTOM, Face.RIGHT, Face.BACK))
                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.BOTTOM, Face.RIGHT, Face.FRONT))));
    }

    @Test
    public void TestgetOriginalLocationOfCurrentCubicleInLocation() {
        Cube myRubik = new Cube();
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        Location yaki = myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.BOTTOM, Face.FRONT));
        assertEquals(true, (new Location(Face.FRONT, Face.RIGHT))
                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.BOTTOM, Face.FRONT))));
    }


}