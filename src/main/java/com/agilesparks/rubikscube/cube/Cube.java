package com.agilesparks.rubikscube.cube;

import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Permutation;
import com.agilesparks.rubikscube.utils.Position;
import com.agilesparks.rubikscube.utils.Rotation;

public class Cube {


    private CubeCubicle cubeCubicles[] = new CubeCubicle[20];

    private Face g_faceOrder[][] = {
            {Face.F, Face.L, Face.B, Face.R}, {Face.R, Face.B, Face.L, Face.F
    }, {Face.U, Face.B, Face.D, Face.F
    }, {Face.U, Face.F, Face.D, Face.B
    }, {Face.U, Face.R, Face.D, Face.L
    }, {Face.U, Face.L, Face.D, Face.R
    }
    };

    public Cube() {
        initializeCubeCubicles();
    }

    private void initializeCubeCubicles() {
        cubeCubicles[0] = new CubeCubicle(new Location(Face.F, Face.U), new Location(Face.F, Face.U), new Position(Face.U, Face.F));
        cubeCubicles[1] = new CubeCubicle(new Location(Face.F, Face.R), new Location(Face.F, Face.R), new Position(Face.U, Face.F));
        cubeCubicles[2] = new CubeCubicle(new Location(Face.F, Face.L), new Location(Face.F, Face.L), new Position(Face.U, Face.F));
        cubeCubicles[3] = new CubeCubicle(new Location(Face.F, Face.D), new Location(Face.F, Face.D), new Position(Face.U, Face.F));
        cubeCubicles[4] = new CubeCubicle(new Location(Face.B, Face.U), new Location(Face.B, Face.U), new Position(Face.U, Face.F));
        cubeCubicles[5] = new CubeCubicle(new Location(Face.B, Face.R), new Location(Face.B, Face.R), new Position(Face.U, Face.F));
        cubeCubicles[6] = new CubeCubicle(new Location(Face.B, Face.L), new Location(Face.B, Face.L), new Position(Face.U, Face.F));
        cubeCubicles[7] = new CubeCubicle(new Location(Face.B, Face.D), new Location(Face.B, Face.D), new Position(Face.U, Face.F));
        cubeCubicles[8] = new CubeCubicle(new Location(Face.U, Face.R), new Location(Face.U, Face.R), new Position(Face.U, Face.F));
        cubeCubicles[9] = new CubeCubicle(new Location(Face.U, Face.L), new Location(Face.U, Face.L), new Position(Face.U, Face.F));
        cubeCubicles[10] = new CubeCubicle(new Location(Face.D, Face.R), new Location(Face.D, Face.R), new Position(Face.U, Face.F));
        cubeCubicles[11] = new CubeCubicle(new Location(Face.D, Face.L), new Location(Face.D, Face.L), new Position(Face.U, Face.F));
        cubeCubicles[12] = new CubeCubicle(new Location(Face.F, Face.U, Face.R), new Location(Face.F, Face.U, Face.R), new Position(Face.U, Face.F));
        cubeCubicles[13] = new CubeCubicle(new Location(Face.F, Face.U, Face.L), new Location(Face.F, Face.U, Face.L), new Position(Face.U, Face.F));
        cubeCubicles[14] = new CubeCubicle(new Location(Face.F, Face.D, Face.R), new Location(Face.F, Face.D, Face.R), new Position(Face.U, Face.F));
        cubeCubicles[15] = new CubeCubicle(new Location(Face.F, Face.D, Face.L), new Location(Face.F, Face.D, Face.L), new Position(Face.U, Face.F));
        cubeCubicles[16] = new CubeCubicle(new Location(Face.B, Face.U, Face.R), new Location(Face.B, Face.U, Face.R), new Position(Face.U, Face.F));
        cubeCubicles[17] = new CubeCubicle(new Location(Face.B, Face.U, Face.L), new Location(Face.B, Face.U, Face.L), new Position(Face.U, Face.F));
        cubeCubicles[18] = new CubeCubicle(new Location(Face.B, Face.D, Face.R), new Location(Face.B, Face.D, Face.R), new Position(Face.U, Face.F));
        cubeCubicles[19] = new CubeCubicle(new Location(Face.B, Face.D, Face.L), new Location(Face.B, Face.D, Face.L), new Position(Face.U, Face.F));

    }

