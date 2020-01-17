package com.agilesparks.rubikscube.cube;

import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;

public class RubikFileReader {
   // FileReader c_fileReader;
    boolean c_fileIsOK;

   // ClassLoader classloader = Thread.currentThread().getContextClassLoader();
    InputStream c_fileReader;
    
    public RubikFileReader() {
    }

    public RubikFileReader(String p_fileLocation) {
      //  try {
           // c_fileReader = new FileReader(p_fileLocation);
         c_fileReader = getClass()
     			.getClassLoader().getResourceAsStream(p_fileLocation);
            c_fileIsOK = true;
     //   } catch (IOException ex) {
     //       c_fileIsOK = false;
     //   }
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

