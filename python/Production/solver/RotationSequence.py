class RotationSequence:

        List<Rotation> c_array = new List<Rotation>()

        def __init__(self):
            c_array.Clear()
        


        def __init__(self, List<Rotation> p_List):
            c_array = p_List

        

        def print(self):
         

            foreach (var l_itr in c_array)

                (l_itr as Rotation).print()
            Console.Write("\n")
        

        def addRotation(self, Rotation p_rotation):
            c_array.Add(p_rotation)
        

        def removeRotation(self):
            c_array.RemoveAt(c_array.Count - 1)
        

        def Boolean isRedundant(self, Rotation p_rotation):
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
                
             else
                l_returnValue = false
            return l_returnValue

        

       def writeToFile(self, RubikFileWriter p_writer):
            foreach (var l_itr in c_array)

                (l_itr as Rotation).writeToFile(p_writer)

            p_writer.write("\n")


        
        def readFromFile(self, RubikFileReader p_reader):
            Rotation l_rotation = new Rotation()

            c_array.Clear()
            while l_rotation.readFromFile(p_reader))
                c_array.Add((new Rotation(l_rotation.getFace(), l_rotation.getDirection())))
            return !(c_array.Count == 0)
        

       
        def getSubRotationLinkedList(self):
            return new RotationSequence(new List<Rotation>(c_array.GetRange(1, c_array.Count)))
        

       def size(self):
            return c_array.Count
        

        def  getFirstRotation(self):
            return c_array[0]
        
        def  getRotation(p_index):
            return c_array[p_index]
        
        def isNotEmpty(self):

            return (c_array.Count > 0)
        

        def getCopy(self):
            RotationSequence l_rotationLinkedList = new RotationSequence()
           

        
            foreach (var l_itr in c_array)

                l_rotationLinkedList.addRotation(l_itr as Rotation)

            return l_rotationLinkedList
        

        def applyToRubik(self, Cube p_rubik):
           

              
            
            foreach (var l_itr in c_array)

                p_rubik.rotateFace(l_itr.getFace(), l_itr.getDirection())


        
    


