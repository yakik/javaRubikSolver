class Color_handler:

    @staticmethod
    def getColorInt(intValue):     # Constructor
        switcher={0: "FRONTCOLOR",
            1: "BACKCOLOR",
            2: "RIGHTCOLOR",
            3: "LEFTCOLOR",
            4: "TOPCOLOR",
            5: "BOTTOMCOLOR"}
        return switcher.get(intValue)

    @staticmethod
    def getColorChar(charValue):
        switcher={'R': "FRONTCOLOR",
            'B': "BACKCOLOR",
            'Y': "RIGHTCOLOR",
            'G': "LEFTCOLOR",
            'O': "TOPCOLOR",
            'W': "BOTTOMCOLOR"}
        return switcher.get(charValue)
        

    






