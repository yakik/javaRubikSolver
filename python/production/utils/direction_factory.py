from production.utils.direction import Direction
class Direction_factory:
    
        @staticmethod
        def getDirectionByInt(intValue):
            if intValue==0:
                return Direction.CW
            else:
                return Direction.CCW