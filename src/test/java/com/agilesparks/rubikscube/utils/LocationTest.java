package com.agilesparks.rubikscube.utils;


import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;

public class LocationTest {

    @Test
    public void isEdge() {
        Location myLocation = new Location(Face.D,Face.L, Face.F);
        assertEquals(false,myLocation.isEdge());
        myLocation = new Location(Face.D,Face.L);
        assertEquals(true,myLocation.isEdge());
    }

    @Test
    public void getFaces() {
        Location myLocation = new Location(Face.D,Face.L, Face.F);
        //taking into account facecs are sorted according to int value
        assertEquals(Face.D,myLocation.getFace0());
        assertEquals(Face.L,myLocation.getFace1());
        assertEquals(Face.F,myLocation.getFace2());
    }

    @Test
    public void equals() {
        Location myLocation = new Location(Face.D,Face.L, Face.F);
        Location mySecondLocation = new Location(Face.L,Face.F, Face.D);
        Location myThirdLocation = new Location(Face.R, Face.F, Face.D);
        assertEquals(true,mySecondLocation.equals(myLocation));
        assertEquals(false, mySecondLocation.equals(myThirdLocation));
    }

    @Test
    public void testGetFloor() {
        assertEquals("1",3, new Location(Face.U,Face.L, Face.F).getFloor());
        assertEquals("2",3, new Location(Face.U,Face.L, Face.B).getFloor());
        assertEquals("3",3, new Location(Face.U,Face.R, Face.F).getFloor());
        assertEquals("4",3, new Location(Face.U,Face.R, Face.B).getFloor());
        assertEquals("5",1, new Location(Face.D,Face.L, Face.F).getFloor());
        assertEquals("6",1, new Location(Face.D,Face.L, Face.B).getFloor());
        assertEquals("7",1, new Location(Face.D,Face.R, Face.F).getFloor());
        assertEquals("8",1, new Location(Face.D,Face.R, Face.B).getFloor());

        assertEquals("10",3, new Location(Face.U,Face.F).getFloor());
        assertEquals("11",3, new Location(Face.U,Face.B).getFloor());
        assertEquals("12",3, new Location(Face.U,Face.L).getFloor());
        assertEquals("13",3, new Location(Face.U,Face.R).getFloor());

        assertEquals("14",2, new Location(Face.F,Face.L).getFloor());
        assertEquals("15",2, new Location(Face.F,Face.R).getFloor());
        assertEquals("16",2, new Location(Face.B,Face.L).getFloor());
        assertEquals("17",2, new Location(Face.B,Face.R).getFloor());

        assertEquals("18",1, new Location(Face.D,Face.L).getFloor());
        assertEquals("19",1, new Location(Face.D,Face.R).getFloor());
        assertEquals("20",1, new Location(Face.F,Face.D).getFloor());
        assertEquals("21",1, new Location(Face.B,Face.D).getFloor());


    }

    @Test
    public void getString() {
        Location myLocation = new Location(Face.D,Face.L, Face.F);
        assertEquals("D, L, F", myLocation.getString());
        myLocation = new Location(Face.D,Face.L);
        assertEquals("D, L",myLocation.getString());

    }
}