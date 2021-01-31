/***************************************************************************
                          Solver.h  -  description
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
#ifndef __Solver_H
#define __Solver_H


#include "Solution.h"
#include "SolutionManager.h"
#include "RotationTree.h"

class Solver
{
public:
	Solver(){}
	void solve(Rubik *p_rubik);
private:
	RotationTree *loadSearchTree();
	void loadRotationTreeFromFile(FILE *p_file, RotationTree *p_tree);
	void loadRotationTreeFromStandart(RotationTree *p_tree, Process *p_process,int p_depth);
	void develop(Solution *p_solution,RotationTree *p_tree,SolutionManager *p_solutionManager
								, int p_onlyFirstFloor);
	void searchTree(int p_minimumValue, RotationTree *p_tree,
								Rubik *p_rubik,Process *p_process,SolutionManager *p_solutionManager,
								Solution *p_prevSolution, int p_onlyFirstFloor);	

};

#endif
