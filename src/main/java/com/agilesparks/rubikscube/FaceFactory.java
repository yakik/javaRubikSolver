package com.agilesparks.rubikscube;

import com.agilesparks.rubikscube.utils.Face;

public class FaceFactory {
    static Face getFaceByInt(int intValue) {
        switch (intValue) {
            case 3:
                return Face.L;
            case 2:
                return Face.R;
            case 0:
                return Face.U;
            case 1:
                return Face.D;
            case 4:
                return Face.F;
            case 5:
                return Face.B;
            default:
                return Face.U;
        }
    }
}
