/***************************************************************************
                          SolutionManager.cpp  -  description
                             -------------------
    begin                : Sat May 26 2001
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

#include "SolutionManager.h"

SolutionManager::SolutionManager()
{
	int i;
	for (i=0;i<41;i++)
		c_solutionList[i] = NULL;
}

	
SolutionManager::~SolutionManager()
{
	int i;
	for (i=0;i<41;i++)
		if (c_solutionList[i] != NULL)
			delete c_solutionList[i];
}


void SolutionManager::addSolution(Process *p_process, Permutation *p_permutation, Solution *p_prevSolution,
																	 int p_value)
{
	int i = p_value;
	SolutionNode *l_currSolutionNode,*l_nextSolutionNode;
	
	if (c_solutionList[i]==NULL)
	{
		c_solutionList[i] = new SolutionNode(new Solution(p_process->getCopy(),p_permutation->getCopy(),p_prevSolution));
	}
	else
	{
		l_currSolutionNode = c_solutionList[i];
		l_nextSolutionNode = c_solutionList[i]->getNext();
		int i=0;
		while (l_nextSolutionNode != NULL)
			if (l_currSolutionNode->getSolution()->getPermutation() == p_permutation)
				break;
			else
			{
				l_currSolutionNode = l_nextSolutionNode;
				l_nextSolutionNode = l_currSolutionNode->getNext();
				i++;
			}
	
		if (l_nextSolutionNode == NULL && i<30)
		{
			SolutionNode *l_newNode = new SolutionNode(new Solution(p_process->getCopy(),
								p_permutation->getCopy(),p_prevSolution));
			l_currSolutionNode->setNext(l_newNode);
	  }
	//  else
	  //	delete  &p_solution;
	}

}
		
Solution *SolutionManager::getBestUndeveloped()
{
	int i=40;
  Solution *l_returnValue = NULL;
	while (i>=0 && l_returnValue ==NULL)
	{
		if (c_solutionList[i]!=NULL)
		{
			SolutionNode *l_node = c_solutionList[i];
			while (l_node!=NULL && l_returnValue ==NULL)
				if (!(l_node->isDeveloped()))
				{
					l_returnValue =  l_node->getSolution();
					l_node->setDeveloped();
				}
				else
					l_node = l_node->getNext();
		}
		i--;
	}
	return l_returnValue;
}		

Solution *SolutionManager::getBest()
{
	int i=40;
  Solution *l_returnValue = NULL;
	while (i>=0 && l_returnValue ==NULL)
	{
		if (c_solutionList[i]!=NULL)
			l_returnValue =  c_solutionList[i]->getSolution();
		i--;
	}
	return l_returnValue;
}		

int SolutionManager::getBestValue()
{
	int i=40;
	int l_returnValue=0;
	while (i>=0 && l_returnValue==0)
	{
		if (c_solutionList[i]!=NULL)
			l_returnValue =  i;
		i--;
	}
	return l_returnValue;
}		
