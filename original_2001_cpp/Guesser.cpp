/***************************************************************************
                          Guesser.cpp  -  description
                             -------------------
    begin                : Fri Apr 20 2001
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
#include "Guesser.h"

int Guesser::depthFirstSearch(Permutation *p_permutation, Rubik *p_rubik, int p_depth, Process *p_process)
{
	int i,j;
	int l_counter=0;
//	if (p_depth == 3)
//	p_rubik->printCube();
	for (i=0;i<6;i++)
		for (j=0;j<2;j++)
		{
		//rotate, then check
			if (p_process->isRedundant(Rotation(i,j)))
				continue;
			p_process->addRotation(Rotation(i,j));
			p_rubik->rotateFace(Rotation(i,j));
		/*	if (p_permutation->isPartRubik(p_rubik))
				return 1;
			else  */
				if (p_depth > 1)
		/*			if*/
					 l_counter = l_counter + depthFirstSearch(p_permutation,p_rubik,(p_depth-1),p_process);
					///*==1*/;
/*						return 1;*/
					l_counter++;
//			p_process->removeRotation(Rotation(i,j));
			p_rubik->rotateFace(Rotation(i,j).getReverse());
		}
	return l_counter;
}

int Guesser::Search2(Permutation *p_permutation, Rubik *p_rubik, int p_depth, Process *p_process)
{
	int i,j,l_diff;

	for (i=0;i<6;i++)
		for (j=0;j<2;j++)
		{
			if (p_depth >= 7)
  			printf ("\ndepth = %d, i=%d, j=%d\n", p_depth,i,j);
		
		//rotate, then check
			if (p_process->isRedundant(Rotation(i,j)))
				continue;
			p_process->addRotation(Rotation(i,j));
			p_rubik->rotateFace(Rotation(i,j));
			if ((l_diff = p_permutation->getDifferece(p_rubik))<=7)
				{
					printf(".");
//					p_process->writeFile();
				}
				if (p_depth > 1)
					 Search2(p_permutation,p_rubik,(p_depth-1),p_process);
//			p_process->removeRotation(Rotation(i,j));
			p_rubik->rotateFace(Rotation(i,j).getReverse());
		}
	return 0;
}
