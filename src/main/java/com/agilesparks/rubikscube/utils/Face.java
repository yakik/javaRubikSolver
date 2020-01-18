package com.agilesparks.rubikscube.utils;

public enum Face {
    TOP('U', 0), BOTTOM('D', 1), RIGHT('R', 2), LEFT('L', 3), FRONT('F', 4), BACK('B', 5)/*, NOTDEFINED('Z', 9)*/; //don't change this sequence, for Rubik's sake!

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
            case LEFT:
                return Face.RIGHT;
            case RIGHT:
                return Face.LEFT;
            case TOP:
                return Face.BOTTOM;
            case BOTTOM:
                return Face.TOP;
            case FRONT:
                return Face.BACK;
            case BACK:
                return Face.FRONT;
//            case NOTDEFINED:
//                return NOTDEFINED;
            default:
                return Face.TOP;
        }
    }
}

