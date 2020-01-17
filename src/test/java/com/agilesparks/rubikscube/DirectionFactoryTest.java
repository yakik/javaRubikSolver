package com.agilesparks.rubikscube;



import static org.junit.Assert.*;

import org.junit.Test;

import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.DirectionFactory;

public class DirectionFactoryTest {

    @Test
    public void getDirectionByInt() {
        DirectionFactory myFactory = new DirectionFactory();
        assertEquals("CWDirection",Direction.CW, DirectionFactory.getDirectionByInt(0));
        assertEquals("CCWDirection",Direction.CCW, DirectionFactory.getDirectionByInt(1));
    }
}