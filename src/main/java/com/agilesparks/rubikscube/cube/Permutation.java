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
        int i;
        System.out.format("\nnumber of cubicles is %d\n", c_cubicles + 1);
        for (i = 0; i <= c_cubicles; i++) {
            System.out.format("CubiclePlace Location:%s", c_Cube_cubicle[i].getLocation().getString());
            System.out.format(" Cubicle Location:%s", c_Cube_cubicle[i].currentCubieOriginalLocation().getString());
            System.out.format(" Cubicle Position:%s\n", c_Cube_cubicle[i].getCubiePosition().getString());
        }
    }

    void load(FileReader p_reader) {
        // reading order is: 12 edges first, then 8 corners
        // reading order: cubicle, current cubie location, current cubie position
        int i;
        Location l_cubicleLocation, l_currCubicleLocation;
        Position l_position;
        FaceFactory l_faceFactory = new FaceFactory();
        try {
            for (i = 0; i < 12; i++) {

                Face l_cubicleFace0, l_cubicleFace1;
                Face l_currCubicleFace0, l_currCubicleFace1;
                Face l_up, l_front;

                l_cubicleFace0 = FaceFactory.getFaceByInt(p_reader.read());
                l_cubicleFace1 = FaceFactory.getFaceByInt(p_reader.read());
                p_reader.read();
                l_currCubicleFace0 = FaceFactory.getFaceByInt(p_reader.read());
                l_currCubicleFace1 = FaceFactory.getFaceByInt(p_reader.read());
                p_reader.read();
                l_up = FaceFactory.getFaceByInt(p_reader.read());
                l_front = FaceFactory.getFaceByInt(p_reader.read());
                p_reader.read();
                l_cubicleLocation = new Location(l_cubicleFace0, l_cubicleFace1);
                l_currCubicleLocation = new Location(l_currCubicleFace0, l_currCubicleFace1);
                l_position = new Position(l_up, l_front);
                addCubicleData(new CubeCubicle(l_cubicleLocation, l_currCubicleLocation, l_position));
            }
            for (i = 0; i < 8; i++) {
                Face l_cubicleFace0, l_cubicleFace1, l_cubicleFace2;
                Face l_currCubicleFace0, l_currCubicleFace1, l_currCubicleFace2;
                Face l_up, l_front;

                l_cubicleFace0 = FaceFactory.getFaceByInt(p_reader.read());
                l_cubicleFace1 = FaceFactory.getFaceByInt(p_reader.read());
                l_cubicleFace2 = FaceFactory.getFaceByInt(p_reader.read());
                p_reader.read();
                l_currCubicleFace0 = FaceFactory.getFaceByInt(p_reader.read());
                l_currCubicleFace1 = FaceFactory.getFaceByInt(p_reader.read());
                l_currCubicleFace2 = FaceFactory.getFaceByInt(p_reader.read());
                p_reader.read();
                l_up = FaceFactory.getFaceByInt(p_reader.read());
                l_front = FaceFactory.getFaceByInt(p_reader.read());
                p_reader.read();
                l_cubicleLocation = new Location(l_cubicleFace0, l_cubicleFace1, l_cubicleFace2);
                l_currCubicleLocation = new Location(l_currCubicleFace0, l_currCubicleFace1, l_currCubicleFace2);
                l_position = new Position(l_up, l_front);
                addCubicleData(new CubeCubicle(l_cubicleLocation, l_currCubicleLocation, l_position));
            }
        } catch (IOException ex) {
        }
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
        return l_value;
    }

    public Permutation getCopy() {
        Permutation l_permutation = new Permutation();
        int i;
        for (i = 0; i < 20; i++)
            l_permutation.addCubicleData(getCubicleData(i));
        return l_permutation;
    }

    public boolean equals( Permutation p_permutation) {
        boolean l_answer = true;
        int i;
        for (i = 0; i < 20; i++)
                    if (!(getCubicleData(i).equals(p_permutation.getCubicleData(i))))
                        return false;
                    else
                        l_answer = true;
        return l_answer;
    }


}