package com.agilesparks.rubikscube.utils;

public class FaceFactory {
    public static Face getFaceByInt(int intValue) {
        switch (intValue) {
            case 3:
                return Face.LEFT;
            case 2:
                return Face.RIGHT;
            case 0:
                return Face.TOP;
            case 1:
                return Face.BOTTOM;
            case 4:
                return Face.FRONT;
            case 5:
                return Face.BACK;
            default:
                return Face.TOP;
        }
    }
}
