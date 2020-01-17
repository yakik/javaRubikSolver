package com.agilesparks.rubikscube;


import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

import com.agilesparks.rubikscube.RotationLinkedList;
import com.agilesparks.rubikscube.RubikFileWriter;
import com.agilesparks.rubikscube.utils.Face;

public class RotationLinkedListTest {

    @Test
    public void isRedundantCW() {
        RotationLinkedList myList = new RotationLinkedList();
                myList.addRotation(new Rotation(Face.F,Direction.CW));
        assertEquals(true,myList.isRedundant(new Rotation(Face.F, Direction.CW)));


    }

    @Ignore
    @Test
    public void testWriteRead() {
        RotationLinkedList myList = new RotationLinkedList();
        myList.addRotation(new Rotation(Face.F,Direction.CW));
        myList.addRotation(new Rotation(Face.U,Direction.CCW));
        RubikFileWriter myWriter = new RubikFileWriter("writeLinked.txt");
        myList.writeToFile(myWriter);
        myWriter.close();
        RubikFileReader myReader = new RubikFileReader("writeLinked.txt");
        RotationLinkedList mySecondList = new RotationLinkedList();
        mySecondList.readFromFile(myReader);
        assertEquals("first",true,myList.get(0).equals(mySecondList.get(0)));
        assertEquals("first",true,myList.get(1).equals(mySecondList.get(1)));
    }



    @Test
    public void isRedundantCCW() {
        RotationLinkedList myList = new RotationLinkedList();
        myList.addRotation(new Rotation(Face.F,Direction.CCW));
        myList.addRotation(new Rotation(Face.F,Direction.CCW));
        assertEquals(true,myList.isRedundant(new Rotation(Face.F, Direction.CCW)));


    }
}