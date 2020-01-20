package com.agilesparks.rubikscube.cube;

import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Position;
import com.agilesparks.rubikscube.utils.Rotation;

public class Cube {


    
    public NewCube newCube = new NewCube();
    
    

    public Cube() {
    }



    public void rotateFace(Face face, Direction direction) {
    	
    	newCube.rotateFace(face, direction);
    	

    }


    public void setPermutation(Permutation p_permutation) {
    	newCube = new NewCube(p_permutation.newCube);

    }


}




