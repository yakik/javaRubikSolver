package com.agilesparks.rubikscube.utils;

public enum LocationInFace {
    TOP('T', 0), BOTTOM('B', 1), RIGHT('R', 2), LEFT('L', 3), TOPRIGHT('E', 4), TOPLEFT('F', 5), BOTTOMRIGHT('G', 6), BOTTOMLEFT('H', 7)/*, NOTDEFINED('Z', 9)*/; //don't change this sequence, for Rubik's sake!

    private final char charValue;      // Private variable
    private final int intValue;

    LocationInFace(char charValue, int intValue) {     // Constructor
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

   
}

