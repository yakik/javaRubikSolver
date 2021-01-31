/***************************************************************************
                          ProcessNode.h  -  description
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
#ifndef __ProcessNode_H
#define __ProcessNode_H

#include <stdio.h>
#include "Rotation.h"

class ProcessNode
{
public:	
	ProcessNode(Rotation p_rotation, ProcessNode *p_prev);
	~ProcessNode(){if (c_next != NULL) delete c_next;}
	void print();
	int isNotEmpty();
	Rotation getRotation();
  ProcessNode *getNext();
  ProcessNode *getPrev();
  void setNext(ProcessNode *p_node){c_next = p_node;}
  void setPrev(ProcessNode *p_node){c_prev = p_node;}
private:
	Rotation c_rotation;
	ProcessNode *c_next;
	ProcessNode *c_prev;
};

#endif
