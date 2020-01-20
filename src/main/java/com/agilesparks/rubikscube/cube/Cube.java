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



	public static int getValueIndirection(Permutation permutation, int p_highestFloor) {
		int  l_value = 0;
		  NewCube fixedCube = new NewCube();
		    l_value = 2*(8-permutation.newCube.countDifferenceFirstFloor(fixedCube));
		    if (p_highestFloor>1)
		    	l_value += 2*(4-permutation.newCube.countDifferenceSecondFloor(fixedCube));
		    if (p_highestFloor>2)
		    	l_value += 2*(8-permutation.newCube.countDifferenceThirdFloor(fixedCube));
		
		    return l_value;
	}


}




