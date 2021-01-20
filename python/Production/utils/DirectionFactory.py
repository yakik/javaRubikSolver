class DirectionFactory:
    
        @staticmethod
        def getDirectionByInt(intValue):
            switch (intValue):
            
                case 0:
                    return Direction.CW
                case 1:
                    return Direction.CCW
                default:
                    return Direction.CW
            
        
    

