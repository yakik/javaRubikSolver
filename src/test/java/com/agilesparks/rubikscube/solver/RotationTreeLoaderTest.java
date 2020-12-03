package com.agilesparks.rubikscube.solver;


import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

import com.agilesparks.rubikscube.cube.RubikFileReader;
import com.agilesparks.rubikscube.solver.RotationSequence;
import com.agilesparks.rubikscube.solver.RotationTree;
import com.agilesparks.rubikscube.solver.RotationTreeLoader;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Rotation;

public class RotationTreeLoaderTest {

    @Test
    public void loadSearchTree() {
//
    }

    
    @Test
    public void numberNodesRotationTree() {
        RotationSequence l_rotationLinkedList = new RotationSequence();
        RotationTree l_tree = new RotationTree();
        RotationTreeLoader.loadRotationTreeFromStandard(l_tree, l_rotationLinkedList, 4);
     //   int numberOfNodes = l_tree.getNumberOfNodes();
     //   assertEquals(11205, numberOfNodes);


    }

    @Ignore
    @Test
    public  void loadRotationTreeFromFile() {
        RotationSequence l_rotationLinkedList = new RotationSequence();
        RotationTree l_tree = new RotationTree();
        forTestRubikFileReader myTestReader = new forTestRubikFileReader("(5,1) (3,1) (1,0) (3,0) (4,0) (3,0) (4,1) (1,1) \n" +
                "(5,1) (3,1) (1,0) (3,0) (5,0) \n");
        RotationTreeLoader.loadRotationTreeFromFile(myTestReader, l_tree);
        assertEquals(Direction.CCW,l_tree.getRotationSequence(1).getRotation(0).getDirection());
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
        RotationSequence l_rotationLinkedList = new RotationSequence();
        RotationTree l_tree = new RotationTree();
        RotationTreeLoader.loadRotationTreeFromStandard(l_tree, l_rotationLinkedList, 1);
        int i=-1;
        for (Face face : Face.values())
            for (Direction direction : Direction.values()) {
            i++;
                int rotationValue = (new Rotation(face,direction)).getValue();
                assertEquals(face, l_tree.getRotationSequence(i).getRotation(0).getFace());
                assertEquals(direction, l_tree.getRotationSequence(i).getRotation(0).getDirection());
            }
    }
}