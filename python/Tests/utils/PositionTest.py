using System
using System.Collections.Generic
using System.Linq
using System.Text
using System.Threading.Tasks
using CSharpRubikSolver
using Microsoft.VisualStudio.TestTools.UnitTesting
using utils

namespace CSharpRubikSolverUTests
{


    [TestClass]
    class PositionTest
    {

        [TestMethod]
        getString():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            Assert.AreEqual("U, F", myPosition.getString())
        }

        [TestMethod]
        rotateCW_U():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CW))
            Assert.AreEqual(Face.LEFT, myPosition.getFace(Face.TOP))
        }

        [TestMethod]
        rotateCW_D():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CW))
            Assert.AreEqual(Face.RIGHT, myPosition.getFace(Face.BOTTOM))
        }

        [TestMethod]
        rotateCCW():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CCW))
            Assert.AreEqual(Face.RIGHT, myPosition.getFace(Face.TOP))
        }

        [TestMethod]
        rotateCCW_D():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.FRONT, Direction.CCW))
            Assert.AreEqual(Face.LEFT, myPosition.getFace(Face.BOTTOM))
        }

        [TestMethod]
        moreRotationTests():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.LEFT, Direction.CW))
            Assert.AreEqual(true, myPosition.equals(new Position(Face.BACK, Face.TOP)))
            myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CW))
            Assert.AreEqual(true, myPosition.equals(new Position(Face.BACK, Face.LEFT)))
            myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CCW))
            Assert.AreEqual(true, myPosition.equals(new Position(Face.BACK, Face.TOP)))
        }

        [TestMethod]
        rotateCCW_DD():
            Position myPosition = new Position(Face.TOP, Face.FRONT)
            myPosition.rotate(new Rotation(Face.BOTTOM, Direction.CCW))
            Assert.AreEqual(Face.BOTTOM, myPosition.getFace(Face.BOTTOM))
        }
        [TestMethod]
        getFace():
        }

        [TestMethod]
        getHorizonalFacebyVirtual():
        }

        [TestMethod]
        equals():
        }

        [TestMethod]
        rotate1():
        }
    }
}