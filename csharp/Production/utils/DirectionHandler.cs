using System;

namespace utils
{
    public static class DirectionHandler{

        public static String getString(this Direction dir)
        {              // Getter
            switch (dir)
            {
                case Direction.CW:
                    return "CW";
                case Direction.CCW:
                    return "CCW";
                default:
                    return "ERROR";
            }

        }

        static public Direction getDirection(int intValue)
        {
            if (intValue == 0)
                return Direction.CW;
            else
                return Direction.CCW;
        }

        static public Direction getDirection(String intValue)
        {
            if (intValue == "0")
                return Direction.CW;
            else
                return Direction.CCW;
        }
     

    static public Direction getOpposite(Direction direction) {
        if (direction == Direction.CW)
            return Direction.CCW;
        else
            return Direction.CW;
    }
}
}
