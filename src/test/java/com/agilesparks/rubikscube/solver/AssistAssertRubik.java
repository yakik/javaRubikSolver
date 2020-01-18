package com.agilesparks.rubikscube.solver;

import static org.junit.Assert.*;

import com.agilesparks.rubikscube.cube.Cube;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;

public class AssistAssertRubik {
    static void myAssertEdge(Face p_firstFace, Face p_secondFace, Cube p_rubik){
       
    	assertTrue("Problem with edge "+Character.toString(p_firstFace.getChar())
        +" / " +Character.toString(p_secondFace.getChar()),(new Location(p_firstFace, p_secondFace))
                        .equals(p_rubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(p_firstFace, p_secondFace)))
                );
    }

    static void myAssertCorner(Face p_firstFace, Face p_secondFace, Face p_thirdFace, Cube p_rubik){
        assertTrue( "Problem with corner "+Character.toString(p_firstFace.getChar())
        +" / " +Character.toString(p_secondFace.getChar())
        +" / " +Character.toString(p_thirdFace.getChar()),(new Location(p_firstFace, p_secondFace, p_thirdFace))
                        .equals(p_rubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(p_firstFace, p_secondFace, p_thirdFace)))
                );
    }

    public static void checkEntireCube(Cube p_rubik){
        myAssertEdge(Face.TOP, Face.LEFT, p_rubik);
        myAssertEdge(Face.TOP, Face.RIGHT, p_rubik);
        myAssertEdge(Face.TOP, Face.FRONT, p_rubik);
        myAssertEdge(Face.TOP, Face.BACK, p_rubik);

        myAssertEdge(Face.BOTTOM, Face.LEFT, p_rubik);
        myAssertEdge(Face.BOTTOM, Face.RIGHT, p_rubik);
        myAssertEdge(Face.BOTTOM, Face.FRONT, p_rubik);
        myAssertEdge(Face.BOTTOM, Face.BACK, p_rubik);

        myAssertEdge(Face.FRONT, Face.LEFT, p_rubik);
        myAssertEdge(Face.FRONT, Face.RIGHT, p_rubik);
        myAssertEdge(Face.BACK, Face.LEFT, p_rubik);
        myAssertEdge(Face.BACK, Face.RIGHT, p_rubik);

        myAssertCorner(Face.BOTTOM, Face.LEFT, Face.BACK, p_rubik);
        myAssertCorner(Face.BOTTOM, Face.LEFT, Face.FRONT, p_rubik);
        myAssertCorner(Face.BOTTOM, Face.RIGHT, Face.BACK, p_rubik);
        myAssertCorner(Face.BOTTOM, Face.RIGHT, Face.FRONT, p_rubik);

        myAssertCorner(Face.TOP, Face.LEFT, Face.BACK, p_rubik);
        myAssertCorner(Face.TOP, Face.LEFT, Face.FRONT, p_rubik);
        myAssertCorner(Face.TOP, Face.RIGHT, Face.BACK, p_rubik);
        myAssertCorner(Face.TOP, Face.RIGHT, Face.FRONT, p_rubik);
    }

}
