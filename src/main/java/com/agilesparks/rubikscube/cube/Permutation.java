package com.agilesparks.rubikscube.cube;

import java.io.FileReader;
import java.io.IOException;

import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.FaceFactory;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Position;



public class Permutation {
    CubeCubicle c_Cube_cubicle[] = new CubeCubicle[20];
    short c_cubicles;
    
    public NewCube newCube = new NewCube();
    public NewCube newCubeOriginal = new NewCube();

    public Permutation() {
        c_cubicles = -1;
    }
    
	public static Permutation getPermutationFromCube(Cube cube) {
		
		
		Location l_rubikLocation[] = {
		        new Location(Face.FRONT, Face.TOP),
		        new Location(Face.FRONT, Face.RIGHT),
		        new Location(Face.FRONT, Face.LEFT),
		        new Location(Face.FRONT, Face.BOTTOM),
		        new Location(Face.BACK, Face.TOP),
		        new Location(Face.BACK, Face.RIGHT),
		        new Location(Face.BACK, Face.LEFT),
		        new Location(Face.BACK, Face.BOTTOM),
		        new Location(Face.TOP, Face.RIGHT),
		        new Location(Face.TOP, Face.LEFT),
		        new Location(Face.BOTTOM, Face.RIGHT),
		        new Location(Face.BOTTOM, Face.LEFT),
		        new Location(Face.FRONT, Face.TOP, Face.RIGHT),
		        new Location(Face.FRONT, Face.TOP, Face.LEFT),
		        new Location(Face.FRONT, Face.BOTTOM, Face.RIGHT),
		        new Location(Face.FRONT, Face.BOTTOM, Face.LEFT),
		        new Location(Face.BACK, Face.TOP, Face.RIGHT),
		        new Location(Face.BACK, Face.TOP, Face.LEFT),
		        new Location(Face.BACK, Face.BOTTOM, Face.RIGHT),
		        new Location(Face.BACK, Face.BOTTOM, Face.LEFT)
		};
		int i;
		Permutation l_permutation = new Permutation();
		l_permutation.newCube = new NewCube(cube.newCube);
		l_permutation.newCubeOriginal = new NewCube(cube.newCube);
		
		for (i = 0; i < 20; i++)
		    l_permutation.addCubicleData(new CubeCubicle(l_rubikLocation[i].getCopy(),
		            cube.getOriginalLocationOfCurrentCubicleInLocation(l_rubikLocation[i]).getCopy(),
		            cube.getPositionOfCubicleOfCubiclePlace(l_rubikLocation[i].getCopy())));
		return l_permutation;
	}
    

    CubeCubicle getCubicleData(int p_index) {
        return c_Cube_cubicle[p_index];
    }

    void addCubicleData(CubeCubicle p_cubicleData) {
        c_cubicles++;
        c_Cube_cubicle[c_cubicles] = p_cubicleData;
    }




    public void print() {
       /* int i;
        System.out.format("\nnumber of cubicles is %d\n", c_cubicles + 1);
        for (i = 0; i <= c_cubicles; i++) {
            System.out.format("CubiclePlace Location:%s", c_Cube_cubicle[i].getLocation().getString());
            System.out.format(" Cubicle Location:%s", c_Cube_cubicle[i].currentCubieOriginalLocation().getString());
            System.out.format(" Cubicle Position:%s\n", c_Cube_cubicle[i].getCubiePosition().getString());
        }*/
    	newCube.print();
    }

  
    public int getValue(int p_highestFloor) {
        int i, l_value = 0;
        for (i = 0; i < 20; i++) {
            Location l_currLocation = c_Cube_cubicle[i].getLocation();
            if (l_currLocation.getFloor() <= p_highestFloor)
                if (c_Cube_cubicle[i].getLocation().equals(c_Cube_cubicle[i].currentCubieOriginalLocation())
                        && (c_Cube_cubicle[i].getCubiePosition().equals(new Position(Face.TOP, Face.FRONT)))
                        )
                    l_value += 2;

        }
        
       
        int OLDvalue=l_value;
      NewCube fixedCube = new NewCube();
        l_value = 2*(8-newCube.countDifferenceFirstFloor(fixedCube));
        if (p_highestFloor>1)
        	l_value += 2*(4-newCube.countDifferenceSecondFloor(fixedCube));
        if (p_highestFloor>2)
        	l_value += 2*(8-newCube.countDifferenceThirdFloor(fixedCube));
       
        if (OLDvalue!=l_value)
        	 System.out.format("Floor: %d OLD  = %d NEW = %d\n", p_highestFloor,OLDvalue,l_value);
        return l_value;
    }

    public Permutation getCopy() {
        Permutation l_permutation = new Permutation();
        int i;
        for (i = 0; i < 20; i++)
            l_permutation.addCubicleData(getCubicleData(i));
        l_permutation.newCube = new NewCube(newCube);
        l_permutation.newCubeOriginal = new NewCube(newCubeOriginal);
        return l_permutation;
    }


}