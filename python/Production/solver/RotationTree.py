using cube
using System
using System.Collections.Generic
using System.Linq
using System.Text
using System.Threading.Tasks

namespace solver


    class RotationTree
    
        List<RotationSequence> c_array = new List<RotationSequence>()
        RotationTree():
        

        addRotationLinkedList(RotationSequence p_list):
            //Console.Write("FFFFF")
            c_array.Add(p_list.getCopy())
        

        getSize():
            return c_array.Count
        

        RotationSequence getRotationSequence(p_index):
            return c_array[p_index]
        

        static RotationTree getRotationTreeFromFile(RubikFileReader p_File):
            RotationTree myTree = new RotationTree()
            RotationSequence l_rotationLinkedList = new RotationSequence()
            while l_rotationLinkedList.readFromFile(p_File))
            
                myTree.addRotationLinkedList(l_rotationLinkedList)
            
            return myTree

        
    

