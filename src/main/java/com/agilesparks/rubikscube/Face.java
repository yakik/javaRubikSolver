package com.agilesparks.rubikscube;

public enum Face {
    U('U', 0), D('D', 1), R('R', 2), L('L', 3), F('F', 4), B('B', 5)/*, NOTDEFINED('Z', 9)*/; //don't change this sequence, for Rubik's sake!

    private final char charValue;      // Private variable
    private final int intValue;

    Face(char charValue, int intValue) {     // Constructor
        this.charValue = charValue;
        this.intValue = intValue;
    }


    public int getIntOfChar() {              // Getter
        return charValue;
    }

    public char getChar(){ return (char) charValue;}

    public int getInt() {              // Getter
        return intValue;
    }

    public Face getOpposite() {
        switch (this) {
            case L:
                return Face.R;
            case R:
                return Face.L;
            case U:
                return Face.D;
            case D:
                return Face.U;
            case F:
                return Face.B;
            case B:
                return Face.F;
//            case NOTDEFINED:
//                return NOTDEFINED;
            default:
                return Face.U;
        }
    }
}

