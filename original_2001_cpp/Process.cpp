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
#include "Process.h"

Process::Process()
{
	c_head = NULL;
	c_tail = NULL;
}

Process::Process(ProcessNode *p_head, ProcessNode *p_tail)
{
	c_head = p_head;
	c_tail = p_tail;
}

void Process::print()
{
	ProcessNode *l_node = c_head;
	while (l_node != NULL)
	{
		l_node->getRotation().print();
		l_node= l_node->getNext();
	}
	printf("\n");
}
	
void Process::addRotation(Rotation p_rotation)
{
	if (c_head == NULL)
	{
		c_head = new ProcessNode(p_rotation, NULL);
		c_tail = c_head;
	}
	else
	{
		ProcessNode *l_node = new ProcessNode(p_rotation, c_tail);
		c_tail->setNext(l_node);
		c_tail = c_tail->getNext();
	}
}

void Process::removeRotation()
{
	ProcessNode *l_prev;
	if (c_tail == c_head)
	{
		delete(c_tail);
		c_tail = NULL;
		c_head = NULL;
	}
	else
	{
	l_prev = c_tail->getPrev();
	delete (c_tail);
	c_tail = l_prev;
	c_tail->setNext(NULL);
	}
}



int Process::isRedundant(Rotation p_rotation)
{
	int l_returnValue=0;
	int l_lastFace, l_lastDirection;		
	if (c_head != NULL)
	{
		l_lastFace = c_tail->getRotation().getFace();
		l_lastDirection = c_tail->getRotation().getDirection();
		// new rotation is opposite to previous
		if (c_tail->getRotation().getReverse()==p_rotation)
			l_returnValue = 1;
		// previous face was opposite and previous face greater then current face
		if (p_rotation.getFace() == oppositeFace(l_lastFace) &&	l_lastFace>p_rotation.getFace())
			l_returnValue = 1;
		// two clockwise rotation of same face
		if ((p_rotation.getFace() == l_lastFace) &&	(l_lastDirection == CW) &&
				(p_rotation.getDirection()==CW))
			l_returnValue = 1;
		if (c_head != c_tail)
		{
			if ((p_rotation.getFace() == l_lastFace) &&	(l_lastDirection == CCW) &&
					(p_rotation.getDirection()==CCW) &&
					(c_tail->getPrev()->getRotation().getFace() == l_lastFace) &&	(l_lastDirection == CCW) &&
					(c_tail->getPrev()->getRotation().getDirection()==CCW))
				l_returnValue = 1;						
		}
  }
	else
		l_returnValue = 0;
	return l_returnValue;

}

int Process::reset(FILE *p_file)
{
	Rotation l_rotation;
	ProcessNode *l_node;	
	if (c_head != NULL)
		delete c_head;
	c_head = NULL;
	c_tail = NULL;
	while (l_rotation.reset(p_file))
	{

		if (c_head == NULL)
		{
			c_head = new ProcessNode(l_rotation,NULL);
			l_node = c_head;
			c_tail = c_head;
		}
		else
		{
			l_node->setNext(new ProcessNode(l_rotation,l_node));
			l_node = l_node->getNext();
			c_tail = l_node;
		}
	}
	if (c_head ==NULL)
		return 0;
	else
		return 1;
}

Process Process::getSubProcess()
{
	return Process(c_head->getNext(), c_tail);
}

Rotation Process::getFirstRotation()
{
	return c_head->getRotation();
}

int Process::isNotEmpty()
{
	if (c_head == NULL)
		return 0;
	else
		return 1;
}

Process *Process::getCopy()
{
	ProcessNode	*l_node = c_head;
	Process *l_process = new Process();
	while (l_node!=NULL)
	{
		l_process->addRotation(l_node->getRotation());
		l_node = l_node->getNext();
	}
	return l_process;
}

void Process::applyToRubik(Rubik *p_rubik)
{
	ProcessNode	*l_node = c_head;
	while (l_node!=NULL)
	{
		p_rubik->rotateFace(l_node->getRotation());
		l_node = l_node->getNext();
	}
}
