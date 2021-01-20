
using utils



    [TestClass]
    class PositionTest
    

        [TestMethod]
        def getString():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            Assert.AreEqual("U, F", myPosition.getString())
        

        [TestMethod]
        def rotateCW_U():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CW))
            Assert.AreEqual(Face.LEFT, myPosition.getFace(Face.TOP))
        

        [TestMethod]
        def rotateCW_D():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CW))
            Assert.AreEqual(Face.RIGHT, myPosition.getFace(Face.BOTTOM))
        

        [TestMethod]
        def rotateCCW():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CCW))
            Assert.AreEqual(Face.RIGHT, myPosition.getFace(Face.TOP))
        

        [TestMethod]
        def rotateCCW_D():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CCW))
            Assert.AreEqual(Face.LEFT, myPosition.getFace(Face.BOTTOM))
        

        [TestMethod]
        def moreRotationTests():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.LEFT, Direction.CW))
            Assert.AreEqual(true, myPosition.equals(new Position(Face.BACK, Face.TOP)))
            myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CW))
            Assert.AreEqual(true, myPosition.equals(new Position(Face.BACK, Face.LEFT)))
            myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CCW))
            Assert.AreEqual(true, myPosition.equals(new Position(Face.BACK, Face.TOP)))
        

        [TestMethod]
        def rotateCCW_DD():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CCW))
            Assert.AreEqual(Face.BOTTOM, myPosition.getFace(Face.BOTTOM))
        
     