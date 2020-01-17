package com.agilesparks.rubikscube;


import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

import com.agilesparks.rubikscube.RotationLinkedList;
import com.agilesparks.rubikscube.RotationTree;
import com.agilesparks.rubikscube.RotationTreeLoader;
import com.agilesparks.rubikscube.utils.Face;

public class RotationTreeLoaderTest {

    @Test
    public void loadSearchTree() {
//
    }

    @Test
    public void numberNodesRotationTree() {
        RotationLinkedList l_rotationLinkedList = new RotationLinkedList();
        RotationTree l_tree = new RotationTree();
        RotationTreeLoader.loadRotationTreeFromStandard(l_tree, l_rotationLinkedList, 4);
     //   int numberOfNodes = l_tree.getNumberOfNodes();
     //   assertEquals(11205, numberOfNodes);


    }

    @Ignore
    @Test
    public  void loadRotationTreeFromFile() {
        RotationLinkedList l_rotationLinkedList = new RotationLinkedList();
        RotationTree l_tree = new RotationTree();
        forTestRubikFileReader myTestReader = new forTestRubikFileReader("(5,1) (3,1) (1,0) (3,0) (4,0) (3,0) (4,1) (1,1) \n" +
                "(5,1) (3,1) (1,0) (3,0) (5,0) \n");
        RotationTreeLoader.loadRotationTreeFromFile(myTestReader, l_tree);
        assertEquals(Direction.CCW,l_tree.getRotationLinkedList(1).get(0).getDirection());
    }

    @Ignore
    @Test
    public void writeToFileXLevelsSecondAndThird() {
        RotationTreeLoader.findGoodRotationLinks("tstFirstFloor.txt", "tstSecondFloor.txt"
        ,"tstThirdFloor.txt",2);
        RotationTree firstFloorTree = new RotationTree();
        RotationTree secondFloorTree = new RotationTree();
        RotationTree thirdFloorTree = new RotationTree();
        RubikFileReader readFirstFloor = new RubikFileReader("tstFirstFloor.txt");
        RubikFileReader readSecondFloor = new RubikFileReader("tstSecondFloor.txt");
        RubikFileReader readThirdFloor = new RubikFileReader("tstThirdFloor.txt");
        RotationTreeLoader.loadRotationTreeFromFile(readFirstFloor,firstFloorTree);
        RotationTreeLoader.loadRotationTreeFromFile(readSecondFloor, secondFloorTree);
        RotationTreeLoader.loadRotationTreeFromFile(readThirdFloor,thirdFloorTree);


    }




    @Test
    public void loadRotationTreeFromStandard() {
        RotationLinkedList l_rotationLinkedList = new RotationLinkedList();
        RotationTree l_tree = new RotationTree();
        RotationTreeLoader.loadRotationTreeFromStandard(l_tree, l_rotationLinkedList, 1);
        int i=-1;
        for (Face face : Face.values())
            for (Direction direction : Direction.values()) {
            i++;
                int rotationValue = (new Rotation(face,direction)).getValue();
                assertEquals(face, l_tree.getRotationLinkedList(i).get(0).getFace());
                assertEquals(direction, l_tree.getRotationLinkedList(i).get(0).getDirection());
            }
    }
}