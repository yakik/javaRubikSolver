/***************************************************************************
                          Process.cpp  -  description
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
#include "ProcessNode.h"


ProcessNode::ProcessNode(Rotation p_rotation, ProcessNode *p_prev)
{
	c_prev = NULL;
	c_next = NULL;
	c_prev = p_prev;
	c_rotation = p_rotation;
}

void ProcessNode::print()
{
	c_rotation.print();
}
	

Rotation ProcessNode::getRotation()
{
	return c_rotation;
}

ProcessNode *ProcessNode::getNext()
{
	return c_next;
}

ProcessNode *ProcessNode::getPrev()
{
	return c_prev;
}
