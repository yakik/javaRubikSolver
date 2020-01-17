package com.agilesparks.rubikscube.cube;
//package com.javarubiksolver.www;
//
//public class CubiclePlace {
//
//
//    Cubicle c_originalCubicle;
//    Cubicle c_currentCubicle;
//    Location c_location;
//
//    // Cuibcle c_cubicles[3][3][3];
//    //Face c_frontViewPoint;
//    //Face c_top_ViewPoint;
//
//
//    CubiclePlace(Location p_location) {
//        Cubicle l_Cubicle;
//        c_location = p_location;
//        l_Cubicle = new Cubicle();
//        (l_Cubicle).setHomeCubicle(this);
//        (l_Cubicle).setCurrentCubicle(this);
//        l_Cubicle.setPosition(new Position(Face.U,Face.F));
//        setHomeCubie(l_Cubicle);
//        setCurrentCubie(l_Cubicle);
//    }
//
//    void rotateCurrentCubicle(Rotation p_rotate){
//        c_currentCubicle.rotate(p_rotate);
//    }
//
//
//    Location getLocation() {
//        return c_location;
//    }
//
//
//    Cubicle getHomeCubie() {
//        return c_originalCubicle;
//    }
//
//    void setHomeCubie(Cubicle p_Cubicle) {
//        c_originalCubicle = p_Cubicle;
//    }
//
//    Cubicle getCurrentCubie() {
//        return c_currentCubicle;
//    }
//
//    void setCurrentCubie(Cubicle p_Cubicle) {
//        c_currentCubicle = p_Cubicle;
//        p_Cubicle.setCurrentCubicle(this);
//    }
//
//
//}