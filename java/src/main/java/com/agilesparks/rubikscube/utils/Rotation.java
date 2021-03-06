package com.agilesparks.rubikscube.utils;

import com.agilesparks.rubikscube.cube.RubikFileReader;
import com.agilesparks.rubikscube.cube.RubikFileWriter;

public class Rotation {

    private Face c_face;
    private Direction c_direction;
    public Rotation() {
    }


    public Rotation(Face p_face, Direction p_direction) {
        c_face = p_face;
        c_direction = p_direction;
    }



    public Rotation(int p_value) {
        if (p_value > 5) {
            c_direction = DirectionFactory.getDirectionByInt(1);
            c_face = FaceFactory.getFaceByInt(p_value - 6);
        } else {
            c_direction = DirectionFactory.getDirectionByInt(0);
            c_face = FaceFactory.getFaceByInt(p_value);
        }
    }

    public void writeToFile(RubikFileWriter p_write){
        String l_toWrite = String.format(" (%d,%d)",c_face.getInt(),c_direction.getInt());
        p_write.write(l_toWrite);
    }

    public boolean readFromFile(RubikFileReader p_reader) {
        int l_int;
        l_int = p_reader.read();
        //System.out.format("%d ",l_int);
        while ((l_int == ' ') || (l_int == 13 /*'\r'*/)){
            l_int = p_reader.read();
           // System.out.format("%d ",l_int);
        }
        
        if ((l_int == /*'\n'*/10)  || (l_int == -1 /*EOF*/) || (l_int != '('))
            return false;
        else {

            c_face = FaceFactory.getFaceByInt(Character.getNumericValue(p_reader.read()));
            p_reader.read();
            c_direction = DirectionFactory.getDirectionByInt(Character.getNumericValue(p_reader.read()));
            p_reader.read();
            return true;
        }
    }


    public int getValue() {
        return (c_face.getInt() + c_direction.getInt() * 6);
    }

    public Face getFace() {
        return c_face;
    }

    public Direction getDirection() {
        return c_direction;
    }

    public void print() {
        System.out.format("(%c,%s)", c_face.getIntOfChar(), c_direction.getString());
    }

    public Rotation getReverse() {
        return new Rotation(c_face, c_direction.getOpposite());
    }

    public boolean equals(
            Rotation p_rotation)

    {
        return ((c_face == p_rotation.c_face) &&
                (c_direction == p_rotation.c_direction));
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (!Rotation.class.isAssignableFrom(obj.getClass())) {
            return false;
        }
        final Rotation other = (Rotation) obj;
        if (this.getFace() != other.getFace()) {
            return false;
        }
        if (this.getDirection() != other.getDirection()) {
            return false;
        }
        return true;
    }
}
