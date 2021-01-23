from production.utils.face import Face
from production.utils.direction import Direction
from production.utils.face_handler import Face_handler
from production.utils.direction_handler import Direction_handler
class Rotation :
        def __init__(self,p_face=None,p_direction=None):
            self.c_face = p_face
            self.c_direction = p_direction

       # def Rotation(self, p_value):
       #     if p_value > 5:
       #         self.c_direction = Direction_factory.getDirectionByInt(1)
       #         self.c_face = Face_handler.getFace(p_value - 6)
       #     else:
       #         self.c_direction = Direction_factory.getDirectionByInt(0)
       #         self.c_face = Face_handler.getFace(p_value)

        def write_to_file(self, p_write):
            l_toWrite = "("+ self.c_face + "," + self.c_direction+")"
            p_write.write(l_toWrite)
        

        def readFromFile(self, p_reader):
            l_int=0
            l_int= p_reader.read()
            #Console.Write("%d ",l_int)
            while (l_int== ' ') or (l_int== 13):
                l_int= p_reader.read()
                # Console.Write("%d ",l_int)
            

            if ((l_int== 10) or (l_int== -1 ) or (l_int!= '(')):
                return False
            else:
                self.c_face = Face_handler.getFaceInt(int(p_reader.read()))
                p_reader.read()
                self.c_direction = Direction_handler.getDirectionInt(int(p_reader.read()))
                p_reader.read()
                return True

        def getValue(self):
            return (self.c_face + self.c_direction * 6)

        def getFace(self):
            return self.c_face

        def getDirection(self):
            return self.c_direction

        def print(self):
            print("(" + Face_handler.getCharValue(self.c_face) + "," + Direction_handler.getString(self.c_direction) + "\n")

        def getReverse(self):
            return Rotation(self.c_face, Direction_handler.getOpposite(self.c_direction))

        def equals(self, p_rotation):
            return ((self.c_face == p_rotation.getFace()) and
                    (self.c_direction == p_rotation.getDirection()))
        

       
        
    

