class Direction_handler:

    @staticmethod
    def getString(thisdir):              # Getter
        if thisdir == "CW":
            return "CW"
        else:
                return "CCW"

    @staticmethod
    def getDirectionInt(intValue):
        if intValue == 0:
            return "CW"
        else:
            return "CCW"

    @staticmethod
    def getDirectionString(intValue):
        if intValue == "0":
            return "CW"
        else:
            return "CCW"

    @staticmethod
    def getOpposite(direction):
        if direction == "CW":
            return "CCW"
        else:
            return "CW"



