from production.utils.direction import Direction
class DirectionFactory:
    
        @staticmethod
        def getDirectionByInt(intValue):
            if intValue==0:
                return Direction.CW
            else:
                return Direction.CCW