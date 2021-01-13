using cube;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using utils;

namespace CSharpRubikSolverUTests
{

    [TestClass]
    public class PermutationTest
    {

        [TestMethod]
        public void getValue()
        {
            Cube myRubik = new Cube();
            myRubik.rotateFace(Face.FRONT, Direction.CW);
            Cube myPermutation = new Cube(myRubik);
            Assert.AreEqual( 10, Cube.getValue(myPermutation, 1), "first floor");
            Assert.AreEqual( 14, Cube.getValue(myPermutation, 2), "second floor");
            Assert.AreEqual(24, Cube.getValue(myPermutation, 3), "third floor");

        }
        [TestMethod]
        public void getValueFull()
        {
            Cube myRubik = new Cube();
            Cube myPermutation = new Cube(myRubik);
            Assert.AreEqual( 40, Cube.getValue(myPermutation, 3));

        }



    }
}