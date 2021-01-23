from production.utils.location_in_face import Location_in_face


class Location_in_face_handler:
   
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

    #@staticmethod
    #def GetLocationInFaceInt(locationInFace):
    #    switcher={Location_in_face.TOP:0,
    #           Location_in_face.BOTTOM:1,
    #            Location_in_face.RIGHT:2,
    #            Location_in_face.LEFT:3,
    #            Location_in_face.TOPRIGHT:4,
    #            Location_in_face.TOPLEFT:5,
    #            Location_in_face.BOTTOMRIGHT:6,
    #            Location_in_face.BOTTOMLEFT:7}
    #    return switcher.get(locationInFace)

