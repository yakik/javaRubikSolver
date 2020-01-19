package com.agilesparks.rubikscube.solver;

import com.agilesparks.rubikscube.cube.Cube;
import com.agilesparks.rubikscube.cube.Permutation;

public class Solution {


    private Permutation c_permutation;
    private RotationLinkedList c_rotationLinkedList;
    private Solution c_prevSolution;


    Solution(RotationLinkedList p_rotationLinkedList, Permutation p_permutation, Solution p_prevSolution) {
        c_rotationLinkedList = p_rotationLinkedList.getCopy();
        c_permutation = p_permutation.getCopy();
        c_prevSolution = p_prevSolution;
    }

    Permutation getPermutation() {
        return c_permutation;
    }

    RotationLinkedList getRotationLinkedList() {
        return c_rotationLinkedList;
    }

    Solution getPrevSolution() {
        return c_prevSolution;
    }

    boolean equals(Solution p_solution)

    {
        return (c_permutation == (p_solution.getPermutation()));
    }

    public void print() {
        if (c_prevSolution != null)
            c_prevSolution.print();
        c_rotationLinkedList.print();
        System.out.format("\n");
    }

    public void applyToRubik(Cube p_rubik) {
        if (c_prevSolution != null)
            c_prevSolution.applyToRubik(p_rubik);
        c_rotationLinkedList.applyToRubik(p_rubik);

    }
}
