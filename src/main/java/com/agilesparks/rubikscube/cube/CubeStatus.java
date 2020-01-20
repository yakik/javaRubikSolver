package com.agilesparks.rubikscube.cube;

import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;

public class CubeStatus {

	public static boolean changesOnlyInThirdFloor(Cube cube, Cube p_comparedPermutation) {
		int l_counter = 0;
		
		
		
		//next line replaced previous code
		l_counter = cube.newCube.countDifferenceThirdFloor(p_comparedPermutation.newCube);
	
		if (l_counter>0) return true;
		else return false;
	}

	public static boolean isDifferentItemsInFirstFloorLessThanThree(Cube cube,
			Cube p_comparedPermutation) {
		int l_counter = 0;
	
		l_counter = cube.newCube.countDifferenceFirstFloor(p_comparedPermutation.newCube);
		
		
		if (l_counter<3) return true;
		        else return false;
	}

	public static boolean isDifferentItemsOnlyInSecondFloorLessThanThree(Cube cube,
			Cube p_comparedPermutation) {
		int l_counter = 0;
		
		l_counter = cube.newCube.countDifferenceSecondFloor(p_comparedPermutation.newCube);
		
		
		
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
