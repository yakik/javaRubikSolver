class RotationSequence:

        List<Rotation> self.c_array = List<Rotation>()

        def __init__(self):
            self.c_array.Clear()
        


        def __init__(self, List<Rotation> p_List):
            self.c_array = p_List

        

        def print(self):
         

            foreach (var l_itr in self.c_array)

                (l_itr as Rotation).print()
            Console.Write("\n")
        

        def addRotation(self, Rotation p_rotation):
            self.c_array.Add(p_rotation)
        

        def removeRotation(self):
            self.c_array.RemoveAt(self.c_array.Count - 1)
        

        def Boolean isRedundant(self, Rotation p_rotation):
            Boolean l_returnValue = False

           l_lastFace
           l_lastDirection
            if self.c_array.Count > 0):
                l_lastFace = self.c_array[(self.c_array.Count - 1)].getFace()
                l_lastDirection = self.c_array[self.c_array.Count - 1].getDirection()
                # rotation is opposite to previous
                if self.c_array[self.c_array.Count - 1].getReverse().equals(p_rotation))
                    l_returnValue = True
                # previouswas opposite and previousgreater then current face
                if (p_rotation.getFace() == FaceHandler.getOpposite(l_lastFace) and ((int)l_lastFace > (int)p_rotation.getFace())))
                    l_returnValue = True
                # two clockwise rotation of same face
                if (p_rotation.getFace() == l_lastFace) and (l_lastDirection == Direction.CW) and
                        (p_rotation.getDirection() == Direction.CW))
                    l_returnValue = True
                #no three counter clockwise rotations
                if self.c_array.Count > 1):
                    if (p_rotation.getFace() == l_lastFace) and (l_lastDirection == Direction.CCW) and
                            (p_rotation.getDirection() == Direction.CCW) and
                            (self.c_array[self.c_array.Count - 2].getFace() == l_lastFace) and (l_lastDirection == Direction.CCW) and
                            (self.c_array[self.c_array.Count - 2].getDirection() == Direction.CCW))
                        l_returnValue = True
                
             else
                l_returnValue = False
            return l_returnValue

        

       def writeToFile(self, RubikFileWriter p_writer):
            foreach (var l_itr in self.c_array)

                (l_itr as Rotation).writeToFile(p_writer)

            p_writer.write("\n")


        
        def readFromFile(self, RubikFileReader p_reader):
            Rotation l_rotation = Rotation()

            self.c_array.Clear()
            while l_rotation.readFromFile(p_reader))
                self.c_array.Add((Rotation(l_rotation.getFace(), l_rotation.getDirection())))
            return !(self.c_array.Count == 0)
        

       
        def getSubRotationLinkedList(self):
            return RotationSequence(List<Rotation>(self.c_array.GetRange(1, self.c_array.Count)))
        

       def size(self):
            return self.c_array.Count
        

        def  getFirstRotation(self):
            return self.c_array[0]
        
        def  getRotation(p_index):
            return self.c_array[p_index]
        
        def isNotEmpty(self):

            return (self.c_array.Count > 0)
        

        def getCopy(self):
           l_rotationLinkedList = RotationSequence()
           

        
            foreach (var l_itr in self.c_array)

                l_rotationLinkedList.addRotation(l_itr as Rotation)

            return l_rotationLinkedList
        

        def applyToRubik(self,p_rubik):
           

              
            
            foreach (var l_itr in self.c_array)

                p_rubik.rotateFace(l_itr.getFace(), l_itr.getDirection())


        
    


