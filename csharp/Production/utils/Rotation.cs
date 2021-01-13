using CSharpRubikSolver;
using cube;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace utils
{
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
                c_face = FaceHandler.getFace(p_value - 6);
            } else {
                c_direction = DirectionFactory.getDirectionByInt(0);
                c_face = FaceHandler.getFace(p_value);
            }
        }

        public void writeToFile(RubikFileWriter p_write) {
            String l_toWrite = String.Format(" (%d,%d)", (int)c_face, (int)c_direction);
            p_write.write(l_toWrite);
        }

        public Boolean readFromFile(RubikFileReader p_reader) {
            int l_int;
            l_int = p_reader.read();
            //Console.Write("%d ",l_int);
            while ((l_int == ' ') || (l_int == 13 /*'\r'*/)) {
                l_int = p_reader.read();
                // Console.Write("%d ",l_int);
            }

            if ((l_int == /*'\n'*/10) || (l_int == -1 /*EOF*/) || (l_int != '('))
                return false;
            else {

                c_face = FaceHandler.getFace((int)Char.GetNumericValue((char)(p_reader.read())));
                p_reader.read();
                c_direction = DirectionHandler.getDirection((int)Char.GetNumericValue((char)(p_reader.read())));
                p_reader.read();
                return true;
            }
        }


        public int getValue() {
            return ((int)c_face + (int)c_direction * 6);
        }

        public Face getFace() {
            return c_face;
        }

        public Direction getDirection() {
            return c_direction;
        }

        public void print() {
            Console.Write("(%c,%s)", FaceHandler.getCharValue(c_face),DirectionHandler.getString(c_direction));
        }

        public Rotation getReverse() {
            return new Rotation(c_face,DirectionHandler.getOpposite(c_direction));
        }

        public Boolean equals(
                Rotation p_rotation)

        {
            return ((c_face == p_rotation.c_face) &&
                    (c_direction == p_rotation.c_direction));
        }

    public Boolean equals(Object obj) { 
            if (obj == null) {
                return false;
            }
            if (!(new Rotation()).GetType().IsAssignableFrom(obj.GetType())) {
            return false;
        }
        Rotation other = (Rotation) obj;
        if (this.getFace() != other.getFace()) {
            return false;
        }
        if (this.getDirection() != other.getDirection()) {
            return false;
        }
        return true;
        }
    }
}
