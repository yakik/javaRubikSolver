using cube;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace solver
{
    public class Solution {


        private Cube c_permutation;
        private RotationSequence c_rotationLinkedList;
        private Solution c_prevSolution;


        public Solution(RotationSequence p_rotationLinkedList, Cube p_permutation, Solution p_prevSolution) {
            c_rotationLinkedList = p_rotationLinkedList.getCopy();
            c_permutation = p_permutation.getCopy();
            c_prevSolution = p_prevSolution;
        }

        public Cube getPermutation() {
            return c_permutation;
        }

        RotationSequence getRotationLinkedList() {
            return c_rotationLinkedList;
        }

        Solution getPrevSolution() {
            return c_prevSolution;
        }

        Boolean equals(Solution p_solution)

        {
            return (c_permutation == (p_solution.getPermutation()));
        }

        public void print() {
            if (c_prevSolution != null)
                c_prevSolution.print();
            c_rotationLinkedList.print();
            Console.Write("\n");
        }

        public void applyToRubik(Cube p_rubik) {
            if (c_prevSolution != null)
                c_prevSolution.applyToRubik(p_rubik);
            c_rotationLinkedList.applyToRubik(p_rubik);

        }
    }
}
