/***************************************************************************
                          Solution.h  -  description
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
#ifndef __Solution_H
#define __Solution_H


#include "Process.h"
#include "Permutation.h"




class Solution
{
public:
	Solution(Process *p_process, Permutation *p_permutation, Solution *p_prevSolution);
	Permutation *getPermutation(){return c_permutation;}
	Process *getProcess(){return c_process;}
	Solution *getCopy();
	Solution *getPrevSolution(){return c_prevSolution;}
	int operator ==(Solution p_solution);
	void print();
	void applyToRubik(Rubik *p_rubik);
	~Solution(){delete c_permutation;delete c_process;}//c_process->remove();}
	
private:

	Permutation *c_permutation;
	Process *c_process;
	Solution *c_prevSolution;

};

#endif
