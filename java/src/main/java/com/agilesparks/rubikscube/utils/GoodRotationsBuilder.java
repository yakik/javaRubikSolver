package com.agilesparks.rubikscube.utils;

import com.agilesparks.rubikscube.cube.Cube;
import com.agilesparks.rubikscube.cube.CubeStatus;
import com.agilesparks.rubikscube.cube.RubikFileWriter;
import com.agilesparks.rubikscube.solver.RotationSequence;

public class GoodRotationsBuilder {

	public static void findGoodRotationLinks(String p_firstFloorFile
	        , String p_secondFloorFile, String p_thirdFloorFile, int p_levels) {
	    RubikFileWriter l_firstWriter = new RubikFileWriter(p_firstFloorFile);
	    RubikFileWriter l_secondWriter = new RubikFileWriter(p_secondFloorFile);
	    RubikFileWriter l_thirdWriter = new RubikFileWriter(p_thirdFloorFile);
	    Cube l_rubik = new Cube();
	    Cube l_initialPermutation = new Cube(l_rubik);
	    RotationSequence l_rotationLinkedList = new RotationSequence();
	    GoodRotationsBuilder.BuildFilesForRotation(l_firstWriter,l_secondWriter,l_thirdWriter
	            ,l_rubik, l_initialPermutation, l_rotationLinkedList, p_levels,"");
	    l_firstWriter.close();
	    l_secondWriter.close();
	    l_thirdWriter.close();
	
	}

	public static void BuildFilesForRotation(RubikFileWriter p_firstFloorFile, RubikFileWriter p_secondFloorFile, RubikFileWriter p_thirdFloorFile
	                                         , Cube p_rubik
	        , Cube p_initialPermutation, RotationSequence p_rotationLinkedList, int p_level, String p_progressString){
	
	    if (p_level == 0) return;
	    if (p_level>5) System.out.println(p_progressString);
	    int i=0;
	    for (Face face : Face.values())
	        for (Direction direction : Direction.values()) {
	        i++;
	        String myProgressString = p_progressString+String.format(".%d",i);
	            Rotation newRotation = new Rotation(face,direction);
	            if (p_rotationLinkedList.isRedundant(newRotation))
	                continue;
	            p_rotationLinkedList.addRotation(newRotation);
	            p_rubik.rotateFace(newRotation.getFace(), newRotation.getDirection());
	            if (CubeStatus.isDifferentItemsInFirstFloorLessThanThree(p_rubik, p_initialPermutation))
	                p_rotationLinkedList.writeToFile(p_firstFloorFile);
	            if (CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(p_rubik, p_initialPermutation))
	                p_rotationLinkedList.writeToFile((p_secondFloorFile));
	            if (CubeStatus.changesOnlyInThirdFloor(p_rubik, p_initialPermutation))
	                p_rotationLinkedList.writeToFile(p_thirdFloorFile);
	
	            BuildFilesForRotation(p_firstFloorFile,p_secondFloorFile,p_thirdFloorFile,
	                   p_rubik,p_initialPermutation, p_rotationLinkedList,p_level-1,myProgressString);
	            p_rotationLinkedList.removeRotation();
	            p_rubik.rotateFace(newRotation.getReverse().getFace(), newRotation.getReverse().getDirection());
	        }
	}
    
}
