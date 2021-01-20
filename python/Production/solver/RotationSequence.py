using CSharpRubikSolver
using System
using System.Collections
using System.Collections.Generic
using System.Linq
using System.Text
using System.Threading.Tasks
using utils
using cube

namespace solver
{

    class RotationSequence {

        List<Rotation> c_array = new List<Rotation>()

        RotationSequence():
            c_array.Clear()
        }


        RotationSequence(List<Rotation> p_List):
            c_array = p_List

        }

        print():
         

            foreach (var l_itr in c_array)

                (l_itr as Rotation).print()
            Console.Write("\n")
        }

        addRotation(Rotation p_rotation):
            c_array.Add(p_rotation)
        }

        removeRotation():
            c_array.RemoveAt(c_array.Count - 1)
        }

        Boolean isRedundant(Rotation p_rotation):
            Boolean l_returnValue = false

            Face l_lastFace
            Direction l_lastDirection
            if c_array.Count > 0):
                l_lastFace = c_array[(c_array.Count - 1)].getFace()
                l_lastDirection = c_array[c_array.Count - 1].getDirection()
                // new rotation is opposite to previous
                if c_array[c_array.Count - 1].getReverse().equals(p_rotation))
                    l_returnValue = true
                // previous face was opposite and previous face greater then current face
                if (p_rotation.getFace() == FaceHandler.getOpposite(l_lastFace) and ((int)l_lastFace > (int)p_rotation.getFace())))
                    l_returnValue = true
                // two clockwise rotation of same face
                if (p_rotation.getFace() == l_lastFace) and (l_lastDirection == Direction.CW) and
                        (p_rotation.getDirection() == Direction.CW))
                    l_returnValue = true
                //no three counter clockwise rotations
                if c_array.Count > 1):
                    if (p_rotation.getFace() == l_lastFace) and (l_lastDirection == Direction.CCW) and
                            (p_rotation.getDirection() == Direction.CCW) and
                            (c_array[c_array.Count - 2].getFace() == l_lastFace) and (l_lastDirection == Direction.CCW) and
                            (c_array[c_array.Count - 2].getDirection() == Direction.CCW))
                        l_returnValue = true
                }
            } else
                l_returnValue = false
            return l_returnValue

        }

        writeToFile(RubikFileWriter p_writer):
            foreach (var l_itr in c_array)

                (l_itr as Rotation).writeToFile(p_writer)

            p_writer.write("\n")


        }
        bool readFromFile(RubikFileReader p_reader):
            Rotation l_rotation = new Rotation()

            c_array.Clear()
            while l_rotation.readFromFile(p_reader))
                c_array.Add((new Rotation(l_rotation.getFace(), l_rotation.getDirection())))
            return !(c_array.Count == 0)
        }

       
        RotationSequence getSubRotationLinkedList():
            return new RotationSequence(new List<Rotation>(c_array.GetRange(1, c_array.Count)))
        }

       size():
            return c_array.Count
        }

        Rotation getFirstRotation():
            return c_array[0]
        }
        Rotation getRotation(p_index):
            return c_array[p_index]
        }
        Boolean isNotEmpty():

            return (c_array.Count > 0)
        }

        RotationSequence getCopy():
            RotationSequence l_rotationLinkedList = new RotationSequence()
           

        
            foreach (var l_itr in c_array)

                l_rotationLinkedList.addRotation(l_itr as Rotation)

            return l_rotationLinkedList
        }

        applyToRubik(Cube p_rubik):
           

              
            
            foreach (var l_itr in c_array)

                p_rubik.rotateFace(l_itr.getFace(), l_itr.getDirection())


        }
    }
}

