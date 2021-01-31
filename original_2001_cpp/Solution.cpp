/***************************************************************************
                          Solution.cpp  -  description
                             -------------------
    begin                : Fri May 25 2001
    copyright            : (C) 2001 by yaki koren
    email                : 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#include "Solution.h"

Solution::Solution(Process *p_process, Permutation *p_permutation, Solution *p_prevSolution)
{
	c_process = p_process->getCopy();
	c_permutation = p_permutation->getCopy();
	c_prevSolution = p_prevSolution;
}

int Solution::operator ==(Solution p_solution)
{
	return (*c_permutation == *(p_solution.getPermutation()));
}

void Solution::print()
{
	if  (c_prevSolution!=NULL)
		c_prevSolution->print();
	c_process->print();
	printf("\n");
}

void Solution::applyToRubik(Rubik *p_rubik)
{
	if  (c_prevSolution!=NULL)
		c_prevSolution->applyToRubik(p_rubik);
	c_process->applyToRubik(p_rubik);

}