    private CubeCubicle getCubeCubicle(Location p_location) {
        if ((new Location(Face.F, Face.U)).equals(p_location)) return cubeCubicles[0];
        if ((new Location(Face.F, Face.R)).equals(p_location)) return cubeCubicles[1];
        if ((new Location(Face.F, Face.L)).equals(p_location)) return cubeCubicles[2];
        if ((new Location(Face.F, Face.D)).equals(p_location)) return cubeCubicles[3];
        if ((new Location(Face.B, Face.U)).equals(p_location)) return cubeCubicles[4];
        if ((new Location(Face.B, Face.R)).equals(p_location)) return cubeCubicles[5];
        if ((new Location(Face.B, Face.L)).equals(p_location)) return cubeCubicles[6];
        if ((new Location(Face.B, Face.D)).equals(p_location)) return cubeCubicles[7];
        if ((new Location(Face.U, Face.R)).equals(p_location)) return cubeCubicles[8];
        if ((new Location(Face.U, Face.L)).equals(p_location)) return cubeCubicles[9];
        if ((new Location(Face.D, Face.R)).equals(p_location)) return cubeCubicles[10];
        if ((new Location(Face.D, Face.L)).equals(p_location)) return cubeCubicles[11];
        if ((new Location(Face.F, Face.U, Face.R)).equals(p_location)) return cubeCubicles[12];
        if ((new Location(Face.F, Face.U, Face.L)).equals(p_location)) return cubeCubicles[13];
        if ((new Location(Face.F, Face.D, Face.R)).equals(p_location)) return cubeCubicles[14];
        if ((new Location(Face.F, Face.D, Face.L)).equals(p_location)) return cubeCubicles[15];
        if ((new Location(Face.B, Face.U, Face.R)).equals(p_location)) return cubeCubicles[16];
        if ((new Location(Face.B, Face.U, Face.L)).equals(p_location)) return cubeCubicles[17];
        if ((new Location(Face.B, Face.D, Face.R)).equals(p_location)) return cubeCubicles[18];
        if ((new Location(Face.B, Face.D, Face.L)).equals(p_location)) return cubeCubicles[19];
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

    public void rotateFace(Rotation p_rotation) {
        Face l_face = p_rotation.getFace();
        switch (l_face) {
            case U:
                 rotate(p_rotation, getCubeCubicle(new Location(Face.U, Face.L))
                        , getCubeCubicle(new Location(Face.U, Face.B))
                        , getCubeCubicle(new Location(Face.U, Face.R))
                        , getCubeCubicle(new Location(Face.U, Face.F)));
             rotate(p_rotation, getCubeCubicle(new Location(Face.U, Face.L, Face.F))
                    , getCubeCubicle(new Location(Face.U, Face.B, Face.L))
                    , getCubeCubicle(new Location(Face.U, Face.R, Face.B))
                    , getCubeCubicle(new Location(Face.U, Face.F, Face.R)));
            return;
            case D:
                rotate(p_rotation, getCubeCubicle(new Location(Face.D, Face.L))
                        , getCubeCubicle(new Location(Face.D, Face.F))
                        , getCubeCubicle(new Location(Face.D, Face.R))
                        , getCubeCubicle(new Location(Face.D, Face.B)));
                rotate(p_rotation, getCubeCubicle(new Location(Face.D, Face.L, Face.F))
                        , getCubeCubicle(new Location(Face.D, Face.F, Face.R))
                        , getCubeCubicle(new Location(Face.D, Face.R, Face.B))
                        , getCubeCubicle(new Location(Face.D, Face.B, Face.L)));
                return;
            case F:
                rotate(p_rotation, getCubeCubicle(new Location(Face.F, Face.L))
                        , getCubeCubicle(new Location(Face.F, Face.U))
                        , getCubeCubicle(new Location(Face.F, Face.R))
                        , getCubeCubicle(new Location(Face.F, Face.D)));
                rotate(p_rotation, getCubeCubicle(new Location(Face.F, Face.L, Face.U))
                        , getCubeCubicle(new Location(Face.F, Face.U, Face.R))
                        , getCubeCubicle(new Location(Face.F, Face.R, Face.D))
                        , getCubeCubicle(new Location(Face.F, Face.D, Face.L)));
                return;
            case B:
                rotate(p_rotation, getCubeCubicle(new Location(Face.B, Face.L))
                        , getCubeCubicle(new Location(Face.B, Face.D))
                        , getCubeCubicle(new Location(Face.B, Face.R))
                        , getCubeCubicle(new Location(Face.B, Face.U)));
                rotate(p_rotation, getCubeCubicle(new Location(Face.B, Face.L, Face.U))
                        , getCubeCubicle(new Location(Face.B, Face.D, Face.L))
                        , getCubeCubicle(new Location(Face.B, Face.R, Face.D))
                        , getCubeCubicle(new Location(Face.B, Face.U, Face.R)));
                return;
            case R:
                rotate(p_rotation, getCubeCubicle(new Location(Face.R, Face.F))
                        , getCubeCubicle(new Location(Face.R, Face.U))
                        , getCubeCubicle(new Location(Face.R, Face.B))
                        , getCubeCubicle(new Location(Face.R, Face.D)));
                rotate(p_rotation, getCubeCubicle(new Location(Face.R, Face.F, Face.U))
                        , getCubeCubicle(new Location(Face.R, Face.U, Face.B))
                        , getCubeCubicle(new Location(Face.R, Face.B, Face.D))
                        , getCubeCubicle(new Location(Face.R, Face.D, Face.F)));
                return;
            case L:
                 rotate(p_rotation, getCubeCubicle(new Location(Face.L, Face.F))
                        , getCubeCubicle(new Location(Face.L, Face.D))
                        , getCubeCubicle(new Location(Face.L, Face.B))
                        , getCubeCubicle(new Location(Face.L, Face.U)));
             rotate(p_rotation, getCubeCubicle(new Location(Face.L, Face.F, Face.U))
                    , getCubeCubicle(new Location(Face.L, Face.D, Face.F))
                    , getCubeCubicle(new Location(Face.L, Face.B, Face.D))
                    , getCubeCubicle(new Location(Face.L, Face.U, Face.B)));
            return;

        }


    }

    void updateCubeCubicle(Location p_location,Location p_currentLocation, Position p_currentPosition){
        getCubeCubicle(p_location).c_currentPosition = p_currentPosition.getCopy();
        getCubeCubicle(p_location).c_currentCubieOriginalLocation = p_currentLocation.getCopy();
}


    public void setPermutation(Permutation p_permutation) {
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




