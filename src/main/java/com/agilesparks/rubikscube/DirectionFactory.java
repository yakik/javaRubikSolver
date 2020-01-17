package com.agilesparks.rubikscube;

public class DirectionFactory {
    static Direction getDirectionByInt(int intValue) {
        switch (intValue) {
            case 0:
                return Direction.CW;
            case 1:
                return Direction.CCW;
            default:
                return Direction.CW;
        }
    }
}
