



    class DirectionHandler:

        @staticmethod
        def getString(this Direction dir):              // Getter
            switch (dir)
            
                case Direction.CW:
                    return "CW"
                case Direction.CCW:
                    return "CCW"
                default:
                    return "ERROR"
            

        

        @staticmethod
        def getDirection(intValue):
            if intValue == 0)
                return Direction.CW
            else
                return Direction.CCW
        

        @staticmethod
        def getDirection(String intValue):
            if intValue == "0")
                return Direction.CW
            else
                return Direction.CCW
        
     

    @staticmethod
    def getOpposite(Direction direction):
        if direction == Direction.CW)
            return Direction.CCW
        else
            return Direction.CW
    


