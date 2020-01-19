package com.agilesparks.rubikscube.cube;


import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

import com.agilesparks.rubikscube.solver.AssistAssertRubik;
import com.agilesparks.rubikscube.utils.Color;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.LocationInFace;
import com.agilesparks.rubikscube.utils.Position;

public class NewCubeTest {
	@Test
    public  void overallTest() {
		NewCube myRubik = new NewCube(), myRubik2 = new NewCube();
		myRubik.rotateFace(Face.FRONT, Direction.CW);
		assertEquals(8,myRubik.countAllDifferences(myRubik2));
		myRubik.rotateFace(Face.TOP, Direction.CW);
		assertEquals(13,myRubik.countAllDifferences(myRubik2));
	}
	
	@Test
    public  void compareFirstFloor() {
		NewCube myRubik = new NewCube(), myRubik2 = new NewCube();
		myRubik.setColor(Face.FRONT, LocationInFace.BOTTOMLEFT, Color.BACKCOLOR);
		myRubik.setColor(Face.BACK, LocationInFace.BOTTOM, Color.FRONTCOLOR);
		myRubik.setColor(Face.FRONT, LocationInFace.TOPLEFT, Color.BACKCOLOR);
		assertEquals(2,myRubik.countDifferenceFirstFloor(myRubik2));
		myRubik.setColor(Face.LEFT, LocationInFace.BOTTOMLEFT, Color.BACKCOLOR);
		assertEquals(3,myRubik.countDifferenceFirstFloor(myRubik2));
		
		
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
	    
}
