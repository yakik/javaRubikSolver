package com.agilesparks.rubikscube.solver;

import static org.junit.Assert.*;

import com.agilesparks.rubikscube.cube.Rubik;
import com.agilesparks.rubikscube.utils.Face;
import com.agilesparks.rubikscube.utils.Location;

public class AssistAssertRubik {
    static void myAssertEdge(Face p_firstFace, Face p_secondFace, Rubik p_rubik){
       
    	assertTrue("Problem with edge "+Character.toString(p_firstFace.getChar())
        +" / " +Character.toString(p_secondFace.getChar()),(new Location(p_firstFace, p_secondFace))
                        .equals(p_rubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(p_firstFace, p_secondFace)))
                );
    }

    static void myAssertCorner(Face p_firstFace, Face p_secondFace, Face p_thirdFace, Rubik p_rubik){
        assertTrue( "Problem with corner "+Character.toString(p_firstFace.getChar())
        +" / " +Character.toString(p_secondFace.getChar())
        +" / " +Character.toString(p_thirdFace.getChar()),(new Location(p_firstFace, p_secondFace, p_thirdFace))
                        .equals(p_rubik.getOriginalLocationOfCurrentCubicleInLocation(new Location(p_firstFace, p_secondFace, p_thirdFace)))
                );
    }

    public static void checkEntireCube(Rubik p_rubik){
        myAssertEdge(Face.U, Face.L, p_rubik);
        myAssertEdge(Face.U, Face.R, p_rubik);
        myAssertEdge(Face.U, Face.F, p_rubik);
        myAssertEdge(Face.U, Face.B, p_rubik);

        myAssertEdge(Face.D, Face.L, p_rubik);
        myAssertEdge(Face.D, Face.R, p_rubik);
        myAssertEdge(Face.D, Face.F, p_rubik);
        myAssertEdge(Face.D, Face.B, p_rubik);

        myAssertEdge(Face.F, Face.L, p_rubik);
        myAssertEdge(Face.F, Face.R, p_rubik);
        myAssertEdge(Face.B, Face.L, p_rubik);
        myAssertEdge(Face.B, Face.R, p_rubik);

        myAssertCorner(Face.D, Face.L, Face.B, p_rubik);
        myAssertCorner(Face.D, Face.L, Face.F, p_rubik);
        myAssertCorner(Face.D, Face.R, Face.B, p_rubik);
        myAssertCorner(Face.D, Face.R, Face.F, p_rubik);

        myAssertCorner(Face.U, Face.L, Face.B, p_rubik);
        myAssertCorner(Face.U, Face.L, Face.F, p_rubik);
        myAssertCorner(Face.U, Face.R, Face.B, p_rubik);
        myAssertCorner(Face.U, Face.R, Face.F, p_rubik);
    }

}
