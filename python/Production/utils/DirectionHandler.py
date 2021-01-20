using System

namespace utils
{
    static class DirectionHandler{

        static String getString(this Direction dir):              // Getter
            switch (dir)
            {
                case Direction.CW:
                    return "CW"
                case Direction.CCW:
                    return "CCW"
                default:
                    return "ERROR"
            }

        }

        static Direction getDirection(intValue):
            if intValue == 0)
                return Direction.CW
            else
                return Direction.CCW
        }

        static Direction getDirection(String intValue):
            if intValue == "0")
                return Direction.CW
            else
                return Direction.CCW
        }
     

    static Direction getOpposite(Direction direction):
        if direction == Direction.CW)
            return Direction.CCW
        else
            return Direction.CW
    }
}
}
