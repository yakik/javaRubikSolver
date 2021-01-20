from enum import Enum

class LocationInFace(Enum):
        TOP=0
        BOTTOM=1
        RIGHT=2
        LEFT=3
        TOPRIGHT=4
        TOPLEFT=5
        BOTTOMRIGHT=6
        BOTTOMLEFT=7#, NOTDEFINED('Z', 9)*/ #don't change this sequence, for Rubik's sake!
    
class LocationInFaceHandle:
   
    @staticmethod
    def GetLocationInFace( intValue):
        switcher={0: LocationInFace.TOP,
               1:LocationInFace.BOTTOM,
                2:LocationInFace.RIGHT,
                3:LocationInFace.LEFT,
                4:LocationInFace.TOPRIGHT,
                5:LocationInFace.TOPLEFT,
                6:LocationInFace.BOTTOMRIGHT,
                7:LocationInFace.BOTTOMLEFT}
        return switcher.get(intValue)

            
           
    


   



