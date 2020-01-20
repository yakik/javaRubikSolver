package com.agilesparks.rubikscube.solver;

import com.agilesparks.rubikscube.cube.Cube;
import com.agilesparks.rubikscube.cube.RubikFileReader;
import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Rotation;

public class Main {

    public static void main(String[] args) {
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
        myRubik.print();
    }
}

