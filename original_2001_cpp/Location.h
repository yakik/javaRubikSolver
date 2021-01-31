/***************************************************************************
                          Location.h  -  description
                             -------------------
    begin                : Sat Apr 14 2001
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
#ifndef __Location_H
#define __Location_H

#include "Face.h"
#include <stdio.h>

class Location
{
public:	

  Location(){}
  Location(int p_face0,int p_face1,int p_face2);
	Location(int p_face0,int p_face1);
	int isEdge();
  int getFace0();
  int getFace1();
  int getFace2();
	int getValue();
	int operator ==(Location p_location);
	int operator !=(Location p_location);
	void print();
private:
	short c_face0, c_face1, c_face2;
	short c_isEdge;

};

#endif
