/***************************************************************************
                          Process.h  -  description
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
#ifndef __Process_H
#define __Process_H

#include <stdio.h>
#include "Rotation.h"
#include "Rubik.h"
#include "ProcessNode.h"

class Process
{
public:	
	Process();
//	~Process(){if (c_head !=NULL) delete c_head;}
	Process(ProcessNode *p_head, ProcessNode *p_tail);
	int reset(FILE *p_file);
	void print();
	void addRotation(Rotation p_rotation);
	void removeRotation();
	int isRedundant(Rotation p_rotation);
	int isNotEmpty();
	Rotation getFirstRotation();
	Process getSubProcess();
	Process *getCopy();
	void applyToRubik(Rubik *p_rubik);
//	void remove(){if (c_head!=NULL ) delete c_head;}
private:
	ProcessNode *c_head;
	ProcessNode *c_tail;
};

#endif
