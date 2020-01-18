package com.agilesparks.rubikscube.solver;

import com.agilesparks.rubikscube.cube.Cube;
import com.agilesparks.rubikscube.cube.CubeCubicle;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;
import com.agilesparks.rubikscube.utils.Permutation;

public class CubeStatus {

	public static boolean changesOnlyInThirdFloor(Cube cube, Permutation p_comparedPermutation) {
		CubeCubicle l_permutationCubicle;
		int l_counter = 0;
		for (int i =0;i<20;i++)
		    if ((l_permutationCubicle=p_comparedPermutation.getCubicleData(i))!=null)
		        if (!CubeStatus.isThirdFloor(l_permutationCubicle.getLocation())) {
		            if (!l_permutationCubicle.getCubiePosition()
		                    .equals(cube.getPositionOfCubicleOfCubiclePlace(l_permutationCubicle.getLocation()))
		                    || !l_permutationCubicle.getCurrentCubieOriginalLocation()
		                    .equals(cube.getOriginalLocationOfCurrentCubicleInLocation(l_permutationCubicle.getLocation())))
		                return false;
		        } else {
		            if (!l_permutationCubicle.getCubiePosition()
		                    .equals(cube.getPositionOfCubicleOfCubiclePlace(l_permutationCubicle.getLocation()))
		                    || !l_permutationCubicle.getCurrentCubieOriginalLocation()
		                    .equals(cube.getOriginalLocationOfCurrentCubicleInLocation(l_permutationCubicle.getLocation())))
		                l_counter++;
		        }
		
		
		if (l_counter>0) return true;
		else return false;
	}

	public static boolean isDifferentItemsInFirstFloorLessThanThree(Cube cube,
			Permutation p_comparedPermutation) {
		CubeCubicle l_permutationCubicle;
		int l_counter = 0;
		for (int i =0;i<20;i++)
		    if ((l_permutationCubicle=p_comparedPermutation.getCubicleData(i))!=null)
		        if (CubeStatus.isFirstFloor(l_permutationCubicle.getLocation()))
		            if (!l_permutationCubicle.getCubiePosition()
		        .equals(cube.getPositionOfCubicleOfCubiclePlace(l_permutationCubicle.getLocation()))
		            || !l_permutationCubicle.getCurrentCubieOriginalLocation()
		                    .equals(cube.getOriginalLocationOfCurrentCubicleInLocation(l_permutationCubicle.getLocation())))
		                l_counter++;
		if (l_counter<3) return true;
		        else return false;
	}

	public static boolean isDifferentItemsOnlyInSecondFloorLessThanThree(Cube cube,
			Permutation p_comparedPermutation) {
		CubeCubicle l_permutationCubicle;
		int l_counter = 0;
		for (int i =0;i<20;i++)
		    if ((l_permutationCubicle=p_comparedPermutation.getCubicleData(i))!=null)
		        if (CubeStatus.isSecondFloor(l_permutationCubicle.getLocation())) {
		            if (!l_permutationCubicle.getCubiePosition()
		                    .equals(cube.getPositionOfCubicleOfCubiclePlace(l_permutationCubicle.getLocation()))
		                    || !l_permutationCubicle.getCurrentCubieOriginalLocation()
		                    .equals(cube.getOriginalLocationOfCurrentCubicleInLocation(l_permutationCubicle.getLocation())))
		                l_counter++;
		        } else {
		            if ((l_permutationCubicle=p_comparedPermutation.getCubicleData(i))!=null)
		                if (CubeStatus.isFirstFloor(l_permutationCubicle.getLocation()))
		                    if (!l_permutationCubicle.getCubiePosition()
		                            .equals(cube.getPositionOfCubicleOfCubiclePlace(l_permutationCubicle.getLocation()))
		                            || !l_permutationCubicle.getCurrentCubieOriginalLocation()
		                            .equals(cube.getOriginalLocationOfCurrentCubicleInLocation(l_permutationCubicle.getLocation())))
		                        return false;
		        }
		
		
		if (l_counter<3) return true;
		else return false;
	}

	static public boolean isFirstFloor(Location p_location){
	    return (p_location.containsFace(Face.BOTTOM));
	
	}

	static public boolean isThirdFloor(Location p_location){
	    return (p_location.containsFace(Face.TOP));
	
	}

	static public boolean isSecondFloor(Location p_location){
	    return (!(isFirstFloor(p_location)||isThirdFloor(p_location)));
	
	}

}
