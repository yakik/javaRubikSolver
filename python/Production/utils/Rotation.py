class Rotation :


        def Rotation(self,p_face,p_direction):
            self.c_face = p_face
            self.c_direction = p_direction
        



        def Rotation(self, p_value):
            if p_value > 5):
                self.c_direction = DirectionFactory.getDirectionByInt(1)
                self.c_face = FaceHandler.getFace(p_value - 6)
             else:
                self.c_direction = DirectionFactory.getDirectionByInt(0)
                self.c_face = FaceHandler.getFace(p_value)
            
        

        def writeToFile(self, RubikFileWriter p_write):
           l_toWrite = String.Format(" (%d,%d)", (int)self.c_face, (int)self.c_direction)
            p_write.write(l_toWrite)
        

        def readFromFile(self, RubikFileReader p_reader):
            l_int
            l_= p_reader.read()
            #Console.Write("%d ",l_int)
            while (l_== ' ') or (l_== 13 /*'\r'*/)):
                l_= p_reader.read()
                # Console.Write("%d ",l_int)
            

            if (l_== /*'\n'*/10) or (l_== -1 /*EOF*/) or (l_!= '('))
                return False
            else:

                self.c_face = FaceHandler.getFace((int)Char.GetNumericValue((char)(p_reader.read())))
                p_reader.read()
                self.c_direction = DirectionHandler.getDirection((int)Char.GetNumericValue((char)(p_reader.read())))
                p_reader.read()
                return True
            
        


        def getValue(self):
            return ((int)self.c_face + (int)self.c_direction * 6)
        

        def getFace(self):
            return self.c_face
        

        def getDirection(self):
            return self.c_direction
        

        def print(self):
            Console.Write("(0,1)", FaceHandler.getCharValue(self.c_face),DirectionHandler.getString(self.c_direction))
        

        def getReverse(self):
            return Rotation(self.c_face,DirectionHandler.getOpposite(self.c_direction))
        

        def equals(self, Rotation p_rotation)

        
            return ((self.c_face == p_rotation.self.c_face) and
                    (self.c_direction == p_rotation.self.c_direction))
        

    def equals(self, Object obj): 
            if obj == null):
                return False
            
            if !(Rotation()).GetType().IsAssignableFrom(obj.GetType())):
            return False
        
        Rotation other = (Rotation) obj
        if this.getFace() != other.getFace()):
            return False
        
        if this.getDirection() != other.getDirection()):
            return False
        
        return True
        
    

