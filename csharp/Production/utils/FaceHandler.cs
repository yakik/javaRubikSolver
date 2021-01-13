namespace utils
{
    public class FaceHandler { 

    static public int getCharValue(Face face)
        {
            switch (face)
            {
                case Face.TOP:
                    return 'U';
                case Face.BOTTOM:
                    return 'D';
                case Face.RIGHT:
                    return 'R';
                case Face.LEFT:
                    return 'L';
                case Face.FRONT:
                    return 'F';
                case Face.BACK:
                    return 'B';
                default:
                    return 'U';
            }

        }

    static public Face getFace(int intValue) {
            switch (intValue)
            {
                case 0:
                    return Face.TOP;
                case 1:
                    return Face.BOTTOM;
                case 2:
                    return Face.RIGHT;
                case 3:
                    return Face.LEFT;
                case 4:
                    return Face.FRONT;
                case 5:
                    return Face.BACK;
                default:
                    return Face.TOP;
            }
          
    }

        static public Face getFace(char charValue)
        {
            switch (charValue)
            {
                case 'U':
                    return Face.TOP;
                case 'D':
                    return Face.BOTTOM;
                case 'R':
                    return Face.RIGHT;
                case 'L':
                    return Face.LEFT;
                case 'F':
                    return Face.FRONT;
                case 'B':
                    return Face.BACK;
                default:
                    return Face.TOP;
            }

        }

     /*   public int getIntOfChar() {              // Getter
        return charValue;
    }

    public char getChar(){ return (char) charValue;}
     */
   /* public int getInt() {              // Getter
        return intValue;
    }
*/
    static public Face getOpposite(Face face) {
        switch (face) {
            case Face.LEFT:
                    return Face.RIGHT;
            case Face.RIGHT:
                return Face.LEFT;
            case Face.TOP:
                return Face.BOTTOM;
            case Face.BOTTOM:
                return Face.TOP;
            case Face.FRONT:
                return Face.BACK;
            case Face.BACK:
                return Face.FRONT;
//            case NOTDEFINED:
//                return NOTDEFINED;
            default:
                return Face.TOP;
        }
    }
}
}

