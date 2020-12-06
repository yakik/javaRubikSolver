package com.agilesparks.rubikscube.solver;


import static org.junit.Assert.*;

import org.junit.*;

import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Rotation;

public class RotationLinkedListTest {

    @Test
    public void isRedundantCW() {
        RotationSequence myList = new RotationSequence();
                myList.addRotation(new Rotation(Face.FRONT,Direction.CW));
        assertEquals(true,myList.isRedundant(new Rotation(Face.FRONT, Direction.CW)));
    }

    @Test
    public void isRedundantCCW() {
        RotationSequence myList = new RotationSequence();
        myList.addRotation(new Rotation(Face.FRONT,Direction.CCW));
        myList.addRotation(new Rotation(Face.FRONT,Direction.CCW));
        assertEquals(true,myList.isRedundant(new Rotation(Face.FRONT, Direction.CCW)));
    }
}