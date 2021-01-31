/***************************************************************************
                          Guesser.h  -  description
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

#ifndef __Guesser_H
#define __Guesser_H

#include "Rubik.h"
#include "Process.h"
#include "Permutation.h"




class Guesser
{
public:
	Guesser(){}
	int depthFirstSearch(Permutation *p_permutation,
											 Rubik *p_rubik, int p_depth, Process *p_process);
	int Search2(Permutation *p_permutation,
											 Rubik *p_rubik, int p_depth, Process *p_process);
											


};

#endif
