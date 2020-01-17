package com.agilesparks.rubikscube.cube;

import com.agilesparks.rubikscube.Position;
import com.agilesparks.rubikscube.Rotation;
import com.agilesparks.rubikscube.utils.Face;

public class CubeCubicle {

    public Location c_locationInCube;
    public Location c_currentCubieOriginalLocation;
    public Position c_currentPosition;

    public void rotateFrom(Rotation p_rotation, CubeCubicle p_source){
        c_currentCubieOriginalLocation = p_source.getCurrentCubieOriginalLocation();
        c_currentPosition = p_source.getCubiePosition();
        c_currentPosition.rotate(p_rotation);
    }

    CubeCubicle() {
    }

    public Location getCurrentCubieOriginalLocation (){
        return c_currentCubieOriginalLocation;
    }
    public CubeCubicle(Location p_location, Location p_cubieLocation, Position p_cubiePosition) {
        c_locationInCube = p_location;
        c_currentCubieOriginalLocation = p_cubieLocation;
        c_currentPosition = p_cubiePosition;
    }

    public Location getLocation() {
        return c_locationInCube;
    }

    public Location currentCubieOriginalLocation() {
        return c_currentCubieOriginalLocation;
    }

    public Position getCubiePosition() {
        return c_currentPosition;
    }

    boolean inPlaceAndPosition(){
        return (this.getLocation().equals(this.currentCubieOriginalLocation()))
                && this.getCubiePosition().equals(new Position(Face.U, Face.F));
    }



    boolean equals(
            CubeCubicle p_cubicleData)

    {
        return (c_locationInCube.equals(p_cubicleData.c_locationInCube) &&
                c_currentCubieOriginalLocation.equals(p_cubicleData.c_currentCubieOriginalLocation) &&
                c_currentPosition.equals(p_cubicleData.c_currentPosition));
    }
}