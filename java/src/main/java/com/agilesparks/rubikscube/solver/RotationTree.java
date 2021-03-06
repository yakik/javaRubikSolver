package com.agilesparks.rubikscube.solver;

import java.util.ArrayList;

import com.agilesparks.rubikscube.cube.RubikFileReader;

public class RotationTree {
    ArrayList<RotationSequence> c_array = new ArrayList<RotationSequence>();
    public RotationTree (){
    }

    public void addRotationLinkedList(RotationSequence p_list){
        //System.out.format("FFFFF");
        c_array.add(p_list.getCopy());
    }

    int getSize(){
        return c_array.size();
    }

    public RotationSequence getRotationSequence(int p_index){
        return c_array.get(p_index);
    }

	public static RotationTree getRotationTreeFromFile(RubikFileReader p_File) {
        RotationTree myTree = new RotationTree();
        RotationSequence l_rotationLinkedList = new RotationSequence();
	    while (l_rotationLinkedList.readFromFile(p_File)) {
	        myTree.addRotationLinkedList(l_rotationLinkedList);
        }
        return myTree;
	
	}
}
