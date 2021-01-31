/***************************************************************************
                          RotationTree.cpp  -  description
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
#include "RotationTree.h"


RotationTree::RotationTree()
{
	int i;
	for (i=0;i<12;i++)
	{
		c_next[i] = NULL;
		c_rotation[i] = 0;
	}
	c_prev = NULL;
}

RotationTree::RotationTree(RotationTree *p_prev)
{
	int i;
	for (i=0;i<12;i++)
	{
		c_next[i] = NULL;
		c_rotation[i] = 0;
	}
	c_prev = p_prev;
}
	
RotationTree::~RotationTree()
{
	int i;
	for (i=0;i<12;i++)
		delete c_next[i];
}
	
void RotationTree::addProcess(Process p_process)
{
	if (p_process.isNotEmpty())
	{
		int l_value = p_process.getFirstRotation().getValue();
		c_rotation[l_value] = 1;
		if (c_next[l_value] == NULL)
			c_next[l_value] = new RotationTree(this);
		c_next[l_value]->addProcess(p_process.getSubProcess());
	}
}

RotationTree *RotationTree::getNext(int p_value)
{
	return c_next[p_value];
}


RotationTree *RotationTree::getPrev()
{
	return c_prev;
}

int RotationTree::getRotation(int p_value, Rotation *p_rotation)
{
	if (c_rotation[p_value] == 0)
		return 0;
	else
	{
		*p_rotation = Rotation(p_value);
		return 1;
	}
}
