package com.agilesparks.rubikscube.cube;


import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

import com.agilesparks.rubikscube.solver.AssistAssertRubik;
import com.agilesparks.rubikscube.solver.CubeStatus;
import com.agilesparks.rubikscube.utils.Color;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.LocationInFace;
import com.agilesparks.rubikscube.utils.Permutation;
import com.agilesparks.rubikscube.utils.Position;

public class NewCubeTest {
	@Ignore
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
	 
	 	@Ignore
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


	    @Ignore
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

	    @Ignore
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

	    @Ignore
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


	    @Ignore
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


	    @Ignore
	    @Test
	    public void constuctorTest() {
	        Cube myRubik = new Cube();
	        int numberOfAssertions = 0;
	        for (Face firstFaceDimension : Face.values()) {
	            for (Face secondFaceDimension : Face.values()) {
	                if (firstFaceDimension != secondFaceDimension
	                        && firstFaceDimension.getOpposite() != secondFaceDimension
//	                        && firstFaceDimension != Face.NOTDEFINED
//	                        && secondFaceDimension != Face.NOTDEFINED
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


	    @Ignore
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

	    @Ignore
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
	    public  void rotateFrontClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.FRONT, Direction.CW);
	        assertEquals("1",Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOM));
	        assertEquals("2",Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        assertEquals("3",Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
	        assertEquals("4",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.FRONT, Direction.CW);
		    myRubik.rotateFace(Face.FRONT, Direction.CW);
		    myRubik.rotateFace(Face.FRONT, Direction.CW);
	        assertEquals("5",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        assertEquals("6",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        assertEquals("7",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
	        assertEquals("8",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateLeftClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.LEFT, Direction.CW);
	        assertEquals("1",Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT));
	        assertEquals("2",Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        assertEquals("3",Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
	        assertEquals("4",Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.LEFT, Direction.CW);
		    myRubik.rotateFace(Face.LEFT, Direction.CW);
		    myRubik.rotateFace(Face.LEFT, Direction.CW);
	        assertEquals("5",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT));       
	        assertEquals("6",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT)); 
	        assertEquals("7",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));    
	        assertEquals("8",Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateRightClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.RIGHT, Direction.CW);
	        assertEquals("1",Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT));
	        assertEquals("2",Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
	        assertEquals("3",Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
	        assertEquals("4",Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.RIGHT, Direction.CW);
		    myRubik.rotateFace(Face.RIGHT, Direction.CW);
		    myRubik.rotateFace(Face.RIGHT, Direction.CW);
	        assertEquals("5",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT));      
	        assertEquals("6",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
	        assertEquals("7",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));   
	        assertEquals("8",Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT,LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateBackClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.BACK, Direction.CW);
	        assertEquals("1",Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP));
	        assertEquals("2",Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
	        assertEquals("3",Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
	        assertEquals("4",Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.BACK, Direction.CW);
		    myRubik.rotateFace(Face.BACK, Direction.CW);
		    myRubik.rotateFace(Face.BACK, Direction.CW);
	        assertEquals("5",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP));     
	        assertEquals("6",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
	        assertEquals("7",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT)); 
	        assertEquals("8",Color.BACKCOLOR, myRubik.getColor(Face.BACK,LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateTopClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.TOP, Direction.CW);
	        assertEquals("1",Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP));
	        assertEquals("2",Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT));
	        assertEquals("3",Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT));
	        assertEquals("4",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.TOP, Direction.CW);
		    myRubik.rotateFace(Face.TOP, Direction.CW);
		    myRubik.rotateFace(Face.TOP, Direction.CW);
	        assertEquals("5",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP));     
	        assertEquals("6",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT));
	        assertEquals("7",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT)); 
	        assertEquals("8",Color.TOPCOLOR, myRubik.getColor(Face.TOP,LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateBottomClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.BOTTOM, Direction.CW);
	        assertEquals("1",Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM));
	        assertEquals("2",Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT));
	        assertEquals("3",Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
	        assertEquals("4",Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.BOTTOM, Direction.CW);
		    myRubik.rotateFace(Face.BOTTOM, Direction.CW);
		    myRubik.rotateFace(Face.BOTTOM, Direction.CW);
	        assertEquals("5",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM));     
	        assertEquals("6",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT));
	        assertEquals("7",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT)); 
	        assertEquals("8",Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM,LocationInFace.BOTTOMLEFT));

	    }

	    
	    @Test
	    public  void rotateFrontCounterClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.FRONT, Direction.CCW);
	        assertEquals("1",Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOM));
	        assertEquals("2",Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        assertEquals("3",Color.RIGHTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
	        assertEquals("4",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.FRONT, Direction.CCW);
		    myRubik.rotateFace(Face.FRONT, Direction.CCW);
		    myRubik.rotateFace(Face.FRONT, Direction.CCW);
	        assertEquals("5",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        assertEquals("6",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        assertEquals("7",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
	        assertEquals("8",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateLeftCounterClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.LEFT, Direction.CCW);
	        assertEquals("1",Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT));
	        assertEquals("2",Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        assertEquals("3",Color.FRONTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
	        assertEquals("4",Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.LEFT, Direction.CCW);
		    myRubik.rotateFace(Face.LEFT, Direction.CCW);
		    myRubik.rotateFace(Face.LEFT, Direction.CCW);
	        assertEquals("5",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.LEFT));       
	        assertEquals("6",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT)); 
	        assertEquals("7",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));    
	        assertEquals("8",Color.LEFTCOLOR, myRubik.getColor(Face.LEFT, LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateRightCounterClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.RIGHT, Direction.CCW);
	        assertEquals("1",Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT));
	        assertEquals("2",Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
	        assertEquals("3",Color.BACKCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
	        assertEquals("4",Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.RIGHT, Direction.CCW);
		    myRubik.rotateFace(Face.RIGHT, Direction.CCW);
		    myRubik.rotateFace(Face.RIGHT, Direction.CCW);
	        assertEquals("5",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.RIGHT));      
	        assertEquals("6",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMRIGHT));
	        assertEquals("7",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));   
	        assertEquals("8",Color.RIGHTCOLOR, myRubik.getColor(Face.RIGHT,LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateBackCounterClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.BACK, Direction.CCW);
	        assertEquals("1",Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP));
	        assertEquals("2",Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
	        assertEquals("3",Color.LEFTCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT));
	        assertEquals("4",Color.BACKCOLOR, myRubik.getColor(Face.BACK, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.BACK, Direction.CCW);
		    myRubik.rotateFace(Face.BACK, Direction.CCW);
		    myRubik.rotateFace(Face.BACK, Direction.CCW);
	        assertEquals("5",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOP));     
	        assertEquals("6",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPRIGHT));
	        assertEquals("7",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.TOPLEFT)); 
	        assertEquals("8",Color.BACKCOLOR, myRubik.getColor(Face.BACK,LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateTopCounterClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.TOP, Direction.CCW);
	        assertEquals("1",Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP));
	        assertEquals("2",Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT));
	        assertEquals("3",Color.LEFTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT));
	        assertEquals("4",Color.TOPCOLOR, myRubik.getColor(Face.TOP, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.TOP, Direction.CCW);
		    myRubik.rotateFace(Face.TOP, Direction.CCW);
		    myRubik.rotateFace(Face.TOP, Direction.CCW);
	        assertEquals("5",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOP));     
	        assertEquals("6",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPRIGHT));
	        assertEquals("7",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.TOPLEFT)); 
	        assertEquals("8",Color.TOPCOLOR, myRubik.getColor(Face.TOP,LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Test
	    public  void rotateBottomCounterClockwise() {
	        //Colors for : Front, Back, Right, Left, Top and Bottom  faces
	    	NewCube myRubik = new NewCube();
	        myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
	        assertEquals("1",Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM));
	        assertEquals("2",Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT));
	        assertEquals("3",Color.RIGHTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT));
	        assertEquals("4",Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM, LocationInFace.BOTTOMLEFT));
	        myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
		    myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
		    myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
	        assertEquals("5",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOM));     
	        assertEquals("6",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMRIGHT));
	        assertEquals("7",Color.FRONTCOLOR, myRubik.getColor(Face.FRONT, LocationInFace.BOTTOMLEFT)); 
	        assertEquals("8",Color.BOTTOMCOLOR, myRubik.getColor(Face.BOTTOM,LocationInFace.BOTTOMLEFT));

	    }
	    
	    @Ignore
	    @Test
	    public void rotateTest2() {
	        Cube myRubik = new Cube();
	        myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
	        assertEquals(true, (new Location(Face.BOTTOM, Face.RIGHT))
	                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.BOTTOM, Face.FRONT))));
	    }

	    @Ignore
	    @Test
	    public void rotateTest3() {
	    	Cube myRubik = new Cube();
	        myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
	        assertEquals(true, (new Location(Face.BOTTOM, Face.RIGHT, Face.BACK))
	                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.BOTTOM, Face.RIGHT, Face.FRONT))));
	    }

	    @Ignore
	    @Test
	    public void TestgetOriginalLocationOfCurrentCubicleInLocation() {
	        Cube myRubik = new Cube();
	        myRubik.rotateFace(Face.FRONT, Direction.CW);
	        Location yaki = myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.BOTTOM, Face.FRONT));
	        assertEquals(true, (new Location(Face.FRONT, Face.RIGHT))
	                .equals(myRubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(Face.BOTTOM, Face.FRONT))));
	    }


}
