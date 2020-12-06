package com.agilesparks.rubikscube.cube;

import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;

public class RubikFileReader {
    boolean c_fileIsOK;

    InputStream c_fileReader;
    
    public RubikFileReader() {
    }

    public RubikFileReader(String p_fileLocation) {
         c_fileReader = getClass()
     			.getClassLoader().getResourceAsStream(p_fileLocation);
            c_fileIsOK = true;
    }

    public int read() {
        if (!c_fileIsOK)
            return -1;
        else
            try {
                int readChar = c_fileReader.read();
            	return readChar;
            } catch (IOException ex) {
                return -1;
            }
    }

    public void close(){
        try {
        c_fileReader.close();
        } catch (IOException ex) {}
    }
}

