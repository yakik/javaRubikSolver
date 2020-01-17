package com.agilesparks.rubikscube;

public enum Direction {
    CW("CW", 0), CCW("CCW", 1);

    private final String stringValue;      // Private variable
    private final int intValue;

    Direction(String stringValue, int intValue) {     // Constructor
        this.stringValue = stringValue;
        this.intValue = intValue;
    }

    public String getString() {              // Getter
        return stringValue;
    }

    public int getInt() {              // Getter
        return intValue;
    }

    public Direction getOpposite() {
        if (this == Direction.CW)
            return Direction.CCW;
        else
            return Direction.CW;
    }
}
