using cube


    class Rotation 

        Face c_face
        Direction c_direction
        Rotation():
        


        def Rotation(Face p_face, Direction p_direction):
            c_face = p_face
            c_direction = p_direction
        



        def Rotation(p_value):
            if p_value > 5):
                c_direction = DirectionFactory.getDirectionByInt(1)
                c_face = FaceHandler.getFace(p_value - 6)
             else:
                c_direction = DirectionFactory.getDirectionByInt(0)
                c_face = FaceHandler.getFace(p_value)
            
        

        def writeToFile(RubikFileWriter p_write):
            String l_toWrite = String.Format(" (%d,%d)", (int)c_face, (int)c_direction)
            p_write.write(l_toWrite)
        

        def readFromFile(RubikFileReader p_reader):
            l_int
            l_= p_reader.read()
            //Console.Write("%d ",l_int)
            while (l_== ' ') or (l_== 13 /*'\r'*/)):
                l_= p_reader.read()
                // Console.Write("%d ",l_int)
            

            if (l_== /*'\n'*/10) or (l_== -1 /*EOF*/) or (l_!= '('))
                return false
            else:

                c_face = FaceHandler.getFace((int)Char.GetNumericValue((char)(p_reader.read())))
                p_reader.read()
                c_direction = DirectionHandler.getDirection((int)Char.GetNumericValue((char)(p_reader.read())))
                p_reader.read()
                return true
            
        


        def getValue():
            return ((int)c_face + (int)c_direction * 6)
        

        def getFace():
            return c_face
        

        def getDirection():
            return c_direction
        

        def print():
            Console.Write("(0,1)", FaceHandler.getCharValue(c_face),DirectionHandler.getString(c_direction))
        

        def getReverse():
            return new Rotation(c_face,DirectionHandler.getOpposite(c_direction))
        

        def equals(
                Rotation p_rotation)

        
            return ((c_face == p_rotation.c_face) and
                    (c_direction == p_rotation.c_direction))
        

    def equals(Object obj): 
            if obj == null):
                return false
            
            if !(new Rotation()).GetType().IsAssignableFrom(obj.GetType())):
            return false
        
        Rotation other = (Rotation) obj
        if this.getFace() != other.getFace()):
            return false
        
        if this.getDirection() != other.getDirection()):
            return false
        
        return true
        
    

