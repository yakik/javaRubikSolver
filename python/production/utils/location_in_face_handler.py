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
        switcher={"LIF_TOP":0,
               "LIF_BOTTOM":1,
                "LIF_RIGHT":2,
                "LIF_LEFT":3,
                "LIF_TOPRIGHT":4,
                "LIF_TOPLEFT":5,
                "LIF_BOTTOMRIGHT":6,
                "LIF_BOTTOMLEFT":7}
        return switcher.get(locationInFace)

