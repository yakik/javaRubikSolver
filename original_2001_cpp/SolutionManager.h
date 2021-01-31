/***************************************************************************
                          SolutionManager.h  -  description
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
#ifndef __SolutionManager_H
#define __SolutionManager_H


#include "Solution.h"




class SolutionManager
{
public:
	SolutionManager();
	~SolutionManager();
	void addSolution(Process *p_process, Permutation *p_permutation, Solution *p_prevSolution,
									 int p_value);
	Solution *getBestUndeveloped();
	Solution *getBest();
	int getBestValue();

private:
	class SolutionNode
	{
	public:
		SolutionNode(Solution *p_solution)
		{
			c_next = NULL;
			c_isDeveloped = 0;
			c_solution = p_solution;
		}		
		~SolutionNode(){delete c_solution;if (c_next!=NULL) delete c_next;}
		Solution *getSolution(){return c_solution;}
		SolutionNode *getNext(){return c_next;}		
		void setNext(SolutionNode *p_solutionNode){c_next = p_solutionNode;}
		int isDeveloped(){return c_isDeveloped;}
		void setDeveloped(){c_isDeveloped = 1;}		
	private:	
		Solution *c_solution;
		SolutionNode *c_next;
		short c_isDeveloped;
	};
	SolutionNode *c_solutionList[41];

};

#endif
