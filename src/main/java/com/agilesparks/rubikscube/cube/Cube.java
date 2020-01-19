package com.agilesparks.rubikscube.cube;

import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Position;
import com.agilesparks.rubikscube.utils.Rotation;

public class Cube {


    private CubeCubicle cubeCubicles[] = new CubeCubicle[20];

    private Face g_faceOrder[][] = {
            {Face.FRONT, Face.LEFT, Face.BACK, Face.RIGHT}, {Face.RIGHT, Face.BACK, Face.LEFT, Face.FRONT
    }, {Face.TOP, Face.BACK, Face.BOTTOM, Face.FRONT
    }, {Face.TOP, Face.FRONT, Face.BOTTOM, Face.BACK
    }, {Face.TOP, Face.RIGHT, Face.BOTTOM, Face.LEFT
    }, {Face.TOP, Face.LEFT, Face.BOTTOM, Face.RIGHT
    }
    };
    
    NewCube newCube = new NewCube();
    
    

    public Cube() {
        initializeCubeCubicles();
    }

    private void initializeCubeCubicles() {
        cubeCubicles[0] = new CubeCubicle(new Location(Face.FRONT, Face.TOP), new Location(Face.FRONT, Face.TOP), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[1] = new CubeCubicle(new Location(Face.FRONT, Face.RIGHT), new Location(Face.FRONT, Face.RIGHT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[2] = new CubeCubicle(new Location(Face.FRONT, Face.LEFT), new Location(Face.FRONT, Face.LEFT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[3] = new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM), new Location(Face.FRONT, Face.BOTTOM), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[4] = new CubeCubicle(new Location(Face.BACK, Face.TOP), new Location(Face.BACK, Face.TOP), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[5] = new CubeCubicle(new Location(Face.BACK, Face.RIGHT), new Location(Face.BACK, Face.RIGHT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[6] = new CubeCubicle(new Location(Face.BACK, Face.LEFT), new Location(Face.BACK, Face.LEFT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[7] = new CubeCubicle(new Location(Face.BACK, Face.BOTTOM), new Location(Face.BACK, Face.BOTTOM), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[8] = new CubeCubicle(new Location(Face.TOP, Face.RIGHT), new Location(Face.TOP, Face.RIGHT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[9] = new CubeCubicle(new Location(Face.TOP, Face.LEFT), new Location(Face.TOP, Face.LEFT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[10] = new CubeCubicle(new Location(Face.BOTTOM, Face.RIGHT), new Location(Face.BOTTOM, Face.RIGHT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[11] = new CubeCubicle(new Location(Face.BOTTOM, Face.LEFT), new Location(Face.BOTTOM, Face.LEFT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[12] = new CubeCubicle(new Location(Face.FRONT, Face.TOP, Face.RIGHT), new Location(Face.FRONT, Face.TOP, Face.RIGHT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[13] = new CubeCubicle(new Location(Face.FRONT, Face.TOP, Face.LEFT), new Location(Face.FRONT, Face.TOP, Face.LEFT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[14] = new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM, Face.RIGHT), new Location(Face.FRONT, Face.BOTTOM, Face.RIGHT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[15] = new CubeCubicle(new Location(Face.FRONT, Face.BOTTOM, Face.LEFT), new Location(Face.FRONT, Face.BOTTOM, Face.LEFT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[16] = new CubeCubicle(new Location(Face.BACK, Face.TOP, Face.RIGHT), new Location(Face.BACK, Face.TOP, Face.RIGHT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[17] = new CubeCubicle(new Location(Face.BACK, Face.TOP, Face.LEFT), new Location(Face.BACK, Face.TOP, Face.LEFT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[18] = new CubeCubicle(new Location(Face.BACK, Face.BOTTOM, Face.RIGHT), new Location(Face.BACK, Face.BOTTOM, Face.RIGHT), new Position(Face.TOP, Face.FRONT));
        cubeCubicles[19] = new CubeCubicle(new Location(Face.BACK, Face.BOTTOM, Face.LEFT), new Location(Face.BACK, Face.BOTTOM, Face.LEFT), new Position(Face.TOP, Face.FRONT));

    }

    private CubeCubicle getCubeCubicle(Location p_location) {
        if ((new Location(Face.FRONT, Face.TOP)).equals(p_location)) return cubeCubicles[0];
        if ((new Location(Face.FRONT, Face.RIGHT)).equals(p_location)) return cubeCubicles[1];
        if ((new Location(Face.FRONT, Face.LEFT)).equals(p_location)) return cubeCubicles[2];
        if ((new Location(Face.FRONT, Face.BOTTOM)).equals(p_location)) return cubeCubicles[3];
        if ((new Location(Face.BACK, Face.TOP)).equals(p_location)) return cubeCubicles[4];
        if ((new Location(Face.BACK, Face.RIGHT)).equals(p_location)) return cubeCubicles[5];
        if ((new Location(Face.BACK, Face.LEFT)).equals(p_location)) return cubeCubicles[6];
        if ((new Location(Face.BACK, Face.BOTTOM)).equals(p_location)) return cubeCubicles[7];
        if ((new Location(Face.TOP, Face.RIGHT)).equals(p_location)) return cubeCubicles[8];
        if ((new Location(Face.TOP, Face.LEFT)).equals(p_location)) return cubeCubicles[9];
        if ((new Location(Face.BOTTOM, Face.RIGHT)).equals(p_location)) return cubeCubicles[10];
        if ((new Location(Face.BOTTOM, Face.LEFT)).equals(p_location)) return cubeCubicles[11];
        if ((new Location(Face.FRONT, Face.TOP, Face.RIGHT)).equals(p_location)) return cubeCubicles[12];
        if ((new Location(Face.FRONT, Face.TOP, Face.LEFT)).equals(p_location)) return cubeCubicles[13];
        if ((new Location(Face.FRONT, Face.BOTTOM, Face.RIGHT)).equals(p_location)) return cubeCubicles[14];
        if ((new Location(Face.FRONT, Face.BOTTOM, Face.LEFT)).equals(p_location)) return cubeCubicles[15];
        if ((new Location(Face.BACK, Face.TOP, Face.RIGHT)).equals(p_location)) return cubeCubicles[16];
        if ((new Location(Face.BACK, Face.TOP, Face.LEFT)).equals(p_location)) return cubeCubicles[17];
        if ((new Location(Face.BACK, Face.BOTTOM, Face.RIGHT)).equals(p_location)) return cubeCubicles[18];
        if ((new Location(Face.BACK, Face.BOTTOM, Face.LEFT)).equals(p_location)) return cubeCubicles[19];
        return null;

    }

    private void rotate(Rotation p_rotation
            , CubeCubicle cubicle1
            , CubeCubicle cubicle2
            , CubeCubicle cubicle3
            , CubeCubicle cubicle4) {
        if (p_rotation.getDirection() == Direction.CW) {
            CubeCubicle tmpCubicle = new CubeCubicle(
                    cubicle4.getLocation(), cubicle4.currentCubieOriginalLocation(), cubicle4.getCubiePosition());
            cubicle4.rotateFrom(p_rotation, cubicle3);
            cubicle3.rotateFrom(p_rotation, cubicle2);
            cubicle2.rotateFrom(p_rotation, cubicle1);
            cubicle1.rotateFrom(p_rotation, tmpCubicle);
        } else {
            CubeCubicle tmpCubicle = new CubeCubicle(
                    cubicle1.getLocation(), cubicle1.currentCubieOriginalLocation(), cubicle1.getCubiePosition());
            cubicle1.rotateFrom(p_rotation, cubicle2);
            cubicle2.rotateFrom(p_rotation, cubicle3);
            cubicle3.rotateFrom(p_rotation, cubicle4);
            cubicle4.rotateFrom(p_rotation, tmpCubicle);
        }

    }
    
    public void rotateFace(Face face, Direction direction) {
    	
    	newCube.rotateFace(face, direction);
    	
    	
    	
    	Rotation rotation = new Rotation(face,direction);
   
    	
        Face l_face = rotation.getFace();
        switch (l_face) {
            case TOP:
                 rotate(rotation, getCubeCubicle(new Location(Face.TOP, Face.LEFT))
                        , getCubeCubicle(new Location(Face.TOP, Face.BACK))
                        , getCubeCubicle(new Location(Face.TOP, Face.RIGHT))
                        , getCubeCubicle(new Location(Face.TOP, Face.FRONT)));
             rotate(rotation, getCubeCubicle(new Location(Face.TOP, Face.LEFT, Face.FRONT))
                    , getCubeCubicle(new Location(Face.TOP, Face.BACK, Face.LEFT))
                    , getCubeCubicle(new Location(Face.TOP, Face.RIGHT, Face.BACK))
                    , getCubeCubicle(new Location(Face.TOP, Face.FRONT, Face.RIGHT)));
            return;
            case BOTTOM:
                rotate(rotation, getCubeCubicle(new Location(Face.BOTTOM, Face.LEFT))
                        , getCubeCubicle(new Location(Face.BOTTOM, Face.FRONT))
                        , getCubeCubicle(new Location(Face.BOTTOM, Face.RIGHT))
                        , getCubeCubicle(new Location(Face.BOTTOM, Face.BACK)));
                rotate(rotation, getCubeCubicle(new Location(Face.BOTTOM, Face.LEFT, Face.FRONT))
                        , getCubeCubicle(new Location(Face.BOTTOM, Face.FRONT, Face.RIGHT))
                        , getCubeCubicle(new Location(Face.BOTTOM, Face.RIGHT, Face.BACK))
                        , getCubeCubicle(new Location(Face.BOTTOM, Face.BACK, Face.LEFT)));
                return;
            case FRONT:
                rotate(rotation, getCubeCubicle(new Location(Face.FRONT, Face.LEFT))
                        , getCubeCubicle(new Location(Face.FRONT, Face.TOP))
                        , getCubeCubicle(new Location(Face.FRONT, Face.RIGHT))
                        , getCubeCubicle(new Location(Face.FRONT, Face.BOTTOM)));
                rotate(rotation, getCubeCubicle(new Location(Face.FRONT, Face.LEFT, Face.TOP))
                        , getCubeCubicle(new Location(Face.FRONT, Face.TOP, Face.RIGHT))
                        , getCubeCubicle(new Location(Face.FRONT, Face.RIGHT, Face.BOTTOM))
                        , getCubeCubicle(new Location(Face.FRONT, Face.BOTTOM, Face.LEFT)));
                return;
            case BACK:
                rotate(rotation, getCubeCubicle(new Location(Face.BACK, Face.LEFT))
                        , getCubeCubicle(new Location(Face.BACK, Face.BOTTOM))
                        , getCubeCubicle(new Location(Face.BACK, Face.RIGHT))
                        , getCubeCubicle(new Location(Face.BACK, Face.TOP)));
                rotate(rotation, getCubeCubicle(new Location(Face.BACK, Face.LEFT, Face.TOP))
                        , getCubeCubicle(new Location(Face.BACK, Face.BOTTOM, Face.LEFT))
                        , getCubeCubicle(new Location(Face.BACK, Face.RIGHT, Face.BOTTOM))
                        , getCubeCubicle(new Location(Face.BACK, Face.TOP, Face.RIGHT)));
                return;
            case RIGHT:
                rotate(rotation, getCubeCubicle(new Location(Face.RIGHT, Face.FRONT))
                        , getCubeCubicle(new Location(Face.RIGHT, Face.TOP))
                        , getCubeCubicle(new Location(Face.RIGHT, Face.BACK))
                        , getCubeCubicle(new Location(Face.RIGHT, Face.BOTTOM)));
                rotate(rotation, getCubeCubicle(new Location(Face.RIGHT, Face.FRONT, Face.TOP))
                        , getCubeCubicle(new Location(Face.RIGHT, Face.TOP, Face.BACK))
                        , getCubeCubicle(new Location(Face.RIGHT, Face.BACK, Face.BOTTOM))
                        , getCubeCubicle(new Location(Face.RIGHT, Face.BOTTOM, Face.FRONT)));
                return;
            case LEFT:
                 rotate(rotation, getCubeCubicle(new Location(Face.LEFT, Face.FRONT))
                        , getCubeCubicle(new Location(Face.LEFT, Face.BOTTOM))
                        , getCubeCubicle(new Location(Face.LEFT, Face.BACK))
                        , getCubeCubicle(new Location(Face.LEFT, Face.TOP)));
             rotate(rotation, getCubeCubicle(new Location(Face.LEFT, Face.FRONT, Face.TOP))
                    , getCubeCubicle(new Location(Face.LEFT, Face.BOTTOM, Face.FRONT))
                    , getCubeCubicle(new Location(Face.LEFT, Face.BACK, Face.BOTTOM))
                    , getCubeCubicle(new Location(Face.LEFT, Face.TOP, Face.BACK)));
            return;

        }


    }

    private void updateCubeCubicle(Location p_location,Location p_currentLocation, Position p_currentPosition){
        getCubeCubicle(p_location).c_currentPosition = p_currentPosition.getCopy();
        getCubeCubicle(p_location).c_currentCubieOriginalLocation = p_currentLocation.getCopy();
}


    public void setPermutation(Permutation p_permutation) {
    	newCube = new NewCube(p_permutation.newCube);
        int i;
        for (i = 0; i < 20; i++)
            updateCubeCubicle(p_permutation.getCubicleData(i).getLocation().getCopy()
                    ,p_permutation.getCubicleData(i).getCurrentCubieOriginalLocation().getCopy()
                    ,p_permutation.getCubicleData(i).getCubiePosition().getCopy());

    }

    public Location getOriginalLocationOfCurrentCubicleInLocation(Location p_cubicleLocation) {
        return  getCubeCubicle(p_cubicleLocation).getCurrentCubieOriginalLocation().getCopy();
        //   getCurrentCubie().getCurrentCubicle().
        // getLocation();
    }

    public Position getPositionOfCubicleOfCubiclePlace(Location p_cubicleLocation) {
        return getCubeCubicle(p_cubicleLocation).getCubiePosition().getCopy();
    }

}




