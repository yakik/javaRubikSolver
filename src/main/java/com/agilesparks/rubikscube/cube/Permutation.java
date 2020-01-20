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

  
    public Permutation getCopy() {
        Permutation l_permutation = new Permutation();
        l_permutation.newCube = new NewCube(newCube);
        return l_permutation;
    }


}