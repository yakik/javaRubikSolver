using cube

using solver
using utils


    [TestClass]
    class RotationLinkedListTest
    

        [TestMethod]
        isRedundantCW():
            RotationSequence myList = new RotationSequence()
            myList.addRotation(new Rotation(Face.FRONT, Direction.CW))
            Assert.AreEqual(true, myList.isRedundant(new Rotation(Face.FRONT, Direction.CW)))
        

        [TestMethod]
        isRedundantCCW():
            RotationSequence myList = new RotationSequence()
            myList.addRotation(new Rotation(Face.FRONT, Direction.CCW))
            myList.addRotation(new Rotation(Face.FRONT, Direction.CCW))
            Assert.AreEqual(true, myList.isRedundant(new Rotation(Face.FRONT, Direction.CCW)))
        
    
