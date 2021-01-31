
/***************************************************************************
                          orientation.h  -  description
                             -------------------
    begin                : Mon Apr 9 2001
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
#ifndef __Position_H
#define __Position_H

#include "Face.h"
#include "Rotation.h"

class Position
{
public:	

  Position(int p_Up, int p_Front){c_currentUp = p_Up; c_currentFront = p_Front;}
  Position(){c_currentUp = U; c_currentFront = F;}
	void rotate(Rotation p_rotation);
	int getFace(int p_viewpoint);
	int operator ==(Position p_position);
	int operator !=(Position p_position);
	void print(){printf("Up=%c, Front=%c", getFaceChar(c_currentUp),getFaceChar(c_currentFront));}
private:
	short c_currentUp;
	short c_currentFront;
	int getHorizonalFacebyVirtual(int p_viewpoint);

};

#endif
