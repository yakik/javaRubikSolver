class Face_handler:

    @staticmethod
    def getCharValue(face):
        if face=="TOP":
            return 'U'
        if face=="BOTTOM":
            return 'D'
        if face=="RIGHT":
            return 'R'
        if face=="LEFT":
            return 'L'
        if face=="FRONT":
            return 'F'
        if face=="BACK":
            return 'B'

       # switcher={"TOP": 'U',
       #         "BOTTOM": 'D',
       #         "RIGHT": 'R',
       #         "LEFT": 'L',
       #         "FRONT": 'F',
       #         "BACK": 'B'}
       # return switcher.get(face)

    @staticmethod
    def getFaceInt(intValue):
        switcher={0: "TOP",
                 1: "BOTTOM",
                 2: "RIGHT",
                 3: "LEFT",
                 4: "FRONT",
                 5: "BACK"}
        return switcher.get(intValue)

    @staticmethod
    def getIntFaceValue(intValue):
        if intValue=="TOP":
            return 0
        if intValue=="BOTTOM":
            return 1
        if intValue=="RIGHT":
            return 2
        if intValue=="LEFT":
            return 3
        if intValue=="FRONT":
            return 4
        if intValue=="BACK":
            return 5

    @staticmethod
    def getFaceChar(charValue):
        switcher = {'U': "TOP",
            'D': "BOTTOM",
            'R': "RIGHT",
            'L': "LEFT",
            'F': "FRONT",
            'B': "BACK"}
        return switcher.get(charValue)

    @staticmethod
    def getOpposite( face):
        switcher = {"LEFT": "RIGHT",
                    "RIGHT": "LEFT",
            "TOP": "BOTTOM",
            "BOTTOM": "TOP",
            "FRONT": "BACK",
            "BACK": "FRONT"}
        return switcher.get(face)