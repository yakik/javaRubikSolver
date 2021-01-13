package com.agilesparks.rubikscube.utils;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;

public class LocationTest {

    @Test
    public void isEdge() {
        Location myLocation = new Location(Face.BOTTOM,Face.LEFT, Face.FRONT);
        assertEquals(false,myLocation.isEdge());
        myLocation = new Location(Face.BOTTOM,Face.LEFT);
        assertEquals(true,myLocation.isEdge());
    }

    @Test
    public void getFaces() {
        Location myLocation = new Location(Face.BOTTOM,Face.LEFT, Face.FRONT);
        //taking into account facecs are sorted according to int value
        assertEquals(Face.BOTTOM,myLocation.getFace0());
        assertEquals(Face.LEFT,myLocation.getFace1());
        assertEquals(Face.FRONT,myLocation.getFace2());
    }

    @Test
    public void equals() {
        Location myLocation = new Location(Face.BOTTOM,Face.LEFT, Face.FRONT);
        Location mySecondLocation = new Location(Face.LEFT,Face.FRONT, Face.BOTTOM);
        Location myThirdLocation = new Location(Face.RIGHT, Face.FRONT, Face.BOTTOM);
        assertEquals(true,mySecondLocation.equals(myLocation));
        assertEquals(false, mySecondLocation.equals(myThirdLocation));
    }

    @Test
    public void testGetFloor() {
        assertEquals("1",3, new Location(Face.TOP,Face.LEFT, Face.FRONT).getFloor());
        assertEquals("2",3, new Location(Face.TOP,Face.LEFT, Face.BACK).getFloor());
        assertEquals("3",3, new Location(Face.TOP,Face.RIGHT, Face.FRONT).getFloor());
        assertEquals("4",3, new Location(Face.TOP,Face.RIGHT, Face.BACK).getFloor());
        assertEquals("5",1, new Location(Face.BOTTOM,Face.LEFT, Face.FRONT).getFloor());
        assertEquals("6",1, new Location(Face.BOTTOM,Face.LEFT, Face.BACK).getFloor());
        assertEquals("7",1, new Location(Face.BOTTOM,Face.RIGHT, Face.FRONT).getFloor());
        assertEquals("8",1, new Location(Face.BOTTOM,Face.RIGHT, Face.BACK).getFloor());

        assertEquals("10",3, new Location(Face.TOP,Face.FRONT).getFloor());
        assertEquals("11",3, new Location(Face.TOP,Face.BACK).getFloor());
        assertEquals("12",3, new Location(Face.TOP,Face.LEFT).getFloor());
        assertEquals("13",3, new Location(Face.TOP,Face.RIGHT).getFloor());

        assertEquals("14",2, new Location(Face.FRONT,Face.LEFT).getFloor());
        assertEquals("15",2, new Location(Face.FRONT,Face.RIGHT).getFloor());
        assertEquals("16",2, new Location(Face.BACK,Face.LEFT).getFloor());
        assertEquals("17",2, new Location(Face.BACK,Face.RIGHT).getFloor());

        assertEquals("18",1, new Location(Face.BOTTOM,Face.LEFT).getFloor());
        assertEquals("19",1, new Location(Face.BOTTOM,Face.RIGHT).getFloor());
        assertEquals("20",1, new Location(Face.FRONT,Face.BOTTOM).getFloor());
        assertEquals("21",1, new Location(Face.BACK,Face.BOTTOM).getFloor());


    }

    @Test
    public void getString() {
        Location myLocation = new Location(Face.BOTTOM,Face.LEFT, Face.FRONT);
        assertEquals("D, L, F", myLocation.getString());
        myLocation = new Location(Face.BOTTOM,Face.LEFT);
        assertEquals("D, L",myLocation.getString());

    }
}