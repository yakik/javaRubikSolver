package com.agilesparks.rubikscube.solver;


import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

import com.agilesparks.rubikscube.cube.Cube;
import com.agilesparks.rubikscube.cube.Permutation;
import com.agilesparks.rubikscube.cube.RubikFileReader;
import com.agilesparks.rubikscube.solver.RotationLinkedList;
import com.agilesparks.rubikscube.solver.RotationTree;
import com.agilesparks.rubikscube.solver.RotationTreeLoader;
import com.agilesparks.rubikscube.solver.Solution;
import com.agilesparks.rubikscube.solver.Solver;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Rotation;

public class SolverTest {


    @Test
    public void simpleRotations() {
        Cube myRubik = new Cube();
        for (int i=0;i<20;i++) {
            myRubik.rotateFace(Face.TOP, Direction.CW);
            myRubik.rotateFace(Face.RIGHT, Direction.CW);
            myRubik.rotateFace(Face.LEFT, Direction.CW);
            myRubik.rotateFace(Face.BOTTOM, Direction.CW);
            myRubik.rotateFace(Face.RIGHT, Direction.CW);
            myRubik.rotateFace(Face.TOP, Direction.CW);
            myRubik.rotateFace(Face.RIGHT, Direction.CW);
            myRubik.rotateFace(Face.BACK, Direction.CW);
            myRubik.rotateFace(Face.LEFT, Direction.CW);
            myRubik.rotateFace(Face.FRONT, Direction.CW);
        }
        for (int i=0;i<20;i++) {
            myRubik.rotateFace(Face.FRONT, Direction.CCW);
            myRubik.rotateFace(Face.LEFT, Direction.CCW);
            myRubik.rotateFace(Face.BACK, Direction.CCW);
            myRubik.rotateFace(Face.RIGHT, Direction.CCW);
            myRubik.rotateFace(Face.TOP, Direction.CCW);
            myRubik.rotateFace(Face.RIGHT, Direction.CCW);
            myRubik.rotateFace(Face.BOTTOM, Direction.CCW);
            myRubik.rotateFace(Face.LEFT, Direction.CCW);
            myRubik.rotateFace(Face.RIGHT, Direction.CCW);
            myRubik.rotateFace(Face.TOP, Direction.CCW);
        }
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CCW);
        AssistAssertRubik.checkEntireCube(myRubik);

    }



    @Test
    public void simpleSolver() {
        Cube myRubik = new Cube();

        myRubik.rotateFace(Face.TOP, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.BOTTOM, Direction.CW);
        RotationTree myTree = new RotationTree();
        RotationLinkedList myRotationLinkedList = new RotationLinkedList();
        myRotationLinkedList.addRotation(new Rotation(Face.TOP, Direction.CCW));
        myTree.addRotationLinkedList(myRotationLinkedList);

        myRotationLinkedList = new RotationLinkedList();
        myRotationLinkedList.addRotation(new Rotation(Face.RIGHT, Direction.CCW));
        myTree.addRotationLinkedList(myRotationLinkedList);

        myRotationLinkedList = new RotationLinkedList();
        myRotationLinkedList.addRotation(new Rotation(Face.LEFT, Direction.CCW));
        myTree.addRotationLinkedList(myRotationLinkedList);

        myRotationLinkedList = new RotationLinkedList();
        myRotationLinkedList.addRotation(new Rotation(Face.BOTTOM, Direction.CCW));
        myTree.addRotationLinkedList(myRotationLinkedList);

        Solver mySolver = new Solver();
        Solution mySolution = mySolver.solve(myRubik,myTree,myTree,myTree);
        mySolution.applyToRubik(myRubik);
        mySolution.print();
        Permutation.getPermutationFromCube(myRubik).print();
        AssistAssertRubik.checkEntireCube(myRubik);

    }

    @Ignore
    @Test
    public void complexSolver() {
        long beginningTime = System.nanoTime();
        Cube myRubik = new Cube();
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        myRubik.rotateFace(Face.BACK, Direction.CW);
        myRubik.rotateFace(Face.LEFT, Direction.CW);
        myRubik.rotateFace(Face.FRONT, Direction.CW);
        myRubik.rotateFace(Face.RIGHT, Direction.CW);
        Solver mySolver = new Solver();
        RotationTree firstFloorTree = new RotationTree();
        RotationTree secondFloorTree = new RotationTree();
        RotationTree thirdFloorTree = new RotationTree();
        RubikFileReader readFirstFloor = new RubikFileReader("FirstFloor.txt");
        RubikFileReader readSecondFloor = new RubikFileReader("SecondFloor.txt");
        RubikFileReader readThirdFloor = new RubikFileReader("ThirdFloor.txt");
        RotationTreeLoader.loadRotationTreeFromFile(readFirstFloor,firstFloorTree);
        RotationTreeLoader.loadRotationTreeFromFile(readSecondFloor, secondFloorTree);
        RotationTreeLoader.loadRotationTreeFromFile(readThirdFloor,thirdFloorTree);

        Solution mySolution = mySolver.solve(myRubik,firstFloorTree, secondFloorTree, thirdFloorTree);
        mySolution.applyToRubik(myRubik);
        mySolution.print();
        long endTime = System.nanoTime();
        System.out.format("Elapsed Time=%d seconds", ((endTime - beginningTime) / 1000000000));
//27-12-2017: started 11:39 PM, Failed
        Permutation.getPermutationFromCube(myRubik).print();
        AssistAssertRubik.checkEntireCube(myRubik);

    }


}