/***************************************************************************
                          Rotation.h  -  description
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
#ifndef __Rotation_H
#define __Rotation_H

#include "Face.h"
#include <stdio.h>

class Rotation
{
public:	
  int reset(FILE *p_file);
  Rotation(){}
  Rotation(int p_value);
  Rotation(int p_face, int p_direction);
  int getFace();
  int getDirection();
  void print();
  Rotation getReverse();
  int getValue();
  int operator ==(Rotation p_rotation);
private:
	short c_face;
	short c_direction;

};

#endif
