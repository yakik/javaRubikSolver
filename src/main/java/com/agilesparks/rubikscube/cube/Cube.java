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


    public void reset(NewCube cube) {
    	newCube = new NewCube(cube);

    }



	public static int getValue(NewCube cube, int p_highestFloor) {
		int  l_value = 0;
		  NewCube fixedCube = new NewCube();
		    l_value = 2*(8-cube.countDifferenceFirstFloor(fixedCube));
		    if (p_highestFloor>1)
		    	l_value += 2*(4-cube.countDifferenceSecondFloor(fixedCube));
		    if (p_highestFloor>2)
		    	l_value += 2*(8-cube.countDifferenceThirdFloor(fixedCube));
		
		    return l_value;
	}


}




