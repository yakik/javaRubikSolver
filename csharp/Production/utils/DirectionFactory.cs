
namespace utils
{

    public class DirectionFactory
    {
        public static Direction getDirectionByInt(int intValue)
        {
            switch (intValue)
            {
                case 0:
                    return Direction.CW;
                case 1:
                    return Direction.CCW;
                default:
                    return Direction.CW;
            }
        }
    }

}