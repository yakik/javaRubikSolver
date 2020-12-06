package com.agilesparks.rubikscube.solver;


import static org.junit.Assert.*;

import org.junit.*;

import com.agilesparks.rubikscube.cube.Cube;
import com.agilesparks.rubikscube.cube.RubikFileReader;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;

public class SolverTest {
    
    //@Ignore
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
        
        RubikFileReader readFirstFloor = new RubikFileReader("FirstFloor.txt");
        RubikFileReader readSecondFloor = new RubikFileReader("SecondFloor.txt");
        RubikFileReader readThirdFloor = new RubikFileReader("ThirdFloor.txt");
        RotationTree firstFloorTree = RotationTree.getRotationTreeFromFile(readFirstFloor);
        RotationTree secondFloorTree = RotationTree.getRotationTreeFromFile(readSecondFloor);
        RotationTree thirdFloorTree = RotationTree.getRotationTreeFromFile(readThirdFloor);
        //System.out.format("****************");
        Solution mySolution = mySolver.solve(myRubik,firstFloorTree, secondFloorTree, thirdFloorTree);
        //System.out.format("****************");
        mySolution.applyToRubik(myRubik);
        //mySolution.print();
        long endTime = System.nanoTime();
        System.out.format("Elapsed Time=%d seconds", ((endTime - beginningTime) / 1000000000));
//27-12-2017: started 11:39 PM, Failed
        //myRubik.print();
        assertTrue(myRubik.equals(new Cube()));

    }


}