package com.agilesparks.rubikscube.cube;

import java.io.FileReader;
import java.io.IOException;

import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.FaceFactory;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Position;



public class Permutation {
    
    public NewCube newCube = new NewCube();

    public Permutation() {
    }
    
	public static Permutation getPermutationFromCube(Cube cube) {
		
		
		Permutation l_permutation = new Permutation();
		l_permutation.newCube = new NewCube(cube.newCube);
		
		return l_permutation;
	}
    


    public void print() {
    	newCube.print();
    }

  
    public int getValue(int p_highestFloor) {
        int  l_value = 0;
      NewCube fixedCube = new NewCube();
        l_value = 2*(8-newCube.countDifferenceFirstFloor(fixedCube));
        if (p_highestFloor>1)
        	l_value += 2*(4-newCube.countDifferenceSecondFloor(fixedCube));
        if (p_highestFloor>2)
        	l_value += 2*(8-newCube.countDifferenceThirdFloor(fixedCube));
       
        return l_value;
    }

    public Permutation getCopy() {
        Permutation l_permutation = new Permutation();
        l_permutation.newCube = new NewCube(newCube);
        return l_permutation;
    }


}