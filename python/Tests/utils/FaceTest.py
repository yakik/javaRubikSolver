
using utils




    [TestClass]
    class FaceTest
    
        [TestMethod]
        def testFaceGetIntGetChar():
            Face myFace = Face.BOTTOM
            Assert.AreEqual(1,(int) myFace)
            Assert.AreEqual('D', FaceHandler.getCharValue(myFace))
            myFace = Face.FRONT
            Assert.AreEqual(4, (int)myFace)
            Assert.AreEqual('F', FaceHandler.getCharValue(myFace))
            myFace = Face.RIGHT
            Assert.AreEqual(2, (int)myFace)
            Assert.AreEqual('R', FaceHandler.getCharValue(myFace))
            myFace = Face.TOP
            Assert.AreEqual(0, (int)myFace)
            Assert.AreEqual('U', FaceHandler.getCharValue(myFace))
            myFace = Face.BACK
            Assert.AreEqual(5, (int)myFace)
            Assert.AreEqual('B', FaceHandler.getCharValue(myFace))
            myFace = Face.LEFT
            Assert.AreEqual(3, (int)myFace)
            Assert.AreEqual('L', FaceHandler.getCharValue(myFace))
        

        [TestMethod]
        def testFaceEquals():
            Face myFace = Face.BOTTOM
            Assert.AreEqual(Face.BOTTOM, myFace)
            Assert.AreEqual(true, myFace == Face.BOTTOM)
        

        [TestMethod]
        def testFaceGetOpposite():
            Face myFace = Face.BOTTOM
            Assert.AreEqual(Face.TOP, FaceHandler.getOpposite(myFace))
            myFace = Face.FRONT
            Assert.AreEqual(Face.BACK, FaceHandler.getOpposite(myFace))
            myFace = Face.RIGHT
            Assert.AreEqual(Face.LEFT, FaceHandler.getOpposite(myFace))
            myFace = Face.TOP
            Assert.AreEqual(Face.BOTTOM, FaceHandler.getOpposite(myFace))
            myFace = Face.BACK
            Assert.AreEqual(Face.FRONT, FaceHandler.getOpposite(myFace))
            myFace = Face.LEFT
            Assert.AreEqual(Face.RIGHT, FaceHandler.getOpposite(myFace))
        

    
