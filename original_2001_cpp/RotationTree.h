/***************************************************************************
                          RotationTree.h  -  description
                             -------------------
    begin                : Sat Apr 28 2001
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

#ifndef __RotationTree_H
#define __RotationTree_H

#include <stdio.h>
#include "Rubik.h"
#include "Rotation.h"
#include "Process.h"

class RotationTree
{
public:	
	RotationTree();
	RotationTree(RotationTree *p_prev);
	~RotationTree();
	RotationTree *getPrev();
	void addProcess(Process p_process);
	int getRotation(int p_value, Rotation *p_rotation);
	RotationTree *getNext(int p_value);
private:
	RotationTree *c_next[12];
	short c_rotation[12];
	RotationTree *c_prev;
};

#endif
