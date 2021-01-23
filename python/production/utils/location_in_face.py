from enum import IntEnum

class Location_in_face(IntEnum):
        TOP=0
        BOTTOM=1
        RIGHT=2
        LEFT=3
        TOPRIGHT=4
        TOPLEFT=5
        BOTTOMRIGHT=6
        BOTTOMLEFT=7#, NOTDEFINED('Z', 9)*/ #don't change this sequence, for Rubik's sake!
    
class LocationInFaceHandler:
   
    @staticmethod
    def GetLocationInFace( intValue):
        switcher={0: Location_in_face.TOP,
                  1:Location_in_face.BOTTOM,
                  2:Location_in_face.RIGHT,
                  3:Location_in_face.LEFT,
                  4:Location_in_face.TOPRIGHT,
                  5:Location_in_face.TOPLEFT,
                  6:Location_in_face.BOTTOMRIGHT,
                  7:Location_in_face.BOTTOMLEFT}
        return switcher.get(intValue)

       

            
           
    


   



