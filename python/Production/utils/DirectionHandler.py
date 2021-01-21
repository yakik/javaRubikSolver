from production.utils.direction import Direction
class DirectionHandler:

    @staticmethod
    def getString(thisdir):              # Getter
        if thisdir == Direction.CW:
            return "CW"
        else:
                return "CCW"
            

    

    @staticmethod
    def getDirectionInt(intValue):
        if intValue == 0:
            return Direction.CW
        else:
            return Direction.CCW
    

    @staticmethod
    def getDirectionString(intValue):
        if intValue == "0":
            return Direction.CW
        else:
            return Direction.CCW
    
    

    @staticmethod
    def getOpposite(direction):
        if direction == Direction.CW:
            return Direction.CCW
        else:
            return Direction.CW



