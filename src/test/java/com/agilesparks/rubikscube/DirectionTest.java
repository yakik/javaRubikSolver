package com.agilesparks.rubikscube;



import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Direction;

public class DirectionTest {
    @Test
    public void testDirectionGetIntGetChar() {
        Direction myDirection = Direction.CW;
        assertEquals(0, myDirection.getInt());
        assertEquals("CW", myDirection.getString());
        myDirection = Direction.CCW;
        assertEquals(1, myDirection.getInt());
        assertEquals("CCW", myDirection.getString());
           };

    @Test
    public void testDirectionEquals() {
        Direction myDirection = Direction.CW;
        assertEquals(Direction.CW, myDirection);
        assertEquals(true, myDirection==Direction.CW);
    }
    @Test
    public void Direction() {
        Direction myDirection = Direction.CW;
        assertEquals(Direction.CCW, myDirection.getOpposite());
        myDirection = Direction.CCW;
        assertEquals(Direction.CW, myDirection.getOpposite());
    }

}