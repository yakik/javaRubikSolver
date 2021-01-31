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

#include "Solver.h"


void Solver::solve(Rubik *p_rubik)
{
	int l_value,l_onlyFirstFloor = 0;
	Permutation *l_permutation = p_rubik->getPermutation();
	SolutionManager *l_solutionManager = new SolutionManager();
	Solution *l_solutionToDev,*l_finalSolution;
 	RotationTree *l_tree = loadSearchTree();
  Process *l_process = new Process();;
	l_value = l_permutation->getValue(0);
	if (l_value < 16)
	{
		l_onlyFirstFloor = 1;
		l_value = l_permutation->getValue(1);
	}
		
 	
 	l_solutionManager->addSolution(l_process,l_permutation,NULL,l_value);
	while ((l_solutionToDev = l_solutionManager->getBestUndeveloped())!=NULL &&
					l_solutionManager->getBestValue()<40)
	{
		develop(l_solutionToDev,l_tree,l_solutionManager,l_onlyFirstFloor);
		printf("Best yet:%d\n",l_solutionManager->getBestValue());	
		if (l_solutionManager->getBestValue()>=14)
			l_onlyFirstFloor = 0;
  }
  l_finalSolution = l_solutionManager->getBest();
  printf("the Solution found values is:%d\n",l_finalSolution->getPermutation()->getValue(l_onlyFirstFloor));
  printf("the process is:\n");
  l_finalSolution->print();
  l_finalSolution->applyToRubik(p_rubik);
  getchar();
  p_rubik->printCube();
}

void Solver::develop(Solution *p_solution,RotationTree *p_tree,SolutionManager *p_solutionManager,
											int p_onlyFirstFloor)
{
	Rubik *l_rubik = new Rubik();
	Permutation *l_permutation = p_solution->getPermutation()->getCopy();
	Process l_process;
	int l_minimumValue = l_permutation->getValue(p_onlyFirstFloor);
//	if (l_minimumValue < 8)
//		l_minimumValue = 8;
	l_rubik->set(l_permutation);
	searchTree(l_minimumValue,p_tree,l_rubik,&l_process,p_solutionManager,
								p_solution,p_onlyFirstFloor);
}


void Solver::searchTree(int p_minimumValue, RotationTree *p_tree,
								Rubik *p_rubik,Process *p_process,SolutionManager *p_solutionManager,
								Solution *p_prevSolution,int p_onlyFirstFloor)
{
	int i;
	Rotation l_rotation;
	RotationTree *l_nextSubTree;
	for (i=0;i<12;i++)
		if (p_tree->getRotation(i,&l_rotation))
		{
			if (!(p_process->isRedundant(l_rotation)))
			{
				p_process->addRotation(l_rotation);
				p_rubik->rotateFace(l_rotation);
				Permutation *l_currPermutation = p_rubik->getPermutation();
				if (l_currPermutation->getValue(p_onlyFirstFloor)>= p_minimumValue)
//					printf("found %d\n", l_currPermutation->getValue(p_onlyFirstFloor));
					p_solutionManager->addSolution(p_process, l_currPermutation,p_prevSolution,l_currPermutation->getValue(p_onlyFirstFloor));
				if ((l_nextSubTree = p_tree->getNext(i))!=NULL)
					searchTree(p_minimumValue,l_nextSubTree,p_rubik,p_process,
											p_solutionManager,p_prevSolution,p_onlyFirstFloor);
				delete l_currPermutation;
				p_process->removeRotation();
				p_rubik->rotateFace(l_rotation.getReverse());
	    }
		}
}

RotationTree *Solver::loadSearchTree()
{
 	Process *l_process = new Process();
 	RotationTree *l_tree = new RotationTree();
 	FILE *l_file;
 	l_file= fopen("permRubik.txt","r");
  loadRotationTreeFromFile(l_file, l_tree);
  loadRotationTreeFromStandart(l_tree,l_process,5);
  fclose(l_file);
  return l_tree;
}

void Solver::loadRotationTreeFromFile(FILE *p_file, RotationTree *p_tree)
{
 	Process *l_process = new Process();
 	while (l_process->reset(p_file))
 	{
 		p_tree->addProcess(*l_process);
 	}

}


void Solver::loadRotationTreeFromStandart(RotationTree *p_tree, Process *p_process,int p_depth)
{
	int i;
	if (p_depth == 0) return;
	for (i=0;i<12;i++)
		{
		if (p_process->isRedundant(Rotation(i)))
			continue;		
		p_process->addRotation(Rotation(i));
		p_tree->addProcess(*p_process);
		loadRotationTreeFromStandart(p_tree,p_process,p_depth-1);
    p_process->removeRotation();
  	}
  return;
}
