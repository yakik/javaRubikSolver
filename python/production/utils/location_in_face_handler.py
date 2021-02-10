class Location_in_face_handler:
   
    @staticmethod
    def GetLocationInFace( intValue):
        switcher={0: "LIF_TOP",
                  1:"LIF_BOTTOM",
                  2:"LIF_RIGHT",
                  3:"LIF_LEFT",
                  4:"LIF_TOPRIGHT",
                  5:"LIF_TOPLEFT",
                  6:"LIF_BOTTOMRIGHT",
                  7:"LIF_BOTTOMLEFT"}
        return switcher.get(intValue)

    @staticmethod
    def GetLocationInFaceInt(locationInFace):
        if locationInFace=="LIF_TOP":
            return 0
        if locationInFace=="LIF_BOTTOM":
            return 1
        if locationInFace=="LIF_RIGHT":
            return 2
        if locationInFace=="LIF_LEFT":
            return 3
        if locationInFace=="LIF_TOPRIGHT":
            return 4
        if locationInFace=="LIF_TOPLEFT":
            return 5
        if locationInFace=="LIF_BOTTOMRIGHT":
            return 6
        if locationInFace=="LIF_BOTTOMLEFT":
            return 7


