class Direction_factory:
    
        @staticmethod
        def getDirectionByInt(intValue):
            if intValue==0:
                return "CW"
            else:
                return "CCW"