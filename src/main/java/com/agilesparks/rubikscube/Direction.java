package com.agilesparks.rubikscube;

public enum Direction {
    CW("CW", 0), CCW("CCW", 1);

    private final String stringValue;      // Private variable
    private final int intValue;

    Direction(String stringValue, int intValue) {     // Constructor
        this.stringValue = stringValue;
        this.intValue = intValue;
    }

    String getString() {              // Getter
        return stringValue;
    }

    int getInt() {              // Getter
        return intValue;
    }

    Direction getOpposite() {
        if (this == Direction.CW)
            return Direction.CCW;
        else
            return Direction.CW;
    }
}
