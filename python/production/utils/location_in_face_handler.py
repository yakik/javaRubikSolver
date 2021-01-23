from production.utils.location_in_face import LocationInFace


class LocationInFaceHandler:
   
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

    #@staticmethod
    #def GetLocationInFaceInt(locationInFace):
    #    switcher={LocationInFace.TOP:0,
    #           LocationInFace.BOTTOM:1,
    #            LocationInFace.RIGHT:2,
    #            LocationInFace.LEFT:3,
    #            LocationInFace.TOPRIGHT:4,
    #            LocationInFace.TOPLEFT:5,
    #            LocationInFace.BOTTOMRIGHT:6,
    #            LocationInFace.BOTTOMLEFT:7}
    #    return switcher.get(locationInFace)

