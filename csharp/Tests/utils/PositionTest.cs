using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CSharpRubikSolver;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using utils;

namespace CSharpRubikSolverUTests
{


    [TestClass]
    public class PositionTest
    {

        [TestMethod]
        public void getString()
        {
            Position myPosition = new Position(Face.TOP, Face.FRONT);
            Assert.AreEqual("U, F", myPosition.getString());
        }

        [TestMethod]
        public void rotateCW_U()
        {
            Position myPosition = new Position(Face.TOP, Face.FRONT);
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CW));
            Assert.AreEqual(Face.LEFT, myPosition.getFace(Face.TOP));
        }

        [TestMethod]
        public void rotateCW_D()
        {
            Position myPosition = new Position(Face.TOP, Face.FRONT);
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CW));
            Assert.AreEqual(Face.RIGHT, myPosition.getFace(Face.BOTTOM));
        }

        [TestMethod]
        public void rotateCCW()
        {
            Position myPosition = new Position(Face.TOP, Face.FRONT);
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CCW));
            Assert.AreEqual(Face.RIGHT, myPosition.getFace(Face.TOP));
        }

        [TestMethod]
        public void rotateCCW_D()
        {
            Position myPosition = new Position(Face.TOP, Face.FRONT);
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CCW));
            Assert.AreEqual(Face.LEFT, myPosition.getFace(Face.BOTTOM));
        }

        [TestMethod]
        public void moreRotationTests()
        {
            Position myPosition = new Position(Face.TOP, Face.FRONT);
            myPosition.rotate(new Rotation(Face.LEFT, Direction.CW));
            Assert.AreEqual(true, myPosition.equals(new Position(Face.BACK, Face.TOP)));
            myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CW));
            Assert.AreEqual(true, myPosition.equals(new Position(Face.BACK, Face.LEFT)));
            myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CCW));
            Assert.AreEqual(true, myPosition.equals(new Position(Face.BACK, Face.TOP)));
        }

        [TestMethod]
        public void rotateCCW_DD()
        {
            Position myPosition = new Position(Face.TOP, Face.FRONT);
            myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CCW));
            Assert.AreEqual(Face.BOTTOM, myPosition.getFace(Face.BOTTOM));
        }
        [TestMethod]
        public void getFace()
        {
        }

        [TestMethod]
        public void getHorizonalFacebyVirtual()
        {
        }

        [TestMethod]
        public void equals()
        {
        }

        [TestMethod]
        public void rotate1()
        {
        }
    }
}