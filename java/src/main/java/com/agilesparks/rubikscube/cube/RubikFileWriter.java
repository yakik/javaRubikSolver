package com.agilesparks.rubikscube.cube;
import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.FileWriter;

public class RubikFileWriter {

    BufferedWriter c_fileWriter;
    boolean c_fileIsOK;


    private static String getResourcePath() {
        try {
            URI resourcePathFile = System.class.getResource("/RESOURCE_PATH").toURI();
            String resourcePath = Files.readAllLines(Paths.get(resourcePathFile)).get(0);
            URI rootURI = new File("").toURI();
            URI resourceURI = new File(resourcePath).toURI();
            URI relativeResourceURI = rootURI.relativize(resourceURI);
            return relativeResourceURI.getPath();
        } catch (Exception e) {
            return null;
        }
    }
    
    
    public RubikFileWriter(String p_fileLocation) {
        try {
            c_fileWriter = new BufferedWriter(new FileWriter(getResourcePath() + p_fileLocation));
            
            c_fileIsOK = true;
        } catch (IOException ex) {
            c_fileIsOK = false;
        }
    }

    public void write(String p_string) {
            try {
                c_fileWriter.write(p_string);
            } catch (IOException ex) {}

    }

    public void close(){
        try {
            c_fileWriter.close();
        } catch (IOException ex) {}
    }
}
