using cube;
using System.Collections.Generic;


namespace solver
{

    public class RotationTree
    {
        List<RotationSequence> c_array = new List<RotationSequence>();
        public RotationTree()
        {
        }

        public void addRotationLinkedList(RotationSequence p_list)
        {
            //Console.Write("FFFFF");
            c_array.Add(p_list.getCopy());
        }

        public int getSize()
        {
            return c_array.Count;
        }

        public RotationSequence getRotationSequence(int p_index)
        {
            return c_array[p_index];
        }

        public static RotationTree getRotationTreeFromFile(RubikFileReader p_File)
        {
            RotationTree myTree = new RotationTree();
            RotationSequence l_rotationLinkedList = new RotationSequence();
            while (l_rotationLinkedList.readFromFile(p_File))
            {
                myTree.addRotationLinkedList(l_rotationLinkedList);
            }
            return myTree;

        }
    }
}
