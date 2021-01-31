using cube;
using solver;
using System;
using utils;

namespace Production
{
    class Program
    {
        static void Main(string[] args)
        {

            //long beginningTime = System.nanoTime();
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


            RubikFileReader readFirstFloor = new RubikFileReader("..\\..\\..\\Resources\\FirstFloor.txt");
            RubikFileReader readSecondFloor = new RubikFileReader("..\\..\\..\\Resources\\SecondFloor.txt");
            RubikFileReader readThirdFloor = new RubikFileReader("..\\..\\..\\Resources\\ThirdFloor.txt");


            RotationTree firstFloorTree = RotationTree.getRotationTreeFromFile(readFirstFloor);
            RotationTree secondFloorTree = RotationTree.getRotationTreeFromFile(readSecondFloor);
            RotationTree thirdFloorTree = RotationTree.getRotationTreeFromFile(readThirdFloor);
            
            Solution mySolution = mySolver.solve(myRubik, firstFloorTree, secondFloorTree, thirdFloorTree);
          
            mySolution.applyToRubik(myRubik);
            mySolution.print();
 
            if (myRubik.equals(new Cube()))
                Console.WriteLine("Solved!");
            else
                Console.WriteLine("Not Solved :-(");
            Console.ReadLine();
        }
    }
}
