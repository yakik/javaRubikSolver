using cube
using solver

using utils



    [TestClass]
    class SolverTest 

        //@Ignore
        [TestMethod]
        complexSolver():
            //long beginningTime = System.nanoTime()
            Cube myRubik = new Cube()
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            myRubik.rotateFace(Face.BACK, Direction.CW)
            myRubik.rotateFace(Face.LEFT, Direction.CW)
            myRubik.rotateFace(Face.FRONT, Direction.CW)
            myRubik.rotateFace(Face.RIGHT, Direction.CW)
            Solver mySolver = new Solver()


            RubikFileReader readFirstFloor = new RubikFileReader("..\\..\\..\\Resources\\FirstFloor.txt")
            RubikFileReader readSecondFloor = new RubikFileReader("..\\..\\..\\Resources\\SecondFloor.txt")
            RubikFileReader readThirdFloor = new RubikFileReader("..\\..\\..\\Resources\\ThirdFloor.txt")

        
            RotationTree firstFloorTree = RotationTree.getRotationTreeFromFile(readFirstFloor)
            RotationTree secondFloorTree = RotationTree.getRotationTreeFromFile(readSecondFloor)
            RotationTree thirdFloorTree = RotationTree.getRotationTreeFromFile(readThirdFloor)
            //System.out.format("****************")
            Solution mySolution = mySolver.solve(myRubik, firstFloorTree, secondFloorTree, thirdFloorTree)
            //System.out.format("****************")
            mySolution.applyToRubik(myRubik)
            mySolution.print()
           // long endTime = System.n nanoTime()
            //Console.WriteLine("Elapsed Time=%d seconds", ((endTime - beginningTime) / 1000000000))
            //27-12-2017: started 11:39 PM, Failed
            //myRubik.print()
            Assert.IsTrue(myRubik.equals(new Cube()))

        


    
