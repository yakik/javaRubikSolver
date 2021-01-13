package com.agilesparks.rubikscube.utils;

public enum Color { 
	FRONTCOLOR('R', 0), BACKCOLOR('B', 1), RIGHTCOLOR('Y', 2), LEFTCOLOR('G', 3), TOPCOLOR('O', 4), BOTTOMCOLOR('W', 5)/*, NOTDEFINED('Z', 9)*/; //don't change this sequence, for Rubik's sake!

    private final char charValue;      // Private variable
    private final int intValue;

    Color(char charValue, int intValue) {     // Constructor
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
