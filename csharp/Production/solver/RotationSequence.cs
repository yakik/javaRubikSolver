using CSharpRubikSolver;
using System;
using System.Collections.Generic;
using utils;
using cube;

namespace solver
{

    public class RotationSequence {

        private List<Rotation> c_array = new List<Rotation>();

        public RotationSequence() {
            c_array.Clear();
        }


        private RotationSequence(List<Rotation> p_List) {
            c_array = p_List;

        }

        public void print() {
         

            foreach (var l_itr in c_array)

                (l_itr as Rotation).print();
            Console.Write("\n");
        }

        public void addRotation(Rotation p_rotation) {
            c_array.Add(p_rotation);
        }

        public void removeRotation() {
            c_array.RemoveAt(c_array.Count - 1);
        }

        public Boolean isRedundant(Rotation p_rotation) {
            Boolean l_returnValue = false;

            Face l_lastFace;
            Direction l_lastDirection;
            if (c_array.Count > 0) {
                l_lastFace = c_array[(c_array.Count - 1)].getFace();
                l_lastDirection = c_array[c_array.Count - 1].getDirection();
                // new rotation is opposite to previous
                if (c_array[c_array.Count - 1].getReverse().equals(p_rotation))
                    l_returnValue = true;
                // previous face was opposite and previous face greater then current face
                if ((p_rotation.getFace() == FaceHandler.getOpposite(l_lastFace) && ((int)l_lastFace > (int)p_rotation.getFace())))
                    l_returnValue = true;
                // two clockwise rotation of same face
                if ((p_rotation.getFace() == l_lastFace) && (l_lastDirection == Direction.CW) &&
                        (p_rotation.getDirection() == Direction.CW))
                    l_returnValue = true;
                //no three counter clockwise rotations
                if (c_array.Count > 1) {
                    if ((p_rotation.getFace() == l_lastFace) && (l_lastDirection == Direction.CCW) &&
                            (p_rotation.getDirection() == Direction.CCW) &&
                            (c_array[c_array.Count - 2].getFace() == l_lastFace) && (l_lastDirection == Direction.CCW) &&
                            (c_array[c_array.Count - 2].getDirection() == Direction.CCW))
                        l_returnValue = true;
                }
            } else
                l_returnValue = false;
            return l_returnValue;

        }

        public void writeToFile(RubikFileWriter p_writer)
        {
            foreach (var l_itr in c_array)

                (l_itr as Rotation).writeToFile(p_writer);

            p_writer.write("\n");


        }
        public bool readFromFile(RubikFileReader p_reader)
        {
            Rotation l_rotation = new Rotation();

            c_array.Clear();
            while (l_rotation.readFromFile(p_reader))
                c_array.Add((new Rotation(l_rotation.getFace(), l_rotation.getDirection())));
            return !(c_array.Count == 0);
        }

       
        RotationSequence getSubRotationLinkedList() {
            return new RotationSequence(new List<Rotation>(c_array.GetRange(1, c_array.Count)));
        }

       public int size() {
            return c_array.Count;
        }

        Rotation getFirstRotation() {
            return c_array[0];
        }
        public Rotation getRotation(int p_index) {
            return c_array[p_index];
        }
        Boolean isNotEmpty() {

            return (c_array.Count > 0);
        }

        public RotationSequence getCopy() {
            RotationSequence l_rotationLinkedList = new RotationSequence();
           

        
            foreach (var l_itr in c_array)

                l_rotationLinkedList.addRotation(l_itr as Rotation);

            return l_rotationLinkedList;
        }

        public void applyToRubik(Cube p_rubik) {
           

              
            
            foreach (var l_itr in c_array)

                p_rubik.rotateFace(l_itr.getFace(), l_itr.getDirection());


        }
    }
}

