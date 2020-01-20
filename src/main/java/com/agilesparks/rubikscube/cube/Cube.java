package com.agilesparks.rubikscube.cube;

import com.agilesparks.rubikscube.utils.Direction;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Position;
import com.agilesparks.rubikscube.utils.Rotation;

public class Cube {


    
    NewCube newCube = new NewCube();
    
    

    public Cube() {
    }
    
    public boolean equals( Cube comparedCube) {
        return newCube.equals(comparedCube.newCube);
    }



    public void rotateFace(Face face, Direction direction) {
    	
    	newCube.rotateFace(face, direction);
    	

    }


    public void reset(Cube cube) {
    	newCube = new NewCube(cube.newCube);

    }



	public static Cube getPermutationFromCube(Cube cube) {
		
		
		return cube.getCopy();
	}



	public static int getValue(Cube l_permutation, int p_highestFloor) {
		int  l_value = 0;
		  NewCube fixedCube = new NewCube();
		    l_value = 2*(8-l_permutation.newCube.countDifferenceFirstFloor(fixedCube));
		    if (p_highestFloor>1)
		    	l_value += 2*(4-l_permutation.newCube.countDifferenceSecondFloor(fixedCube));
		    if (p_highestFloor>2)
		    	l_value += 2*(8-l_permutation.newCube.countDifferenceThirdFloor(fixedCube));
		
		    return l_value;
	}



	public Cube getCopy() {
		// TODO Auto-generated method stub
		Cube cube = new Cube();
		cube.newCube = new NewCube(newCube);
		return cube;
	}





	public void print() {
		newCube.print();
	}


}




