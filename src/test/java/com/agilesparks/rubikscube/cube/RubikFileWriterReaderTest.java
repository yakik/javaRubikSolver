package com.agilesparks.rubikscube.cube;


import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

import com.agilesparks.rubikscube.cube.RubikFileReader;
import com.agilesparks.rubikscube.cube.RubikFileWriter;

public class RubikFileWriterReaderTest {

	@Ignore
	@Test
    public void write() {
        RubikFileWriter myWriter = new RubikFileWriter("Test.txt");
        long myNano = System.nanoTime();
        String myNanoString = String.format("%d",myNano);
        myWriter.write(myNanoString);
        myWriter.close();
        RubikFileReader myReader = new RubikFileReader(("Test.txt"));
        int l_int;
        String l_readString = "";
        while ((l_int = myReader.read())!=-1)
            l_readString+=(char)l_int;
        assertEquals(myNanoString,l_readString);



    }
}