using System
using System.Collections.Generic
using System.Linq
using System.Text
using System.Threading.Tasks
using CSharpRubikSolver
using Microsoft.VisualStudio.TestTools.UnitTesting
using utils

namespace CSharpRubikSolverUTests



    [TestClass]
    class LocationTest
    

        [TestMethod]
        isEdge():
            Location myLocation = new Location(Face.BOTTOM, Face.LEFT, Face.FRONT)
            Assert.AreEqual(false, myLocation.isEdge())
            myLocation = new Location(Face.BOTTOM, Face.LEFT)
            Assert.AreEqual(true, myLocation.isEdge())
        

        [TestMethod]
        getFaces():
            Location myLocation = new Location(Face.BOTTOM, Face.LEFT, Face.FRONT)
            //taking into account facecs are sorted according to value
            Assert.AreEqual(Face.BOTTOM, myLocation.getFace0())
            Assert.AreEqual(Face.LEFT, myLocation.getFace1())
            Assert.AreEqual(Face.FRONT, myLocation.getFace2())
        

        [TestMethod]
        equals():
            Location myLocation = new Location(Face.BOTTOM, Face.LEFT, Face.FRONT)
            Location mySecondLocation = new Location(Face.LEFT, Face.FRONT, Face.BOTTOM)
            Location myThirdLocation = new Location(Face.RIGHT, Face.FRONT, Face.BOTTOM)
            Assert.AreEqual(true, mySecondLocation.equals(myLocation))
            Assert.AreEqual(false, mySecondLocation.equals(myThirdLocation))
        

        [TestMethod]
        testGetFloor():
            Assert.AreEqual(3, new Location(Face.TOP, Face.LEFT, Face.FRONT).getFloor(), "1")
            Assert.AreEqual(3, new Location(Face.TOP, Face.LEFT, Face.BACK).getFloor(), "2")
            Assert.AreEqual(3, new Location(Face.TOP, Face.RIGHT, Face.FRONT).getFloor(), "3")
            Assert.AreEqual(3, new Location(Face.TOP, Face.RIGHT, Face.BACK).getFloor(), "4")
            Assert.AreEqual(1, new Location(Face.BOTTOM, Face.LEFT, Face.FRONT).getFloor(), "5")
            Assert.AreEqual(1, new Location(Face.BOTTOM, Face.LEFT, Face.BACK).getFloor(), "6")
            Assert.AreEqual(1, new Location(Face.BOTTOM, Face.RIGHT, Face.FRONT).getFloor(), "7")
            Assert.AreEqual(1, new Location(Face.BOTTOM, Face.RIGHT, Face.BACK).getFloor(), "8")

            Assert.AreEqual(3, new Location(Face.TOP, Face.FRONT).getFloor(), "10")
            Assert.AreEqual(3, new Location(Face.TOP, Face.BACK).getFloor(), "11")
            Assert.AreEqual(3, new Location(Face.TOP, Face.LEFT).getFloor(), "12")
            Assert.AreEqual(3, new Location(Face.TOP, Face.RIGHT).getFloor(), "13")

            Assert.AreEqual(2, new Location(Face.FRONT, Face.LEFT).getFloor(), "14")
            Assert.AreEqual(2, new Location(Face.FRONT, Face.RIGHT).getFloor(), "15")
            Assert.AreEqual(2, new Location(Face.BACK, Face.LEFT).getFloor(), "16")
            Assert.AreEqual(2, new Location(Face.BACK, Face.RIGHT).getFloor(), "17")

            Assert.AreEqual(1, new Location(Face.BOTTOM, Face.LEFT).getFloor(), "18")
            Assert.AreEqual(1, new Location(Face.BOTTOM, Face.RIGHT).getFloor(), "19")
            Assert.AreEqual(1, new Location(Face.FRONT, Face.BOTTOM).getFloor(), "20")
            Assert.AreEqual(1, new Location(Face.BACK, Face.BOTTOM).getFloor(), "21")


        

        [TestMethod]
        getString():
            Location myLocation = new Location(Face.BOTTOM, Face.LEFT, Face.FRONT)
            Assert.AreEqual("D, L, F", myLocation.getString(),"first")
            myLocation = new Location(Face.BOTTOM, Face.LEFT)
            Assert.AreEqual("D, L", myLocation.getString(),"second")

        
    
