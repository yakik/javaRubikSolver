package com.agilesparks.rubikscube.solver;

import java.util.ArrayList;

public class RotationTree {
    ArrayList<RotationLinkedList> c_array = new ArrayList<RotationLinkedList>();
    public RotationTree (){
    }

    public void addRotationLinkedList(RotationLinkedList p_list){

        c_array.add(p_list.getCopy());
    }

    int getSize(){
        return c_array.size();
    }

    public RotationLinkedList getRotationLinkedList(int p_index){
        return c_array.get(p_index);
    }
}
