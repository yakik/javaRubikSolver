package com.agilesparks.rubikscube.solver;


import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

import com.agilesparks.rubikscube.cube.RubikFileReader;
import com.agilesparks.rubikscube.cube.RubikFileWriter;
import com.agilesparks.rubikscube.solver.RotationSequence;
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

    @Ignore
    @Test
    public void testWriteRead() {
        RotationSequence myList = new RotationSequence();
        myList.addRotation(new Rotation(Face.FRONT,Direction.CW));
        myList.addRotation(new Rotation(Face.TOP,Direction.CCW));
        RubikFileWriter myWriter = new RubikFileWriter("writeLinked.txt");
        myList.writeToFile(myWriter);
        myWriter.close();
        RubikFileReader myReader = new RubikFileReader("writeLinked.txt");
        RotationSequence mySecondList = new RotationSequence();
        mySecondList.readFromFile(myReader);
        assertEquals("first",true,myList.getRotation(0).equals(mySecondList.getRotation(0)));
        assertEquals("first",true,myList.getRotation(1).equals(mySecondList.getRotation(1)));
    }



    @Test
    public void isRedundantCCW() {
        RotationSequence myList = new RotationSequence();
        myList.addRotation(new Rotation(Face.FRONT,Direction.CCW));
        myList.addRotation(new Rotation(Face.FRONT,Direction.CCW));
        assertEquals(true,myList.isRedundant(new Rotation(Face.FRONT, Direction.CCW)));


    }
}