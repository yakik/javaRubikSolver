from production.utils.color import Color
class ColorHandler:

    @staticmethod
    def getColorInt(intValue):     # Constructor
        switcher={0: Color.FRONTCOLOR,
            1: Color.BACKCOLOR,
            2: Color.RIGHTCOLOR,
            3: Color.LEFTCOLOR,
            4: Color.TOPCOLOR,
            5: Color.BOTTOMCOLOR}
        return switcher.get(intValue)

    @staticmethod
    def getColorChar(charValue):
        switcher={'R': Color.FRONTCOLOR,
            'B': Color.BACKCOLOR,
            'Y': Color.RIGHTCOLOR,
            'G': Color.LEFTCOLOR,
            'O': Color.TOPCOLOR,
            'W': Color.BOTTOMCOLOR}
        return switcher.get(charValue)
        

    






